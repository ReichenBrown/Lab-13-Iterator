#Authors: Reichen Brown & Youssab Girgis
#Date: 09/26/2023
#Description: Maintains a task list for the user.

import check_input
from task import Task
from tasklist import Tasklist

def main_menu():
  print("-Tasklist-")
  print("1. Display current task")
  print("2. Display all tasks")
  print("3 Mark current task complete")
  print("4. Add new task")
  print("5. Search by date")
  print("6. Save and quit")
  input = check_input.get_int_range("Enter choice: ", 1, 6)
  return input

def get_date():
  year = check_input.get_int_range("Enter year: ", 2000, 2100)
  month = check_input.get_int_range("Enter month: ", 1, 12)
  day = check_input.get_int_range("Enter day: ", 1, 31)
  if month < 10:
    month = "0"+str(month)
  if day < 10:
    day = "0"+str(day)
  
  return str(month) + "/" + str(day) + "/" + str(year)

def get_time():
  hour = check_input.get_int_range("Enter hour: ", 0, 23)
  min = check_input.get_int_range("Enter minute: ", 0, 59)
  if hour < 10:
    hour = "0" + str(hour)
  if min < 10:
    min = "0" + str(min)

  return str(hour) + ":" + str(min)

def main():
  tasklist = Tasklist()
  repeat = True
  while repeat:
    print("Tasks to complete: " + str(len(tasklist)))
    choice = main_menu()
    
    if choice == 1:
      if tasklist:
        print(f"Current task is: {tasklist.get_current_task()}")
      else:
        print("All Tasks are Complete!")
    
    elif choice == 2:
      if tasklist:
        for task in tasklist:
          print(task)
      else:
        print("All Tasks are Complete!")
    
    elif choice == 3:
      if tasklist:
        print("Marking current task as complete:")
        print(tasklist.get_current_task())
        tasklist.mark_complete()
        if tasklist:
          print(f"Current task is: {tasklist.get_current_task()}")
        else:
          print("All Tasks are Complete!")
      else:
        print("No tasks to mark!")

    elif choice == 4:
      desc = str(input("Enter a task: "))
      print("Enter a due date:")
      date = get_date()
      time = get_time()
      tasklist.add_task(desc, date, time)

    elif choice == 5:
      print("Enter date to search:")
      month = check_input.get_int_range("Enter month: ", 1, 12)
      day = check_input.get_int_range("Enter day: ", 1, 31)
      year = check_input.get_int("Enter year: ")
      date = f"{month}/{day}/{year}"
      count = 1
      print(f"Tasks due on {date}:")
      for task in tasklist:
        if date == task.date:
          print(f"{count}: {task}")
          count += 1
    else:
      repeat = False
      print("Saving List...")
      tasklist.save_file()

    print()

main()