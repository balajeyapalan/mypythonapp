'''
Python  assignment 2
Revere a string with getting input firstname and lastname
'''

first_name = input("Please enter first name: ")
last_name = input("Please enter last name: ")
fullname = first_name + " " + last_name
count = len(fullname)
reversed_string = ""
while (count != 0):
    reversed_string = reversed_string + fullname[count - 1]
    # print(b[count-1])
    count = count - 1

print("Reversed string is : ", reversed_string)
