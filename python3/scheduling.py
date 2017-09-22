def sortedCalendar(myCalendar):
    print("Monday:", myCalendar["Monday"])
    print("Tuesday:", myCalendar["Tuesday"])
    print("Wednesday:", myCalendar["Wednesday"])
    print("Thursday:", myCalendar["Thursday"])
    print("Friday:", myCalendar["Friday"])
    print("Saturday:", myCalendar["Saturday"])
    print("Sunday:", myCalendar["Sunday"])

def calendar():
    myCalendar = {"Monday": "study", "Tuesday": "free",
                  "Wednesday": "read", "Thursday": "cook",
                  "Friday": "free", "Saturday": "party!",
                  "Sunday": "volunteer"}

    print("Here is your current schedule: ")
    sortedCalendar(myCalendar)

    while "free" in myCalendar.values():
        print("You still have a free day")
        event = input("What would you like to do? ")
        when = input("When would you like to do it? ")        
        for day in myCalendar:
            if day == when:
                if myCalendar[day] == "free":
                    myCalendar[day] = event
                    print("Sounds good! Now you have a new event,", event, ", scheduled on", day)
                else:
                    print("Sorry, you already have", myCalendar[day], "scheduled on", day)
    else:
        print("Now your calendar is full. Here is what you have scheduled for next week: ")
        print(myCalendar.items())

def main():
    calendar()

if __name__ == "__main__":
	main()
	
