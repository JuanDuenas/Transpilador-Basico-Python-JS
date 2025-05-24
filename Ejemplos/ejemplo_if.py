def test_conditions(x, y):
    if x > y:
        return "x es mayor"
    elif x < y:
        return "y es mayor"
    else:
        return "son iguales"

def simple_if(a):
    if a > 0:
        return "positivo"
    return "no positivo"