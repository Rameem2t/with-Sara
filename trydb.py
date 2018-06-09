import psycopg2
from pprint import pprint
import speech_recognition as sr
import re


class DatabaseConnection:

    def __init__(self):
        try:
            self.conniction = psycopg2.connect(
                "dbname= 'sample_db' user='raneem' host='localhost' password='123456' port='5432'")
            self.conniction.autocommit = True
            self.cursor = self.conniction.cursor()

        except:
            pprint("Cannot connect to database")

    # create table
    def create_table(self):
        create_table_command = "CREATE TABLE pet(id serial PRIMARY KEY, name varchar (100), age integer NOT NULL)"
        self.cursor.execute(create_table_command)



    # insert new record
    def insert_new_record(self):
        new_record = ("meo", "3")
        insert_command = "INSERT INTO pet(name,age) VALUES('" + new_record[0] + "','" + new_record[1] + "')"
        pprint(insert_command)
        self.cursor.execute(insert_command)

    # display all records
    def query_all(self):
        self.cursor.execute("SELECT * FROM pet")
        cats = self.cursor.fetchall()
        for cat in cats:
            pprint("each pet : {0}".format(cat))

    # update record
    def update_record(self):
        update_comoand = "UPDATE pet SET age=10 where id=1"
        self.cursor.execute(update_comoand)


    # delete table
    def drop_table(self):
        drop_table_command = "DROP TABLE pet "
        self.cursor.execute(drop_table_command)



     # audio to text
    def audio_to_text(self):

        r = sr.Recognizer()

        with sr.AudioFile("/Users/raneem/PycharmProjects/databaseEG/audio_files/harvard.wav") as source:
            audio = r.record(source)

        s = r.recognize_google(audio)

        # spilt string to words
        # wordList = re.sub("[^\w]", " ", s).split()
        # wordList = s.split()
        wordList = s.split()

        print(s)
        print(wordList)


        # to find the criminal words
        for i in range(len(wordList)):
            self.cursor.execute("SELECT name FROM pet WHERE name = '%s'" % wordList[i])

            for row in self.cursor:
                row == ""
                print(row)


if __name__== '__main__':
    database_connection = DatabaseConnection()
    # database_connection.create_table()       # create table
    # database_connection.insert_new_record()  # insert new record
    # database_connection.query_all()          # display all records
    # database_connection.update_record()      # update record
    # database_connection.drop_table()         # delete table
    database_connection.audio_to_text()