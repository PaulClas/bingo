from __future__ import print_function
from mailmerge import MailMerge
from datetime import date
import os
from bingo import card_generator, printing_card

file="english_shit.txt"

bingo_card=card_generator(file)

bingo_dict ={
    "aa": 'hello',
    "ab": 'empty',
    "ac": 'empty',
    "ad": 'empty',
    "04": 'empty',
    "11": 'empty',
    "11": 'empty',
    "12": 'empty',
    "13": 'empty',
    "14": 'empty',
    "20": 'empty',
    "21": 'empty',
    "22": 'empty',
    "23": 'empty',
    "24": 'empty',
    "30": 'empty',
    "31": 'empty',
    "32": 'empty',
    "33": 'empty',
    "34": 'empty',
    "40": 'empty',
    "41": 'empty',
    "42": 'empty',
    "43": 'empty',
    "44": 'empty',
}


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
    template = "bingo_template.docx"
    document = MailMerge(template)
    bingo_dict.update({"aa":"fuck"})
    print(document.get_merge_fields())
    document.merge_pages([bingo_dict])
    document.write("bingo.docx")
        

# for i in range(5):
#     for j in range(5):
#         bingo_dict.update({str(i)+str(j):bingo_card[i][j]})
# #bingo_dict.update({"00":bingo_card[0][0]})
# template = "bingo_template.docx"
# document = MailMerge(template)
# document.merge(
#     aa=lines[j]
# )


