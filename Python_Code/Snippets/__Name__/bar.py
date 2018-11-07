'''
Start this script to see only this script (no imports)
'''


def main():
    print(__name__)

if __name__ == '__main__':
    main()
    print("bar.py is running as __main__")

else:
    main()
    print("bar.py is not running as __main__ but called as :" , __name__)

