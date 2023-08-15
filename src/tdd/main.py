def simple_i_o(inp: str) -> str: return inp


def simple_add(a: int, b: int) -> int: return a + b


def simple_div(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError
    else:
        return a / b
