while True:
    try:
        x = int(input('Enter a number: '))
        break
    except ValueError as e:
        print('\n[!] That\'s not a valid number.')
        print("ValueError occurred: {}".format(e))
    finally:
        print('\nAttempted Input\n')
