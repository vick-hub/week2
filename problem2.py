import os
import sys


def main():
    s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur rhoncus tincidunt sem nec gravida. Sed id convallis quam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus dui purus, ornare vitae metus vitae, feugiat ultricies ipsum. Etiam id ante quis purus rhoncus egestas. Donec vel ligula lacinia, iaculis ipsum vitae, vulputate nunc. Aliquam tellus libero, sagittis quis massa elementum, semper sodales lacus. Sed justo arcu, lobortis quis bibendum ac, fermentum ut mi. Quisque faucibus ex vitae sapien aliquam blandit. Donec fringilla sit amet augue id venenatis. Integer at nibh quis justo consectetur posuere. Nulla facilisis mi massa, sed congue lectus vehicula sed. Quisque placerat ultrices est congue vestibulum. Maecenas fermentum purus et ipsum volutpat, eu convallis risus interdum. Donec vel nunc suscipit, venenatis mi at, convallis sapien. Integer ut metus id neque rhoncus commodo."
    print(len(s))
    # 920
    print(s.count('it'))
    # 13
    print(s.lower())
    h = s.replace('i', '*')
    print(h)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
