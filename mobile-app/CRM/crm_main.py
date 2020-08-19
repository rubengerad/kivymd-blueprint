from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import NavigationLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from views.dashboardview import nav_drawer, code_layout, code_footer

from controllers.dashboardcontroller import DashboardScreen
from controllers.leadcontroller import ListLeadsScreen
from controllers.accountcontroller import ListAccountsScreen

Window.size = (300, 500)
# TESTING CODE FIRST APPROACH
class MCRM(MDApp):
    # def on_start(self):
    #     self.root.ids.dashtoolbar.ids.label_title.font_style = 'Button' #AttributeError: 'NoneType' object has no attribute 'ids'

    def build(self):
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.primary_hue = '700'
        self.theme_cls.theme_style = 'Dark'

        self.screen = Builder.load_string(code_layout)
        self.navlayout = NavigationLayout()
        self.screenmanager = ScreenManager()
        self.screenmanager.id = 'screenmanager'
        self.screenmanager.add_widget(DashboardScreen(name='dashboard'))
        self.screenmanager.add_widget(ListLeadsScreen(name='listleads'))
        self.screenmanager.add_widget(ListAccountsScreen(name='listaccounts'))
        self.navdrawer = Builder.load_string(nav_drawer)
        self.navdrawer.id = 'navdrawer'
        self.navlayout.add_widget(self.screenmanager)
        self.navlayout.add_widget(self.navdrawer)
        self.footer = Builder.load_string(code_footer)
        self.screen.add_widget(self.navlayout)
        self.screen.add_widget(self.footer)
        return self.screen;

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

MCRM().run()
