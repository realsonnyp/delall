def delvars():
    for variable in list(globals().keys()):
        if variable[0] != '_':  # Avoid deleting special variables
            del globals()[variable]
