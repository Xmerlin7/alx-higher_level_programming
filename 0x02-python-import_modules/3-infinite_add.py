#!/usr/bin/python3
if __name__ == "__main__"
    import sys
    argc = len(sys.argv) - 1
    argv = sys.argv
    sum = 0

    for i in range(argc):
        sum = sum + int(argv[i + 1])
    print(sum)
