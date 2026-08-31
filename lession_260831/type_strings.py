print("___Wiederholung")
age = 18 # int
price = 19.99 # float
name = "Sveta" # str
is_name = True # bool

fruits = ["apple", "banana", "orange", "mango"] # list, editierbar
coordinates = [1, 2, 3] # tuple => unveränderbar... Warum?
students = {
    "name": "Sveta",
    "age": 18
} # dict
unique_numbers = {1, 2, 6, 8, 5, 7, 9, 8, 6}
print(unique_numbers)
print(type(unique_numbers))
print(type(students))
print(type(age))
print(type(price))
print(type(name))
print(type(is_name))
print(type(fruits))

s1 = 'Victor'
s2 = "I want to say \"Hi\""
print(s1 + s2)
s3 = "First string \nSecond string\nThird string"
print(s3)
first_name = "John"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name)

long_string = "Hello World"
print(long_string*5) # repeat string 5 times
print()

city = "New York"
temperature = 27.8
text = f"Today in {city} the temperature is {temperature}°C"
print(text)
print()

print("___SLICE___")
word = "Privet"
print(word[0]) #P
print(word[3]) #v
print(word[1:4]) #riv
print(word[0:]) #Privet
print(word[0:len(word)]) #Privet
print(word[:len(word)]) #Privet
print(word[:2]) #Pr
print(word[::-1]) # rückwärts # tevirP
print(word[-1]) # letzte Symbol # t

print("___SLICE in einer ZEILE___")
string = "Hier steht eine Headline"
print(string[1:8:2]) #irse => 1 Stelle, 7 Stellen, jede 2 Stelle raus
print(string[:10:3]) # Hrtt
print()

print("__METHODEN für strings__")
text3 = " I like walking "
text4 = "ich will banana"
print(text3)
print(text3.lower())
print(text3.upper())
print(text4.title())
print(text4.capitalize())
print()

print("__Leerstriche entfernen__")
print(text3.strip()) # Leerstrich rechts + links entfernen
print(text3.rstrip()) # Leerstrich rechts entfernen
print(text3.lstrip()) # Leerstrich links entfernen
print()

print("__Leerstriche entfernen UND Ersetzen__")
print(text3.strip().replace("walking", "hiking"))
print()

print("__Zeile ZERSCHNEIDEN__SPLIT__")
text5 = "i like walking, hinking, reading"
parts = text5.split(" ")
print(parts)
print()

print("__TEILE wieder zusammenfügen__")
print(" ,".join(parts))
print()

print("__FINDEN__")
print(text5.find("walking"))
print(text5.find("hinking"))
print()

print("__Zählen__")
print("abracadabra".count("a"))
print()

print("__Überprüfen__True / False")
print("234567".isdigit())
print("dfghjk".isalpha())
print()

print("__Datum wiedergeben__")
# 31.08.2026 "Year: 2026, month: 08, day: 31"
date = "31.08.2026"

print("__Variante A___")
date_splited = date.split(".")
print(f"Year: {date_splited[2]}, month: {date_splited[1]}, day: {date_splited[0]}")
print()

print("__Variante B__")
day, month, year = date.split(".")
print(f"Year: {year}, month: {month}, day: {day}")