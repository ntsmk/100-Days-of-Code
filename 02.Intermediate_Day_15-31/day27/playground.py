def add(*args): # you can actually use anything after *, like *numbers works too.
    # args is shorten of "arguments"
    for n in args:
        print(args[0])
        return sum(args)

a = add(13,10,12,14)
print(a)

