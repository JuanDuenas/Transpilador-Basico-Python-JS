import ast

code = """
def greet(name):
    print(f"Hello, {name}!")
"""

tree = ast.parse(code)
print(ast.dump(tree, indent=4))