from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from views.dashboardview import dashboard_layout


class DashboardScreen(Screen):
    pass

Builder.load_string(dashboard_layout)

