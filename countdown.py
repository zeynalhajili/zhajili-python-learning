###countdown

from time import sleep

countdown_start = int(input("Please enter number to start:\n"))
countdown = countdown_start

while countdown > 0:
    countdown -= 1
    sleep(2)
    print(countdown)

print(f"Your countdown finished in {countdown_start} seconds")

