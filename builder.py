from bingo import card_generator, printing_card
import os

file="BingoSentences.txt"

if os.path.exists("bingo.docx"):
  os.remove("bingo.docx")
  print("bingo.docx removed")
else:
  print("The file does not exist")

document = Document()

document.add_heading('Bingo PolyVoile', 0)

p = document.add_paragraph("Bingo pour l'équipe d'entrainement de PolyVoile.")
p.add_run('bold').bold = True
p.add_run(' and some ')
p.add_run('italic.').italic = True


records = (
    (3, '101', 'Spam'),
    (7, '422', 'Eggs'),
    (4, '631', 'Spam, spam, eggs, and spam')
)
table = document.add_table(rows=0, cols=5)
card= card_generator(file)

for row in card:
    row_cells = table.add_row().cells
    print(card[0][0])
    a=card[0][0]
    row_cells[0].text = a
# for i in range(3):
#     row_cells = table.add_row().cells
#     print(card[i][0])
#     row_cells[i].txt = records[i][1]
document.save('bingo.docx')