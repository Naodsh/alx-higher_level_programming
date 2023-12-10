#!/usr/bin/python3
""" Module that reads stdin line by line and computes metrics """


import sys


def print_stats(file_sizes, status_codes):
    print(f"File size: {sum(file_sizes)}")
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")


def parse_line(line):
    parts = line.split()
    if len(parts) > 2:
        file_size = int(parts[-1])
        status_code = parts[-2]
        return file_size, status_code
    return None, None


def main():
    file_sizes = []
    status_codes = {}

    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            file_size, status_code = parse_line(line)
            if file_size is not None and status_code is not None:
                file_sizes.append(file_size)
                status_codes[status_code] = status_codes.get(
                        status_code, 0) + 1

            if line_count == 10:
                print_stats(file_sizes, status_codes)
                line_count = 0

    except KeyboardInterrupt:
        print_stats(file_sizes, status_codes)
        raise


if __name__ == "__main__":
    main()
