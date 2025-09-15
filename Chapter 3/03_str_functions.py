name = "dhruvtyagi"

print(len(name))

print(name.endswith("agi"))  # Output: True
print(name.startswith("dhr"))  # Output: True

count = name.count("r") 
print(count)  # Output: 1

capitalized_string = name.capitalize() 
print(capitalized_string)  # Output: "Dhruvtyagi"

index = name.find("vt")
print(index)  # Output: 4

replaced_string = name.replace("t", "l") 
print(replaced_string)  # Output: "dhruvlyagi"