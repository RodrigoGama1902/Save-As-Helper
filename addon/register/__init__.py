

def register_addon():

    from ..addon_prefs import register_properties
    register_properties() 
    
    from ..menu import register_menus
    register_menus()

    from ..operator import register_operators
    register_operators()

    from .keymap import register_keymap
    register_keymap()
    
    from ..addon_props import register_props
    register_props()

def unregister_addon():

    from ..addon_prefs import unregister_properties
    unregister_properties() 
    
    from ..menu import unregister_menus
    unregister_menus()

    from ..operator import unregister_operators
    unregister_operators()
    
    from .keymap import unregister_keymap
    unregister_keymap()
    
    from ..addon_props import unregister_props
    unregister_props()

