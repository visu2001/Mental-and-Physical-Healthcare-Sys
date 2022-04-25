from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton, MDFloatingActionButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList,OneLineListItem
from kivymd.uix.behaviors.magic_behavior import MagicBehavior
import ffpyplayer
# import pillow
Window.size = (460, 700)
screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
    Exercise:
    Yoga:
<MenuScreen>:
    name: 'menu'

    Screen:
        #:set w 300
        #:set h 300
        canvas.before:
            Rectangle:
                pos: self.pos
                source: 'Capture.png'
                pos:(100,150)
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
            pos_hint:{'center_x': 0.3, 'center_y': 0.19}
            text_color:(1, 0, 0)
            on_press: 
                root.manager.current = 'profile'
                root.manager.transition.direction = 'up'
        MDRectangleFlatButton:
            text:'Sign-up'
            pos_hint:{'center_x': 0.5, 'center_y': 0.19}
            text_color:(1, 0, 0)
            on_press: 
                root.manager.current = 'profile'
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
            hint_text:"Enter Username"
            helper_text:"or click on forgot username"
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
                root.manager.current = 'upload'
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
                                    source:'ex1.jpeg'
                                Image:
                                    source:'ex2.jpeg'
                                Image:
                                    source:'ex3.jpeg'
                                Image:
                                    source:'ex4.jpeg'  
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
                        source:'ex1.jpeg'
                    OneLineIconListItem:
                        text:'          COBRA POSITION'        
                        font_style:'Subtitle1'
                        bold:'True'
                        IconLeftWidget:
                            icon:'google-play' 
                    Image:
                        source:'ex2.jpeg'
                    OneLineIconListItem:
                        text:'          WIDE ARM PUSH-UP'        
                        font_style:'Subtitle1'
                        bold:'True'
                        IconLeftWidget:
                            icon:'google-play' 
                    Image:
                        source:'ex3.jpeg'
                    OneLineIconListItem:
                        text:'          PUSH-UP'        
                        font_style:'Subtitle1'
                        bold:'True'
                        IconLeftWidget:
                            icon:'google-play' 
                    Image:
                        source:'ex4.jpeg'
                    ScrollView:          
                MDFloatingActionButton
                    icon:'google-play'
                    pos_hint:{'x':0.32, 'y': 0.72}
                    on_press:
                        import webbrowser
                        webbrowser.open("https://www.youtube.com/watch?v=fq9yA_XVzLA&list=WL&index=3=on") 
                            
                MDFloatingActionButton
                    icon:'google-play'
                    pos_hint:{'x':0.32, 'y': 0.52}
                MDFloatingActionButton
                    icon:'google-play'
                    pos_hint:{'x':0.32, 'y': 0.32}
                MDFloatingActionButton
                    icon:'google-play'
                    pos_hint:{'x':0.32, 'y': 0.12}
                MDFloatingActionButton
                    icon:'google-home'
                    pos_hint:{'x': .88, 'y': 0}
                    on_press: 
                        root.manager.current = 'upload'
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
                        text:'          CROSS BAR'        
                        font_style:'Subtitle1'
                        bold:'True'
                        IconLeftWidget:
                            icon:'google-play' 
                    Image:
                        source:'ex1.jpeg'
                    OneLineIconListItem:
                        text:'          COBRA POSITION'        
                        font_style:'Subtitle1'
                        bold:'True'
                        IconLeftWidget:
                            icon:'google-play' 
                    Image:
                        source:'ex2.jpeg'
                    OneLineIconListItem:
                        text:'          WIDE ARM PUSH-UP'        
                        font_style:'Subtitle1'
                        bold:'True'
                        IconLeftWidget:
                            icon:'google-play' 
                    Image:
                        source:'ex3.jpeg'
                    OneLineIconListItem:
                        text:'          PUSH-UP'        
                        font_style:'Subtitle1'
                        bold:'True'
                        IconLeftWidget:
                            icon:'google-play' 
                    Image:
                        source:'ex4.jpeg'
                    ScrollView:          
                MDFloatingActionButton
                    icon:'google-play'
                    pos_hint:{'x':0.32, 'y': 0.72}
                    on_press:
                        import webbrowser
                        webbrowser.open("https://www.youtube.com/watch?v=fq9yA_XVzLA&list=WL&index=3=on") 
                            
                MDFloatingActionButton
                    icon:'google-play'
                    pos_hint:{'x':0.32, 'y': 0.52}
                MDFloatingActionButton
                    icon:'google-play'
                    pos_hint:{'x':0.32, 'y': 0.32}
                MDFloatingActionButton
                    icon:'google-play'
                    pos_hint:{'x':0.32, 'y': 0.12}
                MDFloatingActionButton
                    icon:'google-home'
                    pos_hint:{'x': .88, 'y': 0}
                    on_press: 
                        root.manager.current = 'upload'                
                  
                    
            
                                         

"""


class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class UploadScreen(Screen):
    pass
class Exercise(Screen):
    pass
class Yoga(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))
sm.add_widget(Exercise(name='exe'))
sm.add_widget(Yoga(name='yog'))

class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        self.theme_cls.primary_palette = "Red"

        return screen


if __name__=='__main__':
    DemoApp().run()
