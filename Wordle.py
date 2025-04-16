import random as rand


#set up variables

wordbank = ["alpha", "beta"]
chosenword = wordbank[rand.randint(0, len(wordbank) - 1)]
letters = []
board = []
wordinput = ""
solved = len(chosenword)
attemptlimit = 5
attempt = 0

#set up functions

def setup(): 
    global letters
    letters = list(chosenword)
    print(letters)
    for boardset in range(len(letters)):
        board.append("_")

def ui():
    global wordinput
    global guess
    global solved
    solved = 0
    print(board)
    board.clear()
    wordinput = input("Guess? ")
    guess = list(wordinput)
    print(guess)

def computation():

    if len(letters) == len(guess):
        for let in range(len(guess)):
            if letters[let] == guess[let]:
                global solved
                board.append(u'\u2713')
                solved =+ 1
            else: 
                for corlet in range(len(guess)):
                    if letters[let] == guess[corlet] and yellow == false:
                        board.append(u'\u25CB')
                        
                                
    else:
        print("Wrong number of letters!")


def game():
    setup()
    for attempt in range(attemptlimit):
        global solved
        if solved != 1:
            ui()
            computation()
            print("Last guess: " + wordinput)
    print(board)
    if solved == 1:
        print("Congratulations you solved it!")
    else: 
        print("You lost :( Nice try!")
    playagain = input("Play again? Y/N")
    if playagain == "Y":
        board.clear()
        solved = 0
        game()

game()
