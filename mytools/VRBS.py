import json
import os
class VRBS:
    def __init__(self):
        with open('parameters/parameters.json','r',encoding='utf-8') as f:
            data=json.load(f)
        self.LX1=data['l_x1']
        self.LY1=data['l_y1']
        self.LX2=data['l_x2']
        self.LY2=data['l_y2']
        self.LNW=data['l_min_w']
        self.LXW=data['l_max_w']
        self.LNH=data['l_min_h']
        self.LXH=data['l_max_h']
        self.RX1=data['r_x1']
        self.RY1=data['r_y1']
        self.RX2=data['r_x2']
        self.RY2=data['r_y2']
        self.RNW=data['r_min_w']
        self.RXW=data['r_max_w']
        self.RNH=data['r_min_h']
        self.RXH=data['r_max_h']
        self.LRT=data['l_ratio']
        self.RRT=data['r_ratio']        
        self.LSCROLL=data['l_scroll']
        self.RSCROLL=data['r_scroll']

        self.left_area=[data['l_x1'],data['l_y1'],data['l_x2']-data['l_x1'],data['l_y2']-data['l_y1']]
        self.right_area=[data['r_x1'],data['r_y1'],data['r_x2']-data['r_x1'],data['r_y2']-data['r_y1']]
        
        with open('resource/已知栏目.txt','r') as f:
            txt=f.readlines()
        self.LIST_NAMES=[x.strip() for x in txt]

        self.img_cnt=0
        if not os.path.exists('result'):
            os.makedirs('result')
        
vrbs=VRBS()