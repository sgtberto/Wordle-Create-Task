import random as rand


#set up variables

wordbank = ["alpha", "beta"]
chosenword = wordbank[rand.randint(0, len(wordbank) - 1)]
letters = []
blank = []
board = []
wordinput = ""
solved = len(chosenword)
attemptlimit = 5
attempt = 0
d = 0

#set up functions

def setup(): 
    global letters
    letters = list(chosenword)
    print(letters)
    for boardset in range(len(letters)):
        blank.append("_")

def ui():
    global wordinput
    global guess
    global solved
    global board
    solved = 0
    print(board)
    board = blank
    wordinput = input("Guess? ")
    guess = list(wordinput)
    print(guess)

def computation():

    if len(letters) == len(guess):
        for corlet in range(len(board)): 
            if guess[0] == letters[0]:
                    print (guess)
                    print(letters)
                    global solved
                    board.insert(corlet, u'\u2713')
                    board.pop(corlet + 1)
                    solved =+ 1
                    letters.pop(0)
                    guess.pop(0) 
                    print("check") 
        for islet in range(len(board)):
            print("guesses")
            print(board[islet])
            print(letters)
            print(guess)
            if board[islet] != u'\u2713':
                for glet in range(len(guess)):
                    for let in range(len(letters)):
                        if guess[glet] == letters[let]:
                            global d
                            board.insert(islet, u'\u25CB')
                            board.pop(islet + 1)
                            letters.pop(let)
                            guess.pop(glet)
                            print("circle")
                            d = 1
                            break
                        else:
                            if let == len(letters) - 1:
                                board.insert(islet, "x")
                                board.pop(islet + 1)
                                guess.pop(glet)
                    if d == 1:
                        d = 0
                        break
        print("iteration")
                                                            
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
    playagain = input("Play again? Y/N ")
    if playagain == "Y":
        board.clear()
        solved = 0
        game()

game()
