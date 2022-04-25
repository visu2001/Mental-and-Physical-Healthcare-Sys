from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton, MDFloatingActionButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.behaviors.magic_behavior import MagicBehavior
from kivy.properties import ObjectProperty
import pandas as pd
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
import re
import PIL

Window.size = (460, 700)
screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    SignupScreen:
    UploadScreen:
    Exercise:
    Yoga:
    Entertainment:
    UserProfile:
    P:
    Y1:
    Y2:
    Y3:
    Y4:
    E1:
    E2:
    E3:
    E4:

<MenuScreen>:
    name: 'menu'

    Screen:
        #:set w 400
        #:set h 400
        canvas.before:
            Rectangle:
                pos: self.pos
                source: 'Capture.png'
                pos:(40,200)
                size:(w,h)
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                title: 'Demo Application'
                halign:'center'
                elevation:10
            MDLabel:
                text:'Health App'
                halign:'center'
                theme_text_color:'Custom'
                text_color:(1, 0, 0)
                font_style:'H4' 
                bold:True
        MDRectangleFlatButton:
            text:'Login'
            pos_hint:{'center_x': 0.4, 'center_y': 0.19}
            text_color:(1, 0, 0)
            on_press: 
                root.manager.current = 'profile'
                root.manager.transition.direction = 'up'
        MDRectangleFlatButton:
            text:'Sign-up'
            pos_hint:{'center_x': 0.6, 'center_y': 0.19}
            text_color:(1, 0, 0)
            on_press: 
                root.manager.current = 'sig'
                root.manager.transition.direction = 'up'

        MDFloatingActionButton
            icon:'instagram'
        MDFloatingActionButton
            icon:'youtube'
            pos_hint:{'x': 0.42, 'y': 0}
        MDFloatingActionButton
            icon:'gmail'
            pos_hint:{'x': .88, 'y': 0}

<ProfileScreen>:
    name: 'profile'
    email : email
    pwd : pwd
    Screen:
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                title: 'Demo Application'
                halign:'center'
                elevation:10
            ScrollView:
        MDFloatingActionButton
            icon:'instagram'
        MDFloatingActionButton
            icon:'youtube'
            pos_hint:{'x': 0.42, 'y': 0}
        MDFloatingActionButton
            icon:'gmail'
            pos_hint:{'x': .88, 'y': 0}
        MDRectangleFlatButton:
            text: 'Back'
            pos_hint: {'center_x':0.5,'center_y':0.2}
            on_press: root.manager.current = 'menu'
        MDTextField:
            id:email
            hint_text:"Enter Email-ID"
            #helper_text:"or click on forgot username"
            helper_text_mode: "on_focus" #persistent
            icon_right:"basketball"
            icon_right_color: app.theme_cls.primary_color #(1,0,0)
            pos_hint:{'center_x':0.5,'center_y':0.6}
            size_hint_x:None  #size_hint:(0.5,0.1)
            width:300
        MDTextField:
            id:pwd
            hint_text:"Enter Password"
            #helper_text:"or click on forgot username"
            helper_text_mode: "on_focus" #persistent
            icon_right:"basketball"
            icon_right_color: app.theme_cls.primary_color #(1,0,0)
            pos_hint:{'center_x':0.5,'center_y':0.5}
            size_hint_x:None  #size_hint:(0.5,0.1)
            width:300
        MDRectangleFlatButton:
            text:'Enter'
            pos_hint:{'center_x':0.5,'center_y':0.4}
            on_press: 
                # root.validate()
                root.manager.current = 'upload'
                root.manager.transition.direction = 'right'
