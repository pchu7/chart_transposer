# Chart Transposer
# Author: Phillip Chu
# Date: 7/7/2021
# Description: A script to transpose the key of a chord chart 
# stored as a word document

# ----------------------
# General Includes
# ----------------------
import docx


# ----------------------
# Variables 
# ----------------------
doc = docx.Document("Living Hope - Test.docx")
transposed_doc = docx.Document()

all_paragraphs = doc.paragraphs

print ( len ( all_paragraphs ) )
for para in all_paragraphs:
    print ( para.text )
    #print ( "----------" )


