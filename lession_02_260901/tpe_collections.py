print("__LISTEN__")
fruits = ["apple", "banana", "cherry"]
numbers = [1,2,3,4,5,6,7,8,9,10]
mix = ["text", 56, 34.7, True, True]
empty = []

print(type(fruits)) # <class 'list'>
print(type(numbers)) # <class 'list'>
print(type(mix)) # <class 'list'>
print(type(empty)) # <class 'list'>
print()

print("length of numbers: ", len(numbers)) # length of numbers:  10
print("length of fruits: ", len(fruits)) # length of fruits:  3

print(fruits[1]) # banana
print(fruits[::-1]) # ['cherry', 'banana', 'apple']
print(fruits[-1]) # cherry

print("__ERSETZEN__")
fruits[1] = "orange"
print(fruits) # ['apple', 'orange', 'cherry']
print()

print("__HINZUFÜGEN__")
fruits.append("lemon")
print(fruits) # ['apple', 'orange', 'cherry', 'lemon']
print()

print("__EINSETZEN__")
fruits.insert(1, "kiwi")
print(fruits) # ['apple', 'kiwi', 'orange', 'cherry', 'lemon']
print()

print("__ENTFERNEN__")
fruits.remove("kiwi")
print(fruits) # ['apple', 'orange', 'cherry', 'lemon']
print()

print("__LETZTEN ELEMENT ENTFERNEN__")
last = fruits.pop()
print(last)
print(fruits)
print()

print("__SORTIEREN__")
numbers2 = [99, 1, 2, 34, 4, 5, 78, 7, 0, 9, 10]
print(sorted(numbers2)) # [0, 1, 2, 4, 5, 7, 9, 10, 34, 78, 99]
print(sorted(numbers2, reverse=True)) # [99, 78, 34, 10, 9, 7, 5, 4, 2, 1, 0]
print()

print("__DIVERSE METHODEN__")
print(min(numbers2), max(numbers2), sum(numbers2)) # 0 99 249
print("Is 34 in numbers2? -->", 34 in numbers2) # Is 34 in numbers2? --> True

print("__VERÄNDERN der LISTE + SORTIEREN__")
numbers2.sort() # .sort (anders als Fkt sorted()) verändert die Liste numbers grundsätzlich
print(numbers2)
print()

print("__SCHLEIFE__")
for fruit in fruits:
    print("I like ", fruit)
print("______________________")
print()

print("__TUPLEs__")
coordinates1 = (10, 20)
single = (34,)
tuple1 = 1, 2, 3
print(type(coordinates1)) # <class 'tuple'>
print(type(single)) # <class 'tuple'>
print(type(tuple1)) # <class 'tuple'>
print()

print(coordinates1[0]) # 10
print(coordinates1[-1]) # 20
print(len(coordinates1)) # 2
print()

print("__IN Variable PACKEN__")
x, y = coordinates1
print(f"x={x}, y={y}") # x=10, y=20
print("______________________")
print()

print("__DICTIONARIES__")
person = {
    "name": "Sveta",
    "age": 18,
    "city": "Berlin"
}
print(person) # {'name': 'Sveta', 'age': 18, 'city': 'Berlin'}
print("Length of my dictionary is: ", len(person)) # Length of my dictionary is:  3
print(person["name"]) # Sveta

print("__KEY PRÜFEN__")
# print(person["email"]) # ERROR
print(person.get("email")) # kein ERROR --> # None
print(person.get("email", "not found")) # kein NONE, sondern nur die DEFAULT-Wert, den wir selbst reingeschrieben haben
print()

print("__KEY HINZUFÜGEN__")
person["email"] = "dfghjk@dfghj.com"
print(person) # {'name': 'Sveta', 'age': 18, 'city': 'Berlin', 'email': 'dfghjk@dfghj.com'}
print()

