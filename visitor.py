from salida_py.Python3ParserVisitor import Python3ParserVisitor

class PythonToJSVisitor(Python3ParserVisitor):
    
    def __init__(self):
        self.js_lines = []
        self.indent_level = 0
    
    def get_indent(self):
        return "  " * self.indent_level
    
    def visitFile_input(self, ctx):
        results = []
        for child in ctx.children:
            if child.getText() != '<EOF>':  # Ignora EOF
                result = self.visit(child)
                if result:
                    results.append(result)
        return "\n".join(results)
    
    def visitFuncdef(self, ctx):
        # def suma(a, b): → function suma(a, b) {
        name = ctx.NAME().getText()
        
        # Extraer parámetros
        params = []
        if ctx.parameters().typedargslist():
            for param in ctx.parameters().typedargslist().NAME():
                params.append(param.getText())
        
        params_str = ", ".join(params)
        
        # Procesar cuerpo
        body = self.visit(ctx.suite())
        
        return f"function {name}({params_str}) {{\n{body}\n}}"
    
    def visitSuite(self, ctx):
        # Procesar todas las declaraciones del cuerpo
        statements = []
        for child in ctx.children:
            result = self.visit(child)
            if result and result.strip():
                statements.append(f"  {result}")  # Indentación
        return "\n".join(statements)
    
    def visitReturn_stmt(self, ctx):
        if ctx.testlist():
            expr = self.visit(ctx.testlist())
            return f"return {expr};"
        return "return;"
    
    def visitTestlist(self, ctx):
        # Procesar lista de expresiones
        tests = []
        for test in ctx.test():
            tests.append(self.visit(test))
        return ", ".join(tests)
    
    def visitTest(self, ctx):
        return self.visit(ctx.or_test())
    
    def visitOr_test(self, ctx):
        if len(ctx.and_test()) == 1:
            return self.visit(ctx.and_test(0))
        
        # Manejar OR múltiples: a or b or c
        result = self.visit(ctx.and_test(0))
        for i in range(1, len(ctx.and_test())):
            right = self.visit(ctx.and_test(i))
            result = f"({result} || {right})"
        return result
    
    def visitAnd_test(self, ctx):
        if len(ctx.not_test()) == 1:
            return self.visit(ctx.not_test(0))
        
        # Manejar AND múltiples
        result = self.visit(ctx.not_test(0))
        for i in range(1, len(ctx.not_test())):
            right = self.visit(ctx.not_test(i))
            result = f"({result} && {right})"
        return result
    
    def visitNot_test(self, ctx):
        if ctx.not_test():  # not not_test
            inner = self.visit(ctx.not_test())
            return f"(!{inner})"
        else:  # comparison
            return self.visit(ctx.comparison())
    
    def visitComparison(self, ctx):
        result = self.visit(ctx.expr(0))
        
        for i in range(len(ctx.comp_op())):
            op = self.visit(ctx.comp_op(i))
            right = self.visit(ctx.expr(i + 1))
            result = f"({result} {op} {right})"
        
        return result
    
    def visitComp_op(self, ctx):
        return ctx.getText()  # <, >, ==, etc. son iguales
    
    def visitExpr(self, ctx):
        result = self.visit(ctx.term(0))
        
        for i in range(1, len(ctx.term())):
            # El operador está en posición impar
            op_node = ctx.getChild(2*i - 1)
            op = op_node.getText()
            right = self.visit(ctx.term(i))
            result = f"({result} {op} {right})"
        
        return result
    
    def visitTerm(self, ctx):
        result = self.visit(ctx.factor(0))
        
        for i in range(1, len(ctx.factor())):
            op_node = ctx.getChild(2*i - 1)
            op = op_node.getText()
            right = self.visit(ctx.factor(i))
            result = f"({result} {op} {right})"
        
        return result
    
    def visitFactor(self, ctx):
        if ctx.factor():  # (+|-) factor
            op = ctx.getChild(0).getText()
            inner = self.visit(ctx.factor())
            return f"({op}{inner})"
        else:  # atom
            return self.visit(ctx.atom())
    
    def visitAtom(self, ctx):
        if ctx.NAME():
            return ctx.NAME().getText()
        elif ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.STRING():
            return ctx.STRING().getText()
        elif ctx.test():  # (test)
            return f"({self.visit(ctx.test())})"
        elif hasattr(ctx, 'list_literal') and ctx.list_literal():
            return self.visit(ctx.list_literal())
        elif hasattr(ctx, 'dict_literal') and ctx.dict_literal():
            return self.visit(ctx.dict_literal())
        
        return "/* ATOM NO RECONOCIDO */"

    def visitIf_stmt(self, ctx):
        """Maneja if/elif/else statements - VERSIÓN CORREGIDA"""
        result = []
        
        # 1. IF principal
        condition = self.visit(ctx.test(0))
        if_body = self.visit(ctx.suite(0))
        result.append(f"if ({condition}) {{")
        result.append(if_body)
        result.append("}")
        
        # 2. Procesar ELIFs y ELSE de forma más segura
        test_count = len(ctx.test())
        suite_count = len(ctx.suite())
        
        current_test_index = 1
        current_suite_index = 1
        
        # Procesar todos los ELIFs
        while current_test_index < test_count:
            elif_condition = self.visit(ctx.test(current_test_index))
            elif_body = self.visit(ctx.suite(current_suite_index))
            result.append(f"else if ({elif_condition}) {{")
            result.append(elif_body)
            result.append("}")
            
            current_test_index += 1
            current_suite_index += 1
        
        # 3. Verificar si hay ELSE final (más suites que tests)
        if current_suite_index < suite_count:
            # Hay un else final
            else_suite = ctx.suite(current_suite_index)
            if else_suite is not None:  # Verificación de seguridad
                else_body = self.visit(else_suite)
                result.append("else {")
                result.append(else_body)
                result.append("}")
        
        return "\n".join(result)

    def visitSimple_stmt(self, ctx):
        """Maneja declaraciones simples"""
        return self.visit(ctx.small_stmt())

    def visitSmall_stmt(self, ctx):
        """Maneja small_stmt"""
        if ctx.expr_stmt():
            return self.visit(ctx.expr_stmt())
        elif ctx.flow_stmt():
            return self.visit(ctx.flow_stmt())
        return ""

    def visitExpr_stmt(self, ctx):
        """Maneja expresiones y asignaciones - CORREGIDO"""
        # Verificar si es asignación comparando el número de hijos
        children_count = len(ctx.children)
        
        if children_count == 1:
            # Solo expresión (no asignación)
            # ctx tiene un solo hijo: testlist
            return self.visit(ctx.testlist())  # ✅ SIN ARGUMENTOS
        
        elif children_count == 3:
            # Asignación: testlist '=' expr_stmt
            # ctx.children[0] = testlist (lado izquierdo)
            # ctx.children[1] = '=' (operador)
            # ctx.children[2] = expr_stmt (lado derecho)
            
            left = self.visit(ctx.testlist())  # ✅ SIN ARGUMENTOS
            right = self.visit(ctx.expr_stmt())  # Recursivo para el lado derecho
            return f"let {left} = {right};"
        
        else:
            # Caso no esperado
            return f"/* EXPR_STMT NO RECONOCIDO: {ctx.getText()} */"

    def visitFlow_stmt(self, ctx):
        """Maneja declaraciones de flujo como return"""
        return self.visit(ctx.return_stmt())

    def visitStatement(self, ctx):
        """Maneja statements compuestos"""
        return self.visit(ctx.compound_stmt())

    def visitCompound_stmt(self, ctx):
        """Maneja declaraciones compuestas (if, def, etc.)"""
        if ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        elif ctx.funcdef():
            return self.visit(ctx.funcdef())
        return ""

    # Métodos adicionales para listas y diccionarios (si los agregaste a la gramática)
    def visitList_literal(self, ctx):
        """Maneja listas [1, 2, 3]"""
        if ctx.testlist():
            elements = self.visit(ctx.testlist())
            return f"[{elements}]"
        return "[]"

    def visitDict_literal(self, ctx):
        """Maneja diccionarios {'key': 'value'}"""
        if hasattr(ctx, 'dict_pairs') and ctx.dict_pairs():
            pairs = self.visit(ctx.dict_pairs())
            return f"{{{pairs}}}"
        return "{}"

    def visitDict_pairs(self, ctx):
        """Maneja pares clave:valor de diccionarios"""
        pairs = []
        if hasattr(ctx, 'dict_pair'):
            for pair in ctx.dict_pair():
                pairs.append(self.visit(pair))
        return ", ".join(pairs)

    def visitDict_pair(self, ctx):
        """Maneja un par clave:valor"""
        key = self.visit(ctx.test(0))
        value = self.visit(ctx.test(1))
        return f"{key}: {value}"


def run_visitor(tree):
    visitor = PythonToJSVisitor()
    return visitor.visit(tree)