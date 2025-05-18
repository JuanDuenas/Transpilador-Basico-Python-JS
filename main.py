from antlr4 import FileStream, CommonTokenStream
from salida_py.Python3Lexer import Python3Lexer
from salida_py.Python3Parser import Python3Parser
from errors import attach_error_listener
from listener import run_listener
from visitor import run_visitor

def parse(source_file):
    input_stream = FileStream(source_file, encoding='utf-8')
    lexer = Python3Lexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = Python3Parser(tokens)

    # Adjuntar manejo de errores
    attach_error_listener(parser)

    # Parsear desde la regla raíz
    tree = parser.file_input()
    return tree

if __name__ == "__main__":
    tree = parse("ejemplo.py")
    # Opción A: usar listener
    run_listener(tree)
    # Opción B: usar visitor
    result = run_visitor(tree)
    print("Visitor devolvió:", result)
