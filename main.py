import mysql.connector
from tabulate import tabulate 

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
            return None
    except mysql.connector.Error as e:
        panic(str(e))
        return None

#add data to the database
def add(connection):
    #try get a cursor on the database
    try:
        cursor = connection.cursor()
    except mysql.connector.Error as e:
        panic(str(e))

    
    while True:
        #get what table the user wants to add to
        inp = input("\nWhat table would you like to add to:\n>(F)ungi\n>(L)ocations\n>(M)ycotoxins\n>(F)ungi (L)ocations\n>(P)resent Toxins\n>(Lo)okalikes\n>>:")
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
                while True:
                    fungus_id = input("Fungus_ID: ")
                    fv = check_query(fungus_id)
                    if fv != None:
                        panic(f"inputs may not contain {fv}")
                        continue
                    location_id = input("Location_ID: ")
                    lv = check_query(location_id)
                    if lv != None:
                        panic(f"inputs may not contain {lv}")
                        continue
                    try:
                        cursor.execute("INSERT INTO fungus_locations (fungus_id, location_id) VALUES (%s, %s)", (fungus_id, location_id)) 
                        connection.commit()
                        break
                    except mysql.connector.Error as e:
                        panic(str(e))
                break
            case "p" | "present toxins":
                while True:
                    fungus_id = input("Fungus_ID: ")
                    fv = check_query(fungus_id)
                    if fv != None:
                        panic(f"inputs may not contain {fv}")
                        continue
                    mycotoxin_id = input("Mycotoxin_ID: ")
                    mv = check_query(mycotoxin_id)
                    if mv != None:
                        panic(f"inputs may not contain {mv}")
                        continue
                    try:
                        cursor.execute("INSERT INTO present_toxins (fungus_id, mycotoxin_id) VALUES (%s, %s)", (fungus_id, mycotoxin_id))
                        connection.commit()
                        break
                    except mysql.connector.Error as e:
                        panic(str(e))
                break
            case "lo" | "lookalikes":
                while True:
                    fungus1_id = input("Fungus1_ID: ")
                    f1v = check_query(fungus1_id)
                    if f1v != None:
                        panic(f"inputs may not contain {f1v}")
                        continue
                    fungus2_id = input("Fungus2_ID: ")
                    f2v = check_query(fungus2_id)
                    if f2v != None:
                        panic(f"inputs may not contain {f2v}")
                        continue
                    try:
                        cursor.execute("INSERT INTO lookalikes (fungus1_id, fungus2_id) VALUES (%s, %s)", (fungus1_id, fungus2_id))
                        connection.commit()
                        break
                    except mysql.connector.Error as e:
                        panic(str(e))
                break

            case _:
                panic("unknown table")

def remove(connection):
    try:
        cursor = connection.cursor()
    except mysql.connector.Error as e:
        panic(str(e))
    while True:
        inp = input("\nWhat table would you like to remove data from:\n>(F)ungi\n>(L)ocations\n>(M)ycotoxins\n>(F)ungi (L)ocations\n>(P)resent Toxins\n>(Lo)okalikes\n>>:")
        match inp.strip().lower():
            case "f" | "fungi":
                inp = input("\nWhat fungus id do you want to remove: ")
                try:
                    cursor.execute("DELETE FROM fungi WHERE id = %s", (inp,))
                    connection.commit()
                    break
                except mysql.connector.Error as e:
                    panic(str(e))
            case "l" | "locations":
                inp = input("\nWhat location id do you want to remove: ")
                try:
                    cursor.execute("DELETE FROM locations WHERE id = %s", (inp,))
                    connection.commit()
                    break
                except mysql.connector.Error as e:
                    panic(str(e))
            case "m" | "mycotoxins":
                inp = input("\nWhat mycotoxin id do you want to remove: ")
                try:
                    cursor.execute("DELETE FROM mycotoxins WHERE id = %s", (inp,))
                    connection.commit()
                    break
                except mysql.connector.Error as e:
                    panic(str(e))
            case "fl" | "fungi locations":
                inp = input("\nWhat fungus location id do you want to remove: ")
                try:
                    cursor.execute("DELETE FROM fungus_locations WHERE id = %s", (inp,))
                    connection.commit()
                    break
                except mysql.connector.Error as e:
                    panic(str(e))
            case "p" | "present toxins":
                inp = input("\nWhat present toxin id do you want to remove: ")
                try:
                    cursor.execute("DELETE FROM present_toxins WHERE id = %s", (inp,))
                    connection.commit()
                    break
                except mysql.connector.Error as e:
                    panic(str(e))
            case "lo" | "lookalikes":
                inp = input("\nWhat lookalike id do you want to remove: ")
                try:
                    cursor.execute("DELETE FROM lookalikes WHERE id = %s", (inp,))
                    connection.commit()
                    break
                except mysql.connector.Error as e:
                    panic(str(e))
            case _:
                panic("Unknown table")
    
