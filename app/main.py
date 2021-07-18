from fastapi import FastAPI, File, UploadFile
from fastai.vision.all import *
from utils import read_image
from json_models.response import Response

app = FastAPI()


@app.post("/predict/", response_model=Response)
async def predict(myfile: UploadFile = File(...)):
    image = read_image(await myfile.read())
    # image = await myfile.read()
    path = Path()
    learn = load_learner(path/'models/model.pkl')
    get_breed, _ , probs = learn.predict(image)

    if probs[0] > probs[1] and probs[0] > probs[2]:
        return {
            "prediction": "german shepherd",
            "probability": probs[0].item()
        }
    elif probs[1] > probs[0] and probs[1] > probs[2]:
        return {
            "prediction": "labrador",
            "probability": probs[1].item()
        }
    elif probs[2] > probs[1] and probs[2] > probs[1]:
        return {
            "prediction": "shihtzu",
            "probability": probs[2].item()
        }

# if __name__ == '__main__':
#     def get_breed(x):
#         return x.split('_')[0]