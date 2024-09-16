from admin_panel.utils import menu

def get_panel_context(request):
    return{"mainmenu": menu}