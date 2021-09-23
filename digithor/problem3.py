
text_line = input()

text_list = list(text_line)

final_list = []

for letter in text_list:

    if letter == 'q':
        final_list.append('a')
    elif letter == 'w':
        final_list.append('b')
    elif letter == 'e':
        final_list.append('c')
    elif letter == 'r':
        final_list.append('d')
    elif letter == 't':
        final_list.append('e')
    elif letter == 'y':
        final_list.append('f')
    elif letter == 'u':
        final_list.append('g')
    elif letter == 'i':
        final_list.append('h')
    elif letter == 'o':
        final_list.append('i')
    elif letter == 'p':
        final_list.append('j')
    elif letter == 'a':
        final_list.append('k')
    elif letter == 's':
        final_list.append('l')
    elif letter == 'd':
        final_list.append('m')
    elif letter == 'f':
        final_list.append('n')
    elif letter == 'g':
        final_list.append('o')
    elif letter == 'h':
        final_list.append('p')
    elif letter == 'j':
        final_list.append('q')
    elif letter == 'k':
        final_list.append('r')
    elif letter == 'l':
        final_list.append('s')
    elif letter == 'z':
        final_list.append('t')
    elif letter == 'x':
        final_list.append('u')
    elif letter == 'c':
        final_list.append('v')
    elif letter == 'v':
        final_list.append('w')
    elif letter == 'b':
        final_list.append('x')
    elif letter == 'n':
        final_list.append('y')
    elif letter == 'm':
        final_list.append('z')
    else:
        final_list.append(letter)

doc = ''.join(map(str, final_list))
print(doc)