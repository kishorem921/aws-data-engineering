Dialogue = "En vazhi, thani vazhi"

print(Dialogue.upper()) #ella characters um capital letters ah maathuthu

print(Dialogue.lower()) # #ella characters um small letters ah maathuthu

print(Dialogue.title()) #ella words layum irukura first letter ah capital letters ah maathuthu

print(Dialogue.capitalize()) #first word oda first letter ah capital letters ah maathuthu

print(Dialogue.replace("vazhi", "path")) #word ah replace panrathu

print(Dialogue.split()) #string ah list ah maathuthu

a = Dialogue.split() #string ah list ah maathi variable la assign panrathu

print("#".join(a)) #join function ah use panni list la irukura words ah oru string ah maathuthu and we can use special characters to separate

print(Dialogue.find("vazhi")) #words oda index ah return panrathu

print(Dialogue.count("vazhi")) #words oda count ah return panrathu

Dialogue = " &    En vazhi, thani vazhi  &    "
print(Dialogue.strip("&")) #leading and trailing whitespace ah remove panrathu

print(Dialogue.startswith("En")) #string la entha word start aaguthu nu check panrathu, bool la result varum(true/false)

print(Dialogue.endswith("vazhi")) #string la entha word end aaguthu nu check panrathu, bool la result varum(true/false)