<SignupScreen>:
    name:'sig'
    name2 : name2
    email : email
    pwd : pwd
    Screen:
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                title: 'Demo Application'
                halign:'center'
                elevation:10
            ScrollView:
        MDFloatingActionButton
            icon:'instagram'
        MDFloatingActionButton
            icon:'youtube'
            pos_hint:{'x': 0.42, 'y': 0}
        MDFloatingActionButton
            icon:'gmail'
            pos_hint:{'x': .88, 'y': 0}
        MDRectangleFlatButton:
            text: 'Back'
            pos_hint: {'center_x':0.5,'center_y':0.2}
            on_press: root.manager.current = 'menu'
        MDTextField:
            id:name2
            hint_text:"Enter Username"
            #helper_text:"or click on forgot username"
            helper_text_mode: "on_focus" #persistent
            icon_right:"basketball"
            icon_right_color: app.theme_cls.primary_color #(1,0,0)
            pos_hint:{'center_x':0.5,'center_y':0.7}
            size_hint_x:None  #size_hint:(0.5,0.1)
            width:300
        MDTextField:
            id:email
            hint_text:"Enter Email-ID"
            #helper_text:"or click on forgot username"
            helper_text_mode: "on_focus" #persistent
            icon_right:"basketball"
            icon_right_color: app.theme_cls.primary_color #(1,0,0)
            pos_hint:{'center_x':0.5,'center_y':0.6}
            size_hint_x:None  #size_hint:(0.5,0.1)
            width:300
        MDTextField:
            id:pwd
            hint_text:"Enter Password"
            #helper_text:"or click on forgot username"
            helper_text_mode: "on_focus" #persistent
            icon_right:"basketball"
            icon_right_color: app.theme_cls.primary_color #(1,0,0)
            pos_hint:{'center_x':0.5,'center_y':0.5}
            size_hint_x:None  #size_hint:(0.5,0.1)
            width:300
        MDRectangleFlatButton:
            text:'Enter'
            pos_hint:{'center_x':0.5,'center_y':0.4}
            on_press: 
                root.signupbtn()
                root.manager.transition.direction = 'right'
    
<UploadScreen>:
    name: 'upload'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                Screen:
                    BoxLayout:
                        orientation: 'vertical'

                        MDToolbar:
                            title: 'Demo Application'
                            elevation: 10
                            left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]

                        OneLineIconListItem:
                            text:'          ENTERTAINMENT'        
                            font_style:'Subtitle1'
                            bold:'True'
                            IconLeftWidget:
                                icon:'movie'   
                                on_press: 
                                    root.manager.current = 'ent'
                                    root.manager.transition.direction = 'down'
                        Carousel:
                            direction:'right'
                            Image:
                                source:'q1.jpg'
                            Image:
                                source:'q2.jpg'
                            Image:
                                source:'q3.jpg'
                            Image:
                                source:'q4.jpg'

                        OneLineIconListItem:
                            text:'          EXERCISE'        
                            font_style:'Subtitle1'
                            bold:'True'
                            IconLeftWidget:
                                icon:'jump-rope'   
                                on_press: 
                                    root.manager.current = 'exe'
                                    root.manager.transition.direction = 'left'

                        ScrollView:
                            GridLayout:
                                rows:2
                                cols:2
                                Image:
                                    source:'ex1.jpeg'
                                Image:
                                    source:'ex2.jpeg'
                                Image:
                                    source:'ex3.jpeg'
                                Image:
                                    source:'ex4.jpeg'  
                        OneLineIconListItem:
                            text:'          YOGA'        
                            font_style:'Subtitle1'
                            bold:'True'
                            IconLeftWidget:
                                icon:'yoga'   
                                on_press: 
                                    root.manager.current = 'yog'
                                    root.manager.transition.direction = 'up'
                        ScrollView:
                            GridLayout:
                                rows:2
                                cols:2
                                Image:
                                    source:'1.jpg'
                                Image:
                                    source:'5.JPG'
                                Image:
                                    source:'4.JPG'
                                Image:
                                    source:'8.JPG'  
                        OneLineIconListItem:
                            text:'          SHOPPING'        
                            font_style:'Subtitle1'
                            bold:'True'
                            IconLeftWidget:
                                icon:'shopping'   
                                on_press:
                                    import webbrowser
                                    webbrowser.open("https://www.flipkart.com/search?q=gym+equipments+for+home&sid=qoc%2Camf%2Cvh3&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_4_na_na_na&as-pos=2&as-type=RECENT&suggestionId=gym+equipments+for+home%7CFitness+Kits&requestId=a61b74c7-39fb-47d9-82e0-173599ee9fcf&as-backfill=on") 

                        Carousel:
                            direction:'right'
                            Image:
                                source:'g2.jpg'
                            Image:
                                source:'g1.jpg'
                            Image:
                                source:'g3.webp'
                            Image:
                                source:'g4.jpg'
                    MDFloatingActionButton
                        icon:'google-home'
                        pos_hint:{'x': .88, 'y': 0}
                        on_press: 
                            root.manager.current = 'upload'












                        Widget:
                        ScrollView:

            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation:'vertical'
                    spacing:'4dp'
                    padding:'1dp'
                    Image:
                        source:'VISU UTKARSH.jpg'
                    MDLabel:
                        text:'                    VISU UTKARSH'
                        bold:'True'
                        font_style:'H6'
                        size_hint_y:None
                        height:self.texture_size[1]
                    MDLabel:
                        text:'                                visutkarsh2000@gamil.com'
                        font_style:'Caption'
                        size_hint_y:None
                        height:self.texture_size[1]
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text:'Entertainment'
                                IconLeftWidget:
                                    icon:'movie'
                                    on_press: 
                                        root.manager.current = 'ent'
                                        root.manager.transition.direction = 'down'    
                            OneLineIconListItem:
                                text:'Exercise'
                                IconLeftWidget:
                                    icon:'jump-rope'
                                    on_press: 
                                        root.manager.current = 'exe'
                                        root.manager.transition.direction = 'up'
                            OneLineIconListItem:
                                text:'Yoga'
                                IconLeftWidget:
                                    icon:'yoga'
                                    on_press: 
                                        root.manager.current = 'yog'
                                        root.manager.transition.direction = 'up'    
                            OneLineIconListItem:
                                text:'Profile'
                                IconLeftWidget:
                                    icon:'face-profile'    
                                    on_press: 
                                        root.manager.current = 'userp'
                                        root.manager.transition.direction = 'right'
                            OneLineIconListItem:
                                text:'Logout'
                                IconLeftWidget:
                                    icon:'logout' 
                                    on_press: 
                                        root.manager.current = 'menu'
                                        root.manager.transition.direction = 'right'

