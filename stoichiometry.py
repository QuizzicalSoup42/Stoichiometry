"""

Stoichiometry thing I made for fun
Don't steal it

- QuizzicalSoup42, 2025

"""

#### -- DEFINING MASS FUNCTION (cause I use it a lot) -- ####

def mass(full):
    global molar_mass
    print()

    mass_input = "2"

    if full:
        mass_input = input("Just molar mass (1) or full equation (2)? ")

    choice = input("Single element (1) or compound (2)? ")
    while choice != "1" and choice != "2":
        choice = input("Single element (1) or compound (2)? ")

    ## - If element - ##

    if choice == "1":
        print()
        print("What element?")
        element = input("Write the element symbol. ").lower()

        # - Error handling - #

        while element not in elements:
            element = input("Please enter a valid element symbol: ").lower()

        # - Get weight from dictionary - #

        molar_mass = elements[element]
        print()
        print("Molar mass of", element, "is", str(molar_mass) + "g/mol")
        print()

        if mass_input == "2":

            ## - Variables - ##

            print("Base equation:\nA * (B / C) = want\n\tA = have\n\tB = top factor\n\tC = bottom factor")
            print()
        
            ## - Input - ##
                
            choice = input("Mols to grams (1) or grams to mols (2)? ")
            while choice != "1" and choice != "2":
                choice = input("Mols to grams (1) or grams to mols (2)? ")
            
            if choice == "1":
                a = float(input("What is A (have)? "))
                b = molar_mass
                c = 1

            if choice == "2":
                a = float(input("What is A (have)? "))
                b = 1
                c = molar_mass

    ## - If compound - ##

    elif choice == "2":
        print()
        amount = int(input("How many elements are in the compound? (if multiple of one element just put it multiple times) "))

        ## - Put elements in compound list - ##
            
        compound = []
        print("Please enter the element symbols one at a time. ")
        print("Ex: H₂O = h [ENTER] h [ENTER] o [ENTER]")
        temp = 1
        while temp <= amount:
            element = input("").lower()

            # - Error handling - #

            while element not in elements:
                element = input("Please enter a valid element symbol: ").lower()

            compound.append(element)
            temp += 1

        ## - Calculate molar mass for compound - ##

        molar_mass = 0
        for i in compound:
            molar_mass += elements[i]

        print("Molar mass of", compound, "is", str(molar_mass) + "g/mol")

        if mass_input == "2":
            
            #### -- MATH -- ####

            ## - Variables - ##

            print("Base equation:\nA * (B / C) = want\n\tA = have\n\tB = top factor\n\tC = bottom factor")
            print()
        
            choice = input("Mols to grams (1) or grams to mols (2)? ")
            while choice != "1" and choice != "2":
                choice = input("Mols to grams (1) or grams to mols (2)? ")
            
            if choice == "1":
                a = float(input("What is A (have)? "))
                b = molar_mass
                c = 1

            if choice == "2":
                a = float(input("What is A (have)? "))
                b = 1
                c = molar_mass

    if mass_input == "2":

        want = (a * b) / c

        if full == True:

            ## - Print answer - ##

            print()
            print("Answer:", str(want))
            print()
    

#### -- ELEMENTS -- ####

