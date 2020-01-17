#!/user/bin/env python3

from datetime import datetime, time

def main():
    choice = "y"
    while choice.lower() == "y":
        # welcome message
        print("birthday calculator")
        print()

        y = input("Enter Name:")
        x = input("Enter birthday (mm/dd/yy:)")

      # find out if birthday is greater than or less than today

      # parse the birthday
        bday = datetime.strptime(x,"%m/%d/%y")
        tday = datetime.now()
        if bday.year > tday.year:
            new_year = bday.year - 100
            bday = datetime(new_year, bday.month, bday.day)

     # print the math
        b = bday.strftime("%A %B %d, %Y") 
        print("Birthday:", b)
        t = tday.strftime("%A %B %d, %Y")
        print("Today:", t)

        age = tday.year - bday.year
        temp_bday = datetime(2020, bday.month, bday.day)
        until_bday = tday - temp_bday
        if temp_bday > tday:
            print(y, "is", age - 1, "years old.")
            print(y, "'s birthday is in", until_bday.days * - 1, "days.")
        elif temp_bday.days < tday:
            print(y, "is", age, "years old.")
            if until_bday == 0:
                print(y, "'s birthday is today!")
            else:
                print(y, "'s birthday was", until_bday.days, "days ago.")

        choice = input("continue (y/n): ")
        print()

if __name__ == "__main__":
    main()
