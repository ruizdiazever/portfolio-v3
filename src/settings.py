import os
from os.path import join, dirname
from dotenv import load_dotenv


# LOAD ENV
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)


# SECRET
DB_DATABASE = os.environ.get("DB_DATABASE")
DB_HOST = os.environ.get("DB_HOST")
DB_SCHEMA = os.environ.get("DB_SCHEMA")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_PORT = os.environ.get("DB_PORT")