elements = {
    "h": 1.0078, "he": 4.0026, "li": 6.938, "be": 9.0122, "b": 10.806, "c": 12.009, "n": 14.006, "o": 15.999, "f": 18.998, "ne": 20.180, "na": 22.990, "mg": 24.305,
    "al": 26.982, "si": 28.084, "p": 30.974, "s": 32.059, "cl": 35.446, "ar": 39.948, "k": 39.098, "ca": 40.078, "sc": 44.956, "ti": 47.867, "v": 50.942, "cr": 51.996,
    "mn": 54.938, "fe": 55.845, "co": 58.933, "ni": 58.693, "cu": 63.546, "zn": 65.38, "ga": 69.723, "ge": 72.63, "as": 74.922, "se": 78.96, "br": 79.904, "kr": 83.798,
    "rb": 85.468, "sr": 87.62, "y": 88.906, "zr": 91.224, "nb": 92.906, "mo": 95.96, "tc": 98.9062, "ru": 101.07, "rh": 102.91, "pd": 106.42, "ag": 107.87, "cd": 112.41,
    "in": 114.82, "sn": 118.71, "sb": 121.76, "te": 127.60, "i": 126.90, "xe": 131.29, "cs": 132.91, "ba": 137.33, "la": 138.91, "ce": 140.12, "pr": 140.91, "nd": 144.24,
    "pm": 145, "sm": 150.36, "eu": 151.96, "gd": 157.25, "tb": 158.93, "dy": 162.50, "ho": 164.93, "er": 167.26, "tm": 168.93, "yb": 175.04, "lu": 174.97, "hf": 178.49,
    "ta": 180.95, "w": 183.84, "re": 186.21, "os": 190.23, "ir": 192.22, "pt": 195.08, "au": 196.97, "hg": 200.59, "tl": 204.38, "pb": 207.2, "bi": 208.98, "po": 209,
    "at": 210, "rn": 222, "fr": 223, "ra": 226, "ac": 227, "th": 232.04, "pa": 231.04, "u": 238.03, "np": 237, "pu": 244, "am": 243, "cm": 247, "bk": 251, "es": 252,
    "fm": 257, "md": 258, "no": 259, "lr": 262, "rf": 261, "db": 262, "sg": 266, "bh": 264, "hs": 269, "mt": 268, "ds": 268, "rg": 268, "cn": 268, "uut": 268, "fl": 268,
    "fl": 268, "uup": 268, "lv": 268, "uus": 268, "uuo": 268
}

#### -- INPUT -- ####

looping = True

