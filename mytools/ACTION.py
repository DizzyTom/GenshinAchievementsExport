import pyautogui
from .VRBS import vrbs
import time
pyautogui.PAUSE=0.001
def click(x,y):
	pyautogui.click(x,y)
	time.sleep(1)
def moveTo(x,y):
	pyautogui.moveTo(x,y)
def lscroll():
	for i in range(vrbs.LSCROLL):
		moveTo((vrbs.LX1+ vrbs.LX2)//2, (vrbs.LY1+ vrbs.LY2)//2)
		pyautogui.scroll(-1)
	moveTo(10,10)
	time.sleep(0.5)
def rscroll():
	for i in range(vrbs.RSCROLL):
		moveTo((vrbs.RX1+ vrbs.RX2)//2, (vrbs.RY1+ vrbs.RY2)//2)
		pyautogui.scroll(-1)
	moveTo(10,10)
	time.sleep(0.5)

def screen_shot(name=None,region=None):
	if name==None:
		if region==None:
			image=pyautogui.screenshot()
		else:
			image=pyautogui.screenshot(region=region)
	else:
		
		name='result/'+str( vrbs.img_cnt )+'_'+name+'.png'
		vrbs.img_cnt+=1
		if region==None:
			image=pyautogui.screenshot(name)
		else:
			image=pyautogui.screenshot(name,region=region)
	return image