import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="#subujikamysql",  
    database="sms"
)

print("System login successfully!")


def add():
    
    
    cursor = conn.cursor()

    sql = "INSERT INTO students (Roll_no,Name,Mobile,City,Course) VALUES (%s,%s,%s,%s, %s)"
    val = (int(input("ENTER ROLL NO : ")),input("ENTER NAME : "),int(input("ENTER MOBILE NO : ")),input("ENTER CITY NAME : "),input("ENTER COURSE NAME : "))
    cursor.execute(sql, val)
    conn.commit()

    print("DATA INSERTED SUCCESSFULLY ")
    


def view():
    print("\nSTUDENTS DETAILS :==>>\n")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()

    for row in result:
        print(row)
    

def update():
    while True:
        view()
        print("\n====================================================================")
        print("||   OPTION FOR UPDATION :===>                                    ||")
        print("====================================================================")
        print("||   1. NAME                                                      ||\n||   2. MOBILE                                                    ||\n||   3. CITY                                                      ||\n||   4. COURSE                                                    ||\n||   5. EXIT                                                      ||")
        print("====================================================================")
        print()
        choice = int(input("ENTER CHOICE FOR UPDATION : "))
        if choice == 1 : 
            cursor = conn.cursor()
            
            Name = input("ENTER NEW NAME : ")
            Roll_no = int(input("ENTER  STUDENT ROLL NO : "))

            sql = "UPDATE students SET Name = %s WHERE Roll_no = %s"
            cursor.execute(sql, (Name , Roll_no))

            conn.commit()

            print("Student name updated successfully!")
            

        elif choice == 2 :
            cursor = conn.cursor()
                    
            Mobile = input("ENTER NEW MOBILE NO : ")
            Roll_no = int(input("ENTER ROLL NO : "))

            sql = "UPDATE students SET Mobile = %s WHERE Roll_no = %s"
            cursor.execute(sql, (Mobile, Roll_no))

            conn.commit()

            print("Student mobile no updated successfully!")
            
        
        elif choice == 3 :
            cursor = conn.cursor()
                    
            City = input("ENTER NEW CITY NAME : ")
            Roll_no = int(input("ENTER ROLL NO : "))
            
            sql = "UPDATE students SET City = %s WHERE Roll_no = %s"
            cursor.execute(sql, (City, Roll_no))
            
            conn.commit()
            
            print("Student city updated successfully!")
            

        elif choice == 4 :
            cursor = conn.cursor()
                            
            Course = input("ENTER NEW COURSE NAME : ")
            Roll_no = int(input("ENTER ROLL NO : "))
            
            sql = "UPDATE students SET Course = %s WHERE Roll_no = %s"
            cursor.execute(sql, (Course, Roll_no))
            
            conn.commit()
            
            
            print("Student course updated successfully!")
        elif choice == 5 :
            print("EXITED FROM UPDATION\nCHANGES SAVED SUCCESSFULLY\n")
            break

        else :
            print(" INVALID CHOICE \n CHOOSE AGAIN")
        

def delete():
    view()
    cursor = conn.cursor()
    Roll_no = int(input("\n[TO DELETE STUDENT DATA]\nENTER ROLL NO : "))

    sql = "DELETE FROM students WHERE Roll_no = %s"

    cursor.execute(sql,(Roll_no,))
    conn.commit()
    print(f"\nROLL NO {Roll_no} STUDENT DATA DELETE SUCCESSFULLY !!\n")

while True:
    
    print ("\n====================================================================\n||                  STUDENT MANAGEMENT SYSTEM                     ||\n====================================================================")
    print("||   1. ADD NEW STUDENTS                                          ||\n||   2. VIEW ALL STUDENTS                                         ||\n||   3. UPDATE STUDENTS DATA                                      ||\n||   4. DELETE STUDENT RECORD                                     ||\n||   5. EXIT                                                      ||")
    print("====================================================================\n")

    choice = int(input("[FROM ABOVE MENU] \nENTER YOUR CHOICE : "))
    print()

    if choice == 1 : 
        add()
    elif choice == 2 : 
        view()
    elif choice == 3 :
        update()
    elif choice == 4 : 
        delete()
    elif choice == 5 :
        print("\nSTUDENT MANAGEMENT SYSTEM IS EXITED !!\n")
        break
    else :
        print(f"NO {choice} OPTION AVALIABLE\nCHOOSE ONLY FROM GIVEN MENU !!\n")

