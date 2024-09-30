import sqlite3
import math;
import random;
def CreateDb():
    con = sqlite3.connect("TaskAutomater.db")
    con.execute("PRAGMA foreign_keys=1")
    c = con.cursor()

    c.execute("""
              CREATE TABLE IF NOT EXISTS Actions(
                id  INTEGER PRIMARY KEY,
               name TEXT  NOT NULL
              )
              """)

    c.execute("""
              CREATE TABLE IF NOT EXISTS Sub_actions(
               id INTEGER PRIMARY KEY,
               name TEXT  NOT NULL,
              path TEXT ,
              action_id INTEGER  ,
              FOREIGN KEY (action_id) REFERENCES Actions (id) ON DELETE CASCADE ON UPDATE CASCADE

              )
              """)
    con.commit()
    con.close()

def populateActions (name):
    id =math.floor(random.random()*1000*9)
    con = sqlite3.connect("TaskAutomater.db")
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

def populateSub_actions (name,path, action_id):
    id =math.floor(random.random()*1000*9)
    con = sqlite3.connect("TaskAutomater.db")
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
    con = sqlite3.connect("TaskAutomater.db")
    c = con.cursor()
  
    c.execute("""
    SELECT * FROM Actions 
    """
    )
    actions = c.fetchall()
    con.commit()
    con.close()
    return actions,

def getAction (id):
    con = sqlite3.connect("TaskAutomater.db")
    c = con.cursor()
  
    c.execute("""
    SELECT * FROM Actions INNER JOIN Sub_actions ON Actions.id=Sub_actions.action_id WHERE Actions.id=:id
    """,{
        "id":id
    }
    )
    actions = c.fetchall()
    con.commit()
    con.close()
    return actions,

def deleteAction(id):
    con = sqlite3.connect("TaskAutomater.db")
    c = con.cursor()
    c.execute("""
              DELETE FROM Actions WHERE id=:id
              """,{
                  "id":id
              })
    con.commit()
    con.close()

def deleteSubAction(id):
    con = sqlite3.connect("TaskAutomater.db")
    c = con.cursor()
     
    c.execute("""
               DELETE FROM Sub_actions WHERE id=:id
               """,{
                   "id":id
               })
    
    con.commit()
    con.close()

CreateDb()

