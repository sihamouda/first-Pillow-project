from PIL import Image
import os 

def resizeALL(path):
    files=os.listdir(path)
    for file in files:
        if file.endswith(".jpg"):
            Image.open(file).resize((1620,2430)).save(os.path.splitext(file)[0]+"_resized.jpg")

resizeALL(".")