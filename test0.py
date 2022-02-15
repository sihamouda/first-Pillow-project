from PIL import Image
import os 

#Create a directory if it does not exist
def CreateDir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("A new directory was created!")

#resize an image with a specific path and save it in a chosen one
def resizeImage(pathImage,pathSave):
    image=Image.open(pathImage).resize((1620,2430))
    fileName=os.path.basename(pathImage).split('.')[0]
    image.save(pathSave+'/'+fileName+'_resized.jpg',dpi=(150,150)) 

#resize all .jpg photos that exist in a specific path (pathSource)
#and save the result in specific path (pathDestination)
#note:pathDestination will be created if it does not exists
def resizeALL(pathSource,pathDestination):
    files=os.listdir(pathSource)
    CreateDir(pathDestination)
    for file in files:
        if file.endswith('.jpg'):
            resizeImage(file,pathDestination)

#watermark a specific image with a logo given an saved to a chosen path with the name new.jpg
def watermarkImage(pathImage,pathLogo,pathSave):
    image=Image.open(pathImage)
    #resize the logo as the givin image so we can watermark even if the image is smaller than the watermark as they have the same ratio
    logo=Image.open(pathLogo).resize((image.width,image.height),Image.BICUBIC) 
    position = ((image.width - logo.width), (image.height - logo.height))
    image.paste(logo, position,logo)
    #save the image with the same name + '_watermarked'
    fileName=os.path.basename(pathImage).split('.')[0]
    image.save(pathSave+'/'+fileName+'_watermarked.jpg')

#watermark all .jpg photos that exist in a specific path (pathSource)
#and save the result in specific path (pathDestination)
#note:pathDestination will be created if it does not exists
def watermarkALL(pathSource,pathLogo,pathDestination):
    files=os.listdir(pathSource)
    CreateDir(pathDestination)
    for file in files:
        if file.endswith('.jpg'):
            watermarkImage(pathSource+'/'+file,pathLogo,pathDestination)
#testing
pathLogo='C:\\Users\\aniss\\Desktop\\PillowStuff\\Watermark\\wm.png'
pathImage='C:\\Users\\aniss\\Desktop\\PillowStuff\\sad dog.jpg'
pathSave='C:\\Users\\aniss\\Desktop\\PillowStuff'

resizeImage(pathImage,pathSave)