# Code to input the number the seconds
seconds = int(input("Enter the number of seconds to be converted: "))

# Code to calculate and print number of seconds and minutes
minutes = seconds // 60
remaining_seconds = seconds % 60
print("Minutes :" , minutes)
print("Seconds :" , remaining_seconds)
