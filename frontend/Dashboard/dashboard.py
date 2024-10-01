import sys
import os
import tkinter as tk
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../","backend")))
from backend import getActions,deleteAction,populateActions


 
def Dashboard(root):
    frame= tk.LabelFrame(root,text="actions")

    
    header = tk.Label(text="Dashbord" ,font="Mono, 16", padx="4", pady="4", justify="center")
    
    header.grid()
    
    actionsFrame = tk.LabelFrame(root,text="Actions",font="Mono, 16",padx="9",pady="9", )
    
    actionsFrame.grid(row="1",column="0", padx="4")
    
    actions = getActions()

    for action in actions:
        
        for index,(id,name) in enumerate(action):
            actionFrame=tk.Frame(actionsFrame,padx="4", pady="4", border="2" ,relief="solid")
            if index<3:
                actionFrame.grid(row="0",column=index,padx="8", pady="8")
            elif index<6:
                actionFrame.grid(row="2",column=index-3,padx="8",pady="8")
            else:
                actionFrame.grid(row="1",column=index-6,padx="8",pady="8") 
            actionHeader = tk.Label(actionFrame,text=name,padx="4",pady="4", font="Mono,8,bold",justify="center")
            actionHeader.grid(row="0",column="1")           
            execute =tk.Button(actionFrame,text="Execute", bg="green", font="Mono,7",fg="white")
            execute.grid(row="1", column=0,padx="1")  
            delete =tk.Button(actionFrame,text="delete", bg="red", font="Mono,7",fg="white",command=deleteAction(id) )
            delete.grid(row="1", column="1",padx="1")  
            Update =tk.Button(actionFrame,text="Update", bg="black", font="Mono,7",fg="white" )
            Update.grid(row="1", column="2",padx="1")  
        

