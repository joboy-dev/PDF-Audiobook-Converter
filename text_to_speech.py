import pyttsx3
from gtts import gTTS, gTTSError

import os
from datetime import datetime
import time

def convert_text_to_speech(text):
    '''Function to convert single page from pdf into speech'''
    
    print('Ensure you are connected to the internet to avoid issues.')
    
    conversion = True
    
    while conversion:
        try:
            audio = gTTS(text=text)
            
            # Get the directory where the script is located
            script_directory = os.path.dirname(os.path.realpath(__file__))
            
            print('You have the option to give the audio file generated a name. If no name is provided, a default name will be provided for you.')
            filename_input = input('Give your file a name: \n')
            
            if filename_input:
                # Define the filename
                filename = f"{filename_input}.mp3"
            else:
                # Define the filename using a timestamp
                filename = datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".mp3"
            
            audio_save_path = os.path.join(script_directory, filename)
            
            print('Saving audio file ... \n')
            audio.save(audio_save_path)
            
            print('Audio file saved successfully.')
            time.sleep(1)
            
            conversion = False
        except gTTSError as gtts_error:
            print('An error has occured while getting ready to save your audio file.')
            print(gtts_error)
            time.sleep(2)
        except Exception as e:
            print('An error occured.')
            print(e)
        
        
def play_now(text):
    '''Function to play audio immediately'''
    
    # reading the text
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()
    
    while True:
        choice = input('Do you wish to save the audio book? Y/N\n').upper()
        
        if choice == 'Y':
            convert_text_to_speech(text)
            break
        elif choice == 'N':
            print('Alright. Thanks for using this service.')
            time.sleep(2)
            break
        else:
            print('Invalid input. Try again')
            

def save_or_play_now(text):
    '''Function that asks the user if they want to save the audio book or just play the book'''
    
    while True:
        choice = input('Press P to play the audio book now, press S to save the book: \n').upper()
        
        if choice == 'S':
            convert_text_to_speech(text)
            break
        elif choice == 'P':
            play_now(text)
            break
        else:
            print('Invalid input. Try again')
    