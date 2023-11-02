#!/usr/bin/python3
if __name__ == "__main__":
    import sys

argv = sys.argv[1:]

num_args = len(argv)

if num_args == 0:
    print("0 arguments.")
else:
    print("{} argument{}:".format(num_args, 's' if num_args > 1 else ''))

    for i, arg in enumerate(argv, 1):
        print("{}: {}".format(i, arg))
