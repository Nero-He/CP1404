from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class DynamicApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.creat_widgets()
        return self.root

    def creat_widgets(self):
        for name in self.name_to_phone:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_label)


DynamicApp().run()
