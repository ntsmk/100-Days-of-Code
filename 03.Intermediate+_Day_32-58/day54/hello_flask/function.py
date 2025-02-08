def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    def one():
        print("one")

    def two():
        print("two")

    return nested_function, one, two


inner_function, a, b = outer_function()
inner_function(), b()