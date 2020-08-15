from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from views.crm_ux_view import main_layout

from controllers.dashboardcontroller import DashboardScreen
from controllers.leadcontroller import ListLeadsScreen
from controllers.accountcontroller import ListAccountsScreen

Window.size = (300, 500)

class PropertyPlanner(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'BlueGray'
        self.theme_cls.primary_hue = '700'
        self.theme_cls.theme_style = 'Dark'

        screen = Builder.load_string(main_layout)
        return screen

    def close_navigation(self):
        if self.root.ids.navdrawer.state == 'open':
            self.root.ids.navdrawer.set_state()

    def display_navigation(self):
        self.root.ids.navdrawer.set_state()

    def showdashboard(self):
        print('Dashboard')
        self.root.ids.screenmanager.current = 'dashboard'
        self.close_navigation()

    def showleads(self):
        print('Leads')
        self.root.ids.screenmanager.current = 'listleads'
        self.close_navigation()

    def showaccounts(self):
        print('Accounts')
        self.root.ids.screenmanager.current = 'listaccounts'
        self.close_navigation()

PropertyPlanner().run()
