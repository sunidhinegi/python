import argparse
# import sys
import csv
import os
import re
from datetime import datetime
# import pandas as pd

# read tasks from the CSV file

def readTasks():
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

def writeTasks(tasks):
    with open('file.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(tasks)

# create

def createTask(title):
    tasks = readTasks()
    for task in tasks:
        if task[1] == title:
            print("Please try entering a task with the different title")
            return
    task_id = len(tasks) + 1
    created_at = str(datetime.now())
    completed_at = str(datetime.now())

    tasks.append([task_id, title, created_at, completed_at , 'incomplete'])

    writeTasks(tasks)
    print("Task is created successfully.")

# edit 

def editTitle(task_id, new_heading, status = None):
    tasks = readTasks()
    for task in tasks:
        if task[0] == task_id:
            task[1] = new_heading
            task[4] = "complete"
            writeTasks(tasks)                                                                                           
            print("Task title updated successfully.")
            return

# delete

# def deleteTask(task_id):
#     tasks = readTasks()
#     for task in tasks:
#         if task[0] == task_id:
#             task[0].drop()


# list tasks
def listTasks(status):
    tasks = readTasks()
    for task in tasks:
        if status == task[4]:
            print(f"id: {task[0]}, title: {task[1]}, status: {task[4]}")
        # elif((status != 'complete') or (status != 'incomplete')):
        #     print(f"ID: {task[0]}, Title: {task[1]}, Status: {task[4]}")
        if status == "all":
            print(f"ID: {task[0]}, Title: {task[1]}, Status: {task[4]}")


def searchTask(title):
    tasks = readTasks()
    for task in tasks:
        search = re.search(title, task[1]) 
        if search:
            if title == task[1]:                  
                print(f"ID: {task[0]}, Title: {task[1]}, Status: {task[4]}")

def main():
    readTasks() #for when the program is run for the first time, the file is created

    parser = argparse.ArgumentParser(description="TODO List Manager")
    parser.add_argument('--create', help="Create a new task with title")
    parser.add_argument('--edit', nargs=3, help="Edit task title. Provide task ID and new title")
    parser.add_argument('--delete', help="Delete a task. Provide task ID")
    parser.add_argument('--list', choices=['all', 'incomplete', 'complete'], help="List tasks")
    parser.add_argument('--search', help="Search tasks by title")
    args = parser.parse_args()

    if args.create:
        createTask(args.create)
    elif args.edit:
        task_id, new_heading, status = args.edit
        
        editTitle(task_id, new_heading , status)
    
    # elif args.delete:
    #     deleteTask(args.delete)
    elif args.list:
        listTasks(args.list)
    elif args.search:
        searchTask(args.search)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

