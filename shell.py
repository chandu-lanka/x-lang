import x_lang

while True:
    text = input("x-lang > ")
    result, error = x_lang.run(text)

    if error:
        print(error.printError())
    else:
        print(result)