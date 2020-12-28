from keras.models import Sequential
from keras.layers import Dense, Activation
import keras.backend as K
from keras.callbacks import EarlyStopping
from sklearn.preprocessing import  MinMaxScaler


def tilted_loss(q, y, f):
    e = (y-f)
    return K.mean(K.maximum(q*e, (q-1)*e), axis=-1)


class QuantileModel:
    __model = None
    __input_dims = 0
    __q = 0.5
    epochs = 2000
    batch_size = 2048
    scaler = MinMaxScaler()

    def rebuild(self):
        self.__model = Sequential()
        self.__model.add(
            Dense(units=16, input_dim=self.__input_dims, activation='relu'))
        self.__model.add(Dense(units=256, input_dim=1, activation='relu'))
        self.__model.add(Dense(1))

        return self.__model

    def get_model(self):
        if self.__model is None:
            self.rebuild()
        return self.__model

    def __init__(self, input_dims, q=0.5):
        self.__input_dims = input_dims
        self.__q = q
        self.rebuild()

    def fit(self, X, y, X_val, y_val):
        y = self.scaler.fit_transform(y.reshape(-1,1))
        y_val = self.scaler.transform(y_val.reshape(-1,1))
        early_stopping_monitor = EarlyStopping(
            monitor='val_loss',
            min_delta=0,
            patience=5,
            verbose=0,
            mode='auto',
            baseline=None,
            restore_best_weights=True
        )
        model = self.rebuild()
        model.compile(loss=lambda y, f: tilted_loss(
            self.__q, y, f),
            optimizer='adam')

        model.fit(X, y, validation_data=(X_val, y_val),
                  callbacks=[early_stopping_monitor],
                  epochs=self.epochs, batch_size=self.batch_size, verbose=
                  0)
        self.__model = model
        return self

    def predict(self, X):
        results = self.scaler.inverse_transform(self.__model.predict(X))
        return results.flatten()
