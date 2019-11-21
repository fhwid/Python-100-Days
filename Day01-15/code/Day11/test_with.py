def main():
    try:
        with open('致橡树.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('error1')
    except LookupError:
        print('error2')
    except UnicodeDecodeError:
        print('error3')


if __name__ == "__main__":
    main()


