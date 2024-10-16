
def camelToSnake():
    camelCase = str(input("Input a camelCase string: "))
    snakeCase = ""
    for index, x in enumerate(camelCase):
        if x == x.upper() and index != 0:
            snakeCase += f"_{x.lower()}"
        else:
            snakeCase += x
    print(snakeCase)



if __name__ == "__main__":
    camelToSnake()
