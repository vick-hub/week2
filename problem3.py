import os
import sys


def main():
    h = "पायथन एक अद्भुत प्रोग्रामिंग भाषा है जिसके माध्यम से मैं बहुत कुछ हासिल कर सकता हूं।"
    print(type(h))
    # <class 'str'>
    y = h.encode("utf-8")
    print(y)
    print(type(y))
    # <class 'bytes'>
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
