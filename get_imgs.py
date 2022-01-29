from mytools.ACTION import click, lscroll, screen_shot
import keyboard
import ctypes
from mytools.OCR import get_left_infos
from mytools.OCR import get_right_images
import os
def main():
    text_list=[]
    while True: 
        texts,rects= get_left_infos( screen_shot())
        all_seen=True
        for text,rect in zip(texts,rects):
            if not text in text_list:
                text_list.append(text)
                click(rect[0]+rect[2]//2,rect[1]+rect[3]//2)
                get_right_images(text)
                all_seen=False 
        if all_seen:
            break
        else:
            lscroll()
if __name__=='__main__':
    if ctypes.windll.shell32.IsUserAnAdmin():
        for x in os.listdir('result'):
            os.remove('result/'+x)
        print("按r开始")
        keyboard.wait('r')
        main()
    else:
        print("没有管理员权限")
