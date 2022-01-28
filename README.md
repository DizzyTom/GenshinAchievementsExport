# genshin_achievements

#### 介绍
基于图像处理和字符识别，将原神中的成就导出为excel 并与全成就列表比对，从而知道自己哪些成就未完成。

#### 2022/1/29
之前的程序参数都写死了，不能适应不同设备的需求，改起来又太麻烦，所以重新设计程序。(假定原神都是以独占全屏模式运行，分辨率未知）

今天先把交互给写了。交互在just_paras.py。
我的参数是根据1920x1080分辨率调整的，如果跟我一样可以直接用我的参数。
如果不一样，按照下面的步骤操作。
首先，截取一张类似parameters/screen_shot.png 的图。把原图覆盖掉。
![Image text](https://raw.githubusercontent.com/DizzyTom/GenshinAchievementsExport/main/parameters/screen_shot.png)
l,r分别代表左和右。 x1,y1,x2,y2为矩形区域的端点坐标。w,h 分别表示过滤有具体成就内容矩形的宽度和高度。ratio用来控制分界线。
通过滑动滑块来调整参数(会自动保存），最终达到的效果如INTRODUCE/交互效果.png。
![Image text](https://raw.githubusercontent.com/DizzyTom/GenshinAchievementsExport/main/INTRODUCE/%E4%BA%A4%E4%BA%92%E6%95%88%E6%9E%9C.png)
按 ’ESC‘键 可以退出交互。