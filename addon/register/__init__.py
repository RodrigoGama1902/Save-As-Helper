

def register_addon():

    from ..addon_prefs import register_properties
    register_properties() 

    from ..operator import register_operators
    register_operators()

    from .keymap import register_keymap
    register_keymap()



def unregister_addon():

    from ..addon_prefs import unregister_properties
    unregister_properties() 

    from ..operator import unregister_operators
    unregister_operators()
    
    from .keymap import unregister_keymap
    unregister_keymap()

