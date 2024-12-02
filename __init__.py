# delall_package/delall/__init__.py

def delall():
    """
    Deletes all variables in the current namespace except for special ones (e.g., '__name__', '__doc__').
    """
    for name in list(globals().keys()):
        if name[0] != '_':  # Avoid deleting special variables
            del globals()[name]
