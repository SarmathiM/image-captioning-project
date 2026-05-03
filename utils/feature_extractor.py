import numpy as np

model = None

try:
    from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
    from tensorflow.keras.preprocessing import image

    model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

    print("✔ ResNet Model Loaded Successfully")

except Exception as e:
    print("❌ ResNet Load Error:", e)
    model = None


def extract_features(img_path):
    if model is None:
        return np.zeros((1, 2048), dtype=np.float32)

    try:
        img = image.load_img(img_path, target_size=(224, 224))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)

        features = model.predict(img, verbose=0)

        return features

    except Exception as e:
        print("❌ Feature extraction error:", e)
        return np.zeros((1, 2048), dtype=np.float32)
    