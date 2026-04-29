import mysql.connector

#print but in red
def panic(text):
    print(f"\033[1;31m {text} \033[0m")

#banned characters to avoid sql injection
NONOS = [';', '(', ')', '"']

#check if a string has any NONO characters
def check_query(query):
    for char in NONOS:
        if char in query:
            return char
    return None

#connect to the database
def connect():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1",
            database="final"
        )
        if connection.is_connected():
            return connection
        else:
            panic("failed to connect")
    except mysql.connector.Error as e:
        panic(str(e))

#add data to the database
def add(connection):
    #try get a cursor on the database
    try:
        cursor = connection.cursor()
    except mysql.connector.Error as e:
        panic(str(e))

    
    while True:
        #get what table the user wants to add to
        inp = input("\nWhat table would you like to add to:\n>(F)ungi\n>(L)ocations\n>(M)ycotoxins\n(F)ungi (L)ocations\n>(P)resent Toxins\n>(Lo)okalikes\n>>:")
        match inp.strip().lower():
            case "f" | "fungi":
                while True:
                    #get the data and check for sql injection
                    name = input("Name: ")
                    nv = check_query(name)
                    if nv != None:
                        panic(f"inputs may not contain {nv}")
                        continue
                    desc = input("Description: ")
                    dv = check_query(desc)
                    if dv != None:
                        panic(f"inputs may not contain {dv}")
                        continue

                    #run the query and push to the database
                    try:
                        cursor.execute("INSERT INTO fungi (name, description) VALUES (%s, %s)", (name, desc))
                        connection.commit()
                        break
                    except mysql.connector.Error as e:
                        panic(str(e))
                break 
            case "l" | "locations":
                while True:
                    region = input("Region: ")
                    rv = check_query(region)
                    if rv != None:
                        panic(f"inputs may not contain {rv}")
                        continue
                    desc = input("Description: ")
                    dv = check_query(desc)
                    if dv != None:
                        panic(f"inputs may not contain {dv}")
                        continue
                    try:
                        cursor.execute("INSERT INTO locations (region, description) VALUES (%s, %s)", (region, desc))
                        connection.commit()
                        break
                    except mysql.connector.Error as e:
                        panic(str(e))
                break
            case "m" | "mycotoxins":
                while True:
                    name = input("Name: ")
                    nv = check_query(name)
                    if nv != None:
                        panic(f"inputs may not contain {nv}")
                        continue
                    effects = input("Effects: ")
                    ev = check_query(effects)
                    if ev != None:
                        panic(f"inputs may not contain {ev}")
                        continue
                    try:
                        cursor.execute("INSERT INTO mycotoxins (name, effects) VALUES (%s, %s)", (name, effects))
                        connection.commit()
                        break
                    except mysql.connector.Error as e:
                        panic(str(e))
                break

            case "fl" | "fungi locations":
                print("add to fungi locations")
                break
            case "p" | "present toxins":
                print("add to present toxins")
                break
            case "lo" | "lookalikes":
                print("add to lookalikes")
                break
            case _:
                panic("unknown table")

def main():
    #add data to any table
    #remove data from any table
    #query any data
    connection = connect()
    
    while True:
        inp = input("What would you like to do?:\n>(A)dd data\n>(R)emove data\n>(S)earch database\n>(Q)uit\n>>: ")
        match inp.strip().lower():
            case "a" | "add":
                add(connection)
            case "r" | "remove":
                print("rm")
            case "s" | "search":
                print("search")
            case "q" | "quit":
                return None
            case _:
                panic("Unrecognized input")

if __name__ == "__main__":
    main()
