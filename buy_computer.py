available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "HDMI cable",
                   "DVD drive"
                   ]
current_choice = "-"
computer_parts = [] #create an empty list

while current_choice != '0':
    if current_choice in "123456": #
        print("Adding {}".format(current_choice))
        if current_choice == '1':
            computer_parts.append("computer") #if the customer choses option 1 we add computer to the list
        elif current_choice == '2':
            computer_parts.append("monitor")
        elif current_choice == '3':
            computer_parts.append("keyboard")
        elif current_choice == '4':
            computer_parts.append("mouse")
        elif current_choice == '5':
            computer_parts.append("mouse mat")
        elif current_choice == '6':
            computer_parts.append("HDMI cable")
    else:
        print("Please add options from the list below: ")
        for number, part in enumerate(available_parts): # number is index position and part is the item from the list
            print("{0}: {1}".format(number +1, part)) # +1 coz indezing starts at 0


    current_choice = input()
print(computer_parts)

#the program creates a new list and lets u add the items to it.