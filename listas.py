#According to the instructions below, we will manage several names in a list

#First, say hello to the user
print(("Hello!").upper().center (55))

#Now, create a list with several names
#The exercise requires at least 5 names, so we will create a list with 5 names
name=["Elisabeth Gonzalez", 
      "Camila Restrepo", 
      "Sofía Jaramillo",
      "María José Peñalosa", 
      "Valeria Ortega"]

#Now, print the list of names
print(("\n" + "Names: ").upper())
print("\n" + "1. Add a name")
print("2. Show names")
print("3. Change a name")
print("4. Delete a name by position")

#I ask them to select an option
option=(input("\nSelect an option: "))

if option=="1":
    #Here I ask for the name that the person wants to add
    new=input("\nEnter the name that you want to add: ")

      #Before adding the name, I check if it is already in the list
    if new in name:
       print("\nThe name already exists.")

    else:
        name.append(new)
        print("\nName added successfully.")
    

elif option=="2":
    #Here I show the names in the list
    print("\nNames in the list: ")
    #I go through the list and show each name
    for n in name:
       print("\n-", n)


elif option=="3":
   #Here I ask which name the user wants to replace
   old=input("\nWhich name do you want to change?: ")

   #Check if the name is in the list
   if old not in name:
      print("\nThat name is not in the list.")

   else: 
      #Here I ask for the new name
      new=input("Write the new name: ")

      if new in name:
         #Check if the name is already in the list
         print("\nThat name already exists.")

      else: 
         #Get the position of the old name
         index=name.index(old)
         #Replace the old name with the new name
         name[index]=new
         print("\nName updated successfully.")

elif option=="4":
   print("\nAvailable positions: ")

   for i in range(len(name)):
      print(i, "-", name[i])

   pos=int(input("\nEnter the position you want to delete: "))
   
   #Validate the position
   if pos < 0 or pos >=len(name):
      print("\n\033[31mInavalid position, try again.\033[0m")

   else:
      #Invalid position
      delete=name.pop(pos)
      print(f"\n\033[32mYpu deleted: {delete}\033[0m")

else:
   #Show final list
   print("\n\033[31mIvalid option.\033[0m")


print("\nFinal list: ", name)