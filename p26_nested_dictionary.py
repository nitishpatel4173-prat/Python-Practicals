# Practical 26: Nested dictionary - retrieve city and zip code

person = {
    "name": "Riya Sharma",
    "age": 22,
    "address": {
        "city": "Vadodara",
        "state": "Gujarat",
        "zip_code": "391760"
    }
}

# Key access: dictionary[outer_key][inner_key]
print("Name     :", person["name"])
print("City     :", person["address"]["city"])
print("Zip code :", person["address"]["zip_code"])

# get() is safer: it returns a default value if the key is missing
print("Country  :", person["address"].get("country", "Not available"))

# Looping through the inner dictionary
print("\nComplete address:")
for key, value in person["address"].items():
    print(f"  {key} -> {value}")
