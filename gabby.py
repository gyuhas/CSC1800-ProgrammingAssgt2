def cousinCheck(name1, name2):
    if (not name1 in tree or not name2 in tree):
        return False

    if (name1 == name2):
        return False

    i = 0
    isCousin = False

    while (i < len(tree) and not isCousin):
        pName = listOfNames[i]

        if (ancestorCheck(pName, name1) and ancestorCheck(pName, name2)):
            isCousin = True

        i += 1

    return isCousin

def parentCheck(name1, name2):
    if (not name1 in tree or not name2 in tree):
        return False
    if (name1 not in tree.get(name2)[0]):
        return False
    return True
