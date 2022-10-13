# Create a timer

from time import sleep

def setTimer(target_duration: int):
    """
    A simple timer function.
    """

    current_duration = 0

    while current_duration < target_duration:
        print(current_duration, end="\r")
        
        sleep(1)
        
        current_duration += 1

    print("Your time is up!")

target_duration = int(input("Enter the duration in seconds: "))

setTimer(target_duration)
