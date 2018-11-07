'''
Start this script to see bar.py being imported, and the function(s) within bar.py being executed.
Then see this main() being executed.
'''

import bar


def main():
    print(__name__)


if __name__ == '__main__':
    main()
    print("foo.py is running as __main__ and called: ", __name__)





# --- Dead Code Start ---
# Here for illustrations purposes only.
else:
    main()
    print("foo.py not running as __main__ but called as :" , __name__)

# --- Dead Code End ---

