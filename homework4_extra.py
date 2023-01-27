# 22) You are given a 0-indexed string array words, where words[i] consists of lowercase English
# letters. In one operation, select any index i such that 0<i<words.length and words[i - 1]
# and words[i] are anagrams, and delete words[i] from words. Keep performing this operation
# as long as you can select an index that satisfies the conditions.
# Return words after performing all operations. It can be shown that selecting the indices for
# each operation in any arbitrary order will lead to the same result.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or
# phrase using all the original letters exactly once.
def are_anagrams(word1, word2):
    if len(word1) != len(word2):
        return False
    word2 = list(word2)
    for i in word1:
        if i in word2:
            word2.remove(i)
        else:
            return False
    return True


def remove_anagrams(words):
    result = [words[0]]
    for i in range(1, len(words)):
        add = True
        for j in result:
            if are_anagrams(words[i], j):
                add = False
        if add:
            result.append(words[i])
    return result


lists = ["abba", "baba", "bbaa", "cd", "cd"]
print("task 22-", remove_anagrams(lists))
print("task 22-", remove_anagrams(['a', 'b', 'a']))


# 23)You are given an array of strings names, and an array heights that consists of distinct
# positive integers. Both arrays are of length n. For each index i, names[i] and heights[i]
# denote the name and height of the ith person. Return names sorted in descending
# order by the people's heights.
def sort_by_heigths(names, heigths):
    to_dict = dict(zip(heigths, names))
    dict_sorted = sorted(to_dict.keys())[::-1]  # descenting order
    names_sorted = []
    for i in dict_sorted:
        names_sorted.append(to_dict[i])
    return names_sorted


print("task 23-", sort_by_heigths(["Marry", "John", "Emma"], [180, 165, 170]))
print("task 23-", sort_by_heigths(["Alice", "Bob", "Bob"], [155, 185, 150]))


# 24) In a special ranking system, each voter gives a rank from highest to lowest to all
# teams participating in the competition.
# The ordering of teams is decided by who received the most position-one votes. If two
# or more teams tie in the first position, we consider the second position to resolve the
# conflict, if they tie again, we continue this process until the ties are resolved. If two or
# more teams are still tied after considering all positions, we rank them alphabetically
# based on their team letter.
# You are given an array of strings votes which is the votes of all voters in the ranking
# systems. Sort all teams according to the ranking system described above.
# Return a string of all teams sorted by the ranking system.
def most_frequent(listt):
    counter = 0
    num = listt[0]

    for i in range(len(listt)):
        curr_frequency = listt.count(listt[i])
        if curr_frequency > counter:
            counter = curr_frequency
            num = i
    return num


def ranking(arr):
    rank = ""
    d = {}
    for i in range(1, len(arr[0])+1):
        d[i] = []
    for i in arr:
        for j in range(len(i)):
            d[j+1].append(i[j])
    for i in range(1, len(arr[0])+1):
        k = most_frequent(d[i])
        rank = rank + d[i][k]
    return rank


print("task 24-", ranking(["abc", "acb", "bac", "acb", "acb"]))
