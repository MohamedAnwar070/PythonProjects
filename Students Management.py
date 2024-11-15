students={}

def add_student():
    print("#####ADD NEW STUDENT#####")
    print("##GIVE REQUIRED DETAILS##")
    stu_name=input("Enter Student Name : ")
    stu_id=int(input("Enter Student ID : "))
    stu_gp=float(input("Enter Student GPA : "))
    students[stu_id]={'Name':stu_name,'GPA':stu_gp}
    print(f"Name : {stu_name} Student Added Succesfully, His/Her ID Is {stu_id}")

def remove_student():
    print("######REMOVE STUDENT######")
    print("##GIVE REQUIRED DETAILS##")
    stu_id=int(input("Enter Student ID To Remove : "))
    if stu_id in students:
        del students[stu_id]
        print(f"{stu_id} Student Removed Succesfully")
    else:
        print("Student not Found")
        
def update_student():
    print("#####UPDATE STUDENT INFO#####")
    print("###GIVE REQUIRED DETAILS###")
    stu_id = int(input("Enter Student ID To Change That Student's Details: "))
    if stu_id in students:
        new_stu_name = input("Enter NEW Student Name: ")
        new_stu_gp = float(input("Enter NEW Student GPA: "))
        students[stu_id] = {'Name': new_stu_name, 'GPA': new_stu_gp}
        print(f"Name: {new_stu_name} & GPA {new_stu_gp} has been updated successfully, and their ID is {stu_id}.")
    else:
        print("Student ID not found.")
        
def display_students_details():
    print("#####STUDENT DEATAILS#####")
    print("##GIVE REQUIRED DETAILS##")
    stu_id=int(input("Enter Student ID To Check Details : "))
    if  stu_id in students:
        print(students)
    else:
        print("Student ID Not Found!")
      
def search_student():
    print("#####SEARCH STUDENT IN DB#####")
    print("####GIVE REQUIRED DETAILS####")
    stu_name=input("Enter Student Name To Search : ")
    for stu_id ,details in students.items():
        if details['Name'].lower()==stu_name.lower():
            print(f"Student Found In Records :\nStudent Name : {details['Name']}\nStudent ID : {stu_id}\nStudent GPA : {details['GPA']}")
        else:
            print("Student Not In Records")
def main():
    while True:
        x='#'
        y="MASOOD THAIKA HR.SEC SCHOOL"
        z="STUDENT PORTAL"
        print(x.center(30,'#'))
        print(y.center(30,'-'))
        print(z.center(30,'-'))
        print(x.center(30,'#'))
        
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Update Student")
        print("4. Display Student Details")
        print("5. Search Student")
        print("6. Exit")

        choice=int(input("Enter Your Choice : "))

        if choice==1:
            add_student()
        elif choice==2:
            remove_student()
        elif choice==3:
            update_student()
        elif choice==4:
            display_students_details()
        elif choice==5:
            search_student()
        elif choice==6:
            print("######THANK YOU#####")
            print("##Exiting Records##")
            break 
        else:
            print("Entered Wrong Number Select Between 1 to 5")
main()

#Coded By ANWAR
