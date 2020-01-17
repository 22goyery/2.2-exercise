#!/usr/bin/env python3

from datetime import datetime, time

# display a welcome message
def main():
    print("The Timer program")
    print()

    # start timer
    input("Press Enter to start...")
    start_time = datetime.now()
    one = start_time.strftime("%H:%M:%S.%f")
    print("start time:", one)
    print()
    
    # stop timer
    input("Press Enter to stop...")  
    stop_time = datetime.now()
    two = stop_time.strftime("%H:%M:%S.%f")
    print("stop time: ",two)
    print()
    
    # calculate elapsed time
    elapsed_time = stop_time - start_time
    minutes = elapsed_time.seconds // 60
    seconds = elapsed_time.seconds % 60
    microseconds = elapsed_time.microseconds
    hours = minutes // 60
    minutes = minutes % 60

    # create time object
    time_object = time(hours, minutes, seconds, microseconds)

    # display results
    print("ELAPSED TIME")
    if minutes > 0:
        print("hours\minutes:", time_object.strftime("%H:%M"))
    print("seconds:", time_object.strftime("%S.%f"))
        
if __name__ == "__main__":
    main()

