import sys

def CharCounter():
   # [print(arg) for arg in sys.argv]
 
    string = ""

    for num in range(1,len(sys.argv)):
        string+= str(sys.argv[num])



    alphabet = 'abcdefghijklmnñopqrstuvwxyz'
    dictionarie = {}
    counter=0

    for character in string:
        if character in alphabet:
            if character in dictionarie:
                counter = dictionarie[character]
                counter+=1
                dictionarie[character] = counter
            else:
                counter =1
                dictionarie[character] = counter

    return dictionarie
    

result = CharCounter()

print("number of appeareances per character:" )   
[print(key +"\t"+  str(result[key])) for key in result ]


