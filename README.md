# Text-to-MP3

A simple Python utility for converting `.txt` files into `.mp3` audio
files.

The script is designed primarily for **Windows drag-and-drop use**. Drag
a text file onto the Python script, and it will automatically create an
MP3 with the same base filename in the same folder.

## How It Works

Example:

``` text
Chapter_1.txt
      ↓
Drag onto Convert_Text_to_Audio_1.0.py
      ↓
Chapter_1.mp3
```

The program will:

1.  Check that the input file is a `.txt` file.
2.  Read the text using UTF-8 encoding.
3.  Convert the text to speech using `gTTS`.
4.  Save the resulting MP3 beside the original text file.
5.  Display the location of the saved MP3.
6.  Display the approximate audio length of the MP3.

The current script uses `gTTS` for text-to-speech conversion and
`mutagen` to read the duration of the generated MP3.

## Requirements

The script was written for **Python 3.10**.

Install the required packages from PowerShell or Command Prompt:

``` powershell
py -3.10 -m pip install gTTS
py -3.10 -m pip install mutagen
```

`sys` is part of the Python standard library and does not need to be
installed separately.

## Windows Drag-and-Drop

The easiest way to use the program on Windows is:

1.  Save or create a `.txt` file.
2.  Locate `Convert_Text_to_Audio_1.0.py`.
3.  Drag the `.txt` file onto the Python script.
4.  The program will start automatically.
5.  Wait for the MP3 conversion to finish.
6.  The resulting `.mp3` file will appear in the same location as the
    original `.txt` file.

The drag-and-drop behavior works because Windows passes the dropped
filename to the script as a command-line argument, which the program
reads using:

``` python
file = sys.argv[1]
```

## Example Output

``` text
Starting Program

Starting to Read File: D:\Text-to-MP3\Testing.txt
Done Reading File!

Converting Text to Speech
Done Converting Text to Speech

Saving to MP3
Done Saving File: D:\Text-to-MP3\Testing.mp3

MP3 Length: 0:03

Press Enter to close...
```

## Notes

`gTTS` requires an internet connection because the text-to-speech
conversion uses Google's service.

This utility is intended for converting text that you have the right or
permission to use. Generated audio should be handled in accordance with
the copyright, license, and terms that apply to the original text.

Privacy Note: gTTS uses Google's online text-to-speech functionality and requires an internet connection. 
Text submitted for conversion is sent to Google's servers for processing. 
Do not use this utility for confidential or sensitive information.

## Example Files

This repository may include:

``` text
Testing.txt
Testing.mp3
```

These demonstrate the expected input and output format.

## License

MIT License.
