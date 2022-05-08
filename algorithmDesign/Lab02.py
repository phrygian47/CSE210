# 1. Name:
#      -Robert Elliott-
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      -This program reads a json file, then separates it into two lists so you can compare the elements between the two. 
#           then you prompt the user for input on username and password, if both match in the same place of both lists, it prints 'you are authenticated'-
# 4. What was the hardest part? Be as specific as possible.
#      -I haven't worked with json files before, knowing no how they work it seems fairly simple as you just treat them as dictionaries (at this for this assignment)
#           the other hardest part was remembering the different methods used for dictionaries so that I could actually get it into two different lists of usernames and passwords
#           Also for some reason even though I downloaded the json file into the same folder as my Lab02.py file, it would not see it so I had to use the relative filepath instead.
#           if this causes errors for your testing because of different folder names and path writing conventions (if on mac instead of windows), the filepath just needs to be changed.-
# 5. How long did it take for you to complete the assignment?
#      -this program took me about 4 hours with the reading of review material, figuring our why the local filepath of "Lab02.json" wasn't working, and coding-
import json

def main():
    # Get a list of usernames and passwords from the given json file
    usernames, passwords = parse_json("algorithmDesign\Lab02.json")
    # Ask the user for a username and password
    username = input("Username: ")
    password = input("Password: ")
    # Compare the given username and password with the lists
    if (username in usernames) and (password in passwords):
        index = usernames.index(username)
        if (username == usernames[index]) and (password == passwords[index]):
            # If username and password are in both lists and in the same index
            print("You are authenticated!")
        else:
            print("You are not authorized to use the system.")
    else:
        print("You are not authorized to use the system")
          
                

def parse_json(file):
    with open(file) as json_file:
        dict = json.load(json_file)
        values = list(dict.values())
        usernames = list(values[0])
        passwords = list(values[1])
        return usernames, passwords
    
    
if __name__ == "__main__":
    main()