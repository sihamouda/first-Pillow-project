from PIL import Image
import os 

#Create a directory if it does not exist
def CreateDir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("A new directory was created!")

#resize all .jpg photos that exist in a specific path (pathSource)
#and save the result in specific path (pathDestination)
#note:pathDestination will be created if it does not exists
def resizeALL(pathSource,pathDestination):
    files=os.listdir(pathSource)
    CreateDir(pathDestination)
    for file in files:
        if file.endswith(".jpg"):
            Image.open(file).resize((1620,2430)).save(pathDestination+"/"+ os.path.splitext(file)[0]+"_resized.jpg")

#testing
resizeALL(".","C:\\Users\\aniss\\Desktop\\PillowStuff\\NewFolder2")