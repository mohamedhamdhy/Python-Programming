# String And String Function
s = "tutor Joes"
print(s)
print(type(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.count("t"))
print(s.endswith("ED"))
print(s.find("o"))
print(s.find("o", 5))
print(s.replace("o", '0'))
a = "joes1234"
print("Is Upper : ", a.isupper())
print("Is Lower : ", a.islower())
print("Is Alpha Numeric : ", a.isalnum())
print("Is Alpha : ", a.isalpha())
s = "he\nis\ngood"
print(s)
print(s.splitlines())
print(s.splitlines(True))
a = "Tutor Joes Computer Education"
print(a.split(" "))
a = "Tutor,Joes,Computer,Education"
print(a.split(","))
s="    Joes     "
print(len(s))
print(len(s.strip()))
print(len(s.lstrip()))
print(len(s.rstrip()))
s='12-03-2020'
print(s.partition('-'))