from kivy.app import App
from kivy.clock import Clock
class MainApp(App):
   def on_start(self):
       Clock.schedule_interval(self.update_label, 2)
       Clock.schedule_once(self.focus_text_input, 2)
   def focus_text_input(self, *args):
       self.root.ids.input.focused = True
   def update_label(self, args):
       # Update my label
        self.root.ids.counter.text = str(int(self. root.ids.counter.text) + 1)
MainApp ().run()