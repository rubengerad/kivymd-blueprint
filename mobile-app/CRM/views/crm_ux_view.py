main_layout = '''
Screen:
    name:'dashboard'

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "MDNavigationDrawer"
        left_action_items: [["menu", lambda x: app.display_navigation()]]    
    
    NavigationLayout:

        ScreenManager:
            id: screenmanager
            DashboardScreen:
            ListLeadsScreen:
            ListAccountsScreen:
        
        MDNavigationDrawer:
            id:navdrawer
            MDBoxLayout:
                spacing:'8dp'
                padding:'8dp'
                orientation:'vertical'
                Image:
                    source:'assets/mcrm.png'

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Dashboard'
                            on_press: 
                                app.showdashboard()
                            IconLeftWidget:
                                icon: 'home'   
                        OneLineIconListItem:
                            text: 'Leads'
                            on_press: 
                                app.showleads()
                            IconLeftWidget:
                                icon: 'account'
                        OneLineIconListItem:
                            text: 'Accounts'
                            on_press: 
                                app.showaccounts()
                            IconLeftWidget:
                                icon: 'book'
                                        
    MDBottomAppBar:
        MDToolbar:
            mode:'end'
            icon:'plus-thick'
            elevation:20    
            on_action_button: app.display_navigation()    
'''