<Exercise>:
    name:'exe'
    Screen:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'EXERCISE'
                        halign:'center'
                        right_action_items:[['keyboard-backspace', lambda x: setattr(root.manager, 'current', 'upload')]]
                        left_action_items:[['jump-rope']]
                        elevation:10
                    OneLineIconListItem:
                        text:'          CROSS BAR'        
                        font_style:'Subtitle1'
                        bold:'True'
                        IconLeftWidget:
                            icon:'google-play' 
                    Image:
                        source:'crossbar.gif'
                    OneLineIconListItem:
                        text:'          COBRA POSITION'        
                        font_style:'Subtitle1'
                        bold:'True'
                        IconLeftWidget:
                            icon:'google-play' 
                    Image:
                        id:gif
                        source:'cobra.gif'
                    OneLineIconListItem:
                        text:'          WIDE ARM PUSH-UP'        
                        font_style:'Subtitle1'
                        bold:'True'
                        IconLeftWidget:
                            icon:'google-play' 
                    Image:
                        source:'widearm.gif'
                    OneLineIconListItem:
                        text:'          PUSH-UP'        
                        font_style:'Subtitle1'
                        bold:'True'
                        IconLeftWidget:
                            icon:'google-play' 
                    Image:
                        source:'KTnX664Lc.gif'
                    ScrollView:          
                MDFloatingActionButton
                    id : c1
                    icon:'google-play'
                    pos_hint:{'x':0.32, 'y': 0.72}
                    on_press:
                        root.count1()
                        # import webbrowser
                        # webbrowser.open("shorturl.at/anuDG=on") 

                MDFloatingActionButton
                    id:c2
                    icon:'google-play'
                    pos_hint:{'x':0.32, 'y': 0.52}
                    on_press:
                        root.count2()
                        # import webbrowser
                        # webbrowser.open("shorturl.at/uAR37=on") 
                MDFloatingActionButton
                    id:c3
                    icon:'google-play'
                    pos_hint:{'x':0.32, 'y': 0.32}
                    on_press: gif.anim_delay = 0.10
                    on_press: gif._coreimage.anim_reset(True)
                    on_press:
                        root.count3()
                        # import webbrowser
                        # webbrowser.open("shorturl.at/dvHIL=on") 
                MDFloatingActionButton
                    id:c4
                    icon:'google-play'
                    pos_hint:{'x':0.32, 'y': 0.12}
                    on_press:
                        root.count4()
                        # import webbrowser
                        # webbrowser.open("shorturl.at/evzIK=on") 
                MDFloatingActionButton
                    icon:'google-home'
                    pos_hint:{'x': .88, 'y': 0}
                    on_press: 
                        root.manager.current = 'upload'
                MDFloatingActionButton
                    icon:'monitor'
                    pos_hint:{'x':0.88, 'y': 0.72}
                    on_press: 
                        root.info1()  
                MDFloatingActionButton
                    icon:'monitor'
                    pos_hint:{'x':.88, 'y': .52}
                    on_press: 
                        root.info2()      
                MDFloatingActionButton
                    icon:'monitor'
                    pos_hint:{'x':.88, 'y': .32}
                    on_press: 
                        root.info3()      
                MDFloatingActionButton
                    icon:'monitor'
                    pos_hint:{'x':.88, 'y': .12}
                    on_press: 
                        root.info4()   
