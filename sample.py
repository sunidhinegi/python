import argparse
import csv
import os
import re
from datetime import datetime
import pandas as pd

class Exercise:
     

    def readTasks(self):
        tasks = []
        if not os.path.exists('file.csv'):
            with open('file.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['id', 'title', 'created at', 'completed at', 'status'])
                writer.writerows(tasks)

        else:
            with open('file.csv', 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    tasks.append(row)
        return tasks

# write tasks to the CSV file

    def writeTasks(self,tasks):
        with open('file.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(tasks)

# create

    def createTask(self,title):
        obj = Exercise()
        tasks = obj.readTasks()
        for task in tasks:
            if task[1] == title:
                print("Please try entering a task with the different title")
                return
        task_id = len(tasks) + 1
        created_at = str(datetime.now())
        completed_at = str(datetime.now())

        tasks.append([task_id, title, created_at, completed_at , 'incomplete'])

        obj.writeTasks(tasks)
        print("Task is created successfully.")

# edit 

    def editTitle(self,task_id, new_heading, status = None):
        obj2 = Exercise()
        tasks = obj2.readTasks()
        for task in tasks:
            if task[0] == task_id:
                task[1] = new_heading
                task[4] = "complete"
                obj2.writeTasks(tasks)                                                                                           
            print("Task title updated successfully.")
            return

# delete

    def deleteTask(self,id):
        obj6 = Exercise()
        tasks = obj6.readTasks()
        newTask = []
        # newObj = Exercise()
        # tasks = newObj.readTasks()
        # for task in tasks:
        #     if task[1] == title:
        #         task[0].drop()
        # df = pd.read_csv('file.csv')
        # df = df.drop(df[df.title == titles])
        # df.to_csv('example_3.csv', index=False)
        for task in tasks:
            if task[0] != id:
                newTask.append(id)
        obj6.writeTasks(newTask)  
        print("deleted")      


# list tasks
    def listTasks(self,status):
        obj3 = Exercise()
        tasks = obj3.readTasks()
        for task in tasks:
            if status == task[4]:
                print(f"id: {task[0]}, title: {task[1]}, status: {task[4]}")
        # elif((status != 'complete') or (status != 'incomplete')):
        #     print(f"ID: {task[0]}, Title: {task[1]}, Status: {task[4]}")
            if status == "all":
                print(f"ID: {task[0]}, Title: {task[1]}, Status: {task[4]}")


    def searchTask(self,title):
        obj4 = Exercise()
        tasks = obj4.readTasks()
        for task in tasks:
            search = re.search(title, task[1]) 
            if search:
                if title == task[1]:                  
                    print(f"ID: {task[0]}, Title: {task[1]}, Status: {task[4]}")

def main():
    obj5 = Exercise()
    obj5.readTasks() #for when the program is run for the first time, the file is created

    parser = argparse.ArgumentParser(description="TODO List Manager")
    parser.add_argument('--create', help="Create a new task with title")
    parser.add_argument('--edit', nargs=3, help="Edit task title. Provide task ID and new title")
    parser.add_argument('--delete', help="Delete a task. Provide title")
    parser.add_argument('--list', choices=['all', 'incomplete', 'complete'], help="List tasks")
    parser.add_argument('--search', help="Search tasks by title")
    args = parser.parse_args()

    if args.create:
        obj5.createTask(args.create)
    elif args.edit:
        task_id, new_heading, status = args.edit
        
        obj5.editTitle(task_id, new_heading , status)
    elif args.delete:
        obj5.deleteTask(args.delete)
    elif args.list:
        obj5.listTasks(args.list)
    elif args.search:
        obj5.searchTask(args.search)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
