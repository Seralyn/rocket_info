
def rocket_inquiry(rocket_name):
    inside_function = True
    while inside_function == True:
        rocketQues01 = f"What would you like to know about the {rocket_name}?\n"
        print (rocketQues01)
        possAns = input('''Here are your choices:
            A: Who made it
            B: Its payload capacity
            C: Its height
            D: Its diameter
            E: Its mass
            F: Back\n''')
        if possAns == "A":
            print(dct1[rocket_name][1] + "\n")
        elif possAns == "B":
            print(dct1[rocket_name][2] + "\n")
        elif possAns == "C":
            print(dct1[rocket_name][3] + "\n")
        elif possAns == "D":
            print(dct1[rocket_name][4] + "\n")
        elif possAns == "E":
            print(dct1[rocket_name][5] + "\n")A
        elif possAns == "F":
            print(returningMsg)
            inside_function = False

appRunning = True
while appRunning == True:
    dct1 = {
        'Saturn V': ["Saturn V",
                     "NASA - National Aeronautics & Space Administration",
                     "Payload Capacity to LEO: 140,000kg (310,000 lbs)",
                     "Height: 110.6m (363ft)",
                     "Diameter: 10.1m (33ft)",
                     "Mass: 2,970,000 kg"],
        "Soyuz": ["Soyuz",
                  "Roscosmos",
                  "Payload Capacity to LEO: 6,450 kilograms (14,220 lbs)",
                  "Height: 45.6m (150 ft)",
                  "Diameter: 10.3m (34ft)",
                  "Mass: 308,000 kg"],
        "Delta III": ["Delta III",
                      "ULA - United Launch Alliance",
                      "Payload Capacity to LEO: 8,290 kg (18,280 lbs)",
                      "Height: 35m (115ft)", "Diameter: 4m (13ft)", "Mass: 301,450 kg"],
        "Ariane 62": ["Ariane 62",
                      "ESA - European Space Agency",
                      "Payload Capacity to LEO: 10,350 kg (22,817 lbs)",
                      "Height: 63m (207ft)",
                      "Diameter: 5.4m (18ft)",
                      "Mass: 530,000–860,000 kg"]
    }


    #0 = Rocketname, 1 = agency, 2 = payload capacity to low-earth orbit, 3 = height, 4 = diameter, 5 = mass

    #examples of pulling styles
    #print(dct1["Saturn V"][1])
    #print(dct1["Gabi"])

    ques01 = '''Which rocket would you like to learn about today?
    Your options are:
    A) Saturn V
    B) Soyuz
    C) Delta III
    D) Ariane 62
    E) Quit'''

    returningMsg = "Returning to previous menu."

    print(ques01)

    answer = input("Please enter the letter corresponding to your selection below.\n")

    if answer == "A":
        rocket_inquiry("Saturn V")

    elif answer == "B":
        rocket_inquiry("Soyuz")

    elif answer == "C":
        rocket_inquiry("Delta III")

    elif answer == "D":
        rocket_inquiry("Ariane 62")

    elif answer == "E":
        break
