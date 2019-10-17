""" Entry point four our twitoff flask app """
#Run this out of TWITOFF folder

from .app import create_app #.app porque esta en la misma carpeta

APP = create_app()
