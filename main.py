from fastai.vision.all import *
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import zipfile
import warnings

warnings.filterwarnings("ignore")


def load_model():
    model = load_learner('fashion_classifier.pkl')
    return model


class ImageData(BaseModel):
    file: UploadFile
    description: str


app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ZIP_DIR = os.path.join(BASE_DIR, "zip_folder/zipped")
UNZIP_DIR = os.path.join(BASE_DIR, "zip_folder/unzipped")


@app.post("/zip")
async def predict(file: UploadFile):
    save_file_path = os.path.join(ZIP_DIR, file.filename)
    with open(save_file_path, "wb") as f:
        f.write(file.file.read())

    with zipfile.ZipFile(save_file_path, 'r') as zip_ref:
        zip_ref.extractall(UNZIP_DIR)

    model = load_model()
    result = []
    if os.listdir(UNZIP_DIR):
        print("Images found in the directory.")

        # Load images one after another
        for image in os.listdir(UNZIP_DIR):
            if image.lower().endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(UNZIP_DIR, image)
                # Process the image
                pred, pred_idx, probs = model.predict(img_path)
                result.append({image: pred})
                print(f"Predicted class: {pred}, Probability: {probs[pred_idx]}")

    else:
        print("No Images found in the directory.")
    return result
