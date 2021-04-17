travel_distance = int(input("Enter distance here"))

number_of_days = 0
total_distance = total_distance + travel_distance

if total_distance < 100:
  travel_distance = int(input("Enter distance here"))
  number_of_days = number_of_days + 1
else:
  print("It took " + number_of_days + " days to surpass 100km driven.")
  