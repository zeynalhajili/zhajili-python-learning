# We want to create a program to calculate the time it takes to download a file
# We ask the user 2 questions. File size in megabytes and internet speed in megabits/ second
# Convert the file size to megabits (1 megabyte = 8 megabits), then calculate the download time
# Display the number of seconds the download will take
# Use your countdown timer to display the download process taking place
# end with printing "download complete!"

from time import *

file_size=int(input("Please enter file size in megabytes:\n"))
internet_speed=int(input("Please enter internet speed in megabits/seconds:\n"))
    
convert_to_megabits = file_size * 8
download_time = round(convert_to_megabits / internet_speed)

print(f"It will take {download_time} seconds to download file ...")

while download_time > 0:
    sleep(2)
    print(f"Remaining time {round(download_time)} seconds..")
    download_time -=2
    
print("Download is completed!")