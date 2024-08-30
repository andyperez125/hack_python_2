"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""

def fn_hack_1(s):
    result = s
    _ls = []

    txt_ls = [result[i:i+3] for i in range(0, len(result), 3)]

    for txt in txt_ls:
        if len(txt) % 2 != 0:
            content = f"{txt[0]}{txt[1].upper()}{txt[2]}"
            _ls.append(content)
        else:
            _ls.append(txt)
    
    result = "".join(_ls)
    return result

# Ejemplo de uso
palabra1 = "fooziman"
palabra2 = "qux"
palabra3 = "eq"

resultado1 = fn_hack_1(palabra1)
resultado2 = fn_hack_1(palabra2)
resultado3 = fn_hack_1(palabra3)

print("Palabra 1 modificada:", resultado1)
print("Palabra 2 modificada:", resultado2)
print("Palabra 3 modificada:", resultado3)


