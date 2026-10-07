def reverse_string(s):
    result = ""
    for i in range(len(s)-1, -1, -1):
        result += s[i]
    return result

print("Reverse of 'hello':", reverse_string("hello"))


def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

print("Palindrome check 'madam':", is_palindrome("madam"))
print("Palindrome check 'python':", is_palindrome("python"))


def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v = 0
    c = 0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    return v, c

print("Vowels/Consonants in 'education':", count_vowels_consonants("education"))


def find_duplicates(s):
    freq = {}
    duplicates = []
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for key in freq:
        if freq[key] > 1:
            duplicates.append(key)
    return duplicates

print("Duplicates in 'programming':", find_duplicates("programming"))


def remove_spaces(s):
    result = ""
    for ch in s:
        if ch != " ":
            result += ch
    return result

print("Remove spaces:", remove_spaces("the sky is blue"))


def substring_occurrence(s, sub):
    count = 0
    for i in range(len(s) - len(sub) + 1):
        if s[i:i+len(sub)] == sub:
            count += 1
    return count

print("Occurrences of 'ana' in 'banana':", substring_occurrence("banana", "ana"))


def is_anagram(a, b):
    if len(a) != len(b):
        return False
    freq_a = {}
    freq_b = {}
    for ch in a:
        freq_a[ch] = freq_a.get(ch, 0) + 1
    for ch in b:
        freq_b[ch] = freq_b.get(ch, 0) + 1
    return freq_a == freq_b

print("Anagram check 'listen' & 'silent':", is_anagram("listen", "silent"))
print("Anagram check 'hello' & 'world':", is_anagram("hello", "world"))


def to_uppercase(s):
    result = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch
    return result

print("Uppercase of 'python':", to_uppercase("python"))


def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest

print("Longest word:", longest_word("the quick brown fox jumps"))


def replace_char(s, old, new):
    result = ""
    for ch in s:
        if ch == old:
            result += new
        else:
            result += ch
    return result

print("Replace 'l' with 'x' in 'hello':", replace_char("hello", "l", "x"))
