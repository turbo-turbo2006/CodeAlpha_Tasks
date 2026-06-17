# PART 1: THE BRAIN (Functions & If-Else)

# 1. Define a function here. Give it a descriptive name and set it up to accept one parameter (the user's message).
def greeting():
    print("Hi!")

def convo():
    print("I'm fine, thanks!")

def farewell():
    print("Goodbye!")

#  PART 2: THE ENGINE (Loops & Input/Output)
     
while True:
    # Printing a quick welcome message to the console so the user knows the bot is awake.
        print("Welcome to the rule based Chatbot")
        var = input("Give your input :(Hello),(How are you)or(Bye)").lower()

        if var == "hello":
            greeting()

        elif var == "how are you":
            convo()
        # Write an IF statement to check if the user typed "bye".
        # If true, use the command to BREAK out of the loop and shut the program down.
        elif var == "bye":
            farewell()
            break
    
        else:
            print("try other commands")
    
