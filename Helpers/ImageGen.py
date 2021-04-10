import matplotlib.pyplot as plt
import numpy as np
import os
import random
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
#%matplotlib inline

def plotImages(images_arr):
    fig, axes = plt.subplots(1, 10, figsize=(20,20))
    axes = axes.flatten()
    for img, ax in zip( images_arr, axes):
        ax.imshow(img)
        ax.axis('off')
    plt.tight_layout()
    plt.show()


gen = ImageDataGenerator(rotation_range=0.1, width_shift_range=0.01, height_shift_range=0.01, shear_range=0.015, zoom_range=0.01, 
    channel_shift_range=5., horizontal_flip=False)


chosen_img = r'[*/DIRECTORY/TO/SPECIFIC/IMAGE/HERE*]/25.JPG'
image_path = '[*/DIRECTORY/TO/GENERATED/IMAGES/DESTINATION/HERE*]'
image = np.expand_dims(plt.imread(chosen_img),0)
# plt.imshow(image[0])

aug_iter = gen.flow(image)


aug_images = [next(aug_iter)[0].astype(np.uint8) for i in range(15)]

# plotImages(aug_images)
count = 0
for batch in gen.flow(image, batch_size=1,save_to_dir= image_path, save_format='JPG'):
    count += 1
    if count > 15:
        break