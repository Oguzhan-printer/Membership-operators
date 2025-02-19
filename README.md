TASK 1
This task checks if a fruit entered by the user is present in a predefined list of fruits.

Fruit List: fruits = ['apple', 'pear', 'strawberry', 'cherry'] creates a list named fruits containing four fruit names.

User Input: wanted_fruit = str(input('take a fruit name :')) prompts the user to enter a fruit name. The input is converted to a string (though it likely already is) and stored in the wanted_fruit variable.

Membership Check: if wanted_fruit in fruits: checks if the wanted_fruit is present in the fruits list. The in operator is used for this membership test.

Output:

If the fruit is found in the list, it prints a message confirming that the user has that fruit (using an f-string for formatted output).
If the fruit is not found, it prints a message indicating that the user doesn't have that fruit.


TASK 2
This task checks if a character entered by the user is present in a predefined password.

Password: password = 'PyThOn123' sets the password to the string 'PyThOn123'.

User Input: enter_character = str(input('enter your character: ')) prompts the user to enter a character.  The input is converted to a string and stored in the enter_character variable.

Non-Membership Check: if enter_character not in password: checks if the entered character is not present in the password string. The not in operator is used for this.

Output:

If the character is not in the password, it prints a message saying so.
If the character is in the password, it prints a message confirming its presence.
