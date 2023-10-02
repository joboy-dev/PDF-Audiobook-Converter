import time

import utils
from pdf_to_text_functions import convert_single_page, convert_all_pages, is_file_allowed
from text_to_speech import save_or_play_now

print(utils.logo)

while True:
    text = ''
    pdf_path = input('Enter the full path to your PDF file: \n')
    
    print('Checking file format ... \n')
    time.sleep(1)
    
    if is_file_allowed(pdf_path):
        print('Processing file ... \n')
        time.sleep(2)
        try:
            # open pdf file
            with open(file=pdf_path, mode='rb') as pdf:
                while True:
                    print('Do you want to convert all pages to audiobook or a single page?\n')
                    choice = input('Press A to convert all pages into audiobook and S to convert a single page into audiobook: \n').upper()
                    
                    if choice == 'S':
                        text = convert_single_page(pdf)
                        
                        print('Generating audio book ... \n')
                        time.sleep(2)
                        save_or_play_now(text)
                        break
                    elif choice == 'A':
                        text = convert_all_pages(pdf)
                        
                        print('Generating audio book ... \n')
                        time.sleep(2)
                        save_or_play_now(text)
                        break
                    else:
                        print('Invalid choice. Try again')
        except FileNotFoundError:
            print('This file does not exist. Try again.')
        
        break
    else:
        print('This file format is not allowed. Try again.')