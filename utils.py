from hashfuncs import base_hash, blake2_hash
import os

constants = {
    # Causa ricorsione, outidr non può stare qua. merda.
    #"outdir":"",
    "basedir":"",
    "hashfun":blake2_hash
}



#   Esplora le sottodirectory della basedir e per ciascun elemento
#   crea un file di testo .fsimg se si tratta di un file,
#   crea la rispettiva cartella in outdir altrimenti.
#
#   :param [base] base dir
def new_image(base, outdir):
    filelist = os.listdir(base)

    for x in filelist:
        # Absolute path per la sorgente
        filepath = base + os.path.sep + x
        # Absolute path per la destinazione
        outputpath = outdir + os.path.sep + x
        if os.path.isdir(filepath):         # se è cartella...
            add_out(outputpath)             # crea la corrispettiva cartella in outdir
            new_image(filepath, outputpath) # Ricorsione nella cartella in questione
    
        else:                               # altrimenti
            hash_result = makehash(filepath)# esegue l'hash
            add_out(outputpath, True, hash_result)# crea il file .fsimg



# Questa funzione viene usata fondamentalmente in due modi:
#   1) per creare una cartella; in tal caso basta passare solo il nome
#   2) per creare un file immagine; in tal caso bisogna specificare
#      il fatto che sia un file (file=True) e l'hash del contenuto (hash_result="blablabla")

def add_out(output_path, file=False, hash_result=None):
    if output_path == "" or output_path==None: raise Exception("[add_out function] Output path cannot be null")

    if os.path.exists(output_path):
        # TODO Se abilitata la sovrascrittura (per ora mi serve sempre)
        os.remove(output_path)

    if file:
        with open(output_path+".fsimg", "wb") as f:
            f.write(hash_result)
    else:
        os.makedirs(output_path)


# Funzione che ritorna l'hash di un file.
# La funzione è specificata in _constants["hashfun"]
def makehash(filepath):
    content = ""
    if not os.path.isfile(filepath):
        raise Exception("[ERROR] {} is not a file".format(filepath))

    with open(filepath, "rb") as f:
        content = f.read()
    f = constants["hashfun"]
    return f(content)