print("__KEY ÄNDERN__")
person["age"] = 32
print(person) # {'name': 'Sveta', 'age': 32, 'city': 'Berlin', 'email': 'dfghjk@dfghj.com'}
print()

print("__PAAR ENTFERNEN__")
del person["city"]
print(person) # {'name': 'Sveta', 'age': 32, 'email': 'dfghjk@dfghj.com'}
print()

print("__PRÜFEN__")
print("name" in person)
print("phone" in person)
print()

print("__DIVERSE Typen der DICTIONARIES__")
dict_any = {
    1: "paz", # Keys sollen unique sein
    "two": 2,
    (0,1): "paz", # Values können sich wiederholen
}
dict_any[(True, False)] = True
print(dict_any) # {1: 'paz', 'two': 2, (0, 1): 'paz', (True, False): True}
dict_any[(False, True)] = "FGHJK" # (False, True) = (0,1) => gleich wie in Zeile 127, also Kein KEY hinzugefügt oder verändert, ABER Value verändert!!!
print(dict_any) # {1: 'paz', 'two': 2, (0, 1): FGHJK, (True, False): True}
print()

print("__ÄNDERN des KEYs__")
print((True, False) == (1,0)) # True
print(dict_any) # {1: 'paz', 'two': 2, (0, 1): 'FGHJK', (True, False): True}

print("__DIVERSES aus der Liste AUSGEBEN__")
prices = {
    "apple": 1.5,
    "banana": 2.0,
    "cherry": 3.0,
}
for product in prices:
    print("Product: ", product)
# Product:  apple
# Product:  banana
# Product:  cherry

for product, price in prices.items():
    print(f"Product: {product}, price: {price}$")
# Product: apple, price: 1.5$
# Product: banana, price: 2.0$
# Product: cherry, price: 3.0$
print()

print(list(prices.keys())) # ['apple', 'banana', 'cherry']
print(list(prices.values())) # [1.5, 2.0, 3.0]
print(sum(prices.values())) # 6.5
print("______________________")
print()

print("__SET__")
# Mehrzahl von Diverses, Keine DUPLIKATE möglich
colors = {"red", "green", "blue"}
print(colors) # {'blue', 'green', 'red'}
colors.discard("red")
print(colors) # {'green', 'blue'}
print("red" in colors) #False
print("green" in colors) # True
print()

numbers_set = {1, 2, 1, 4, 6, 6, 5, 8, 1, 9, 10} # sortiert und gibt nur die Uniques raus
print(numbers_set) # {1, 2, 4, 5, 6, 8, 9, 10}
print()

print("__TYP SET ZUWEISEN__")
empty_dict = {} # <class 'dict'>
print(type(empty_dict))
empty_set = set() # macht einen Set daraus
print(type(empty_set)) # <class 'set'>
print()

print("__IM SET HINZUFÜGEN__")
colors.add("yellow")
print(colors) # {'green', 'yellow', 'blue'}
print()

print("__WIEDERHOLUNG__")
names = ["Ivan", "Jose", "Jose", "Nina", "Ivan"] # eine LISTE erstellen
print(names)

unique_names = set(names) # in SET UMWANDELN = alle Duplikate entfernen
print(unique_names)
print()

print("__SETs ZUSAMMENSETZEN__")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 | set2) # {1, 2, 3, 4, 5, 6} # zeigt UNIQUES in einem Set zusammengesetzt
print(set1 & set2) # {3, 4} # zeigt nur DUPLIKATE
print(set1 - set2) # {1, 2} # zeigt vom ERSTEN Set nur UNIQUE
print(set2 - set1) # {5, 6} # zeigt vom ERSTEN Set nur UNIQUE
print(set1 ^ set2) # {1, 2, 5, 6} # zeigt OHNE DUPLIKATE in einem Set zusammengesetzt
set3 = {5, 8, 4, 1}
set4 = {10, 4, 7, 6, 5}
print(set3 & set4) # {4, 5}
print(set3 ^ set4) # {1, 6, 7, 8, 10}