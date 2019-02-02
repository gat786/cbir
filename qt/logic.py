from LSBSteg import LSBSteg as steganography
import cv2
from stegano import lsb

def checkIfDataIsHidden(imagePath):
    text = lsb.reveal(imagePath)
    return text

def addSecret(imagePath,data):    
    secret = lsb.hide(imagePath,data)
    secret.save('/temp/editing.png')






# steg = steganography(cv2.imread('bing.jpg'))
# new_im = steg.encode_text("message to be encoded")
# cv2.imwrite("out.png",new_im)

# im = cv2.imread("hello.png")
# steg = steganography(im)
# print(steg.decode_text())
# if(len(steg.decode_text())>0):
#     print("message detected")
# else:
#     print("no hidden message")