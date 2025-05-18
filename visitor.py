from salida_py.Python3ParserVisitor import Python3ParserVisitor

# * Extiende Python3ParserVisitor y sobreescribe visitFuncdef, regresando valores o transformándolos.
# * Visitor es mejor para construir estructuras de datos (AST intermedio)
class MiVisitor(Python3ParserVisitor):
    def visitFuncdef(self, ctx):
        nombre = ctx.NAME().getText()
        # aquí podrías construir y devolver un nodo AST, p.ej.:
        # return FunctionNode(name=nombre, body=...)
        return nombre

def run_visitor(tree):
    visitor = MiVisitor()
    return visitor.visit(tree)