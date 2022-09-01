def offset_table(needle: str) -> dict:
    """
    This function creates a dictionary of offsets
    """
    offsets = {}
    n = len(needle)

    for i in range(n - 2, -1, -1):
        if needle[i] not in offsets:
            offsets[needle[i]] = n - i - 1

    if needle[n - 1] not in offsets:
        offsets[needle[n - 1]] = n

    offsets['*'] = n
    return offsets


def boyer_mur(haystack: str, needle: str) -> int:
    if len(needle) > len(haystack) or len(needle) == 0 or len(haystack) == 0:
        return -1

    offsets = offset_table(needle)
    j = i = k = len(needle)
    while j > 0 and i <= len(haystack):
        if haystack[k - 1] == needle[j - 1]:
            k -= 1
            j -= 1
        else:
            if haystack[i - 1] in offsets:
                i += offsets[haystack[i - 1]]
            else:
                i += offsets['*']
            j = len(needle)
            k = i

    if j <= 0:
        return k + 1
    else:
        return -1


def test():
    str1, str2, str3, str4 = 'sdjghksjahfjdsh', '', 'olololo', 'saaaaaaaaaaaaaaaaaaaaaa'
    sub_str1, sub_str2, sub_str3, sub_str4 = 'fj', 'ssgasv', '', 'aaaa'
    assert boyer_mur(str1, sub_str1) == 11
    assert boyer_mur(str2, sub_str2) == -1
    assert boyer_mur(str3, sub_str3) == -1
    assert boyer_mur(str4, sub_str4) == 2


def main():
    test()
    string = input('Input a string: ')
    substring = input('Input a substring: ')
    answer = boyer_mur(string, substring)
    if answer == -1:
        print('There is no such substring.')
    else:
        print(answer)


if __name__ == "__main__":
    main()