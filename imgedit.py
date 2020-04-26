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
    for i in range(2):
        list1.append(bslist.findChildren('dt')[i].text)
        list2.append(bslist.findChildren('dd')[i+1].text)
    plist=list(zip(list1,list2))
    playerplist.append(plist)

def drawtext(player, msg):
    image = Image.open('img/'+player+'.jpg')
    draw = ImageDraw.Draw(image)
    if image.size[0]<250:
        font = ImageFont.truetype('NanumGothic.ttf', size=8)
    else:
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
             playerplist[i][1][0]+':'+playerplist[i][1][1])
