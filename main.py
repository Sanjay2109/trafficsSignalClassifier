import tensorflow as tf
import numpy as np
from PIL import Image
import tensorflowjs as tfjs

classes = {0: 'Speed limit (20km/h)',
           1: 'Speed limit (30km/h)',
           2: 'Speed limit (50km/h)',
           3: 'Speed limit (60km/h)',
           4: 'Speed limit (70km/h)',
           5: 'Speed limit (80km/h)',
           6: 'End of speed limit (80km/h)',
           7: 'Speed limit (100km/h)',
           8: 'Speed limit (120km/h)',
           9: 'No passing',
           10: 'No passing veh over 3.5 tons',
           11: 'Right-of-way at intersection',
           12: 'Priority road',
           13: 'Yield',
           14: 'Stop',
           15: 'No vehicles',
           16: 'Vehicle > 3.5 tons prohibited',
           17: 'No entry',
           18: 'General caution',
           19: 'Dangerous curve left',
           20: 'Dangerous curve right',
           21: 'Double curve',
           22: 'Bumpy road',
           23: 'Slippery road',
           24: 'Road narrows on the right',
           25: 'Road work',
           26: 'Traffic signals',
           27: 'Pedestrians',
           28: 'Children crossing',
           29: 'Bicycles crossing',
           30: 'Beware of ice/snow',
           31: 'Wild animals crossing',
           32: 'End speed + passing limits',
           33: 'Turn right ahead',
           34: 'Turn left ahead',
           35: 'Ahead only',
           36: 'Go straight or right',
           37: 'Go straight or left',
           38: 'Keep right',
           39: 'Keep left',
           40: 'Roundabout mandatory',
           41: 'End of no passing',
           42: 'End no passing vehicle > 3.5 tons'}


def image_processing(img):
    data = []
    image = Image.open(img)
    image = image.resize((30, 30))
    data.append(np.array(image))
    X_test = np.array(data)
    Y_prediction = model.predict(X_test)
    return Y_prediction


def load_model(model_path):
    """
  Loads a saved model from a specified path.
  """
    print(f"Loading saved model from: {model_path}")
    real_one = tf.keras.models.load_model(model_path)
    print("Finished loading the model.\n")
    return real_one


model = load_model("traffic-sign-model")

predictions = image_processing("test.png")
listed_predictions = predictions.flatten().tolist()
max_prediction_index = np.argmax(listed_predictions)
print(f"Index of the highest probability in predictions: {max_prediction_index}")
print(f"Predicted class: {classes[np.argmax(listed_predictions)]}")

# tfjs.converters.save_keras_model(model, "tfjs_model")


