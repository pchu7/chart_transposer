# Chart Transposer
# Author: Phillip Chu
# Date: 7/7/2021
# Description: A script to transpose the key of a chord chart 
# stored as a word document

# ----------------------
# General Includes
# ----------------------
import docx


document = docx.Document("Living Hope - A (Album Version).docx")
all_paragraphs = document.paragraphs

for para in all_paragraphs:
    print ( para.text )
    #print ( "----------" )

