accounts_layout = """
<ListAccountsScreen>:
    name:'listaccounts'
    MDToolbar:
        title: 'Customer Details'
        pos_hint: {'top':.87}
        height:'40dp'

    BoxLayout:
        orientation:'vertical'
        padding:'8dp'
        spacing:'8dp'

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
        title: 'Customer Details'
        pos_hint: {'top':.87}
        height:'40dp'

    BoxLayout:
        orientation:'vertical'
        padding:'8dp'
        spacing:'8dp'

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