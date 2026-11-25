# Practical 3: String indexing, slicing and manipulation

text = "Python Programming"

print("String :", text)
print("Length :", len(text))

# ---------- Indexing ----------
print("\n--- Indexing ---")
print("First character  text[0]  :", text[0])
print("Last character   text[-1] :", text[-1])
print("Eighth character text[7]  :", text[7])

# ---------- Slicing  [start : stop : step] ----------
print("\n--- Slicing ---")
print("text[0:6]   :", text[0:6])
print("text[7:]    :", text[7:])
print("text[:6]    :", text[:6])
print("text[-11:]  :", text[-11:])
print("text[::2]   :", text[::2])
print("text[::-1]  :", text[::-1])

# ---------- Manipulation ----------
print("\n--- Manipulation ---")
print("upper()           :", text.upper())
print("lower()           :", text.lower())
print("swapcase()        :", text.swapcase())
print("replace()         :", text.replace("Programming", "Language"))
print("find('Pro')       :", text.find("Pro"))
print("count('m')        :", text.count("m"))
print("startswith('Py')  :", text.startswith("Py"))
print("strip()           :", "   hello   ".strip())
print("split()           :", text.split())
print("join()            :", "-".join(["2026", "11", "17"]))
print("concatenation     :", "Hello, " + "World")
print("repetition        :", "Hi " * 3)

# ---------- Strings are immutable ----------
try:
    text[0] = "J"
except TypeError as error:
    print("\nError:", error)
