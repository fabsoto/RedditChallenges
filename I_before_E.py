def check(word):
    if "cie" in word:
        return False
    elif "cei" in word:
        return True
    elif "ei" in word:
        return False
    elif "ie" in word:
        return True
    else:
        return True