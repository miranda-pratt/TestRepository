# Import random
import random


# Main program procedure
def main():

    # Run the function play_choice to determine whether the user wants to play or exit
    # The returned value is stored in the variable choice

    choice = play_choice()

    # If choice is equal to 1 (exit the program)
    if choice == "1":

        print("Thanks for playing guess the number")
        quit()

    # If choice is equal to 2 (play the game)
    elif choice == "2":

        # Call the function generate_number to generate a random number between 0 and 100
        # Store the returned value in the variable number
        number = generate_number()

        # Set the number of lives remaining to 8
        lives_remaining = 8

        # Guessing loop
        # Keep guessing while the lives_remaining does not equal 0
        while lives_remaining != 0:

            # Call the function guess() and store the returned value in the variable user_guess
            user_guess = guess()

            if user_guess.isnumeric():

                # If the guess is equal to the random number
                if int(user_guess) == int(number):

                    # Call the just_right procedure with the number and lives_remaining arguments to customise
                    # the message
                    just_right(number, lives_remaining)
                    # Recall main
                    main()

                # If the guess is greater than the random number
                elif int(user_guess) > int(number):

                    # Call the too_high procedure to print a message saying the number was too high
                    too_high()

                    # Decrement the lives_remaining by 1
                    lives_remaining -= 1

                    # Call the function print_lives_remaining to print no of lives remaining
                    # Argument lives_remaining to pass the value of lives_remaining to the procedure
                    print_lives_remaining(lives_remaining)

                # If the guess is less than the random number
                elif int(user_guess) < int(number):

                    # Call the too_low procedure to print a message saying the number was too low
                    too_low()

                    # Decrement the lives_remaining by 1
                    lives_remaining -= 1

                    # Argument lives_remaining to pass the value of lives_remaining to the procedure
                    print_lives_remaining(lives_remaining)

                # Else invalid input
                # Display a message but don't decrement the lives_remaining variable
                else:

                    print("Invalid input, please try again")

            # Else invalid input
            # Display a message but don't decrement the lives_remaining variable
            else:

                print("Invalid input, please try again")

        # When lives_remaining gets to 0, break the while loop and print game over message
        # Then recall main to start again
        else:

            print("Game over, number was " + str(number))
            main()

    # If the input is not 1 or 2, display a message and recall main
    else:

        print("Invalid input, please try again")
        main()


# Play game function
# Returns the user input of whether the user wants to exit or play
def play_choice():

    return input("Enter 1 to exit or 2 to play: ")


# Generate number function
# Returns a random number between 0 and 100
def generate_number():

    return random.randint(0, 100)


# Guess function
# Returns the user guess of the number
def guess():

    return input("Enter your guess (0-100): ")


# Procedure to print "too high" if guess is greater than the random number
def too_high():

    print("Too high")


# # Procedure to print "too low" if guess is less than the random number
def too_low():

    print("Too low")


# Procedure to print congratulations when the play wins and then recalls main()
def just_right(number, lives_remaining):

    print("Well done, you guess the number " + str(number) + " with " + str(lives_remaining) + " lives remaining")
    main()


# Procedure to print lives remaining
# Parameter lives_remaining to personalise the message with no of lives remaining
# Uses an if statement for one life to provide better grammar
def print_lives_remaining(lives_remaining):

    if lives_remaining == 1:

        print("You have 1 life remaining")

    else:

        print("You have " + str(lives_remaining) + " lives remaining")


# At the beginning of the program, welcome the user and call the main game function
print("Welcome to guess the number")

main()
