import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)" )

text = input('Enter your email address: ')

matches = pattern.findall(text)

if matches:
    print("This is a valid email address")
else:
    print("This is not a valid email address")   
    
    
# r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$%#@]).{8,}$'