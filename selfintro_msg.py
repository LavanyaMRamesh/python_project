
while True:
    i = input("Press S to continue and Press any key to exit = ")
    if i == "s" :
        print("1.SELF INTRODUCTION ")
        print("2.UNKNOWN MESSAGE")
        g=input("enter 1 or 2 = ")
        if g == '1':
            name= input("Enter your Name = ")
            place=input("Enter the place you belong to =")
            graduation=input("enter post or under =")
            branch =input("Enter the branch = ")
            clg= input("enter college Name = ")
            hobbies = input("enter your Hobbies =")

            print("SELF INTRODUCTION  OF ",name)
            print("***********************************")
            print("Hi,")
            print("My self ",name,"I am from ",place,".")
            print("I am pursuing my ",graduation,"graduation in ",branch,"from ",clg)
            print("My hobbies are ",hobbies)
            print()
            print("That's all about me!")
            print("Thank you very much for giving a great opportunity to introduce myself behind you.. ")
            print("***********************************************************")



        elif g == '2':
            name = input("Enter your Name =")
            name1 = input("Enter your friends =")
            year = input("Enter No of years together =")
            place = input("Enter the place you met =")


            print("FRIENDSHIP OF ", name, "AND ", name1)
            print("*********************************")
            print()
            print("There lived two  friends named", name, "and", name1)
            print("They met ", year, " years ago in ", place)
            print()
            print("THERE'S A SURPRISE WISH FROM AN UNKNOWN")
            print("HEY YOU---")
            print("WE WISH U TO STAY TOGETHER FOREVER AND CHERISH WITH MANY MEMORIES TOGETHER")
        else:
            print("INVALID INPUT")

    else:
        exit()






















