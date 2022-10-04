import random

gridSize=5
cards=1

def read_bingo(file):
    with open(file) as f:
        lines = f.readlines()
        j=0
        for i in range(0, len(lines)):
            if (i %2 == 0):
                lines[j] = lines[i].strip()
                if(i==0):
                    lines[j] = lines[j][2:]
                j+=1
        nb_lines=j
    return lines, nb_lines

def read_names(file):
    with open(file) as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            lines[i] = lines[i].strip()
    return lines

def card_generator(file):
    temp=read_bingo(file)
    bingo_text=temp[0]
    nb_lines=temp[1]
    bingoCard = []
    for h in range(cards):
        card = []
        randRange= range(0, temp[1])
        card=random.sample(randRange, gridSize*gridSize)
        for i in range(gridSize):
            row = []
            for j in range(gridSize):
                string=bingo_text[card[i+j*gridSize]]
                if string != " ":
                    row.append(string)
            bingoCard.append(row)
    return bingoCard

def printing_card(bingoCard):
    for i in range(5):
        for j in range(5):
            print(bingoCard[i][j], end=" | ")

def get_names(file):
    names=read_names(file)
    return names