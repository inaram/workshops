'''
Shopping exercises use list structure to represent a collection of shopping list items. 
Input: user identifies the number and names of the items 
Output: completed shopping list
'''
def shopping0():
    '''
    v1.0
    concepts: For
    '''
    shoppingList = []
    numberOfItems = int(raw_input("How many items would you like to buy today? "))
    print "Please enter one item per line and hit enter"
    for position in range(numberOfItems):
        item = raw_input(": ")
        shoppingList.append(item)
    print "Today you want to buy", shoppingList


def shopping1():
    '''
    v1.1
    concepts: For, If
    '''
    shoppingList = []
    numberOfItems = int(raw_input("How many items would you like to buy today? "))
    print "Please enter one item per line and hit enter"
    for position in range(numberOfItems):
        item = raw_input(": ")
        if item not in shoppingList:
            shoppingList.append(item)
    print "Today you want to buy", shoppingList


def shopping2():
    '''
    v1.2
    concepts: For, If
	    Nested for loops and if statements
		Checking user input
    '''
    shoppingList = []
    numberOfItems = int(raw_input("How many items would you like to buy today? "))
    print "Please enter one item per line and hit enter"
    for position in range(numberOfItems):
        item = raw_input(": ")
        if "," in item:
            items = item.split(",")
            for item in items:
                if item not in shoppingList:
                    shoppingList.append(item)
        if item not in shoppingList:
            shoppingList.append(item)
    print "Today you want to buy", shoppingList


def shopping3():
    '''
    v1.3
    concepts: For, If
		Nested for loops and if statements
		Checking user input
		Helper functions 
    '''
    shoppingList = []
    numberOfItems = int(raw_input("How many items would you like to buy today? "))
    print "Please enter one item per line and hit enter"
    for position in range(numberOfItems):
        item = raw_input(": ")
        if "," in item:
            items = item.split(",")
            for item in items:
                print "in comma items, on item", item
                shoppingList = listChecker(shoppingList, item)
        else:
            shoppingList = listChecker(shoppingList, item)
    print "Today you want to buy", 
    listDisplay(shoppingList)

def listChecker(shoppingList, item):
    '''Checks whether the item is already in the list
    Helper function for shoppping3(), v1.3
    '''
    itemTemp = item.strip()
    itemTemp = itemTemp.lower()
    if itemTemp[-1] == "s": #plural for most words
        itemTemp = itemTemp[:-1]
    if itemTemp not in shoppingList:
        shoppingList.append(itemTemp)
    return shoppingList

def listDisplay(shoppingList):
    '''
    Displays the list in user-friendly form
    Helper function for shopping3(), v.1.3
    '''
    for item in shoppingList:
        if shoppingList.index(item) == len(shoppingList) - 1:
            print "and", item + ".", 
        else:    
            print item + ",", 



def main():
    shopping0()
    shopping1()
    shopping2()
    shopping3()


if __name__ == "__main__":
	main()


