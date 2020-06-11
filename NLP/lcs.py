def lcs_test(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)
    c = [[0 for i in range(s2_len + 1)] for j in range(s1_len + 1)]
    f = [[0 for i in range(s2_len + 1)] for j in range(s1_len + 1)]
    for i in range(s1_len):
        for j in range(s2_len):
            if s1[i] == s2[j]:
                c[i + 1][j + 1] = c[i][j] + 1
                f[i + 1][j + 1] = 'o'
            elif c[i + 1][j] > c[i][j + 1]:
                c[i + 1][j + 1] = c[i + 1][j]
                f[i + 1][j + 1] = 'l'
            else:
                c[i + 1][j + 1] = c[i][j + 1]
                f[i + 1][j + 1] = 'u'
    return c, f


def get_str(f, s1, s1_len, s2_len):
    if s1_len == 0 or s2_len == 0:
        return
    if f[s1_len][s2_len] == 'o':
        get_str(f, s1, s1_len - 1, s2_len - 1)
        print(s1[s1_len - 1], end='')
    elif f[s1_len][s2_len] == 'l':
        get_str(f, s1, s1_len, s2_len - 1)
    else:
        get_str(f, s1, s1_len - 1, s2_len)


s1, s2 = 'ABCBDAB', 'BDCABA'
c, f = lcs_test(s1, s2)
for i in c:
    print(i)
print('')
for i in f:
    print(i)
print(s1, s2 + ' -> ', end='')
get_str(f, s1, len(s1), len(s2))
print()
