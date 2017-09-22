def decoder():
    coded = "pYWplY thZnk thVt cWmpXtYr scZYncY Zs thY Vrt Wf gYnZXsYs bXt thY VctXVl rYVlZty Zs thY WppWsZtY, jXst mVny pYWplY dWZng thZngs thVt bXZld Wn YVch WthYr, lZkY V wVll Wf mZnZ stWnYs. - dWnVld knXth"
    message=""
    for letter in coded:
        if letter == "V":
            message = message + "a"
        elif letter == "W":
            message = message + "o"
        elif letter == "X":
            message = message + "u"
        elif letter == "Y":
            message = message + "e"
        elif letter == "Z":
            message = message + "i"
        else:
            message = message + letter
    print("The actual message is: ")
    print(message)
    
def coder():
    original="people think that computer science is the art of geniuses but the actual reality is the opposite, just many people doing things that build on each other, like a wall of mini stones. - donald knuth"
    message=""
    for letter in original:
        if letter == "a":
            message = message + "V"
        elif letter == "o":
            message = message + "W"
        elif letter == "u":
            message = message + "X"
        elif letter == "e":
            message = message + "Y"
        elif letter == "i":
            message = message + "Z"
        else:
            message = message + letter
    print("The coded message is: ")
    print(message)        


def main():
    coder()
    decoder()

if __name__ == "__main__":
	main()
	