while looping:

    choice = input("Mass (1), volume (2), particles (3), multi (4), or substance ratios (5)? ").lower()

    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
        choice = input("Mass (1), volume (2), particles (3), multi (4), or substance ratios (5)? ").lower()

    #### -- MASS -- ####

    if choice == "1":
        full = True
        mass(full)
    
    #### -- VOLUME -- ####

    elif choice == "2":
        
        ## - Variables - ##

        print("Base equation:\nA * (B / C) = want\n\tA = have\n\tB = top factor\n\tC = bottom factor")
        print()

        ## - Input - ##
        
        choice = input("Mols to volume (1) or volume to mols (2)? ")
        while choice != "1" and choice != "2":
            choice = input("Mols to volume (1) or volume to mols (2)? ")
        
        if choice == "1":
            a = float(input("What is A (have)? "))
            b = 22.4
            c = 1

        if choice == "2":
            a = float(input("What is A (have)? "))
            b = 1
            c = 22.4

        ## - Math - ##

        want = (a * b) / c

        ## - Print answer - ##

        print()
        print("Answer:", str(want))
        print()

    #### -- PARTICLES -- ####

    if choice == "3":

        ## - Variables - ##
        
        print()
        print("Base equation:\nA * (B / C) = want\n\tA = have\n\tB = top factor\n\tC = bottom factor")
        print("If there are exponents, write as such: __ * 10^12")
        print()

        ## - Input - ##

        choice = input("Mols to particles (1) or particles to mols (2)? ")
        while choice != "1" and choice != "2":
            choice = input("Mols to particles (1) or particles to mols (2)? ")
        
        if choice == "1":
            a = float(input("What is A (have)? "))
            b = 22.4
            c = 1

        if choice == "2":
            a = input("What is A (have)? ")
            b = 1
            c = 22.4

            # - Exponent calc - #

            a_list = a.split(" * 10^")
            a1 = float(a_list[0])
            a2 = float(a_list[1])
            a = a1 * (10 ** a2)

        ## - Math - ##

        want = (a * b) / c

        ## - Print answer - ##

        print()
        print("Answer:", str(want))
        print()
        
        
    #### -- MULTIPLE FACTORS -- ####
    
    if choice == "4":

        full = False
        
        ## - Explanation - ##
        
        print()
        print("Base equation:\nA * (B / C) * (D / E)")
        print("A = Want\tB = Top first factor\tC = Bottom first factor\nD = Top second factor\tE = Bottom second factor")
        print("All you need to enter is A (want). If you are converting to mass, you will need to input the element(s) and it will automatically calculate the molar mass.")
        input("Press [ENTER] to continue. ")
        
        ## - Variables - ##
        
        transfer1 = input("What are you transferring to mols first? (mass (1), volume (2), or particles (3)) ").lower()
        
        while transfer1 != "1" and transfer1 != "2" and transfer1 != "3":
            transfer1 = input("What are you transferring to mols first? (mass (1), volume (2), or particles (3)) ").lower()
            
        transfer2 = input("What are you transferring from mols? (mass (1), volume (2), or particles (3)) ").lower()
        
        while transfer2 != "1" and transfer2!= "2" and transfer2!= "3":
            transfer2 = input("What are you transferring from mols? (mass (1), volume (2), or particles (3)) ").lower()
        
        #### -- IF MASS --> ??? -- ####
        
        if transfer1 == "1":
            mass(full)
            
            ## - Mass --> Volume - ##
            
            if transfer2 == "2":
                
                ## - Math - ##
                                
                d = 1
                e = 22.4
                
                answer = (want * d) / e
                
                print()
                print(answer, "liters")
                
            ## - Mass --> Particles - ##
            
            if transfer2 == "3":
                
                ## - Math - ##
                
                d = 6.02 * (10 ** 23)
                e = 1
                
                answer = (want * d) / e
                
                print()
                print(answer, "particles")
            
        #### -- IF PARTICLES --> ??? -- ####
        
        if transfer1 == "3":
            a = float(input("What is A (have)? "))
            a_list = a.split(" * 10^")
            a1 = float(a_list[0])
            a2 = float(a_list[1])
            a = a1 * (10 ** a2)
            print()
            
            b = 6.02 * (10 ** 23)
            c = 1
            
            mols = (a * b) / c
            
            ## - Particles --> Mass - ##
            
            if transfer2 == "1":
                mass(full)

                ## - MATH - ##
                
                d = 1
                e = float(molar_mass)
                
                answer = (mols * d) / e
                
                print()
                print(answer, "grams")
                
            ## - Particles --> Volume - ##
            
            if transfer2 == "2":
                
                d = 1
                e = 22.4
                
                answer = (mols * d) / e
                
                print()
                print(answer, "liters")
                
        #### -- VOLUME --> ??? -- ####
            
        if transfer1 == "2":
            
            a = float(input("What is A (have)? "))
            print()
            b = 22.4
            c = 1
            
            mols = (a * b) / c
            
            ## - Volume --> Particles - ##
            
            if transfer2 == "3":
                
                d = 6.02 * (10 ** 23)
                e = 1
                
                answer = (mols * d) / e
                
                print()
                print(answer, "particles")
                
            ## - Volume --> Mass - ##
            
            if transfer2 == "1":
                
                mass(full)
                        
                ## - MATH - ##
                
                d = 1
                e = molar_mass
                
                answer = (mols * d) / e
                
                print()
                print(answer, "grams")
                

    #### -- SUBSTANCE RATIOS -- ####

    if choice == "5":

        full = False

        ## - 1st reactant / product - ##

        print("What is the first reactant / product?")
        print("This is the one you have, even if it's a product.")

        mass(full)

        ## - 2nd reactant / product - ##

        print("What is the second reactant / product?")
        print("This is the one you DON'T have, even if it's a reactant.")

        mass(full)

        ## - Input - ##

        print("What is the ratio?")
        ratio = input("Ex: 1-2 ")

        ### - MATH - ###

        ratio_list = ratio.split("-")
        ratio1 = ratio_list[0]
        ratio2 = ratio_list[1]

        choice = input("Is the first reactant / product in mols (1) or grams (2)? ")
        while choice != "1" and choice != "2":
            choice = input("Is the second reactant / product in mols (1) or grams (2)? ")

        if choice == "1":
            a = float(input("How many mols? "))
            mols2 = (a * int(ratio2)) / int(ratio1)
        elif choice == "2":
            a = float(input("How many grams? "))
            b = 1
            c = molar_mass

            mols = (a * b) / c
            mols2 = (mols * int(ratio2)) / int(ratio1)
        
        choice = input("Is the second reactant / product in mols (1) or grams (2)? ")
        while choice != "1" and choice != "2":
            choice = input("Is the second reactant / product in mols (1) or grams (2)? ")
        if choice == "1":
            answer = mols2
        if choice == "2":
            answer = (mols2 * molar_mass2) / 1

        ## - Print answer - ##

        print()
        print("The number of grams required / will be produced is:", str(answer))

    ## - Again? - ##

    loop = input ("Do another equation? (y/n) ")
    if loop == "y":
        print()
        print()
    else:
        looping = False

