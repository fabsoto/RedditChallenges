def balanced(name):
    name = str(name).lower()
    result = True
    for i in range(1, len(name)):
        if name.count(name[i]) != name.count(name[i-1]):
            result = False
            break
    return result