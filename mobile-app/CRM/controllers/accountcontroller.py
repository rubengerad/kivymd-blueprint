from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from views.accountview import accounts_layout

class ListAccountsScreen(Screen):
    pass

class ManageAccountsScreen(Screen):
    pass

Builder.load_string(accounts_layout)