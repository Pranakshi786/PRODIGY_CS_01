def ceaser_cipher():
    ed=input("Type encrypt for encyption and decrypt for decryption: ")
    if ed=='encrypt':
        encrypt=input("Type your message: ")
        shift=int(input("Enter shift key: "))
        for i in encrypt:
            i=ord(i)
            i+=shift
            i=chr(i)
            print(i,end="")
        print()
        ask_again=input("Do you want to try again (Yes or No)? ")
        if ask_again=='Yes':
            ceaser_cipher()
        else:
            print("Till next time...")
    elif ed=='decrypt':
        decrypt=input("Type your message: ")
        shift=int(input("Enter shift key: "))
        for i in decrypt:
            i=ord(i)
            i-=shift
            i=chr(i)
            print(i,end="")
        print()
        ask_again=input("Do you want to try again (Yes or No)? ")
        if ask_again=='Yes':
            ceaser_cipher()
        else:
            print("Till next time...")
    else:
        print("enter valid text")
ceaser_cipher()