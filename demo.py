# First step: Import libraries
from dotenv import load_dotenv
from os import getenv
import psycopg2

# Step 2: We will load the .env file
load_dotenv()


# Step 3: Let's create a class
class PGSQL:
    # Step 3a: Create our user, password, server variables from the ENV file
    # __ (dunder) sets a variable to be a secret, therefore not accessible outside the class itself.
    __user = getenv("USER")
    __password = getenv("PASSWORD")
    __server = getenv("SERVER")
    # Step 3b: Connect to the database
    __pg_con = psycopg2.connect(
        dbname=__user,
        user=__user,
        password=__password,
        host=__server
    )
    # Step 3c: Create a cursor object
    __cur = __pg_con.cursor()
    
    # Step 5: Create tables function
    def create_tables(self, sql_filepath:str):
        # Uses the static method available to the class to create a string of the SQL Commands we wrote earlier
        start = self.create_file(sql_filepath)
        # Split based on end of query
        tables = start.split(';')
        # Iterate through the list of queries
        for table in tables:
            try:
                print(table)
                # Execute the SQL Command
                self.__cur.execute(table)
                # Commit the changes we have made to the database
                self.__pg_con.commit()
            # Except statement catches any programming error messages from psycopg2
            except psycopg2.ProgrammingError as msg:
                # Prints the message that we skip
                print(f'Command Skipped: {msg}')
                
    def insert_data(self, sql_filepath :str):
        start = self.create_file(sql_filepath)
        data_to_insert = start.split(';')
        for insert in data_to_insert:
            try:
                print(insert)
                self.__cur.execute(insert)
                self.__pg_con.commit()
            except psycopg2.ProgrammingError as msg:
                print(f'Command Skipped: {msg}')
                
                
    # Step 4: Create a static method
    @staticmethod
    def create_file(filepath : str):
        """ Open a file by the filepath and apply it to an SQL Table"""
        with open(filepath, 'r') as f:
            sql_file = f.read()
        return sql_file
    
if __name__ == '__main__':
    p = PGSQL()
    p.create_tables(r'C:\Users\Alex Lucchesi\OneDrive\Desktop\da_sql_day_1\amazon_mock_create.sql')
    p.insert_data(r'C:\Users\Alex Lucchesi\OneDrive\Desktop\da_sql_day_1\amazon_mock_insert.sql')