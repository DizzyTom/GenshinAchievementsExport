from .VRBS import vrbs
def minDistance(w1,w2):
    m,n = len(w1),len(w2)
    if(m==0):
	    return m
    if(n==0):
	    return n
    step = [[0]*(n+1)for _ in range(m+1)]
    for i in range(1,m+1):step[i][0]=i
    for j in range(1,n+1):step[0][j]=j
    for i in range(1,m+1):
	    for j in range(1,n+1):
		    if w1[i-1] == w2[j-1] :
			    diff=0
		    else:diff=1
		    step[i][j] = min(step[i-1][j-1],min(step[i-1][j],step[i][j-1]))+diff	
    return step[m][n]
def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False


def is_number(uchar):
    if uchar >= u'\u0030' and uchar<=u'\u0039':
        return True
    else:
        return False

 
def is_alphabet(uchar):
    if (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):
        return True
    else:
        return False


def is_other(uchar):
    if not (is_chinese(uchar) or is_number(uchar) or is_alphabet(uchar)):
        return True
    else:
        return False


def CH_EN(txt):
    ans=''
    for x in txt:
        if not is_other(x):
            ans+=x 
    return ans

def Find(a,LIST=vrbs.LIST_NAMES):
    dis=[]
    for name in LIST:
        dis.append(minDistance(CH_EN(a),CH_EN(name)))
    return LIST[dis.index(min(dis))]

def Find2(a,b,lista,listb):
    dis=[]
    for namea,nameb in zip(lista,listb):
        dis.append(minDistance(CH_EN(a+b),CH_EN(namea+nameb)))
    index=dis.index(min(dis))
    return lista[index],listb[index]