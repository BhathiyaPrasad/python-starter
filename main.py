command  = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("Car Started...")
    elif command == "stop":
        print("Car Stopped...")
    elif command == "help":
        print("""
Start  = To start the car
Stop   = To stop the car
Quit   = To exit the game
        """     )
    else :
        print("I don't understand that...")