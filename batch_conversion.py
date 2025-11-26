
#
# batch_conversion.py : data una cartella processa tutti i files audio presenti convertendoli in testo.
#					  

from elenca_files import elenca_files
from speech_to_txt import converti_in_testo

FILE,TIPO = 0,1

def processa_files(percorso_cartella,lista_files_tipi):
    
    print(f'\nFiles presenti nella cartella {percorso_cartella} : \n')
    
    for file_e_tipo in lista_files_tipi:        
        tipo = file_e_tipo[TIPO]
        
        if tipo in ('m4a','mp3','3ga','wav'):
            file_audio = percorso_cartella + '\\' + file_e_tipo[FILE]
            
            # converti in testo.
            converti_in_testo(file_audio,tipo)    
            print(f'Convertito file audio: {file_audio} ({tipo})')
        
if __name__ == "__main__":

    percorso_cartella,lista_files_tipi = elenca_files()
    
    processa_files(percorso_cartella,lista_files_tipi)