<Yoga>:
    name:'yog'
   
    Screen:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'YOGA'
                        halign:'center'
                        right_action_items:[['keyboard-backspace', lambda x: setattr(root.manager, 'current', 'upload')]]
                        left_action_items:[['yoga']]
                        elevation:10
                    OneLineIconListItem:
                        text:'          SURYA NAMSKAR'        
                        font_style:'Subtitle1'
                        bold:'True'
                        IconLeftWidget:
                            icon:'google-play' 
                    Image:
                        source:'surya.gif'
                    OneLineIconListItem:
                        text:'           MARJARYASANA'        
                        font_style:'Subtitle1'
                        bold:'True'
                        IconLeftWidget:
                            icon:'google-play' 
                    Image:
                        source:'cat.gif'
                    OneLineIconListItem:
                        text:'          VIRABHADRASANA'        
                        font_style:'Subtitle1'
                        bold:'True'
                        IconLeftWidget:
                            icon:'google-play' 
                    Image:
                        source:'virabhadrasana.gif'
                    OneLineIconListItem:
                        text:'          ANULOM VILOM'        
                        font_style:'Subtitle1'
                        bold:'True'
                        IconLeftWidget:
                            icon:'google-play' 
                    Image:
                        source:'anulom vilom.gif'
                    ScrollView:
                 
                MDFloatingActionButton
                    id : c1
                    icon:'google-play'
                    pos_hint:{'x':0.32, 'y': 0.72}
                    on_press:
                        root.count1()
                        # import webbrowser
                        # webbrowser.open("shorturl.at/sxGLM=on") 
                        

                MDFloatingActionButton
                    id:c2
                    icon:'google-play'
                    pos_hint:{'x':0.32, 'y': 0.52}
                    on_press:
                        root.count2()
                        import webbrowser
                        webbrowser.open("shorturl.at/bgrDZ=on") 
                MDFloatingActionButton
                    id:c3
                    icon:'google-play'
                    pos_hint:{'x':0.32, 'y': 0.32}
                    on_press:
                        root.count3()
                        # import webbrowser
                        # webbrowser.open("shorturl.at/qDVZ8=on") 
                MDFloatingActionButton
                    id:c4
                    icon:'google-play'
                    pos_hint:{'x':0.32, 'y': 0.12}
                    on_press:
                        root.count4()
                        # import webbrowser
                        # webbrowser.open("shorturl.at/gjpvF=on") 
                MDFloatingActionButton
                    icon:'google-home'
                    pos_hint:{'x': .88, 'y': 0}
                    on_press: 
                        root.manager.current = 'upload'     
                MDFloatingActionButton
                    icon:'monitor'
                    pos_hint:{'x':0.88, 'y': 0.72}
                    on_press: 
                        root.info1()  
                MDFloatingActionButton
                    icon:'monitor'
                    pos_hint:{'x':.88, 'y': .52}
                    on_press: 
                        root.info2()      
                MDFloatingActionButton
                    icon:'monitor'
                    pos_hint:{'x':.88, 'y': .32}
                    on_press: 
                        root.info3()      
                MDFloatingActionButton
                    icon:'monitor'
                    pos_hint:{'x':.88, 'y': .12}
                    on_press: 
                        root.info4()                   

