
def camelToSnake():
    camelCase = str(input("Input a camelCase string: "))
    snakeCase = ""
    for x in camelCase:
        if x == x.upper():
            snakeCase += f"_{x.lower()}"
        else:
            snakeCase += x
    print(snakeCase)



if __name__ == "__main__":
    camelToSnake()
