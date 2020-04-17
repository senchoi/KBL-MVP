
from kivy.config import Config
Config.set('kivy', 'default_font', [
    'NanumGothic',
    'NanumGothic.ttf'
])

from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import *

try:
    from bigdataW4 import ranking
except:
    class MainApp(App):
        def build(self):
            return Label(text="Connect to internet\n인터넷을 연결하세요")
    if __name__ == '__main__':
        MainApp().run()


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x+1)+". "+ranking[x][0]+"\n"+
                      "{:.1f}".format(ranking[x][1])+
                      " points",
                      'on_press':lambda x=x:self.showPopup(x)}
                     for x in range(10)]

        
    def showPopup(self,i):
        popup = Popup(title=ranking[i][0],
            content=Image(source=ranking[i][2], size_hint_y=1, size_hint_x=1,
                          allow_stretch=True),
            size_hint=(None, None), size=("300dp", "300dp"))
        popup.open()
        

class MainApp(App):
    def build(self):
        return RV()

if __name__ == '__main__':
    MainApp().run()
