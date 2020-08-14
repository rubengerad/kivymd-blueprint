accounts_layout = """
<ListAccountsScreen>:
    name:'listaccounts'
    MDToolbar:
        title: 'Mobile CRM'
        left_action_items: [['menu', lambda x:app.display_navigation()]]
        pos_hint: {'top':1}
        elevation:10   

    MDBoxLayout:
        orientation:'vertical'
        pos_hint:{'top':1}
        padding:'0dp'
        spacing:'0dp'

        MDRectangleFlatButton:
            text:'Customer Details'
            size_hint_x:'30dp'
            halign:'center'  
            text_color:  0, 0, 1, 1
            md_bg_color: app.theme_cls.primary_light
            pos_hint:{'top_y':1}

        MDTextField:
            hint_text: 'Name'
            helper_text: 'Enter full name'
            helper_text_mode: 'on_focus'
            width:'250dp' 

            
        MDTextField:
            hint_text: 'Company'
            helper_text: 'Enter Company Name'
            helper_text_mode: 'on_focus'
        
        MDTextField:
            hint_text: 'Address'
            helper_text: 'Enter business or home address'
            helper_text_mode: 'on_focus'

        MDTextField:
            hint_text: 'Phone'
            helper_text: 'Enter business phone or mobile'
            helper_text_mode: 'on_focus'

        MDTextField:
            hint_text: 'Email'
            helper_text: 'Enter email address'
            helper_text_mode: 'on_focus'



<ManageLeadsScreen>:
    name:'manageleads'
    MDToolbar:
        title: 'Mobile CRM'
        left_action_items: [['menu', lambda x:app.display_navigation()]]
        pos_hint: {'top':1}
        elevation:10   

    MDBoxLayout:
        orietation:'vertical'
        padding:'3dp'
        spacing:'2dp'

        MDLabel:
            text:'Property Details'
            halign:'center'
            theme_text_color:'Primary'

        MDTextField:
            hint_text: 'Name'
            helper_text: 'Enter full name'
            helper_text_mode: 'on_focus'
            width:'250dp' 

        MDTextField:
            hint_text: 'Address'
            helper_text: 'Enter business or home address'
            helper_text_mode: 'on_focus'

        MDTextField:
            hint_text: 'Phone'
            helper_text: 'Enter business phone or mobile'
            helper_text_mode: 'on_focus'

        MDTextField:
            hint_text: 'Email'
            helper_text: 'Enter email address'
            helper_text_mode: 'on_focus'
"""