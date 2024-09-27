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
              FOREIGN KEY (action_id) REFERENCES Actions (id)

              )
              """)
    con.commit()
    con.close()

def populateActions (name):
    id =math.floor(random.random()*87)
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
    id =math.floor(random.random()*87)
    con = sqlite3.connect("TaskAutomater.db")
    c = con.cursor()
  
    query =c.execute("""
     INSET INTO Sub_actions(name,id,path,action_id) VALUES(:name ,:id,:path,:action_id)
     
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
    SELECT *,oid FROM Actions 
    """
    )
    actions = c.fetchall()
    con.commit()
    con.close()
    return actions,

populateActions("meduim commoda")
print(getActions())
