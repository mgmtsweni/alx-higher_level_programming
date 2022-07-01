#!/usr/bin/python3
if __name__ == "__main__":
    import sys 

    argn = len(sys.argv) - 1
    results = 0
    for i in range(argn):
        results += int(sys.argv[i + 1])
    print("{}".format(results))
