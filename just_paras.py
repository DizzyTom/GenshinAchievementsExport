import json 
import cv2
from mytools.RECTS import *
def draw_rect(image,bbox,color,thick=2):
    cv2.rectangle(image,(bbox[0],bbox[1]),(bbox[0]+bbox[2],bbox[1]+bbox[3]),color,thick)
def onChange(data):
    for k in data.keys():
        trackbar_window_name= left_trackbar_window_name if 'l' in k else right_trackbar_window_name
        pos=cv2.getTrackbarPos(k, trackbar_window_name)
        if pos>0:
            data[k]=pos
        else:
            return data
    with open(json_path,'w',encoding='utf-8') as f:
        json.dump(data,f)
    return data
if __name__=='__main__':
    json_path='parameters/parameters.json' 
    image_path='parameters/screen_shot.png'
    image_window_name='Just_parameters'
    left_trackbar_window_name='Left_Trackbars'
    right_trackbar_window_name='Right_Trackbars'
    with open(json_path,'r',encoding='utf-8') as f:
        data=json.load(f)

    image=cv2.imread(image_path,cv2.IMREAD_COLOR)
    image_height=image.shape[0]
    image_width=image.shape[1]

    cv2.namedWindow(left_trackbar_window_name,cv2.WINDOW_NORMAL)
    cv2.resizeWindow(left_trackbar_window_name, 800,600)
    cv2.namedWindow(right_trackbar_window_name,cv2.WINDOW_NORMAL)
    cv2.resizeWindow(right_trackbar_window_name, 800,600)
    cv2.namedWindow(image_window_name,cv2.WINDOW_NORMAL)
    cv2.resizeWindow(image_window_name,1280,800)

    for i,(k,v) in enumerate(data.items()):
        trackbar_window_name= left_trackbar_window_name if 'l' in k else right_trackbar_window_name
        count= image_width if i%2==0 else image_height
        cv2.createTrackbar(k, trackbar_window_name, v, count, onChange)
    red=(0,0,255)
    blue=(255,0,0)
    green=(0,255,0)
    light_blue=(255,255,0)
    yellow=(0,255,255)
    while True:
        data=onChange(data)
        image_show=image.copy()
        left_area=[data['l_x1'],data['l_y1'],data['l_x2']-data['l_x1'],data['l_y2']-data['l_y1']]
        right_area=[data['r_x1'],data['r_y1'],data['r_x2']-data['r_x1'],data['r_y2']-data['r_y1']]
        draw_rect(image_show,left_area,blue)
        draw_rect(image_show,right_area,green)
        image_canny=cv2.Canny(image,50,100)
        contours=cv2.findContours(image_canny,cv2.CHAIN_APPROX_SIMPLE,cv2.RETR_CCOMP)[0]
        rects=[cv2.cv2.boundingRect(contour) for contour in contours]
        left_rects= filter_rects(rects,left_area,data['l_min_w'],data['l_max_w'],data['l_min_h'],data['l_max_h'])
        right_rects=filter_rects(rects,right_area,data['r_min_w'],data['r_max_w'],data['r_min_h'],data['r_max_h'])
        for rect in left_rects:
            draw_rect(image_show,rect,red)
            l_ratio=data['l_ratio']/image_width
            cv2.line(image_show,(rect[0]+int(l_ratio*rect[2]),rect[1]),(rect[0]+int(l_ratio*rect[2]),rect[1]+rect[3]),yellow,2)
        for rect in right_rects:
            draw_rect(image_show,rect,light_blue)
            r_ratio=data['r_ratio']/image_height
            cv2.line(image_show,(rect[0]+int(r_ratio*rect[2]),rect[1]),(rect[0]+int(r_ratio*rect[2]),rect[1]+rect[3]),yellow,2)
        cv2.imshow(image_window_name,image_show)
        if cv2.waitKey(1)==27:
            break

    