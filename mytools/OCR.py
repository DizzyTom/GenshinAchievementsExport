from .VRBS import vrbs
from .RECTS import *
from paddleocr import PaddleOCR
import cv2
import numpy as np
from .TEXT import Find
from .ACTION import rscroll, screen_shot
import os
ocr= PaddleOCR(lang='ch')

def Image2Result(image):   
    result= ocr.ocr(image)
    texts=[]
    for line in result:
        text=line[1][0]
        rect=[line[0][0][0],line[0][0][1],line[0][2][0]-line[0][0][0],line[0][2][1]-line[0][0][1]]
        texts.append(text)
    return texts
def get_left_infos(image):
    image=cv2.cvtColor(np.asarray(image),cv2.COLOR_RGB2BGR)
    image_canny=cv2.Canny(image,50,100)
    contours=cv2.findContours(image_canny,cv2.CHAIN_APPROX_SIMPLE,cv2.RETR_CCOMP)[0]
    rects=[cv2.cv2.boundingRect(contour) for contour in contours]
    left_rects= filter_rects(rects,vrbs.left_area,vrbs.LNW, vrbs.LXW ,vrbs.LNH , vrbs.LXH)
    left_rects= short_rects(left_rects)
    left_rects.sort(key=lambda x:x[1])
    texts=[]
    for rect in left_rects:
        left=rect[0]
        up=rect[1]
        right=rect[0]+rect[2]
        down=rect[1]+rect[3]
        left=left+int( vrbs.LRT/image.shape[1]*(right-left))
        text= Find(Image2Result( image[up:down,left:right]))
        texts.append(text)
    return texts,left_rects
def get_right_images(name):
    last_img=[]
    while True:
        image=screen_shot(name,region=vrbs.right_area)        
        image=cv2.cvtColor(np.asarray(image),cv2.COLOR_RGB2BGR)
        if len(last_img)==0 or cv2.PSNR(last_img,image)<25:
            rscroll()
            last_img=image
        else:
            vrbs.img_cnt-=1
            os.remove('result/'+str( vrbs.img_cnt )+'_'+name+'.png')
            break
