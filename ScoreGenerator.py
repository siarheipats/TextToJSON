import time

while True:
    userName = input("Please, enter the user name: ")
    score = input("Please, enter the score: ")
    command = "run " + userName + " " + score
    with open('scores.txt', 'w') as outfile:
        outfile.write(command)
    time.sleep(1)