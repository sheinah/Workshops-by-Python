class Book:
    def __init__(self, title, color):
        self.title = title
        self.color = color

# Instance objects of Book class
blue_book = Book("The blue kid", "Blue")
green_book = Book("The frog story", "Green")

# Printing the type of the books

print(type(blue_book))
# <class '__main__.Book'>
print(type(green_book))
# <class '__main__.Book'>

import random # Module for random operations

class BaseGame:

    # Lenght which the message is centered
    message_lenght = 60
    
    description = ""    
        
    def __init__(self, points_to_win, n_lives=3):
        """Base game class

        Args:
            points_to_win (int): the points the game will need to be finished 
            n_lives (int): The number of lives the student have. Defaults to 3.
        """
        self.points_to_win = points_to_win

        self.points = 0
        
        self.lives = n_lives

    def get_numeric_input(self, message=""):

        while True:
            # Get the user input
            user_input = input(message) 
            
            # If the input is numeric, return it
            # If it isn't, print a message and repeat
            if user_input.isnumeric():
                return int(user_input)
            else:
                print("The input must be a number")
                continue     
             
    def print_welcome_message(self):
        print("PYTHON MULTIPLICATION GAME".center(self.message_lenght))

    def print_lose_message(self):
        print("SORRY YOU LOST ALL OF YOUR LIVES".center(self.message_lenght))

    def print_win_message(self):
        print(f"CONGRATULATION YOU REACHED {self.points}".center(self.message_lenght))
        
    def print_current_lives(self):
        print(f"Currently you have {self.lives} lives\n")

    def print_current_score(self):
        print(f"\nYour score is {self.points}")

    def print_description(self):
        print("\n\n" + self.description.center(self.message_lenght) + "\n")

    # Basic run method
    def run(self):
        self.print_welcome_message()
        
        self.print_description()

game = BaseGame(5)

# Accessing game message lenght class attr from class
print(game.message_lenght) # 60

# Accessing the message_lenght class attr from class
print(BaseGame.message_lenght)  # 60

# Accessing the points instance attr from instance
print(game.points) # 0

# Accesing the points instance attribute from class
#print(BaseGame.points) # Attribute error


class RandomMultiplication(BaseGame):

    description = "In this game you must answer the random multiplication correctly\nYou win if you reach 5 points, or lose if you lose all your lives"

    def __init__(self):
        # The numbers of points needed to win are 5
        # Pass 5 "points_to_win" argument
        super().__init__(5)

    def get_random_numbers(self):

        first_number = random.randint(1, 10)
        second_number = random.randint(1, 10)

        return first_number, second_number
        
    def run(self):
        
        # Call the upper class to print the welcome messages
        super().run()
        

        while self.lives > 0 and self.points_to_win > self.points:
            # Gets two random numbers
            number1, number2 = self.get_random_numbers()

            operation = f"{number1} x {number2}: "

            # Asks the user to answer that operation 
            # Prevent value errors
            user_answer = self.get_numeric_input(message=operation)

            if user_answer == number1 * number2:
                print("\nYour answer is correct\n")
                
                # Adds a point
                self.points += 1
            else:
                print("\nSorry, your answer is incorrect\n")

                # Substracts a live
                self.lives -= 1
            
            self.print_current_score()
            self.print_current_lives()
            
        # Only get executed when the game is finished
        # And none of the conditions are true
        else:
            # Prints the final message
            
            if self.points >= self.points_to_win:
                self.print_win_message()
            else:
                self.print_lose_message()

'''
    # Parent class
    def __init__(self, points_to_win, n_lives=3):

    # Basic run method
    # Parent method
    def run(self):
        self.print_welcome_message()
        
        self.print_description()
    def run(self):
        
        # Call the upper class to print the welcome messages
        super().run()
        
    # Child class
    def __init__(self):
        # The numbers of points needed to win are 5
        # Pass 5 "points_to_win" argument
        super().__init__(5)
'''

class TableMultiplication(BaseGame):

    description = "In this game you must resolve the complete multiplication table correctly\nYou win if you solve 2 tables"
    
    def __init__(self):
        # Needs to complete 2 tables to win
        super().__init__(2)

    def run(self):

        # Print welcome messages
        super().run()

        while self.lives > 0 and self.points_to_win > self.points:
            # Gets two random numbers
            number = random.randint(1, 10)            

            for i in range(1, 11):
                
                if self.lives <= 0:
                    # Ensure that the game can't continue 
                    # if the user depletes the lives

                    self.points = 0
                    break 
                
                operation = f"{number} x {i}: "

                user_answer = self.get_numeric_input(message=operation)

                if user_answer == number * i:
                    print("Great! Your answer is correct")
                else:
                    print("Sorry your answer isn't correct") 

                    self.lives -= 1

            self.points += 1
            
        # Only get executed when the game is finished
        # And none of the conditions are true
        else:
            # Prints the final message
            
            if self.points >= self.points_to_win:
                self.print_win_message()
            else:
                self.print_lose_message()

if __name__ == "__main__":

    print("Select Game mode")

    choice = input("[1],[2]: ")

    if choice == "1":
        game = RandomMultiplication()
    elif choice == "2":
        game = TableMultiplication()
    else:
        print("Please, select a valid game mode")
        exit()

    game.run()

                