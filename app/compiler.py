def compile_input(text: str, callables: dict = {}):
    bytecode = compile(text, filename = './.err', mode = 'eval')
    callable = lambda n: eval(bytecode, callables, {'n': n})

    def func(n: int) -> int: return callable(n)

    return func