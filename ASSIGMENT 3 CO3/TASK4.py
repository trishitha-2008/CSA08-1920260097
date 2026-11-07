ai = {101, 102, 103, 104}
iot = {103, 104, 105, 106}
all_students = {101, 102, 103, 104, 105, 106, 107}

print("Both electives:", ai & iot)
print("Exactly one:", ai ^ iot)
print("Neither:", all_students - (ai | iot))
