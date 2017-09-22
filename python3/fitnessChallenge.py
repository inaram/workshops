def fitnessChallenge():
    challengeLength = int(input("How many days do you want your fitness challenge to last? "))
    totalMinutes = 0
    totalDays = 0 

    for day in range(1, challengeLength + 1):
        answer = input("Have you exercised today? (y/n): ")
        if answer == "y" or answer == "yes" or answer == "Y" or answer == "Yes" or answer == "YES":
            totalDays += 1
            print("Great job!")
            addMinutes = int(input("For how many minutes? "))
            totalMinutes = totalMinutes + addMinutes
            print("Keep up the good work!")
            
    if totalMinutes != 0 or totalDays != 0:
        print("Congratulations! You have exercised for %d day(s) out of your %d-day challenge" % (totalDays, challengeLength))
        print("Total number of minutes:", totalMinutes)

def main():
    fitnessChallenge()

if __name__ == "__main__":
	main()
	

