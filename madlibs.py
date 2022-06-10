# Madlib will take input from user and complete the blanks
programName = ""
print("Welcome to Isha Foundation")
programName = input("Which Program you want to Register ")
print("Welcome to Program " + programName)
print("Welcome to Program {}".format(programName))
print(f"Welcome to Program {programName}")

adjective = input("Enter Adjective")
saveSoilCountry = input("Enter the Country")
saveSoilState = input("Enter the State")

madLibs = f"Out {adjective} Sadhguru will be travelling to different countries. First country will be \
    {saveSoilCountry} and the first State will be {saveSoilState}" 
print(madLibs)