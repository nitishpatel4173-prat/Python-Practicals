# Practical 2: Type casting and data types in Python

# ---------- Part A: Built-in data types ----------
age = 21                               # int
price = 99.75                          # float
name = "Aarav"                         # str
is_student = True                      # bool
number = 3 + 4j                        # complex
fruits = ["apple", "banana"]           # list
point = (10, 20)                       # tuple
marks = {"maths": 90, "python": 95}    # dict
unique_ids = {1, 2, 2, 3}              # set (duplicates are removed)
nothing = None                         # NoneType

values = [age, price, name, is_student, number,
          fruits, point, marks, unique_ids, nothing]

print("--- Data types ---")
for item in values:
    print(f"{str(item):<35} -> {type(item).__name__}")

# ---------- Part B: Implicit type casting ----------
print("\n--- Implicit type casting ---")
whole = 5
decimal = 2.5
result = whole + decimal          # int is automatically promoted to float
print(f"{whole} + {decimal} = {result} -> {type(result).__name__}")

# ---------- Part C: Explicit type casting ----------
print("\n--- Explicit type casting ---")
print("int('123') + 7      =", int("123") + 7)
print("int(9.99)           =", int(9.99))
print("float('3.14') * 2   =", float("3.14") * 2)
print("str(2026) + ' year' =", str(2026) + " year")
print("bool(0), bool('Hi') =", bool(0), bool("Hi"))
print("list('abc')         =", list("abc"))
print("tuple([1, 2, 3])    =", tuple([1, 2, 3]))
print("set([1, 1, 2, 3])   =", set([1, 1, 2, 3]))
print("ord('A'), chr(66)   =", ord("A"), chr(66))
print("int('1010', 2)      =", int("1010", 2))

# ---------- Part D: Invalid casting is handled with try/except ----------
try:
    int("abc")
except ValueError as error:
    print("\nCasting error:", error)
