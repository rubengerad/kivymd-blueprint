dashboard_layout = '''
<DashboardScreen>:
    name:'dashboard'
    MDToolbar:
        title: 'Mobile CRM'
        left_action_items: [['menu', lambda x:app.display_navigation()]]
        pos_hint: {'top':1}
        elevation:10

    MDRectangleFlatButton: 
        text: 'Welcome to Mobile CRM'
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        on_press: app.loginview()

    MDBottomAppBar:
        MDToolbar:
            mode:'end'
            icon:'plus-thick'
            elevation:20    
            on_action_button: app.display_navigation()
'''
nav_drawer = '''
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
'''
