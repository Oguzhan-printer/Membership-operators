#Task 1

fruits =['apple','pear', 'strawberry', 'cherry']
wanted_fruit = str(input('take a fruit name :'))

if wanted_fruit in fruits:
    print(f'you have  {wanted_fruit}')
else:
    print('you don have this fruit')


#Task 2

password = 'PyThOn123'
enter_character = str(input('enter your character: '))

if enter_character not in password:
    print('This character is not in the password')
else:
    print('This character is in the password')

 