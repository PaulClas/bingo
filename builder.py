from mailmerge import MailMerge
from docx2pdf import convert
import shutil
from pathlib import Path
from datetime import date
from bingo import card_generator, get_names

bingo_dict ={
    "name":"John Doe",
    "date":"date",
    "aa": 'empty',
    "ab": 'empty',
    "ac": 'empty',
    "ad": 'empty',
    "ae": 'empty',
    "ba": 'empty',
    "bb": 'empty',
    "bc": 'empty',
    "bd": 'empty',
    "be": 'empty',
    "ca": 'empty',
    "cb": 'empty',
    "cc": 'empty',
    "cd": 'empty',
    "ce": 'empty',
    "da": 'empty',
    "db": 'empty',
    "dc": 'empty',
    "dd": 'empty',
    "de": 'empty',
    "ea": 'empty',
    "eb": 'empty',
    "ec": 'empty',
    "ed": 'empty',
    "ee": 'empty',
}

def clean_repo():
    if (Path("./docx").exists()):
        shutil.rmtree("./docx")
        print("Folder docx deleted")
    if (Path("./pdf").exists()):
        shutil.rmtree("./pdf")
        print("Folder pdf deleted")
    else:
        print("Good to go")
        
def create_path(path):
    Path("./"+path).mkdir(parents=True, exist_ok=True)
    
def path_manager(name,format):
    create_path(format)
    file_name="BingoPolyVoile_"+name+"."+format
    file_path= "./"+format+"/"+file_name
    return file_path

def valid_xml_char_ordinal(c):
    codepoint = ord(c)
    return (
        0x20 <= codepoint <= 0xD7FF or
        codepoint in (0x9, 0xA, 0xD) or
        0xE000 <= codepoint <= 0xFFFD or
        0x10000 <= codepoint <= 0x10FFFF
        )

def generate_docx_card(bingo_card,name):
    dic_keys=list(bingo_dict.keys())
    bingo_dict.update({dic_keys[0]:name})
    bingo_dict.update({dic_keys[1]:date.today().strftime("%d/%m/%Y")})
    dic_counter=2
    for i in range(5):
        for j in range(5):
            temp=''.join(c for c in bingo_card[i][j] if valid_xml_char_ordinal(c))
            bingo_dict.update({dic_keys[dic_counter]:temp})
            dic_counter=dic_counter+1
    template = "./template/bingo_template.docx"
    document = MailMerge(template)
    document.merge_pages([bingo_dict])
    saved_file_docx=path_manager(name,"docx")
    document.write(saved_file_docx)
    saved_file_pdf=path_manager(name,"pdf")
    convert(saved_file_docx, saved_file_pdf)
    
def generate_docx_cards(bingo_file, names_file):
    names= get_names(names_file)
    for name in names:
        bingo_card=card_generator(bingo_file)
        generate_docx_card(bingo_card,name)

clean_repo()
generate_docx_cards("./data/BingoSentences.txt", "./data/PolyVoileNames.txt")



