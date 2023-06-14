
def get_menu(opt,_ussd_actual,_ussd):
    menu = ""
    if opt.childs:
        if len(opt.childs) > 1 or (len(opt.childs) == 1 and -1 not in opt.childs):
            for i, child in enumerate(opt.childs):
                menu = menu + str(i+1) + '. ' + _ussd.root[child].name + '\n'
        else:            
            menu = _get_final_action(opt,_ussd_actual,_ussd) + ' 1. ' + _ussd.root[-1].name + '\n'        
    return menu

def _get_final_action(opt,_ussd_actual,_ussd):
    action = "Ha ocurrido un problema"
    if opt.function is None:
        is_success = _ussd.set_activity(_ussd_actual)
        if is_success == True:
            action = opt.action
    else:
        action = opt.function()
    return action