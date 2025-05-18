from salida_py.Python3ParserVisitor import Python3ParserVisitor

# Nodo AST simple para demostración


class FunctionNode:
    def __init__(self, name, params=None, body=None):
        self.name = name
        self.params = params or []
        self.body = body or []

    def to_js(self):
        params = ", ".join(self.params)
        # Suponemos que los elementos de body ya son strings JS
        body_js = "\n".join(self.body)
        return f"function {self.name}({params}) {{\n{body_js}\n}}"


class MiVisitor(Python3ParserVisitor):
    # Override de la regla raíz file_input (débese corresponder con tu gramática)
    def visitFile_input(self, ctx):
        results = []
        # ctx.jugador children incluirá definiciones de funciones u otras declaraciones
        for child in ctx.children:
            res = self.visit(child)
            if res is not None:
                results.append(res)
        return results

    def visitFuncdef(self, ctx):
        # Extrae nombre
        nombre = ctx.NAME().getText()
        # Podrías extraer parámetros y cuerpo aquí, pero devolvemos solo el nombre
        return nombre

    # Para cualquier otro nodo que quieras capturar, crea más overrides


def run_visitor(tree):
    visitor = MiVisitor()
    return visitor.visit(tree)
