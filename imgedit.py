from bigdataW4 import ranking, top10shooter, playerimg
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

playerplist=[]
def getprofiletext(p_i):
    list1=[]
    list2=[]
    plist=[]
    baseurl="https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query={}"
    global playerplist
    
    htmldoc=urlopen(baseurl.format(quote(top10shooter[p_i])))
    bsprofile=BeautifulSoup(htmldoc,'html.parser')
    bslist=bsprofile.find('dl',class_='detail_profile')
    for i in range(3):
        list1.append(bslist.findChildren('dt')[i].text)
        list2.append(bslist.findChildren('dd')[i+1].text)
    plist=list(zip(list1,list2))
    playerplist.append(plist)

def drawtext(player, msg):
    image = Image.open('img/'+player+'.jpg')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('NanumGothic.ttf', size=16)
    
    (x, y) = (10, 10)
    message = msg
    outline='rgb(255, 255, 255)'
    color = 'rgb(0, 0, 0)'
    draw.text((x-1, y-1), message, fill=outline, font=font)
    draw.text((x+1, y-1), message, fill=outline, font=font)
    draw.text((x+1, y+1), message, fill=outline, font=font)
    draw.text((x-1, y+1), message, fill=outline, font=font)
    draw.text((x, y), message, fill=color, font=font)
    image.save('img/'+player+'edit.jpg')

for i in range(10):
    getprofiletext(i)
for i,name in enumerate(top10shooter):
    drawtext(name,playerplist[i][0][0]+':'+playerplist[i][0][1]+'\n'+
             playerplist[i][1][0]+':'+playerplist[i][1][1][:17] + '\n'+
             playerplist[i][1][1][17:35]+('\n'if playerplist[i][1][1][17:35] else '')+
             playerplist[i][2][0]+':'+playerplist[i][2][1][:15] +'\n'+
             playerplist[i][2][1][15:33]+('\n'if playerplist[i][2][1][15:33] else '')+
             playerplist[i][2][1][33:51]+('\n'if playerplist[i][2][1][33:51] else '')+
             playerplist[i][2][1][51:69]+('\n'if playerplist[i][2][1][51:69] else ''))
