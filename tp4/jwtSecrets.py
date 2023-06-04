import jwt
import json

#string = '{ "username":"Franco", "admin":"True"}'


#json = json.loads(string)

#bruh 
encoded = jwt.encode({ "username":"Franco", "admin":"True"},"secret",algorithm="HS256")

print(f"{str(encoded)}")