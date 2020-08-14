from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import NavigationLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from views.dashboardview import nav_drawer

from controllers.dashboardcontroller import DashboardScreen
from controllers.leadcontroller import ListLeadsScreen
from controllers.accountcontroller import ListAccountsScreen

Window.size = (300, 500)

class PropertyPlanner(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'BlueGray'
        self.theme_cls.primary_hue = '700'
        self.theme_cls.theme_style = 'Dark'

        navlayout = NavigationLayout()
        self.screenmanager = ScreenManager()
        self.screenmanager.id = 'screenmanager'
        self.screenmanager.add_widget(DashboardScreen(name='dashboard'))
        self.screenmanager.add_widget(ListLeadsScreen(name='listleads'))
        self.screenmanager.add_widget(ListAccountsScreen(name='listaccounts'))
        self.navdrawer = Builder.load_string(nav_drawer)
        self.navdrawer.id = 'navdrawer'
        navlayout.add_widget(self.screenmanager)
        navlayout.add_widget(self.navdrawer)

        return navlayout;

    def close_navigation(self):
        if self.navdrawer.state == 'open':
            self.navdrawer.set_state()

    def display_navigation(self):
        self.navdrawer.set_state()

    def showdashboard(self):
        print('Dashboard')
        self.screenmanager.current = 'dashboard'
        self.close_navigation()

    def showleads(self):
        print('Leads')
        self.screenmanager.current = 'listleads'
        self.close_navigation()

    def showaccounts(self):
        print('Accounts')
        self.screenmanager.current = 'listaccounts'
        self.close_navigation()

PropertyPlanner().run()
