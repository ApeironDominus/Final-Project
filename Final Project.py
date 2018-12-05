#Custom Car Shop
#Daniel Causey
#CIS-120-102-FA18

#Define Variables
totalCost = 0
#Engine Variables
vTwinEngineCost = 200
v4EngineCost = 400
v6EngineCost = 1000
v8EngineCost = 1600
v12EngineCost = 2500
v16EngineCost = 10000
smallElectricMotor = 500
medElectricMotor = 1000
largeElectricMotor = 2000
nuclearReactor = 250000
#Chassis Variables
motorcycle = 1200
sedan = 2000
sports = 4000
sportsUtility = 6000
truck = 10000
luxury = 20000
militaryGrade = 40000
#Paintjob Variables
solid = 200
metallic = 500
pearlescent = 2000
matte = 3000
carbonFiber = 10000
#Interior Variables
fabric = 500
pLeather = 1000
standardLeather = 2500
luxuryLeather = 10000
#Menu Variables
userExit = False
userMenuChoice = 0
userSubMenuChoice = 0
userSubMenuExit = False
userPurchaseMenuChoice = 0
userPurchaseMenuExit = False
engineSelection = False
chassisSelection = False
paintStyleSelected = False
paintColorSelected = False
interiorSelected = False
#Color Array
colors = ["Red", "Orange", "Yellow", "Blue", "Purple", "Green", "Black", "White", "Grey"]

#Receipt Part 1
def printReceipt1():
    file = open("receipt.txt", "w")
    file.write("Thank you for your purchase!\n")

#Receipt Part 2
def printReceipt2():
    file = open("receipt.txt", "a")
    file.write("Total Cost: " + str(totalCost) + "\n")
    file.write("*************************" + "\n")
    file.write("Please come again!")
    
#Receipt Part 3
def printReceipt3():
    import webbrowser
    webbrowser.open("receipt.txt")

#View Cart Part 1
def viewCart1():
    file = open("cart.txt", "w")
    file.write ("These are the current contents of your cart,\n")

#View Cart Part 2
def viewCart2():
    import webbrowser
    webbrowser.open("cart.txt")

printReceipt1()
viewCart1()

