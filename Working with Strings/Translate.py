name = input ("Enter your name: ")
name1 = name.lower()

secret_name = str.maketrans(
    {"a": "ABD" , "m": "MNO" , "u": "UVW" , 
     "d": "DEF" , "m": "MIJ" , "o": "OOO", 
     "r": "RST" , "h": "HIJ", "b": "BBC"
     }) 


print("Your secret name :",name1.translate(secret_name))
print("Your real name :",name)