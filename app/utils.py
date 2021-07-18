from typing import Dict
from io import BytesIO
import numpy as np
from PIL import Image
from fastai.vision.all import *

def read_image(file: bytes) -> PILImage:
    img = Image.open(BytesIO(file))
    fastimg = PILImage.create(np.array(img.convert('RGB')))

    return fastimg

def get_breed(x):
    return x.split('_')[0]
