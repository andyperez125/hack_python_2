"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""

"""  
def fn_hack_3(s):
    result = s
    vowels = ["a", "e", "i", "o", "u"]
    _str = []

    for txt in result:
        if txt == 'a':
            _str.append('@')
        elif txt == 'e':
            _str.append('3')
        elif txt == 'i':
            _str.append('¡')
        elif txt == 'o':
            _str.append('0')
        elif txt == 'u':
            _str.append('v')
        elif txt == 'x':
            _str.append('X')
        elif txt == 'q':
            _str.append('Q')
        else:
            _str.append(txt)

    result = "".join(_str)
    return result

# Palabras proporcionadas
palabra1 = "fooziman"
palabra2 = "barziman"
palabra3 = "3q"
palabra4 = "qu"
palabra5 = "qux"

# Aplicar la función a cada palabra
resultado1 = fn_hack_3(palabra1)
resultado2 = fn_hack_3(palabra2)
resultado3 = fn_hack_3(palabra3)
resultado4 = fn_hack_3(palabra4)
resultado5 = fn_hack_3(palabra5)

print("Palabra 1 modificada:", resultado1)
print("Palabra 2 modificada:", resultado2)
print("Palabra 3 modificada:", resultado3)
print("Palabra 4 modificada:", resultado4)
print("Palabra 5 modificada:", resultado5)



"""
def fn_hack_3(s):
    result = s
    vowels = ["a", "e", "i", "o", "u"]
    _str = []

    for txt in result:
        if txt == 'a':
            _str.append('@')
        elif txt == 'e':
            _str.append('3')
        elif txt == 'i':
            _str.append('¡')
        elif txt == 'o':
            _str.append('0')
        elif txt == 'u':
            _str.append('v')
        elif txt == 'x':
            _str.append('X')
        elif txt == 'q':
            _str.append('Q')
        elif txt == 'f':
            _str.append('F')
        elif txt == 'b':
            _str.append('B')
        else:
            _str.append(txt)

    result = "".join(_str)
    return result

# Palabras proporcionadas
palabra1 = "fooziman"
palabra2 = "barziman"
palabra3 = "3q"
palabra4 = "qu"
palabra5 = "qux"

# Aplicar la función a cada palabra
resultado1 = fn_hack_3(palabra1)
resultado2 = fn_hack_3(palabra2)
resultado3 = fn_hack_3(palabra3)
resultado4 = fn_hack_3(palabra4)
resultado5 = fn_hack_3(palabra5)

print("Palabra 1 modificada:", resultado1)
print("Palabra 2 modificada:", resultado2)
print("Palabra 3 modificada:", resultado3)
print("Palabra 4 modificada:", resultado4)
print("Palabra 5 modificada:", resultado5)
