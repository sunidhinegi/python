import mysql.connector as connector
import argparse
from datetime import datetime


# con = connector.connect(host='localhost', port='3306',user='root',password='drupal',database='pyDb')
# # print(con);

# query = 'create table if not exists names(id int primary key, title varchar(200), created_at datetime, completed_at datetime, status varchar(200))'

# cursors = con.cursor()
# cursors.execute(query)
# print("table is created")

# def insert(nameid, name, createddate, completedate, status):
#     query = "INSERT into names(id, title, created_at, completed_at, status) VALUES({},'{}',{},{},'{}')"

# cursors = con.cursor()
# cursors.execute(query)
# con.commit()
# print("entry done")

# insert(1, "sona", "2021-1-31", "2021-1-31", "incomplete")
# print("new")

class Databases:

    def __init__(self):
        self.con = connector.connect(host='localhost', port='3306',user='root',password='drupal',database='pyDb')
        print(self.con)
        query = 'create table if not exists names(id int AUTO_INCREMENT primary key, title varchar(200), created_at datetime, completed_at datetime, status varchar(200))'

        cursors = self.con.cursor()
        cursors.execute(query)
        print("table is created")

    def insert(self, titles): 

        #to check if the same task already exists

        # check_qu = "SELECT title FROM names"
        # taskExistQuery = 
        #insert a new task
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        query = "insert into names(title,created_at) values('{}', '{}')".format(titles, formatted_date) 
        cur = self.con.cursor() 
        cur.execute(query)
        self.con.commit()
        print("entry has been successfully done")



     #FETCH DATA FROM TABLE
    def fetchItems(self):
        query = "SELECT * from names"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("id:", row[0])
            print("title:", row[1])
            print("created_at:", row[2])
            print("completed_at:", row[3])
            print("status:", row[4])

     #update/edit the record
    def update(self, id, newName, newStatus):
        query = "UPDATE names set title='{}' , status='{}' where id={}".format(newName, newStatus, id)
        cur = self.con.cursor() 
        cur.execute(query)
        self.con.commit()
        print("updated")

    # mark as complete
    def complete(self, id):
        query = "UPDATE names set status = 'complete' where id = {}".format(id)  
        cur = self.con.cursor() 
        cur.execute(query)
        self.con.commit()  
        print("task is marked as complete")

    #delete a record
    def delete(self,id):
        query = "DELETE FROM names where id = {}".format(id)
        cur = self.con.cursor() 
        cur.execute(query)
        self.con.commit() 
        print("the selected task is deleted")


    def search(self,title):
        query = "SELECT * from names where title = '{}'".format(title)
        cur = self.con.cursor() 
        cur.execute(query)
        for row in cur:
            print("id:", row[0])
            print("title:", row[1])
            print("created_at:", row[2])
            print("completed_at:", row[3])
            print("status:", row[4])



    # def main():
    #     parser = argparse.ArgumentParser(description="TODO List Manager")
    #     parser.add_argument('--create', help="Create a new task with title")
    #     parser.add_argument('--edit', nargs=3, help="Edit task title. Provide task ID and new title")
    #     parser.add_argument('--delete', help="Delete a task. Provide task ID")
    #     parser.add_argument('--list', choices=['all', 'incomplete', 'complete'], help="List tasks")
    #     parser.add_argument('--search', help="Search tasks by title")

        






