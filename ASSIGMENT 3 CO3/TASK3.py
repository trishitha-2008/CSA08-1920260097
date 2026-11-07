complaints = [
    "water problem",
    "road problem",
    "water shortage",
    "road damage"
]

count = {}

for word in " ".join(complaints).split():
    count[word] = count.get(word, 0) + 1

print("Word count:", count)
print("Top complaints:", sorted(count.items(),
      key=lambda x: x[1], reverse=True))
