full_name = input('Please enter your full name:')
name_length = len(full_name)

while True:
    if len(full_name) == 0:
        print('You haven\'t entered anything. Please enter your full name.')
        full_name = input('Please enter your full name:')
    elif len(full_name) > 0 and len(full_name) < 4:
        print('You have entered less than 4 characters.\nPlease make sure that you have entered your name and surname.\n')
        full_name = input('Please enter your full name:')
    elif len(full_name) > 25:
        print('You have entered more than 25 characters. \nPlease make sure that you have only entered your full name.')
        full_name = input('Please enter your full name:')
    else:
        print('Thank you for entering your name.')
        break

#Tried to add a check for user entering a space to make it
#more likely they have entered two seperate names.
#Researched in/not but have not been able to make it work:

# no_space = ('') not in full_name

    # elif no_space == True:
    #     print('Please enter your first name AND your surname.')
    #     full_name = input('Please enter your full name:')