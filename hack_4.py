"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    letra = ["f", "b", "n"]
    _str = []

    for txt in result:
        if txt not in letra:
            _str.append(txt)

    result = "".join(_str)
    return result

# Palabras proporcionadas
palabra1 = "fooziman"
palabra2 = "barziman"
palabra3 = "qux"

# Aplicar la función a cada palabra
resultado1 = fn_hack_4(palabra1)
resultado2 = fn_hack_4(palabra2)
resultado3 = fn_hack_4(palabra3)

print("Palabra 1 sin vocales:", resultado1)
print("Palabra 2 sin vocales:", resultado2)
print("Palabra 3 sin vocales:", resultado3)
