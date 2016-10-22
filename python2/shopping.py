def shopping():
    myList = []
    numberOfItems = int(raw_input("How many items would you like to buy today? "))
    print "Please enter one item per line and hit enter"
    for position in range(numberOfItems):
        print position + 1
        item = raw_input(": ")
        myList.append(item)
    print "Today you want to buy", myList

def main():
    shopping()

if __name__ == "__main__":
	main()


