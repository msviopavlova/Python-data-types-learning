available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "HDMI cable",
                   "DVD drive"
                   ]
#valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]#need lectures on comprehention
valid_choices = []
for i in range(1, len(available_parts) + 1):#we r adding 1 to the length, outside paremthesis
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = [] #create an empty list

while current_choice != '0':
    if current_choice in valid_choices:
        print("Adding {}".format(current_choice))
        index =int(choice) - 1 # look at line 34
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)
    else:
        print("Please add options from the list below: ")
        for number, part in enumerate(available_parts): # number is index position and part is the item from the list
            print("{0}: {1}".format(number +1, part)) # +1 coz indezing starts at 0


    current_choice = input()
print(computer_parts)

#the program creates a new list and lets u add the items to it.

# the choice is 1 greater than the item index but its easy to fix by subtracting 1.
# issue is current_choices is a string
