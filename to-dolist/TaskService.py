from Task import Task
import os

class TaskService:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        with open("taskdata.txt","a") as f:
                f.write(task.description+"\n");
                self.tasks.append(task);
                return self.tasks

    def get_all_task(self):
        self.tasks=[];
        with open("taskdata.txt","r") as f:
            for line in f:
                if line.strip():
                    self.tasks.append(Task(line.strip()));
            
        return self.tasks

    def update_task(self,number,new_value):
        self.tasks = [];
        with open("taskdata.txt","r") as f:
            for line in f:
                if line.strip():
                     self.tasks.append(Task(line.strip()));

        os.remove("taskdata.txt");
        self.tasks[number].description = new_value;
        with open("taskdata.txt","a") as f:
            for x in self.tasks:
                f.write(x.description+"\n");
            
        return self.tasks;
            

    def delete_task(self,number):
        self.tasks = [];
        with open("taskdata.txt","r") as f:
            for line in f:
                if line.strip():
                    self.tasks.append(Task(line.strip()));
        self.tasks.pop(number);
        os.remove("taskdata.txt");
        with open("taskdata.txt","a") as f:
             for x in self.tasks:
                 f.write(x.description+"\n");
        return self.tasks;

        
    
        
               
			



