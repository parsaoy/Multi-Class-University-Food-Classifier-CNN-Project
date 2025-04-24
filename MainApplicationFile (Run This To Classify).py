"""
    This Python program classifies images University of Tabriz Foods.
    To classify an image,
    run the Python file and enter the file path of the image.
    By Parsa Yousefinezhad
"""

from keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image

model_path = '/Users/parsa/Desktop/trained_model_final2'
model = load_model(model_path)

datagen_train = ImageDataGenerator(rescale=1./255)
datagen_val = ImageDataGenerator(rescale=1./255, validation_split=0.22)

class_names = {0: 'Ghosht_Garch', 1: 'Gorme_Sabzi', 2: 'Havij', 3: 'Joje', 4: 'Kabab', 5: 'Mahi', 6: 'Makaroni', 7: 'Morgh', 8: 'Naget'}

while(True):

    image_path = input("\033[2;46;36mEnter Image Path:\033[0m ")
    
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)/255.0
# ************
    predictions = model.predict(img_array)
# ************

    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = predictions[0][np.argmax(predictions[0])]

    print(f"\x1B[41;2;35mPredicted Class: {predicted_class}\033[0m")
    print(f"\033[1;42;34mConfidence: {confidence:.2%}\033[0m")
    print('\x1B[1;1;33m*********************************\033[0m\n')