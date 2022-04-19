import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

__labels = None
__data_columns = None
__model = None

# Takes Image as input and return the prediction and confidence percentage
def get_predicted_item(img_path):
    try:
        img = image.load_img(img_path, target_size=(224, 224))
    except:
        img = image.load_img("./static/uploads/test.jpg", target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    img_preprocessed = tf.keras.applications.efficientnet.preprocess_input(
        img_batch)
    pred_item = __labels[np.argmax(__model.predict([img_preprocessed]))]
    pred = np.max(__model.predict([img_preprocessed]))*100
    return pred_item, pred


# Loads the model and labels
def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __labels

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __labels = __data_columns[:]

    global __model
    if __model is None:
        __model = tf.keras.models.load_model(
            "./artifacts/efficientnetb0/model5a.07-0.88.hdf5")
    print("loading saved artifacts...done")

# LABELS
def get_labels():
    return __labels


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    # print(get_labels())
    print(get_predicted_item("./static/uploads/test.jpg"))
