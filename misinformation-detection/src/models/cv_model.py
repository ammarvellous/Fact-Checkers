from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator

class CVModel:
    def __init__(self, input_shape, num_classes):
        self.model = self.build_model(input_shape, num_classes)

    def build_model(self, input_shape, num_classes):
        model = Sequential()
        model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Conv2D(64, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Conv2D(128, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Flatten())
        model.add(Dense(128, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(num_classes, activation='softmax'))
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def train(self, train_data, validation_data, epochs=10, batch_size=32):
        datagen = ImageDataGenerator(rescale=1.0/255.0)
        train_generator = datagen.flow(train_data[0], train_data[1], batch_size=batch_size)
        validation_generator = datagen.flow(validation_data[0], validation_data[1], batch_size=batch_size)

        self.model.fit(train_generator, validation_data=validation_generator, epochs=epochs)

    def evaluate(self, test_data):
        test_generator = ImageDataGenerator(rescale=1.0/255.0).flow(test_data[0], test_data[1])
        return self.model.evaluate(test_generator)