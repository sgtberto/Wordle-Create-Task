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
    letters = list(chosenword)
    print(letters)
    for boardset in range(len(letters)):
        board.append("_")

def ui():
    global wordinput
    print(board)
    board.clear()
    wordinput = input("Guess? ")

def computation():

    if len(wordinput) == len(chosenword):
        for let in range(len(chosenword)):
            for corlet in range(len(wordinput)):
                if chosenword[let] == wordinput[corlet]:
                    global solved
                    board.append(u'\u2713')
                    solved =+ 1
    else:
        print("Wrong number of letters!")
    print(board)

def game():
    setup()
    for attempt in range(attemptlimit):
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
