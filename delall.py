def delall():
    for name in list(globals().keys()):
        if name[0] != '_':  # Avoid deleting special variables
            del globals()[name]
            
