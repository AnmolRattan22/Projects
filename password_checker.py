def password_checker(password):
    upper = False
    lower = False
    digit = False
    special = False
    
    special ='!@#$%^&*()-_=+\\|[]{};:/.>?'
    if len(password) < 8 or len(password) > 12:
        print("Invalid password.")
    else:
        
        for i in password:
            if i.isupper():
                upper = True
            elif i.islower():
                lower = True
            elif i.isdigit():
                digit = True
            elif i in special:
                special = True

        
        if upper and lower and digit and special:
            print("Valid password")
        else:
            print("Invalid password.")

def main():
    password = input("Enter your password: ")
    password_checker(password)

main()