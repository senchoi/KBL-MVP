from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, sys
url="http://m.kbl.or.kr/stats/player.asp"
try:
    html_doc=urlopen(url)
except:
    print("인터넷을 연결하세요")
    sys.exit()

bs=BeautifulSoup(html_doc,'html.parser')
top10shooter=[]
playerPoints=[]

playerDic=[]
def getTop10():
    td_list=bs.find_all('td',class_='l39')
    for i,player in enumerate(td_list):
        if i<10:
            top10shooter.append(player.text)
    '''
    for player in top10shooter:
        print(player)
    '''

def getTop10PlayerPoints():
    list1=[]
    pointList=bs.find_all('td')
    for tag in pointList:
        if bool(re.match(r'^-?\d+(?:\.\d+)?$', tag.text)):
            list1.append(float(tag.text))
    for i in range(10):
        list1.pop(0)
    for i in range(10):
        templist=[]
        for j in range(9):
            templist.append(list1.pop(0))
        playerPoints.append(templist)
    '''
    for i in playerPoints:
        print(i)
    '''

def makePlayerDic(player,points,img,num=10):
    templist=[sum(points[i])for i in range(num)]
    return list(zip(player,templist,img))

def rank(Dic):
    return sorted(Dic, key=(lambda x:x[1]), reverse=True)
getTop10()
playerimg=['img/'+name+'edit.jpg' for name in top10shooter]
getTop10PlayerPoints()
playerDic=makePlayerDic(top10shooter,playerPoints,playerimg)
ranking=rank(playerDic)