#Menu
while (userExit == False):
    print ("Welcome to Cecil's Custom Car Consortium!")
    print ("What would you like to do?")
    print ("1. Add an item to your car.")
    print ("2. View your car.")
    print ("3. Checkout and exit.")
    userSubMenuExit = False
    userMenuChoice = int(input())
    if (userMenuChoice == 1):
        while (userSubMenuExit == False):
            print ("What type of part would you like to add to your car, remember you can only have one of each?")
            print ("1. Engine Choices")
            print ("2. Chassis Choices")
            print ("3. Paintjob Options")
            print ("4. Color Options")
            print ("5. Interior Variables")
            print ("6. Return to prior menu")
            userPurchaseMenuExit = False
            userSubMenuChoice = int(input())

            if (userSubMenuChoice == 1):
                while (userPurchaseMenuExit == False):
                    print ("What type of Engine would you like to use?")
                    print ("1. V-Twin Engine - $200")
                    print ("2. V-4 Engine - $400")                
                    print ("3. V-6 Engine - $1000")
                    print ("4. V-8 Engine - $1600")
                    print ("5. V-12 Engine - $2500")
                    print ("6. V-16 Engine - $10000")
                    print ("7. Small Electric Motor - $500")
                    print ("8. Medium Electric Motor - $100")
                    print ("9. Large Electric Motor - $2000")
                    print ("10. Nuclear Reactor - $250000")
                    print ("11. Return to prior menu")
                    userPurchaseMenuChoice = int(input())

                    if (userPurchaseMenuChoice == 1):
                        if engineSelection == False:
                            totalCost = totalCost + vTwinEngineCost
                            file = open ("cart.txt", "a")
                            file.write ("Engine: V-Twin Engine " + "$200" + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Engine: V-Twin Engine " + "$200" + "\n")
                            engineSelection = True
                            break
                        elif engineSelection == True:
                            print ("You already have an engine and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 2):
                        if engineSelection == False:
                            totalCost = totalCost + v4EngineCost
                            file = open ("cart.txt", "a")
                            file.write ("Engine: V-4 Engine " + "$400" + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Engine: V-4 Engine " + "$400" + "\n")
                            engineSelection = True
                            break
                        elif engineSelection == True:
                            print ("You already have an engine and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 3):
                        if engineSelection == False:
                            totalCost = totalCost + v6EngineCost
                            file = open ("cart.txt", "a")
                            file.write ("Engine: V-6 Engine " + "$1000" + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Engine: V-6 Engine " + "$1000" + "\n")
                            engineSelection = True
                            break
                        elif engineSelection == True:
                            print ("You already have an engine and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 4):
                        if engineSelection == False:
                            totalCost = totalCost + v8EngineCost
                            file = open ("cart.txt", "a")
                            file.write ("Engine: V-8 Engine " + "$1600" + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Engine: V-8 Engine " + "$1600" + "\n")
                            engineSelection = True
                            break
                        elif engineSelection == True:
                            print ("You already have an engine and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 5):
                        if engineSelection == False:
                            totalCost = totalCost + v12EngineCost
                            file = open ("cart.txt", "a")
                            file.write ("Engine: V-12 Engine " + "$2500" + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Engine: V-12 Engine " + "$2500" + "\n")
                            engineSelection = True
                            break
                        elif engineSelection == True:
                            print ("You already have an engine and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 6):
                        if engineSelection == False:
                            totalCost = totalCost + v16EngineCost
                            file = open ("cart.txt", "a")
                            file.write ("Engine: V-16 Engine " + "$10000" + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Engine: V-16 Engine " + "$10000" + "\n")
                            engineSelection = True
                            break
                        elif engineSelection == True:
                            print ("You already have an engine and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 7):
                        if engineSelection == False:
                            totalCost = totalCost + smallElectricMotor
                            file = open ("cart.txt", "a")
                            file.write ("Engine: Small Electric Motor " + "$500" + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Engine: Small Electric Motor " + "$500" + "\n")
                            engineSelection = True
                            break
                        elif engineSelection == True:
                            print ("You already have an engine and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 8):
                        if engineSelection == False:
                            totalCost = totalCost + medElectricMotor
                            file = open ("cart.txt", "a")
                            file.write ("Engine: Medium Electric Motor " + "$1000" + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Engine: Medium Electric Motor " + "$1000" + "\n")
                            engineSelection = True
                            break
                        elif engineSelection == True:
                            print ("You already have an engine and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 9):
                        if engineSelection == False:
                            totalCost = totalCost + largeElectricMotor
                            file = open ("cart.txt", "a")
                            file.write ("Engine: Large Electric Motor " + "$2000" + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Engine: Large Electric Motor " + "$2000" + "\n")
                            engineSelection = True
                            break
                        elif engineSelection == True:
                            print ("You already have an engine and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 10):
                        if engineSelection == False:
                            totalCost = totalCost + v4EngineCost
                            file = open ("cart.txt", "a")
                            file.write ("Engine: V-4 Engine " + "$400" + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Engine: V-4 Engine " + "$400" + "\n")
                            engineSelection = True
                            break
                        elif engineSelection == True:
                            print ("You already have an engine and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                    elif (userPurchaseMenuChoice == 11):
                        userPurchaseMenuExit = True
                        break
                    else:
                        print("Please enter a valid number.")

                
            elif (userSubMenuChoice == 2):
                while (userPurchaseMenuExit == False):
                    print ("What type of Chassis would you like to use?")
                    print ("1. Motorcycle Chassis - $1200")
                    print ("2. Sedan Chassis - $2000")                
                    print ("3. Sports Chassis - $4000")
                    print ("4. Sports Utility Chassis - $6000")
                    print ("5. Truck Chassis - $10000")
                    print ("6. Luxury Chassis - $20000")
                    print ("7. Military Grade Chassis - $40000")
                    print ("8. Return to prior menu")
                    userPurchaseMenuChoice = int(input())

                    if (userPurchaseMenuChoice == 1):
                        if chassisSelection == False:
                            totalCost = totalCost + motorcycle
                            file = open ("cart.txt", "a")
                            file.write ("Chassis: Motorcycle " + "$1200" + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Chassis: Motorcycle " + "$1200" + "\n")
                            chassisSelection = True
                            break
                        elif chassisSelection == True:
                            print ("You already have a chassis and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 2):
                        if chassisSelection == False:
                            totalCost = totalCost + sedan
                            file = open ("cart.txt", "a")
                            file.write ("Chassis: Sedan " + "$2000" + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Chassis: Sedan " + "$2000" + "\n")
                            chassisSelection = True
                            break
                        elif chassisSelection == True:
                            print ("You already have a chassis and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 3):
                        if chassisSelection == False:
                            totalCost = totalCost + sports
                            file = open ("cart.txt", "a")
                            file.write ("Chassis: Sports " + "$4000" + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Chassis: Sports " + "$4000" + "\n")
                            chassisSelection = True
                            break
                        elif chassisSelection == True:
                            print ("You already have a chassis and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 4):
                        if chassisSelection == False:
                            totalCost = totalCost + sportsUtility
                            file = open ("cart.txt", "a")
                            file.write ("Chassis: Sports Utility " + "$6000" + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Chassis: Sports Utility " + "$6000" + "\n")
                            chassisSelection = True
                            break
                        elif chassisSelection == True:
                            print ("You already have a chassis and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 5):
                        if (chassisSelection == False):
                            totalCost = totalCost + truck
                            file = open ("cart.txt", "a")
                            file.write ("Chassis: Truck " + "$10000" + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Chassis: Truck " + "$10000" + "\n")
                            chassisSelection = True
                            break
                        elif (chassisSelection == True):
                            print ("You already have a chassis and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 6):
                        if (chassisSelection == False):
                            totalCost = totalCost + luxury
                            file = open ("cart.txt", "a")
                            file.write ("Chassis: Luxury " + "$20000" + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Chassis: Luxury " + "$20000" + "\n")
                            chassisSelection = True
                            break
                        elif (chassisSelection == True):
                            print ("You already have a chassis and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 7):
                        if (chassisSelection == False):
                            totalCost = totalCost + militaryGrade
                            file = open ("cart.txt", "a")
                            file.write ("Chassis: Military Grade " + "$40000" + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Chassis: Military Grade " + "$40000" + "\n")
                            chassisSelection = True
                            break
                        elif (chassisSelection == True):
                            print ("You already have a chassis and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 8):
                        userPurchaseMenuExit = True
                        break
                    else:
                        print("Please enter a valid number.")
                           
                
            elif (userSubMenuChoice == 3):
                while (userPurchaseMenuExit == False):
                    print ("What type of Paintjob would you like to use?")
                    print ("1. Solid Paintjob - $200")
                    print ("2. Metallic Paintjob - $500")                
                    print ("3. Pearlescent Paintjob - $2000")
                    print ("4. Matte Paintjob - $3000")
                    print ("5. Carbon Fiber Paintjob - $10000")
                    print ("6. Return to prior menu")
                    userPurchaseMenuChoice = int(input())

                    if (userPurchaseMenuChoice == 1):
                        if paintStyleSelected == False:
                            totalCost = totalCost + solid
                            file = open ("cart.txt", "a")
                            file.write ("Paintjob: Solid " + "$200" + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Paintjob: Solid " + "$200" + "\n")
                            paintStyleSelected = True
                            break
                        elif paintStyleSelected == True:
                            print ("You already have a paintjob and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 2):
                        if paintStyleSelected == False:
                            totalCost = totalCost + metallic
                            file = open ("cart.txt", "a")
                            file.write ("Paintjob: Metallic " + "$500" + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Paintjob: Metallic " + "$500" + "\n")
                            paintStyleSelected = True
                            break
                        elif paintStyleSelected == True:
                            print ("You already have a paintjob and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 3):
                        if paintStyleSelected == False:
                            totalCost = totalCost + pearlescent
                            file = open ("cart.txt", "a")
                            file.write ("Paintjob: Pearlescent " + "$2000" + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Paintjob: Pearlescent " + "$2000" + "\n")
                            paintStyleSelected = True
                            break
                        elif paintStyleSelected == True:
                            print ("You already have a paintjob and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 4):
                        if paintStyleSelected == False:
                            totalCost = totalCost + matte
                            file = open ("cart.txt", "a")
                            file.write ("Paintjob: Matte " + "$3000" + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Paintjob: Matte " + "$3000" + "\n")
                            paintStyleSelected = True
                            break
                        elif paintStyleSelected == True:
                            print ("You already have a paintjob and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 5):
                        if paintStyleSelected == False:
                            totalCost = totalCost + carbonFiber
                            file = open ("cart.txt", "a")
                            file.write ("Paintjob: Carbon Fiber " + "$10000" + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Paintjob: Carbon Fiber " + "$10000" + "\n")
                            paintStyleSelected = True
                            break
                        elif paintStyleSelected == True:
                            print ("You already have a paintjob and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 6):
                        userPurchaseMenuExit = True
                        break
                    else:
                        print("Please enter a valid number.")

            elif (userSubMenuChoice == 4):
                while (userPurchaseMenuExit == False):
                    print ("What color paint would you like to use?")
                    print ("1. Red")
                    print ("2. Orange")                
                    print ("3. Yellow")
                    print ("4. Blue")
                    print ("5. Purple")
                    print ("6. Green")
                    print ("7. Black")
                    print ("8. White")
                    print ("9. Grey")
                    print ("10. Return to prior menu")
                    userPurchaseMenuChoice = int(input())

                    if (userPurchaseMenuChoice == 1):
                        if paintColorSelected == False:
                            file = open ("cart.txt", "a")
                            file.write ("Paint Color: " + str(colors[0]) + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Paint Color: " + str(colors[0]) + "\n")
                            paintColorSelected = True
                            break
                        elif paintColorSelected == True:
                            print ("You already have a paintjob and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 2):
                        if paintColorSelected == False:
                            file = open ("cart.txt", "a")
                            file.write ("Paint Color: " + str(colors[1]) + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Paint Color: " + str(colors[1]) + "\n")
                            paintColorSelected = True
                            break
                        elif paintColorSelected == True:
                            print ("You already have a paintjob and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 3):
                        if paintColorSelected == False:
                            file = open ("cart.txt", "a")
                            file.write ("Paint Color: " + str(colors[2]) + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Paint Color: " + str(colors[2]) + "\n")
                            paintColorSelected = True
                            break
                        elif paintColorSelected == True:
                            print ("You already have a paintjob and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 4):
                        if paintColorSelected == False:
                            file = open ("cart.txt", "a")
                            file.write ("Paint Color: " + str(colors[3]) + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Paint Color: " + str(colors[3]) + "\n")
                            paintColorSelected = True
                            break
                        elif paintColorSelected == True:
                            print ("You already have a paintjob and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 5):
                        if paintColorSelected == False:
                            file = open ("cart.txt", "a")
                            file.write ("Paint Color: " + str(colors[4]) + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Paint Color: " + str(colors[4]) + "\n")
                            paintColorSelected = True
                            break
                        elif paintColorSelected == True:
                            print ("You already have a paintjob and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    if (userPurchaseMenuChoice == 6):
                        if paintColorSelected == False:
                            file = open ("cart.txt", "a")
                            file.write ("Paint Color: " + str(colors[5]) + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Paint Color: " + str(colors[5]) + "\n")
                            paintColorSelected = True
                            break
                        elif paintColorSelected == True:
                            print ("You already have a paintjob and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 7):
                        if paintColorSelected == False:
                            file = open ("cart.txt", "a")
                            file.write ("Paint Color: " + str(colors[6]) + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Paint Color: " + str(colors[6]) + "\n")
                            paintColorSelected = True
                            break
                        elif paintColorSelected == True:
                            print ("You already have a paintjob and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 8):
                        if paintColorSelected == False:
                            file = open ("cart.txt", "a")
                            file.write ("Paint Color: " + str(colors[7]) + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Paint Color: " + str(colors[7]) + "\n")
                            paintColorSelected = True
                            break
                        elif paintColorSelected == True:
                            print ("You already have a paintjob and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 9):
                        if paintColorSelected == False:
                            file = open ("cart.txt", "a")
                            file.write ("Paint Color: " + str(colors[8]) + "\n")
                            file = open ("receipt.txt", "a")
                            file.write ("Paint Color: " + str(colors[8]) + "\n")
                            paintColorSelected = True
                            break
                        elif paintColorSelected == True:
                            print ("You already have a paintjob and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 10):
                        userPurchaseMenuExit = True
                        break
                    else:
                        print("Please enter a valid number.")

            elif (userSubMenuChoice == 5):
                while (userPurchaseMenuExit == False):
                    print ("What type of Interior would you like to use?")
                    print ("1. Fabric Interior - $500")
                    print ("2. Pseudo-Leather Interior - $1000")                
                    print ("3. Leather Interior - $2500")
                    print ("4. Luxury Leather Interior - $10000")
                    print ("5. Return to prior menu")
                    userPurchaseMenuChoice = int(input())

                    if (userPurchaseMenuChoice == 1):
                        if interiorSelected == False:
                            totalCost = totalCost + fabric
                            file = open ("receipt.txt", "a")
                            file.write ("Interior: Fabric " + "$500" + "\n")
                            file = open ("cart.txt", "a")
                            file.write ("Interior: Fabric " + "$500" + "\n")
                            interiorSelected = True
                            break
                        elif interiorSelected == True:
                            print ("You already have a interior and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 2):
                        if interiorSelected == False:
                            totalCost = totalCost + pLeather
                            file = open ("receipt.txt", "a")
                            file.write ("Interior: Pseudo-Leather " + "$1000" + "\n")
                            file = open ("cart.txt", "a")
                            file.write ("Interior: Pseudo-Leather " + "$1000" + "\n")
                            interiorSelected = True
                            break
                        elif interiorSelected == True:
                            print ("You already have a interior and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 3):
                        if interiorSelected == False:
                            totalCost = totalCost + standardLeather
                            file = open ("receipt.txt", "a")
                            file.write ("Interior: Leather " + "$2500" + "\n")
                            file = open ("cart.txt", "a")
                            file.write ("Interior: Leather " + "$2500" + "\n")
                            interiorSelected = True
                            break
                        elif interiorSelected == True:
                            print ("You already have a interior and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 4):
                        if interiorSelected == False:
                            totalCost = totalCost + luxuryLeather
                            file = open ("receipt.txt", "a")
                            file.write ("Interior: Luxury Leather " + "$10000" + "\n")
                            file = open ("cart.txt", "a")
                            file.write ("Interior: Luxury Leather " + "$10000" + "\n")
                            interiorSelected = True
                            break
                        elif interiorSelected == True:
                            print ("You already have a interior and may not fit more than one in your car.")
                            userPurchaseMenuExit = True
                            break
                    elif (userPurchaseMenuChoice == 5):
                        userPurchaseMenuExit = True
                        break
                    else:
                        print("Please enter a valid number.")

            elif (userSubMenuChoice == 6):
                break
            else:
                print("Please enter a valid number.")

    elif (userMenuChoice == 2):
        viewCart2()

    elif (userMenuChoice == 3):
        printReceipt2()
        printReceipt3()
        userExit = True
    else:
        print("Please enter a valid number.")
