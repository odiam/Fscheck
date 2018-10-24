#!/usr/bin/python
import click
import os

from os.path import expanduser
from utils import constants, new_image


# TODO: Creare una funzione di hash e testarla.
# TODO: Fare in modo che new_image sovrascriva file omonimi

# Non ho ancora letto bene la documentazione di click,
# dunque lo scopo di questa funzione mi è ancora oscuro.
# Viene chiamato nel main.
@click.group()
def cli():
    pass

@cli.command("hello")
def hello():
    print("HELLO_WORLD")


# comando: python fscheck.py new -p percorso-da-'hashare' -o percorso dell'hash
@cli.command("new")
@click.option("-p", "--path", required=True)
@click.option("-o", "--output-dir", default=expanduser("~") + "/.fscheck")
#@click.option("-h", "--hash-function", ) valore fissato in un insieme di costanti
def new_image_controller(path=expanduser("~"), output_dir=expanduser("~") + "/.fscheck"):
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    constants["basedir"] = path # path da "hashare"
    constants["outdir"] = output_dir # output path
    # constants["hashfun"] = None
    new_image(path, output_dir)
    print(constants)
    


if __name__ == "__main__":
    #run_web = False
    cli(standalone_mode="False")

    # TEST
    #import tests