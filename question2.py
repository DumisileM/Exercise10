# define variables
correct_pin = "2021"
max_attempts = 3
attempts = 0
attempts_left = max_attempts - attempts

# ask user for PIN
supplied_pin = input("Enter your PIN: ")

# while user hasn't reached the naximum attempts
while 0 <= attempts < max_attempts:
    # increase number of attempts each time
    attempts += 1
    # check whether user PIN matches correct PIN
    if supplied_pin == correct_pin:
        print("Congratulations, you haven't forgot your PIN!")
        break
    # if user PIN does not match correct PIN and maximum number of attempts has not been reached, keep asking for PIN
    elif supplied_pin != correct_pin and attempts != max_attempts:
        print("The PIN is incorrect, please try again. You have", (max_attempts - attempts), "attempts left.")
        supplied_pin = input("Enter your PIN: ")
# when user reaches maximum number of attempts, print end message
if attempts == max_attempts:
    print("You have reached the maximum number of attempts!")


