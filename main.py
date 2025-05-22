from antlr4 import FileStream, CommonTokenStream
from salida_py.Python3Lexer import Python3Lexer
from salida_py.Python3Parser import Python3Parser
from errors import attach_error_listener, TranspileSyntaxError
from listener import run_listener
from visitor import run_visitor
import argparse


def parse(source_file):
    input_stream = FileStream(source_file, encoding='utf-8')
    lexer = Python3Lexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = Python3Parser(tokens)

    # Adjuntar manejo de errores
    attach_error_listener(parser)

    # Retorna el parseo desde la regla raíz
    return parser.file_input()


def main():
    cli = argparse.ArgumentParser(description="Transpiler Python → JS")
    cli.add_argument("source", help="Archivo .py de entrada")
    args = cli.parse_args()

    try:
        tree = parse(args.source)
        run_listener(tree)
        result = run_visitor(tree)
        print("Visitor devolvió:", result[0])
    except TranspileSyntaxError as e:
        print(f"Error de sintaxis: {e}")
        # sys.exit(1)  # si quieres terminar con código de error


if __name__ == "__main__":
    main()
