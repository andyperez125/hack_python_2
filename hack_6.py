"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    
    
    # se asignas los valores que se intercambiarna las letras 
    mapping = {
        "a": "1",
        "b": "-",
        "c": "3",
        "d": "-",
        "e": "5"
    }
    
    # Si la lista no tiene nada osea esta vacia devueleve  ["0"]
    if not s:
        return ["0"]
    
    # se realiza la convecion de los caracteres 
    result = [mapping.get(char, char) for char in s]
    return result


print(fn_hack_6(["a","b","c","d","e"]))  # restultado de la Salida: ["1","-","3","-","5"]
print(fn_hack_6([]))  #  resultado de la otra salida Salida: ["0"]

