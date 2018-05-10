languages = ['EN', 'ES', 'FR', 'GE', 'PO']
for lang in languages:
    f = open(lang + '.txt', 'r')
    text = f.read()
    f.close()

    alpha_chars = []

    for char in text:
        if str(char) in '\n1234567890()[]\{\}"!?.,:;-_/':
            alpha_chars.append(' ')
        elif str(char).isalpha() or char == ' ':
            alpha_chars.append(char)

    new_text = ''.join(alpha_chars)

    new_text = new_text.lower()

    g = open(lang + 'plain.txt', 'w')
    g.write(new_text)
    g.close()


    matrix_dict = {}

    for n in range(len(new_text)-1):
        prefix = new_text[n]
        suffix = new_text[n+1]
        if matrix_dict.get(prefix, ''):
            if matrix_dict[prefix].get(suffix, ''):
                matrix_dict[prefix][suffix] += 1
            else:
                matrix_dict[prefix][suffix] = 1
        else:
            matrix_dict[prefix] = {suffix: 1}

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    matrix_list = [[] for i in range(26)]

    for n, prefix in enumerate(alphabet):
        if not matrix_dict.get(prefix, ''):
            matrix_list[n] = ['0' for i in range(26)]
            continue
        for m, suffix in enumerate(alphabet):
            if matrix_dict[prefix].get(suffix, ''):
                matrix_list[n].append(str(matrix_dict[prefix][suffix]))
            else:
                matrix_list[n].append('0')

    rows = [', '.join(matrix_list[n]) for n in range(26)]

    matrix = '; '.join(rows)

    print(matrix)

    h = open(lang + 'matrix.txt', 'w')
    h.write(matrix)
    h.close()
