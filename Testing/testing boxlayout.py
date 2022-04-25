import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout

Window.size = (300, 500)

navigation_helper = """
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
                
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
"""


class BoxLayoutApp(MDApp):

    def build(*args):

        Builder.load_string(navigation_helper)
        screen = MDBoxLayout(orientation='vertical')
        HB = MDBoxLayout(orientation='horizontal')
        btn1 = Button(text="One")
        btn2 = Button(text="Two")
        HB.add_widget(btn1)
        HB.add_widget(btn2)
        VB = MDBoxLayout(orientation='vertical')
        btn3 = Button(text="Three")
        btn4 = Button(text="Four")
        VB.add_widget(btn3)
        VB.add_widget(btn4)
        screen.add_widget(HB)
        screen.add_widget(VB)
        return screen


root = BoxLayoutApp()
root.run()