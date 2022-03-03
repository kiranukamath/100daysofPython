import random

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(",")

#Write your code below this line 👇

#Get the total number of items in list.
num_items = len(names)
#Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, num_items - 1)
#Pick out random person from list of names using the random number.
print(names)
person_who_will_pay = names[0]

print(person_who_will_pay + " is going to buy the meal today!")