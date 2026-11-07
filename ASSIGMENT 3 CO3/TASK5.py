temp = [4, 6, 55, 3, -60, 9, 7, 5]

clean = [x for x in temp if -50 <= x <= 50]
fahrenheit = [(x * 9/5) + 32 for x in clean]

print("Clean readings:", clean)
print("Fahrenheit:", fahrenheit)

alarms = [(i+1, x) for i, x in enumerate(clean)
          if x < 2 or x > 8]

print("Alarm readings:", alarms)
