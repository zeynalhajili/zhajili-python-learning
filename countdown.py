###countdown

from time import sleep

countdown_start = int(input("Please enter number to start:\n"))
countdown = countdown_start

while countdown > 0:
    print(countdown)  # Print the current countdown value
    sleep(2)          # Wait for 2 seconds
    countdown -= 1    # Decrement the countdown

print(f"Your countdown finished in {countdown_start} seconds")