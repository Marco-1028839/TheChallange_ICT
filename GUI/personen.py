from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager, SlideTransition

class PersonGegevensScreen(Screen):
    def __init__(self, **kwargs):
        super(PersonGegevensScreen, self).__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', spacing='10dp', padding='10dp')
        label = MDLabel(text='Welcome to the Person Gegevens Screen!', halign='center')
        back_button = MDRaisedButton(text="Back", on_release=self.go_back)
        layout.add_widget(label)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'home'