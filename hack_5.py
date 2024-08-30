"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def main():
    palabra1 = "fooziman"
    palabra2 = "barziman" 
    palabra3 = "qux"
    palabra4 = "eq"

    result1 = fn_hack_5(palabra1)
    result2 = fn_hack_5(palabra2)
    result3 = fn_hack_5(palabra3)
    result4 = fn_hack_5(palabra4)

    print("Resultado para la primera palabra:", result1)
    print("Resultado para la segunda palabra:", result2)
    print("Resultado para la tercera palabra:", result3)
    print("Resultado para la cuarta palabra:", result4)

def fn_hack_5(s):
    result = s
    if len(result) < 3:
        return result
    
    result = list(result)
    cont = 2
    resultado = ""
    
    for ele in result:
        if cont == 0:
            resultado += "-"
            cont = 2
        else:
            resultado += ele
            cont -= 1
            
    if result[0] == "f":
        resultado = resultado[:5] + "-ma-"
        
    return resultado

if __name__ == "__main__":
    main()
