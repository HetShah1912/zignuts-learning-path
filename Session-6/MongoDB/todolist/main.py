from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

db = client.todo_db
task_collection = db.task

# insert function
def createTask(description):
  task = {
    'task' : description
  }
  result = task_collection.insert_one(task)
  print(f"Task Created With Id : {result.inserted_id}")

# read 
def readTask():
  tasks = task_collection.find()
  for doc in tasks:
    print(f"{doc['task']}")


while True:
  print("1. Create Task")
  print("2. View Task")
  print("3. Exit")

  choice = input("Enter Your Choice : ")

  if choice=='1':
    description = input("Enter your Task : ")
    createTask(description)
  elif choice=='2':
    readTask()
  elif choice=='3':
    break
  else:
    print("Provide a Valid Option")