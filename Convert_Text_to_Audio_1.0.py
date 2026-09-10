#!/usr/bin/env python3.10

# Required Packages
from gtts import gTTS
import sys
from mutagen.mp3 import MP3

'''
Ensure The Following Modules Are Installed Prior to Running:
py -3.10 -m pip install gTTS
py -3.10 -m pip install mutagen
'''


def main():

    ################################Parameters#############################

    # Just drag and drop file onto python script
    file = sys.argv[1]
    #file = "Testing.txt"

    #######################################################################

    print ("Starting Program")
    print ("\n")

    # If file not a TXT kills the program with a warning message
    if not file.lower().endswith(".txt"):
        sys.exit("Error: File must be a .txt file")

    # Get the file name by splitting on the right side
    split_file_name = file.rsplit(".", 1)
    base_file_name = split_file_name[0]

    print ("Starting to Read File: " + file)
    # Read the text into file
    with open(file, "r", encoding="utf-8") as open_file:
        text = open_file.read()
    print ("Done Reading File!")
    print ("\n")

    # Convert text to speech
    print ("Converting Text to Speech")
    tts = gTTS(text=text, lang="en")
    print ("Done Converting Text to Speech")
    print ("\n")

    # Save as MP3
    print ("Saving to MP3")
    output_file_name = base_file_name + ".mp3"
    tts.save(output_file_name)
    print("Done Saving File: " + output_file_name)
    print ("\n")

    # Get the Audio Size of the Final MP3 for Reference
    audio = MP3(output_file_name)
    seconds = audio.info.length
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    print(f"MP3 Length: {minutes}:{seconds:02d}")
    print ("\n")
    

    # Keeps the Window Open Till User Closes
    input("Press Enter to close...")

if __name__ == "__main__":
    main()
