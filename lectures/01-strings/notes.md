# 01 — Strings

## They do
- [ ] BroCode: strings are easy (username criteria)

name = input("Enter your full name: ")

# result = len(name)
# result = name.find("o")


print(results)
return: amount of characters in name (ex. bro code = 8)

# result = name.rfind("q")
*rfind is reverse search*

# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
---

**phone number example**

result = phone_number.count("-")
phone_number = phone_number.replace(" ")

enter your phone #: 1-234-567-8901
return: 1 234 567 8901 (*dashes were removed*) 

** validate user input exercise ** 
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter username")

if len(username) > 12:
  print("username cannot be more than 12 characters")
elif not username.find(" ") == -1:
  print ("username cannot contain spaces")
elif not username.isalpha():
  print ("username cannot contain numbers")
else: 
  print(f"Welcome{username}")

---

## We do
- rep 1:


## I do (unseen, solo)
- attempt:

## Stuck points
-username.isalpha checks for spacing and numbers (idk the other rules of things and wht they do to call back on when practicing but maybe i can do the practice on my own heere)
