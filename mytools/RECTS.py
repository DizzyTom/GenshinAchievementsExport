def cross_2rects(recta,rectb):
    centera=[recta[0]+recta[2]/2,recta[1]+recta[3]/2]
    centerb=[rectb[0]+rectb[2]/2,rectb[1]+rectb[3]/2]
    if abs(centera[0]-centerb[0])< (recta[2]+rectb[2])/2 and abs(centera[1]-centerb[1])< (recta[3]+ rectb[3]) /2:
        return True
    return False

def cross_rects(recta,rects):
    for rect in rects:
        if cross_2rects(rect,recta):
            return True
    return False

def filter_rects(rects,area,minw,maxw,minh,maxh):
    ans=[]
    for rect in rects:
        if cross_2rects(rect,area) and minw<rect[2]<maxw and minh<rect[3]<maxh:
            ans.append(rect)
    return ans