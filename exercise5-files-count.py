file = open("What is Python.txt", "r")
text = file.read()

search_term = input("Type a word to search:\n")

instances_found = int(text.count(search_term))

if instances_found > 0:
    print(f"Your word was found {instances_found} times")
else:
    print("word not found")