<Entertainment>:
    name:'ent'
    Screen:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'ENTERTAINMENT'
                        halign:'center'
                        right_action_items:[['keyboard-backspace', lambda x: setattr(root.manager, 'current', 'upload')]]
                        left_action_items:[['movie']]
                        elevation:10
                    OneLineIconListItem:
                        text:'          MATRIX 2021'        
                        font_style:'Subtitle1'
                        bold:'True'
                        IconLeftWidget:
                            icon:'magnet-on'  
                    Carousel:
                        direction:'right'
                        Image:
                            source:'q1.jpg'
                        Image:
                            source:'q2.jpg'
                        Image:
                            source:'q3.jpg'
                        Image:
                            source:'q4.jpg'

                    OneLineIconListItem:
                        text:'          VIKINGS VALHALLA 2022'        
                        font_style:'Subtitle1'
                        bold:'True'
                        IconLeftWidget:
                            icon:'litecoin' 
                                
                    Carousel:
                        direction:'right'
                        Image:
                            source:'q2.jpg'
                        Image:
                            source:'q3.jpg'
                        Image:
                            source:'q4.jpg'
                        Image:
                            source:'q1.jpg'

                    OneLineIconListItem:
                        text:'          LOVE HOSTEL 2022'        
                        font_style:'Subtitle1'
                        bold:'True'
                        IconLeftWidget:
                            icon:'pistol' 
                    Carousel:
                        direction:'right'
                        Image:
                            source:'q3.jpg'
                        Image:
                            source:'q4.jpg'
                        Image:
                            source:'q1.jpg'
                        Image:
                            source:'q2.jpg'

                    OneLineIconListItem:
                        text:'          RIM OF THE WORLD 2019'        
                        font_style:'Subtitle1'
                        bold:'True'
                        IconLeftWidget:
                            icon:'chemical-weapon' 
                    Carousel:
                        direction:'right'
                        Image:
                            source:'q4.jpg'
                        Image:
                            source:'q1.jpg'
                        Image:
                            source:'q2.jpg'
                        Image:
                            source:'q3.jpg'

                    ScrollView:   
                MDFloatingActionButton
                    icon:'google-play'
                    pos_hint:{'x':0.28, 'y': 0.72}
                    on_press:
                        import webbrowser
                        webbrowser.open("https://meet.google.com/=on") 

                MDFloatingActionButton
                    icon:'google-play'
                    pos_hint:{'x':0.28, 'y': 0.52}
                    on_press:
                        import webbrowser
                        webbrowser.open("https://meet.google.com/=on") 
                MDFloatingActionButton
                    icon:'google-play'
                    pos_hint:{'x':0.28, 'y': 0.32}
                    on_press:
                        import webbrowser
                        webbrowser.open("https://meet.google.com/=on") 
                MDFloatingActionButton
                    icon:'google-play'
                    pos_hint:{'x':0.28, 'y': 0.12}      
                    on_press:
                        import webbrowser
                        webbrowser.open("https://meet.google.com/?authuser=0=on")  
                MDFloatingActionButton
                    icon:'google-home'
                    pos_hint:{'x': .88, 'y': 0}
                    on_press: 
                        root.manager.current = 'upload'                
                    
<UserProfile>:
    name:'userp'
    Screen:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'PROFILE'
                        halign:'center'
                        right_action_items:[['keyboard-backspace', lambda x: setattr(root.manager, 'current', 'upload')]]
                        left_action_items:[['face-profile']]
                        elevation:10
                    Image:
                        source:'VISU UTKARSH.jpg'
                    ScrollView:
                    GridLayout:
                        rows:3
                        cols:2
                        MDLabel:
                            text:'              NAME'
                            bold:'True'
                            font_style:'Subtitle1'
                        MDLabel:
                            text:'VISU UTKARSH'
                            bold:'True'
                            font_style:'Subtitle1'
                        MDLabel:
                            text:'              EMAIL-ID'
                            bold:'True'
                            font_style:'Subtitle1'
                        MDLabel:
                            text:'visutkarsh2000@gmail.com'
                            bold:'True'
                            font_style:'Subtitle1'
                        MDLabel:
                            text:'              COIN'
                            bold:'True'
                            font_style:'Subtitle1'
                        MDLabel:
                            text:'100'
                            bold:'True'
                            font_style:'Subtitle1'
                    ScrollView:
                MDFloatingActionButton
                    icon:'google-home'
                    pos_hint:{'x': .88, 'y': 0}
                    on_press: 
                        root.manager.current = 'upload'



<P>:
    Label:
        text : "Please enter valid information"
        size_hint : 0.2, 0.1
        pos_hint : {"x" : 0.3, "top" : 0.8}
<Y1>:
    Label:
        text: "SURYA NAMSKAR"
<Y2>:
    Label:
        text: "MARJARYASANA"
<Y3>:
    Label:
        text: "VIRABHADRASANA"
<Y4>:
    Label:
        text: "ANULOM VILOM"
<E1>:
    Label:
        text: "CROSS BAR"
<E2>:
    Label:
        text: "COBRA POSTION"
<E3>:
    Label:
        text: "WIDE ARM PUSH-UP"
