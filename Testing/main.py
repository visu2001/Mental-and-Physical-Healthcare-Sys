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

class windowManager(ScreenManager):
    pass

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
            sm.current_screen = 'upload'
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
        if self.email.text != "" and self.name2.text != "" and self.pwd.text != "":  # and bool(re.fullmatch(regex,self.email.text))
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
    c1 = ObjectProperty(0)
    c2 = ObjectProperty(0)
    c3 = ObjectProperty(0)
    c4 = ObjectProperty(0)

    def count1(self):
        self.a = self.c1
        self.c1 = self.a + 1

    def info1(self):
        show = Y1()
        window = Popup(title=str(self.c1), content=show,
                       size_hint=(None, None), size=(150, 100))
        window.open()

    def count4(self):
        self.a = self.c4
        self.c4 = self.a + 1

    def info4(self):
        show = Y4()
        window = Popup(title=str(self.c4), content=show,
                       size_hint=(None, None), size=(150, 100))
        window.open()

    def count2(self):
        self.a = self.c2
        self.c2 = self.a + 1

    def info2(self):
        show = Y2()
        window = Popup(title=str(self.c2), content=show,
                       size_hint=(None, None), size=(150, 100))
        window.open()

    def count3(self):
        self.a = self.c3
        self.c3 = self.a + 1

    def info3(self):
        show = Y3()
        window = Popup(title=str(self.c3), content=show,
                       size_hint=(None, None), size=(150, 100))
        window.open()


class Entertainment(Screen):
    pass


class UserProfile(Screen):
    pass


users = pd.read_csv('login.csv')
kv = Builder.load_file('hel.kv')
# Create the screen manager
sm = windowManager()
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
        self.theme_cls.primary_palette = "Red"

        return sm


if __name__ == '__main__':
    DemoApp().run()
