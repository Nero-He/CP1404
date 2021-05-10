from kivy.app import App
from kivy.lang import Builder


class Calculation(App):
    def build(self):
        self.title = 'Convert m to km'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        value = self.get_values()
        result = value * 1.609344
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, modify):
        value = self.get_values() + modify
        self.root.ids.input_number.text = str(value)
        self.handle_calculate()

    def get_values(self):
        value = int(self.root.ids.input_number.text)
        return value


Calculation().run()
