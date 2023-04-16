import sqlite3
import geopy
from scrapers import *

#Setting up sqlite3 database
conn = sqlite3.connect('main.db')  #This connects to the DB file and, if there is no file, creates one
cursor = conn.cursor()  #Cursor is used for interacting with the DB
cursor.execute("CREATE TABLE data (store TEXT, food TEXT, price INTEGER)")#This line creates the table for the DB and sets the rows we need


