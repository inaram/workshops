def skillImprover():
    skillLevel = 0
    while skillLevel < 10:
        print "Keep programming!"
        skillLevel = skillLevel + 1
        print "Now your skill level is %d" % skillLevel
    print "Congratulations! You have completed the training." 

def main():
    skillImprover()

if __name__ == "__main__":
	main()

