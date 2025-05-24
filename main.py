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
    cli.add_argument("-o", "--output", help="Archivo .js de salida (opcional)")
    args = cli.parse_args()

    try:
        tree = parse(args.source)
        run_listener(tree)
        result = run_visitor(tree)
        
        # Mejorar el output
        js_code = result if isinstance(result, str) else str(result)
        print("=== CÓDIGO JAVASCRIPT GENERADO ===")
        print(js_code)
        
        # Guardar en archivo si se especifica
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(js_code)
            print(f"\n✅ Guardado en: {args.output}")
            
    except TranspileSyntaxError as e:
        print(f"❌ Error de sintaxis: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()