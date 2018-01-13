'''
Shopping exercises use list structure to represent a collection of shopping list items.
Verisions of shopping#() built on each other to demonstrate incremental programming. 
'''
def shopping0():
    '''v1.0
    concepts: Variable Names '''
    shoppingList = []
    numberOfItems = int(input("How many items would you like to buy today? "))
    print("Today you want to buy", numberOfItems, "item(s)")

def shopping1():
    '''v1.1
    concepts: If '''
    shoppingList = []
    numberOfItems = int(input("How many items would you like to buy today? "))
    if numberOfItems > 0:
        print("Today you want to buy", numberOfItems, "item(s)")
        
def shopping2():
    '''v1.2
    concepts: Else '''
    shoppingList = []
    numberOfItems = int(input("How many items would you like to buy today? "))
    if numberOfItems > 0:
        print("Today you want to buy", numberOfItems, "item(s)")
    else:
        print("Today you don't want to buy anything")

def shopping3():
    '''v1.3
    concepts: Elif '''
    shoppingList = []
    numberOfItems = int(input("How many items would you like to buy today? "))
    if numberOfItems == 1:
        print("Today you want to buy 1 item")
    elif numberOfItems > 1:
        print("Today you want to buy", numberOfItems, "items")
    else:
        print("Today you don't want to buy anything")

def shopping4():
    '''v1.4
    concepts: For, In '''
    shoppingList = []
    numberOfItems = int(input("How many items would you like to buy today? "))

    if numberOfItems == 1:
        item = input(": ")
        shoppingList.append(item)
        print("Today you want to buy 1 item")
        print("Item is ", shoppingList[0])
        
    elif numberOfItems > 1:
        print("Please enter one item per line and hit enter")    
        for position in range(numberOfItems):
            item = input(": ")
            shoppingList.append(item)
        print("Today you want to buy", numberOfItems, "items")
        print("Items are", shoppingList)

    else:
        print("Today you don't want to buy anything")

def shopping5():
    '''v1.5
    concepts: Not '''
    shoppingList = []
    numberOfItems = int(input("How many items would you like to buy today? "))

    if numberOfItems == 1:
        item = input(": ")
        shoppingList.append(item)
        print("Today you want to buy 1 item")
        print("Item is ", shoppingList[0])

    elif numberOfItems > 1:
        print("Please enter one item per line and hit enter")    
        for position in range(numberOfItems):
            item = input(": ")
            if item not in shoppingList:
                shoppingList.append(item)
        print("Today you want to buy", len(shoppingList), "items")
        print("Items are", shoppingList)

    else:
        print("Today you don't want to buy anything")

        
def shopping6():
    '''v1.6
    concepts: nested for loops '''
    shoppingList = []
    numberOfItems = int(input("How many items would you like to buy today? "))

    if numberOfItems == 1:
        item = input(": ")
        shoppingList.append(item)
        print("Today you want to buy 1 item")
        print("Item is ", shoppingList[0])

    elif numberOfItems > 1:
        print("Please enter one item per line and hit enter")    
        for position in range(numberOfItems):
            item = input(": ")
            if "," in item:
                items = item.split(",")
                for item in items:
                    item = item.strip()
                    if item not in shoppingList:
                        shoppingList.append(item)        
            elif item not in shoppingList:
                shoppingList.append(item)
        print("Today you want to buy", len(shoppingList), "items")
        print("Items are", shoppingList)

    else:
        print("Today you don't want to buy anything")

def main():
#    shopping0()
#    shopping1()
#    shopping2()
#    shopping3()
#    shopping4()
#    shopping5()
    shopping6()


if __name__ == "__main__":
	main()


