import os, re
from PyPDF2 import PdfWriter, PdfReader



#pdf_path = input("Please provide your pdf file path that you would like to be split"
pdf_path = 'illustrative-hedge-funds-2018-web.pdf'


#make a function to split the pdfs into seperate pages. Should have a variable for file path
#than one variable of extracted text you would like each individual file named by
def split_pdf(pdf_path):
    with open(f"{pdf_path}", 'rb') as infile:
        #reader object to get info regarding page numbers etc...
        reader = PdfReader(infile)

        #loop through each page
        i = 0
        while i < len(reader.pages):
            #loop through each page

            #initialize pdf object
            writer = PdfWriter()
            #add a page to the object
            writer.add_page(reader.pages[i])
           

            #open a new pdf file to write to
            try:
                with open(f"{i}_{extract_pdf_text(i, pdf_path)}.pdf", 'wb') as output_file:
                    #write to the new pdf adding the single page to the pdf
                    writer.write(output_file)
                    
            except:
                print(f"Page {i} has no custody account number")
                pass
            i+=1
    


#how do we just extract text from first 20 letters of header
def extract_pdf_text(page_number, file):
    with open(f"{file}", 'rb') as infile:
        #create reader object
        reader = PdfReader(infile)
        #read through page
        page = reader.pages[page_number]
        #extract text into variable
        text = page.extract_text()
        #pattern of a custody account
        custody_pattern = re.compile(r'\d{9}')
        #, search for custody account in extracted text for the page
        matches = custody_pattern.finditer(text)
        #if there is a match return the match
        if matches:
            for match in matches:
                return match.group(0)
            
        else:
            return 'No custody account available'
   
    
        
        


split_pdf(pdf_path)

# with open("illustrative-hedge-funds-2018-web.pdf", 'rb') as infile:
#         #create reader object
#         reader = PdfReader(infile)
#         #read through page
#         page = reader.pages[0]
#         #extract text into variable
#         text = page.extract_text()
#         #pattern of a custody account
#         custody_pattern = re.compile(r'financial')
#         #, search for custody account in extracted text for the page
#         matches = custody_pattern.finditer(text)
#         #if there is a match return the match
#         if matches:
#             for match in matches:
#                 print(text)
#                 print(match.group(0))
            
#         else:
#             print('no custody account info')
        
      