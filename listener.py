from antlr4 import ParseTreeWalker
from salida_py.Python3ParserListener import Python3ParserListener

# * Extiende Python3ParserListener y sobreescribe métodos enterFuncdef, exitIf_stmt, etc.
# * Listener es mejor para acciones secundarias (logging, validaciones, etc.)
class MiListener(Python3ParserListener):
    def enterFuncdef(self, ctx):
        print("Encontrada función:", ctx.NAME().getText())

def run_listener(tree):
    walker = ParseTreeWalker()
    walker.walk(MiListener(), tree)