print("========================================")
print(".....Welcome to the Student Manager.....")
print("========================================")

students=[]
while True:
    print("\nChoose the option form bellow: ")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display All Student")
    print("5. Sort Student")
    print("6. total Student")
    print("7. Exit")
    inp = input("Choose from 1-7: ")
    if inp == '1':
        again = 'y'
        while again == 'y':
            std = input("\nEnter the name of Student you want to add: ").capitalize()
            students.append(std)
            print(std, " has been added to the student list :)\n")
            again = input("Do you want to add another student (y/n): ")
            if again != 'y':
                break
    elif inp == '2':
        while True:
            name = input("\nEnter the name of the student you want to delete: ").capitalize()
            a= students.count(name)
            if a > 0:
                cnf = input("\nAre you sure? (y/n): ")
                if cnf =='y':
                    students.remove(name)
                    print(name, " was removed from the student list.")
            else:
                print(name, " was not found in the student list...")
            cont = input("Do you want to remove another Student (y/n): ")
            if cont != 'y':
                break
    elif inp == '3':
        while True:
            name = input("\nEnter the name of the student you want to find: ").capitalize()
            if students.count(name)> 0 :
                print(name, " was found in the list on index:   ", students.index(name))
            else:
                print(name, " was not found in the list :(")
            ch = input("\nDo you want to find an other student (y/n): ")
            if ch != 'y':
                break
    elif inp == '4':
        a=len(students)
        while True:
            print("Here is the entire list of students: \n")
            for std in students:
                print("         ",students.index(std)+1,".", std)
            a = input("Do you want to display all the students again? (y/n): ")
            if a != 'y':
                break
    elif inp == '5':
        while True: 
            print("\n1. Sort in ascending order")
            print("2. Reverse the list")
            a = input("Choose the sort:")
            if a == '2':
                students.reverse()
                print("\nThe reversed list is bellow: ")
                for std in students:
                    print("          ",students.index(std)+1,".", std)
            elif a == '1':
                print("\nThe sorted student list A-Z is bellow:")
                students.sort()
                for std in students:
                    print("         ",students.index(std)+1,".", std)
            b = input("Do you want to sort again? (y/n): ")
            if b != 'y':
                break
    elif inp == '6':
        while True:
            a = len(students)
            print("\nTotal number of students are: ", a)
            c = input("\nDo you want to check the student count again? (y/n): ")
            if c != 'y':
                break
    elif inp == '7':
        print("\n Good bye ...💗...\n")
        break
    else:
        print("\nInvalid input, choose from 1-7")
        