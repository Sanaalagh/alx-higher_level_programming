#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    """Print statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

def parse_line(line, total_size, status_codes):
    """Parse a log line and update statistics."""
    parts = line.split()
    if len(parts) >= 7:
        try:
            size = int(parts[-1])
            code = int(parts[-2])
            total_size += size

            if code in status_codes:
                status_codes[code] += 1
            else:
                status_codes[code] = 1

        except ValueError:
            pass

    return total_size, status_codes

def main():
    """Main function."""
    total_size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            total_size, status_codes = parse_line(line, total_size, status_codes)
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()

