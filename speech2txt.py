
#
# speech2txt.py : trasforma il parlato registrato (.m4a/.mp3/.3ga/.wav) in file di testo.
#
#                     n.b.: installare :
#
#                               ffmpeg da https://www.gyan.dev/ffmpeg/builds/
#                               pip install audioop-lts
#                               pip install SpeechRecognition
#
#


from seleziona_file import seleziona
from speech_to_txt import converti_in_testo

if __name__ == "__main__":
    
    file_audio,tipo = seleziona() # apre una finestra di selezione del file
    
    converti_in_testo(file_audio,tipo)