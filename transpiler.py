from antlr4 import FileStream, CommonTokenStream
from salida_py.Python3Lexer import Python3Lexer
from salida_py.Python3Parser import Python3Parser

# 1. Leer archivo fuente
input_stream = FileStream("ejemplo.py", encoding='utf-8')

# 2. Instanciar lexer y token stream
lexer = Python3Lexer(input_stream)
tokens = CommonTokenStream(lexer)

# 3. Crear parser y parsear la regla raíz (por ejemplo, file_input)
parser = Python3Parser(tokens)
# * Cada llamada a una regla (aquí file_input()) devuelve un objeto ParserRuleContext que es la raíz del parse tree
# * inicia parseo desde file_input 
tree = parser.file_input()
