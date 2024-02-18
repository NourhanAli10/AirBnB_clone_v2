#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models import *

if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage() 
else:
    storage = FileStorage()
"""A unique FileStorage/DBStorage instance for all models.
"""
storage.reload()
