import string


# Open the file in read mode
text = open("What is Python.txt", "r")
  
# Create an empty dictionary
dictionary_of_all_words = dict()
  
# Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()
  
    # Convert the characters in line to 
    # lowercase to avoid case mismatch
    line = line.lower()

    # Remove the punctuation marks from the line
    line = line.translate(line.maketrans("", "", string.punctuation))
  
    # Split the line into words
    words = line.split(" ")
    
  
    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in dictionary_of_all_words:
            # Increment count of word by 1
            dictionary_of_all_words[word] = dictionary_of_all_words[word] + 1
        else:
            # Add the word to dictionary with count
            if word == "":
                continue
            else:
                dictionary_of_all_words[word] = 1

#this converts the dictionary on a list of tuples [(key1, value1), (key2, value2), (key3, value3), .......]
sorted_dictionary = sorted(dictionary_of_all_words.items(), key=lambda x: x[1], reverse=True)
#print(type(sorted_dictionary[1]))

for x in sorted_dictionary:
    print (f"{x[0]} : {x[1]}")

text.close()
    