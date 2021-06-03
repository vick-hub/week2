import os
import sys


def main():
    t = "Apache license"
    t.title()
    print(t.center(60))
    r = "Version 2.0, January 2004"
    r.title()
    print(r.center(60))
    q = "http://www.apache.org/licenses/"
    print(q.center(60))
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
