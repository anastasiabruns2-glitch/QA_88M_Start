print("__FEHLERMELDUNGEN__")
# res = 10/0
# print(res)
# print("Hi") # wird nicht gedruckt, weil bei res ein ERROR entsteht

try:
    res = 10/0
    print("Res is", res)
except ZeroDivisionError:
    print("Division by zero")

print("Hi") # durch try wird das Programm trotz des ERRORs weiter ausgeführt
print()

print("__AUS STRING INT MACHEN__")
input_str = "avf"
input_str1 = "67"
# number = int(input_str) # ohne try ERROR

try:
    number = int(input_str1)
    print(number)
except ValueError:
    print("Only integers are allowed")
print()

def divide(a, b):
    try:
        return print(a / b)
    except ZeroDivisionError:
        print("Division by zero")
    except TypeError:
        print("Type error")

divide(1, 2) # 0.5
divide(0, 2) # 0.0
divide(1, 0) # Division by zero
divide(1, "0") # Type error
print()

try:
    numbers = [7, 4, 3]
    print(numbers[3])
except IndexError as e:
    print(e)
    print(type(e).__name__)

print("__TRY-EXCEPT(A, B)__")
def divide2(a, b):
    try:
        return print(a / b)
    except (ZeroDivisionError, TypeError) as e: # V1
        print(e)

divide2(1, "python")
divide2(1, "0")
divide2(1, 0)
print()

print("__TRY-EXCEPT-EXCEPT-EXCEPT__")
try:
    data = {
        "name": "John",
        "age": 25,
    }
    print(data["email"])
except KeyError:           #das was als erstes erwartet wird
    print("Key error")
except TypeError:
    print("Type error")
except Exception:          # für sonstige Fehler
    print("Unexcepted error")
print()

print("__TRY-EXCEPT-ELSE__")
try:
    number = int("4456")
except ValueError:              # wenn es nicht geht
    print("Only integers are allowed")
else:                           # wenn es klappt, dann
    print("Success, it is a number: ", number)
print()

print("__TRY-EXCEPT-FINALLY__")
try:                            # versuchen
    print("Try part")
    result = 10 / 0
except ZeroDivisionError:       # wenn gescheitert
    print("Division by zero")
finally:                        # unabhängig davon
    print("Always finished")
print()

print("__TRY-EXCEPT-ELSE-FINALLY__")
def type_age(age):
    try:
        age = int(age)
    except (TypeError, ValueError) as e:
        print("Type error or Value error")
    else:
        print("Success, it is a number: ", age)
    finally:
        print("Type age")
type_age(18) # Success, it is a number:  18 # Type age
type_age("25") # Success, it is a number:  25 # Type age
type_age("achtzehn") # Type error or Value error  # Type age
type_age("17b") # Type error or Value error  # Type age
