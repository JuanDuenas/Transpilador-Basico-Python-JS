import re  

def transpilar_python_a_js(codigo_python):  
    # Convertir def a function  
    codigo_js = re.sub(r'def\s+(\w+)\((.*?)\):', r'function \1(\2) {', codigo_python)  

    # Convertir print a console.log  
    codigo_js = re.sub(r'print\((.*?)\)', r'console.log(\1);', codigo_js)  

    # Agregar llaves de cierre  y quita los espacios en blanco
    codigo_js = codigo_js.strip() + '\n}'

    return codigo_js  

# Ejemplo de entrada  
codigo_python = """  
def saludar(nombre):  
    print("Hola, " + nombre)  
"""  

# Convertir  
codigo_js = transpilar_python_a_js(codigo_python)  
print(codigo_js)  