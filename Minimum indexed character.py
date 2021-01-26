def printMinIndexChar(string,patt):
    #return required char
    for i in string:
        if i in patt:
            return i
    return "$"