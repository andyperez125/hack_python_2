"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(s):
    result = s
    vowels = ["a", "e", "i", "o", "u"]
    _str = []

    for txt in result:
        if txt not in vowels:
            _str.append(txt)

    result = "".join(_str)
    return result

# Palabras proporcionadas
palabra1 = "fooziman"
palabra2 = "barziman"
palabra3 = "qux"

# Aplicar la función a cada palabra
resultado1 = fn_hack_2(palabra1)
resultado2 = fn_hack_2(palabra2)
resultado3 = fn_hack_2(palabra3)

print("Palabra 1 sin vocales:", resultado1)
print("Palabra 2 sin vocales:", resultado2)
print("Palabra 3 sin vocales:", resultado3)