<E4>:
    Label:
        text: "PUSH-UP"

"""
class PopupWindow(Screen):
    def btn(self):
        popFun()



class P(Screen):
    pass
class Y1(Screen):
    pass
class Y2(Screen):
    pass
class Y3(Screen):
    pass
class Y4(Screen):
    pass
class E1(Screen):
    pass
class E2(Screen):
    pass
class E3(Screen):
    pass
class E4(Screen):
    pass

def popFun():
    show = P()
    window = Popup(title="ERROR!!", content=show,
                   size_hint=(None, None), size=(300, 300))
    window.open()


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    email = ObjectProperty(None)
    pwd = ObjectProperty(None)
    def validate(self):


        if self.email in (users['Email']):
            sm.current_screen='upload'
            self.email = ""
            self.pwd = ""
        else:
            popFun()




class SignupScreen(Screen):
    name2 = ObjectProperty(None)
    email = ObjectProperty(None)
    pwd = ObjectProperty(None)

    def signupbtn(self):

        user = pd.DataFrame([[self.name2.text, self.email.text, self.pwd.text]],
                            columns=['Name', 'Email', 'Password'])
        # regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if self.email.text != "" and self.name2.text !="" and self.pwd.text!="" : #and bool(re.fullmatch(regex,self.email.text))
            if self.email.text not in users['Email'].unique():
                user.to_csv('login.csv', mode='a', header=False, index=False)

                self.name2.text = ""
                self.email.text = ""
                self.pwd.text = ""
                sm.current = 'exe'
        else:

            popFun()

class UploadScreen(Screen):
    pass


class Exercise(Screen):
    c1 = ObjectProperty(0)
    c2 = ObjectProperty(0)
    c3 = ObjectProperty(0)
    c4 = ObjectProperty(0)

    def count1(self):
        self.a = self.c1
        self.c1 = self.a + 1

    def info1(self):
        show = E1()
        window = Popup(title=str(self.c1), content=show,
                       size_hint=(None, None), size=(150, 100))
        window.open()

    def count4(self):
        self.a = self.c4
        self.c4 = self.a + 1

    def info4(self):
        show = E4()
        window = Popup(title=str(self.c4), content=show,
                       size_hint=(None, None), size=(150, 100))
        window.open()

    def count2(self):
        self.a = self.c2
        self.c2 = self.a + 1

    def info2(self):
        show = E2()
        window = Popup(title=str(self.c2), content=show,
                       size_hint=(None, None), size=(150, 100))
        window.open()

    def count3(self):
        self.a = self.c3
        self.c3 = self.a + 1

    def info3(self):
        show = E3()
        window = Popup(title=str(self.c3), content=show,
                       size_hint=(None, None), size=(150, 100))
        window.open()


class Yoga(Screen):
    c1= ObjectProperty(0)
    c2=ObjectProperty(0)
    c3=ObjectProperty(0)
    c4=ObjectProperty(0)
    def count1(self):
        self.a=self.c1
        self.c1=self.a+1
    def info1(self):
        show = Y1()
        window = Popup(title=str(self.c1), content=show,
                           size_hint=(None, None), size=(150,100))
        window.open()

    def count4(self):
        self.a = self.c4
        self.c4 = self.a + 1

    def info4(self):
        show = Y4()
        window = Popup(title=str(self.c4), content=show,
                       size_hint=(None, None), size=(150,100))
        window.open()

    def count2(self):
        self.a = self.c2
        self.c2 = self.a + 1

    def info2(self):
        show = Y2()
        window = Popup(title=str(self.c2), content=show,
                       size_hint=(None, None), size=(150,100))
        window.open()

    def count3(self):
        self.a = self.c3
        self.c3 = self.a + 1

    def info3(self):
        show = Y3()
        window = Popup(title=str(self.c3), content=show,
                       size_hint=(None, None), size=(150,100))
        window.open()



class Entertainment(Screen):
    pass

class UserProfile(Screen):
    pass
users = pd.read_csv('login.csv')
# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(SignupScreen(name='sig'))
sm.add_widget(UploadScreen(name='upload'))
sm.add_widget(Exercise(name='exe'))
sm.add_widget(Yoga(name='yog'))
sm.add_widget(Entertainment(name='ent'))
sm.add_widget(UserProfile(name='userp'))


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        self.theme_cls.primary_palette = "Red"

        return screen


if __name__ == '__main__':
    DemoApp().run()
