from PIL import Image
import os 

def CreateDir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("A new directory was created!")

def resizeALL(pathSource,pathDestination):
    files=os.listdir(pathSource)
    CreateDir(pathDestination)
    for file in files:
        if file.endswith(".jpg"):
            Image.open(file).resize((1620,2430)).save(pathDestination+"\\"+ os.path.splitext(file)[0]+"_resized.jpg")


resizeALL(".","C:\\Users\\aniss\\Desktop\\PillowStuff\\NewFolder2")