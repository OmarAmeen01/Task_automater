
import sqlite3
import math
import random
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..","db")))

def populateActions (name):
    id =math.floor(random.random()*1000*9)
    con = sqlite3.connect("db/TaskAutomater.db")
    c = con.cursor()
  
    c.execute("""
                  INSERT INTO Actions (id, name)
                         VALUES (:id, :name)
                    """,
                    {
                         "id": id,
                         "name": name,
                               })

    con.commit()
    con.close()

def populateSubActions (name,path, action_id):
    id =math.floor(random.random()*1000*9)
    con = sqlite3.connect("db/TaskAutomater.db")
    c = con.cursor()
  
    query =c.execute("""
     INSERT INTO Sub_actions (name,id,path,action_id) VALUES(:name ,:id,:path,:action_id)
     
     """,{
        "id":id,
        "name":name,
        "path":path,
        "action_id":action_id,
    })


    con.commit()
    con.close()



def getActions ():
    con = sqlite3.connect("db/TaskAutomater.db")
    c = con.cursor()
  
    c.execute("""
    SELECT * FROM Actions 
    """
    )
    actions = c.fetchall()
    con.commit()
    con.close()
    return actions,

def getSubActions(id):
    con = sqlite3.connect("db/TaskAutomater.db")
    c = con.cursor()
  
    c.execute("""
    SELECT * FROM  Sub_actions WHERE action_id:id
    """,{
        "id":id
    }
    )
    actions = c.fetchall()
    con.commit()
    con.close()
    return actions,

def deleteAction(id):
    con = sqlite3.connect("db/TaskAutomater.db")
    c = con.cursor()
    c.execute("""
              DELETE FROM Actions WHERE id=:id
              """,{
                  "id":id
              })
    con.commit()
    con.close()

def deleteSubAction(id):
    con = sqlite3.connect("db/TaskAutomater.db")
    c = con.cursor()
     
    c.execute("""
               DELETE FROM Sub_actions WHERE id=:id
               """,{
                   "id":id
               })
    
    con.commit()
    con.close()
 



