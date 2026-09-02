print("__SCHLEIFEN__")
print("__FOR-IN-Lister__")
fruits2 = ["apple", "banana", "cherry"]
for fruit in fruits2:
    print("I like ", fruit) # gibt jeden Element in einem Satz jeweils pro Zeile aus

for letter in "banana":
    print(letter) # gibt jeden Buchstaben jeweils pro Zeile aus
print()

print("__FOR-IN-RANGE__")
for i in range(5): # startet bei 0 bis 5
    print(i)
print()

for i in range(1, 5): # Bereich von 1 bis 5
    print(i)
print()

print("__WHILE__")
count = 1
while count < 5: # Zum Zähler hinzuzählen + ausgeben
    print(count)
    count += 1 # vorwärts
print()

n = 5
while n > 0:
    print(n)
    n -= 1 # rückwärts
print()

cash = 0
while cash < 100:
    cash += 10
    print("My cash --> ", cash)
print()

print("__ABBRECHEN bei__")
for num in [2, 5, 6, 9, 0, 3]:
    if num == 9:
        print("I found 9")
        break
    print(num)
print()

print("__FORTFÜHREN__")
for number in range(1, 11):
    if number % 2 == 0:
        continue
    print("Ungerade Zahlen:", number)

for number in range(1, 21):
    if number % 3 != 0:
        continue
    print("Durch 3 Teilbar: ", number)
print()

print("__FUNKTION__")
def add(a, b):
    return a + b
res = add(1, 2) # V1
print(res)
print("Sum is -->", add(1, 2)) #V2
print()

def is_even(num):
    return num % 2 == 0

print(is_even(2)) # True
print(is_even(5)) # False
print()

def min_max(numbers):
    return min(numbers), max(numbers)

print(min_max([4, 6, 8, 2, 9])) # V1: gleich ausgeben
low, high = min_max([4, 6, 8, 2, 9]) # V2: in eine Var rein,
print(f"low = {low}, high = {high}") # und dann ausgeben
print()

def summa_list(numbers):
    summa = 0
    for n in numbers:
        summa += n
    return summa
print(summa_list([4, 6, 8, 2, 9]))
print()

print("__DURCHSCHNITT__")
def avg(numbers):
    return summa_list(numbers) / len(numbers)
print(avg([4, 6, 8, 2, 9]))

print("__MENGE__")
my_list = ["dog", "cat", "mouse", "rabbit", "horse", "house", "field"]
def count_words_longer_three_chars(words):
    counter = 0
    for word in words:
        if len(word) > 3:
            counter += 1
    return counter
print("Count is -->", count_words_longer_three_chars(my_list))
print()

print("__MENGE der LAUTE__")
def amount_of_vowels(text):
    counter = 0
    for char in text.lower():
        if char in "aeiou":
            counter += 1
    return counter
print("Count is -->", amount_of_vowels("AbracadAbra nicht mIt vielen Buchstaben"))
print(amount_of_vowels("Python")) # weil y nicht in der Liste von
print()