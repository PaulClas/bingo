import random

gridSize=5
cards=1

def card_generator(file):
    with open(file) as f:
        lines = f.readlines()
        print(len(lines))
        j=0
        for i in range(0, len(lines)):
            if (i %2 == 0):
                lines[j] = lines[i].strip()
                if(i==0):
                    lines[j] = lines[j][2:]
                j+=1
        nb_lines=j
    bingoCard = []
    for h in range(cards):
        card = []
        randRange= range(0, nb_lines)
        card=random.sample(randRange, gridSize*gridSize)
        for i in range(gridSize):
            row = []
            for j in range(gridSize):
                string=lines[card[i+j*gridSize]]
                if string != " ":
                    row.append(string)
            bingoCard.append(row)
    return bingoCard

def printing_card(bingoCard):
    for i in range(5):
        for j in range(5):
            print(bingoCard[i][j], end=" | ")
