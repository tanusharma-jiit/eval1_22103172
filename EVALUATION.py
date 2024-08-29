def mark_present(student_name , name):
    print(" name before appending : ")
    for name in student_name :
        print(name)
        print(" ")
    print("\n")
    student_name.append(name)     
    print(" name after appending : ")
    for name in student_name :
        print(name)
        print(" ")
    print("\n")
def remove_student(student_name , name):  
    print("\n name before removing : ")
    for name in student_name :
        print(name)
        print(" ")
       
    student_name.remove(name)     
    print("\n name after removing : ")
    for name in student_name :
        print(name)
        print(" ")
    
def is_present(student_name , name):
    if name in student_name :
        print("student is present")
    else :
         print("student is not  present")
    print("\n")
def display_attendance(student_name):
    for name in student_name :
        print(name)
        print(" ")
    print("\n")
        
dic={1 : ['riya'] , 2 :['leena'] , 3: ['neena'] , 4: [] , 5 : [] , 6 : [] , 7 :[]}

day = input("enter day : ")

student_name=['riya']
name1= input("enter name for adding in list")
mark_present(student_name , name1)
name2= input("enter name for removing from list")
remove_student(student_name , name2)
name3= input("enter name for chekcing from list")
is_present(student_name , name3)
display_attendance(student_name)
