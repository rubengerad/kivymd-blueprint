from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from views.leadview import leads_layout

class ListLeadsScreen(Screen):
    pass

class ManageLeadsScreen(Screen):
    pass

Builder.load_string(leads_layout)