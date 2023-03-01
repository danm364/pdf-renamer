import os, re
from PyPDF2 import PdfWriter, PdfReader

#Need to figure out how to split pages




with open('illustrative-hedge-funds-2018-web.pdf', 'rb') as infile:

    reader = PdfReader(infile)

    #we want to read in one page copy it to the file we are writing to.
    
    #add a page to writer file from reader file
    #loop through each page
    i = 0
    while i < len(reader.pages):
        #loop through each page
        writer = PdfWriter()
        writer.add_page(reader.pages[i])
        i+=1
        with open(f"output_{i}.pdf", 'wb') as output_file:
            writer.write(output_file)
    
    #how do we create a new pdf for each page to be stored in?
    
        
        