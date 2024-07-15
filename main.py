#!/usr/bin/env python3


# Love You App
# GitHub: https://github.com/kozyol/LoveYouApp
#
# This app generates random love you text
# each time 'get love' button pressed
#
# This app can be a good gift :)


# Imports
import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.actionbar import ActionBar, ActionView, ActionPrevious


# KV config
with open("main.kv", "r") as kv:
    Builder.load_string(kv.read())


# MainMenu screen
class MainMenuScreen(Screen):
    # Love you in different languages
    love_texts = [
        "Je t’aime\n",
        "Te quiero\n",
        "ani ohev otach\n",
        "Ich liebe dich\n",
        "Volim te\n",
        "Ti amo\n",
        "Eu te amo\n",
        "Jag älskar dig\n",
        "Te iubesc\n",
        "I love you\n",
        "Ek he jou lief\n",
        "Te dua\n",
        "Ana behibek\n",
        "Yes kex sirumem\n",
        "Ngo oiy ney a\n",
        "Doset daram\n",
        "Mahal kita\n",
        "Mina rakastan sinua\n",
        "Aishiteru or Anata ga daisuki desu\n",
        "Seni Seviyorum\n",
        "Phom rak khun\n",
        "Lu`bim ta\n",
        "Ya tebya liubliu\n",
        "Te iubesc\n",
        "Eg elski teg\n",
        "люблю тебя\n",
        "Ma armastan sind\n",
        "Afgreki’\n",
    ]

    # Say love method
    def say_love(self, result):
        # Result text
        prev = result.text
        # New text
        temp = random.choice(MainMenuScreen.love_texts)
        # Add new text to result
        result.text = prev + temp


# Main class
class LoveYouApp(App):

    # Build method
    def build(self):

        # Root screen
        root = ScreenManager()

        # Main menu screen
        self.MainMenuScreen = MainMenuScreen(name="MainMenu")
        root.add_widget(self.MainMenuScreen)

        # Set current screen to main menu and return root
        root.current = "MainMenu"
        return root


# Run App
LoveYouApp().run()
