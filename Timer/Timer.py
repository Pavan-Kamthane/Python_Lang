from time import sleep

target_duration = int(input("Enter the duration in seconds: "))

current_duration = 0

while current_duration < target_duration:
    print(current_duration, end="\r")
    
    sleep(1)
    
    current_duration += 1

print("Your time is up!")
