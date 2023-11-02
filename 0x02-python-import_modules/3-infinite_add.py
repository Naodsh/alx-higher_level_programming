#!/usr/bin/python3
if __name__ == "__main__":
    import sys

argv = sys.argv[1:]

total_sum = 0
for arg in argv:
    total_sum += int(arg)

print(total_sum)
