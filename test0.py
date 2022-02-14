from PIL import Image
import os 

def resizeALL(pathSource,pathDestination):
    files=os.listdir(pathSource)
    for file in files:
        if file.endswith(".jpg"):
            Image.open(file).resize((1620,2430)).save(pathDestination+"\\"+ os.path.splitext(file)[0]+"_resized.jpg")

resizeALL(".","C:\\Users\\aniss\\Desktop\\PillowStuff\\NewFolder")