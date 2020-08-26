'''
Given two strings, a and b , that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.

Input :

test cases,t
two strings a and b, for each test case
Output:

Desired O/p

Constraints :

string lengths<=10000

Note :

Anagram of a word is formed by rearranging the letters of the word.

For e.g. -> For the word RAM - MAR,ARM,AMR,RMA etc. are few anagrams.
'''

t = int(input())
for _ in range(t):
    a = input()
    b = input()
    a_counter = {}
    for char in a:
        a_counter[char] = a_counter.get(char, 0) + 1

    b_counter = {}
    for char in b:
        b_counter[char] = b_counter.get(char, 0) + 1

    print(a_counter)
    print(b_counter)


    # word_1 = []
    # for char in input():
    #     word_1.append(char)
    # word_2 = []
    # for char in input():
    #     word_2.append(char)
    # dupes = []

    # for char in word_1:
    #     if char in word_2:
    #         word_1.remove(char)
    #         word_2.remove(char)

    # for char in word_2:
    #     if char in word_1:
    #         word_2.remove(char)
    #         word_1.remove(char)

    # print(len(word_1) + len(word_2))


    # letters_to_rm = 0

    # for char in word_1:
    #     if char not in word_2:
    #         letters_to_rm += 1

    # for char in word_2:
    #     if char not in word_1:
    #         letters_to_rm += 1

    # print(letters_to_rm)
