#!Frank Bonini, Gabrielle Yuhas, Kaitlyn Krill
#!/usr/lib/python
import sys

def parentCheck(name1, name2):
    if (not name1 in tree or not name2 in tree):
        return False
    if (name1 not in tree.get(name2)[0]):
        return False
    return True

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

#Todo: for-loop for file reading; or while loop

#Get input properly
INPUT = "X this input should be obtained properly, unlike this."

#Split the input here. we will have to work with a split input in every of the below comparison statements
SplittedList = INPUT.split()

#Our person object. To have "instances" of this object, change the values in this dictionary, then .copy() it for use in anything else.
person = {'name' : "", "parents" : [], "children" : []}

#The family tree. Dictionary of the "person" object, having the names as keys
tree = {'name' : person}

#Keep for reference
#person['name'] = "John"
#tree[person['name']] = person.copy()
#person['name'] = "Joe"
#tree[person['name']] = person.copy()



#Condition for relationship comparison
if(INPUT.startswith('X')):

    print('placeholder')

    print(SplittedList)
    


elif(INPUT.startswith('W')):
    #Condition for relationship listing
    print('placeholder')

else:
    #Condition for adding relationships
    print('placeholder')
    


