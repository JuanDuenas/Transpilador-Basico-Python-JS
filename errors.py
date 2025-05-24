from antlr4.error.ErrorListener import ErrorListener


# * Para convertir errores en excepciones claras indicando ubicación exacta
class TranspileSyntaxError(SyntaxError):
    pass


class MiErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, col, msg, e):
        raise TranspileSyntaxError(f"Error en línea {line}:{col} → {msg}")


def attach_error_listener(parser):
    parser.removeErrorListeners()
    parser.addErrorListener(MiErrorListener())