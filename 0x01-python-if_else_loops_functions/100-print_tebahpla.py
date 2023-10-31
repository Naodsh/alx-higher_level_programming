#!/usr/bin/python3
for i in range(ord('z'), ord('A') - 1, -1):
    print(f"{chr(i)}", end=('' if i % 2 == 1 else ''))
