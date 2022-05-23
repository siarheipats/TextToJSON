import time
import json


def read_text_file():
    """ This method reads the text file and splits it by " ".
        It returns a list of separated words"""
    with open('scores.txt', 'r') as infile:
        text = infile.readline()
    return text.split()


def clear_file():
    """ This method overwrites the text file by placing 'awaiting' command
     that will signal microservice that it is waiting for a command"""
    with open('scores.txt', 'w') as outfile:
        outfile.write("awaiting")


def write_to_JSON(text_list):
    """ This method writes the results from the text files to a JSON file """
    current_scores = []
    if text_list[1] == "" or text_list[2] == "":
        print("No UserName or Score recieved")
        return
    score = {
        "user": text_list[1],
        "score": text_list[2]
    }
    # get current scores:
    try:
        with open('scores.json') as openfile:
            current_scores = json.load(openfile)
    except:
        print("File is empty. Adding the first score")
    # add new score
    current_scores.append(score)
    with open('scores.json', 'w') as outfile:
        json.dump(current_scores, outfile, indent=4, separators=(',',': '))
    clear_file()
    print( text_list[1], " score of ", text_list[2], " was added to scores.json file!")


print("Listening 'scores.txt' ")
while True:
    result = read_text_file()
    if len(result) == 3:
        write_to_JSON(result)
    elif result[0] == "awaiting":
        time.sleep(2)
    else:
        print("Invalid command")
        clear_file()
        time.sleep(2)
