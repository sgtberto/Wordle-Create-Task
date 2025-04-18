import random as rand


#set up variables

wordbank = ["alpha", "beta"]
chosenword = []
letters = []
solved = 0
blank = []
board = []
wordinput = ""
attemptlimit = 5
attempt = 0
d = 0

#set up functions

def setup():
    global chosenword
    global letters
    global solved
    chosenword = wordbank[rand.randint(0, len(wordbank) - 1)]
    solved = len(chosenword)
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
            if guess[corlet] == letters[corlet]:
                    print (guess)
                    print(letters)
                    global solved
                    board.insert(corlet, u'\u2713')
                    board.pop(corlet + 1)
                    solved =+ 1
                    letters.insert(corlet, "_")
                    letters.pop(corlet + 1)
                    guess.insert(corlet, "_")
                    guess.pop(corlet + 1) 
                    print("check") 
        for islet in range(len(board)):
            global d
            print("guesses")
            print(board)
            print(letters)
            print(guess)
            if board[islet] != u'\u2713':
                for glet in range(len(guess)):
                    for let in range(len(letters)):
                        if guess[glet] == letters[let] and guess[glet] != "_":
                            board.insert(islet, u'\u25CB')
                            board.pop(islet + 1)
                            letters.insert(let, "_")
                            letters.pop(let + 1)
                            guess.insert(glet, "_")
                            guess.pop(glet + 1)
                            print("circle")
                            print(letters)
                            print(guess)
                            d = 1
                            print(d)
                            break                
                    if d == 1:
                        print("break")
                        break
                if d == 1:
                    print("break 2")
                    d = 0
                    break

                board.insert(islet, "x")
                board.pop(islet + 1)
                letters.insert(let, "_")
                letters.pop(let + 1)
                guess.insert(glet, "_")
                guess.pop(glet + 1)  
                print("haha") 
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
