from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class AmarAI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.padding = 10
        self.spacing = 10
        
        self.title = Label(text='Amar AI - Tomar AI', font_size=24, size_hint_y=0.1)
        self.add_widget(self.title)
        
        self.output = Label(text='Namaskar! Ami Amar AI. Kichu jiggasa koro.', size_hint_y=0.6)
        self.add_widget(self.output)
        
        self.input = TextInput(hint_text='Ekhane likho...', size_hint_y=0.15, multiline=False)
        self.add_widget(self.input)
        
        self.btn = Button(text='Pathao', size_hint_y=0.15)
        self.btn.bind(on_press=self.send)
        self.add_widget(self.btn)

    def send(self, instance):
        q = self.input.text
        if not q:
            return
        self.output.text = f"Tumi bolle: {q}\n\nUttor: Ami ekhon offline achi, kintu khub taratari online asbo!"
        self.input.text = ""

class AmarAIApp(App):
    def build(self):
        return AmarAI()

if __name__ == '__main__':
    AmarAIApp().run()
