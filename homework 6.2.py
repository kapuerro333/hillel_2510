
while True:
    message = input("Enter a message: ")
    if 'h' in message.lower():
        for char in message:
            if char in "hH":
                print(char)
        break
    else:
        print("No 'h' or 'H' is displayed. Try again.")