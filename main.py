from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    
    work:str
    status:bool= False 


tasks = []
id = 1
@app.get("/")
def hello():
     return {"HEll" :"Yes"}

@app.get("/hello")
def read():
    return tasks

@app.post("/add_tasks")

def add_task(task: Task ):
    global id 
    new_task = {
        "id": id,
         "work": task.work,
         "status": task.status 



    }
    tasks.append(new_task)
    id +=1


    return new_task


@app.put("/tasks/{task_id}")
def update_status(task_id:int ):
      for element in tasks:
           if element["id"] == task_id:
                element["status"] = True 
                return element
      return {"message": "Element not found"}

@app.delete("/tasks/del/{task_id}")
def del_task (task_id:int):
     for element in tasks:
          if element["id"] == task_id:
               tasks.remove(element)
               return{"Message":"Deleted Successfully"}
     return {"message": "No such task found"}    

            
            

    



    
   


