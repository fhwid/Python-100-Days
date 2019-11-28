def main():
    try:
        with open('mm.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open('mm_c.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('error1')
    except IOError as e:
        print('error2')
    print('game over.')



if __name__ == "__main__":
    main()


