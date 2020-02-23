UpperCaseLetters = 0
Digits = 0
UserID = input("Your User ID: ")

for i in range(len(UserID)):
    if 65 <= ord(UserID[i]) <= 90:
        UpperCaseLetters += 1
    elif 48 <= ord(UserID[i]) <= 57:
        Digits += 1
    else:
        continue

if len(UserID)!=7 or UpperCaseLetters != 3 or Digits != 4:
    print("not valid")
else:
    print("valid")