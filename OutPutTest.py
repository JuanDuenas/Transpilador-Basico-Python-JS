import re  

def transpilar_python_a_js(codigo_python):  
    # Convertir def a function  
    codigo_js = re.sub(r'def\s+(\w+)\((.*?)\):', r'function \1(\2) {', codigo_python)  

    # Convertir print a console.log  
    codigo_js = re.sub(r'print\((.*?)\)', r'console.log(\1);', codigo_js)  

    # Agregar llaves de cierre  
    codigo_js = re.sub(r'\n\s{4}', '\n}', codigo_js, count=1)  # Cierre básico  

    return codigo_js  

# Ejemplo de entrada  
codigo_python = """  
def saludar(nombre):  
    print("Hola, " + nombre)  
"""  

# Convertir  
codigo_js = transpilar_python_a_js(codigo_python)  
print(codigo_js)  