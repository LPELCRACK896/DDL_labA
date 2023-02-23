from regex_to_posfix import infix_to_posfix

def main():
    regex = input("Ingresa expresion regex: ")

    posfix, err, alphabet = infix_to_posfix(regex)

    if(err):
        print(err.name)
        print(err.details)
    else:
        print(f"Posfix: {posfix}")

if __name__ == "__main__":
    main()