from datetime import datetime, timedelta, date

def main():
    startDateStr = input("Enter the starting date in MM-DD-YYYY format - default = today: ")

    dateObject = datetime.strptime(startDateStr, '%m-%d-%Y').date() if startDateStr else date.today()

    addDays = input("Enter the number of days to add: ")
    newDate = dateObject + timedelta(days=int(addDays))

    print('The new date is:')
    print(newDate)



if __name__ == "__main__":
    main()