def search(connection):
    try:
        cursor = connection.cursor()
    except mysql.connector.Error as e:
        panic(str(e))
    
    while True:
        inp = input("What table would you like to search:\n>(F)ungi\n>(L)ocations\n>(M)ycotoxins\n>(F)ungi (L)ocations\n>(P)resent Toxins\n>(Lo)okalikes\n>>:")
        table = ""
        column = ""
        match inp.strip().lower():
            case "f" | "fungi":
                table = "fungi"
                inp = input("what column are you searching:\n>(ID)\n>(N)ame\n>(D)escription\n>>")
                match inp.strip().lower():
                    case "id":
                        column = "id"
                    case "n" | "name":
                        column = "name"
                    case "d" | "description":
                        column = "description"
                    case _:
                        panic("unknown column")
                        continue
                break
                        
            case "l" | "locations":
                table = "locations"
                inp = input("what column are you searching:\n>(ID)\n>(R)egion\n>(D)escription\\n>>")
                match inp.strip().lower():
                    case "id":
                        column = "id"
                    case "r" | "region":
                        column = "region"
                    case "d" | "description":
                        column = "description"
                    case _:
                        panic("unknown column")
                        continue
                break

            case "m" | "mycotoxins":
                table = "mycotoxins"
                inp = input("what column are you searching:\n>(ID)\n>(N)ame\n>(E)ffects\\n>>")
                match inp.strip().lower():
                    case "id":
                        column = "id"
                    case "n" | "name":
                        column = "name"
                    case "e" | "effects":
                        column = "effects"
                    case _:
                        panic("unknown column")
                        continue
                break

            case "fl" | "fungus locations":
                table = "fungus_locations"
                inp = input("what column are you searching:\n>(ID)\n>(F)ungus ID\n>(L)ocation ID\\n>>")
                match inp.strip().lower():
                    case "id":
                        column = "id"
                    case "f" | "fungus id":
                        column = "fungus_id"
                    case "l" | "location id":
                        column = "location_id"
                    case _:
                        panic("unknown column")
                        continue
                break

            case "p" | "present toxins":
                table = "present_toxins"
                inp = input("what column are you searching:\n>(ID)\n>(F)ungus ID\n>(M)ycotoxin ID\\n>>")
                match inp.strip().lower():
                    case "id":
                        column = "id"
                    case "f" | "fungus id":
                        column = "fungus_id"
                    case "m" | "mycotoxin id":
                        column = "mycotoxin_id"
                    case _:
                        panic("unknown column")
                        continue
                break

            case "lo" | "lookalikes":
                table = "lookalikes"
                inp = input("what column are you searching:\n>(ID)\n>(F)ungus (1) ID\n>(F)ungus (2) ID\\n>>: ")
                match inp.strip().lower():
                    case "id":
                        column = "id"
                    case "f1" | "fungus 1 id":
                        column = "fungus1_id"
                    case "f2" | "fungus 2 id":
                        column = "fungus2_id"
                    case _:
                        panic("unknown column")
                        continue
                break
            case _:
                panic("unknown table")
                continue
    
    while True:
        s = input(f"What should {column} in {table} contain:\n>>")
        sv = check_query(s)
        if sv != None:
            panic(f"query may not contain {sv}")
        
        try:
            cursor.execute(f"SELECT * FROM {table} WHERE {column} LIKE \"%{s}%\"", ())
            break
        except mysql.connector.Error as e:
            panic(str(e))
    values = cursor.fetchall()
    headers = [val[0].upper() for val in cursor.description]
    print(tabulate(values, headers=headers, tablefmt="grid"))
        

def main():
    connection = connect()
    if connection == None:
        panic("ABORTING")
        return None
    while True:
        inp = input("What would you like to do?:\n>(A)dd data\n>(R)emove data\n>(S)earch database\n>(Q)uit\n>>: ")
        match inp.strip().lower():
            case "a" | "add":
                add(connection)
            case "r" | "remove":
                remove(connection)
            case "s" | "search":
                print("search")
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM fungi")
                values = cursor.fetchall()
                headers = [val[0].upper() for val in cursor.description]
                
                print(tabulate(values, headers=headers, tablefmt="grid"))

                search(connection)
            case "q" | "quit":
                return None
            case _:
                panic("Unrecognized input")

if __name__ == "__main__":
    main()
