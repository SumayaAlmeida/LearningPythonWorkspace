list1 = [10, 20, 30, 40, 50, 60]
list2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
list3 = [5, 10, 15]
list4 = [1, 2, 3, 4, 5, 6]

print(F"LIST 1: {list1}")
print(F"LIST 2: {list2}")
print(F"LIST 3: {list3}")
print(F"LIST 4: {list4}")


def list_multiply (list_1, list_2):
    result =[]
    if len(list_1) <= len(list_2):
        for i in range(len(list_1)):
            num = list_1[i] * list_2[i]
            result.append(num)
    else:
         for i in range(len(list_2)):
            num = list_1[i] * list_2[i]
            result.append(num)


    return result
    
print(f"If list1 is shorter than list2, not all numbers in list2 will be used:\n {list_multiply(list1, list2)}")
print(f"If list1 is longer than list2, then not all numbers in list1 will be multiplied:\n {list_multiply(list1, list3)}")
print(f"If the lists's len is equal all numbers in list1 will be multiplied:\n {list_multiply(list1, list4)}")

print(F"LIST 1: {list1}")
print(F"LIST 2: {list2}")
print(F"LIST 3: {list3}")
print(F"LIST 4: {list4}")




