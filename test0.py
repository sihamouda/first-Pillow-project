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

#watermark a specific image with a logo given an saved to a chosen path with the name new.jpg
def watermark(pathImage,pathLogo,pathSave):
    image=Image.open(pathImage)
    #resize the logo as the givin image so we can watermark even if the image is smaller than the watermark as they have the same ratio
    logo=Image.open(pathLogo).resize(image.width,image.height) 
    position = ((image.width - logo.width), (image.height - logo.height))
    image.paste(logo, position,logo)
    image.save(pathSave+'/new.jpg')

#testing
pathLogo='C:\\Users\\aniss\\Desktop\\PillowStuff\\Watermark\\wm.png'
pathImage='C:\\Users\\aniss\\Desktop\\PillowStuff\\TLP_0653-Edit_resized.jpg'
pathSave='C:\\Users\\aniss\\Desktop\\PillowStuff'

resizeALL(pathSave,pathSave)
watermark(pathImage,pathLogo,pathSave)