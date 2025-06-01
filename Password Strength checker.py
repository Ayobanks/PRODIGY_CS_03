import string

password = input("Enter your password — to check the strength: ")
print("Checking strength....")
length = len(password)
#for weak password
if length < 8 or password.islower() or password.isupper() or password.isnumeric():
    print("❌ Your password is weak — perfect invitation for hackers.")
#for okay password
elif 8 < length < 12:
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isnumeric() for char in password)

    if has_upper and has_lower and has_digit:
        print("🟡 Your password is okay, But you can do better!")

    else:
       print("❌ Your password is weak — perfect invitation for hackers.")  
#for strong password
elif length > 12:
     has_upper = any(char.isupper() for char in password)
     has_lower = any(char.islower() for char in password)
     has_digit = any(char.isnumeric() for char in password)
     has_symbol = any(char in string.punctuation for char in password)

     if has_upper and has_lower and has_digit and has_symbol:
         print("✅ Perfect passsword!!!")

     elif has_upper and has_lower and has_digit:
        print("🟡 Your password is okay, But you can do better!")

     else:
         print("❌ Your password is weak — perfect invitation for hackers.") 

