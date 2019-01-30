from LSBSteg import LSBSteg as steganography
import cv2
from stegano import lsb

secret = lsb.hide('hello.png','hello')
secret.save('secret.png')

print(lsb.reveal('hello.png'))





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