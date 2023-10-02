import PyPDF2

import time

def is_file_allowed(file_path):
    '''Function to guard against all file types except for pdf'''
    
    if '.pdf' in file_path:
        return True
    else:
        return False


def convert_single_page(pdf):
    '''Function to convert only a single page in the pdf into an audiobook'''
    
    conversion = True
    while conversion:
        finalText = ''
        try:
            # initialize pdf file reader
            pdf_reader = PyPDF2.PdfReader(pdf)
            
            print(f'\nNOTE: This pdf has only {len(pdf_reader.pages)} pages\n')
            
            # get page number as input
            pageNo = int(input('Enter page number: \n'))
            
            # get the page content and store in a variable
            page = pdf_reader.pages[pageNo-1]
            
            # extract text
            finalText= page.extract_text()
            
        except IndexError:
            print('The pdf does not have this page number. PLease try again.')
        except Exception as e:
            print('An error occured. Please try again.')
            print(e)
            
            conversion - False
        # No errors
        else:
            conversion = False
            
            print('Getting file contents ... \n')
            time.sleep(1)
            
            return finalText
        
            
def convert_all_pages(pdf):
    '''Function to convert all pages in the pdf into an audiobook'''
    
    conversion = True
    while conversion:
        # create an empty string to store final text output
        finalText = ''
        try:
            # initialize pdf file reader
            pdf_reader = PyPDF2.PdfReader(pdf)
            
            # loop through the number of pages in the pdf
            for page_no in range(len(pdf_reader.pages)):
                # get a single page and store in a variable
                page = pdf_reader.pages[page_no]
                
                # extract text
                finalText += page.extract_text()
        except Exception as e:
            print('An error occured. Please try again.')
            print(e)
            conversion = False
            
        # No errors
        else:
            conversion = False
            
            print('Getting file contents ... \n')
            time.sleep(1)
            
            return finalText
