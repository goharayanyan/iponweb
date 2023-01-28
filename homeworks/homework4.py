# 1)Տրված է թվաբանական պրոգրեսիայի առաջին և երկրորդ անդամները։
# Տրված n֊ի համար, վերադարձնել այդ պրոգրեսիայի n֊րդ անդամը։
# լուծում 1
def progressia_rec(a1, a2, n):  # rekursive
    if n == 1:
        return a1
    return progressia_rec(a1, a2, n-1)+(a2-a1)


print("task 1-", progressia_rec(1, 3, 6))


# լուծում 2
def progressia_iter(a1, a2, n):  # iterative
    d = a2-a1
    return a1+d*(n-1)


print("task 1-", progressia_iter(1, 3, 6))


# 2) CodeMaster-ը նոր է վերադարձել գնումներից։ Նա սկանավորեց իր գնած ապրանքների
# չեկը և ստացված շարանը տվեց Ratiorg֊ին՝ պարզելու գնված ապրանքների
# ընդհանուր թիվը: Քանի որ Ratiorg-ը բոտ է, նա անպայման պատրաստվում է այն
# ավտոմատացնել, ուստի նրան անհրաժեշտ է ծրագիր, որը կամփոփի բոլոր թվերը,
# որոնք հայտնվում են տվյալ մուտքագրում:
# Օգնեք Ratiorg-ին՝ գրելով ֆունկցիա, որը վերադարձնում է տվյալ inputString-ում
# հայտնված թվերի գումարը։

def ratiorg(string):
    x = string.split()
    count = 0
    for i in x:
        if i.isdigit():
            count += int(i)
    return count


print("task 2- ", ratiorg("2 apples, 12 oranges"))


# 3) Մուտքագրեք երեք ամբողջ թիվ: Տպեք «Տեսակավորված» բառը, եթե թվերը նշված են
# ոչ աճող կամ չնվազող հերթականությամբ, իսկ «Չտեսակավորված» հակարակ
# դեպքում:
def is_sorted(arr):
    if all(arr[i] <= arr[i+1] for i in range(len(arr) - 1)):
        return "Sorted"
    if all(arr[i] >= arr[i+1] for i in range(len(arr) - 1)):
        return "Sorted"
    return "Unsorted"


print("task 3- ", is_sorted([1, 2, 3]))
print("task 3- ", is_sorted([1, 3, 2]))
print("task 3- ", is_sorted([5, 0, -4]))


# 4)Գրել ֆունկցիա, որը տրված բնական թվի համար կստուգի,
# արդյոք այն կատարյալ թիվ է, թե ոչ։
def is_perfect(n):
    # gtnenq bajanarerneri gumary
    div_sum = 0  # n-y hastat bajanarar e
    for i in range(1, n//2+1):
        if n % i == 0:
            div_sum += i
    if div_sum == n:
        return "n is perfect"
    return "n is not perfect"


print("task 4-", is_perfect(28))


# 5)Գրել ծրագիր, որը տրված թվային արժեքներով ցուցակի համար,
# կհաշվի նրա էլեմենտների գումարը։
def elem_sum(a):
    s = 0
    for i in a:
        s += i
    return s


print("task 5-", elem_sum([5, 6, 7]))


# 6)Գրել ֆունկցիա, որը տրված թվային արժեքներով ցուցակի համար, կվերադարձնի այդ
# ցուցակի ամենամեծ էլեմենտը։
def list_max(a):
    maximum = a[0]
    for i in a:
        if maximum < i:
            maximum = i
    return maximum


print("task 6-", list_max([4, 7, 3]))


# 7)Գրել ֆունկցիա, որը տրված ցուցակից կջնջի տրված արժեքին հավասար բոլոր
# էլեմենտները։
def del_x(arr, x):
    for i in range(1, arr.count(x)+1):
        arr.remove(x)
    return arr


print("task 7-", del_x([2, 3, 4, 2, 3], 2))


# 8) Գրեք ֆունկցիա որը կվերադարձնի տրված թվային արժեքներով ցուցակի բոլոր
# էլեմենտների արտադրյալը։

def elem_mult(arr):
    mult = 1
    for i in arr:
        mult *= i
    return mult


print("task 8-", elem_mult([2, 4, 7]))


# 9)Գրեք ֆունկցիա՝ տողը հակադարձելու համար, եթե դրա երկարությունը 4-ի
# բազմապատիկ է։
def rev(a):
    if len(a) % 4 == 0:
        return a[::-1]  # or return a.reverse()
    return a


print("task 9-", rev("Hello"))


# 10) Գրեք ֆունկցիա՝ որը տրված բնական n թվի համար վերադարձնում է Ֆիբոնաչիի n-րդ
# անդամը։ Խնդիրը լուծել և ռեկուրսիվ, և իտերատիվ մեթոդներով։
# when the first element is 1
def fib_rec(n):
    if n == 1 or n == 2:  # first and second values
        return 1
    return fib_rec(n-1) + fib_rec(n-2)


print("task 10-", fib_rec(8))


def fib_iter(n):
    prev = 0
    this = 1
    for i in range(1, n):
        prev, this = this, prev+this
    return this


print("task 10-", fib_iter(8))


# 11) Գրել ֆունկցիա, որը տրված 2 բնական թվերի համար կվերադարձնի նրանց
# ամենափոքր ընդհանուր բազմապատիկը։
# լուծում 1
def lcm(a, b):  # using euclidean algorithm
    x = a
    y = b
    if a < b:
        a, b = b, a
    rem = a % b
    while rem != 0:
        a = b
        b = rem
        rem = a % b
    return (x * y)//b


print("task 11-", lcm(15, 70))


# 12) Գրեք python ծրագիր՝ նշված թվի հաջորդ ամենափոքր պալինդրոմը գտնելու համար:
# Օրինակ 119-ի համար հաջորդ պալինդրոմը 121 է
def next_pol(x):
    x += 1  # so that if the given number is already polyndom,function returns the next one, not itself
    while True:
        n = str(x)
        if n != n[::-1]:
            x += 1
            continue
        break
    return x


print("task 12-", next_pol(121))


# 13) Ռոբոտը կանգնած է ուղղանկյուն ցանցի վրա և ներկայումս գտնվում է կետում (X0,
# Y0): Կոորդինատները ամբողջ թիվ են։ Այն ստանում է N հեռակառավարման
# հրամաններ: Յուրաքանչյուր հրաման մեկն է՝ վեր, վար, ձախ, աջ: Ճիշտ հրաման
# ստանալուց հետո ռոբոտը մեկ միավոր է տեղափոխում տվյալ ուղղությամբ։ Եթե
# ռոբոտը սխալ հրաման է ստանում, նա պարզապես անտեսում է այն: Որտե՞ղ է
# գտնվելու ռոբոտը բոլոր հրամաններին հետևելուց հետո:
def robot(tupl):
    x0 = 0
    y0 = 0
    for i in tupl:
        if i == "right":
            x0 += 1
        elif i == "left":
            x0 -= 1
        elif i == "up":
            y0 += 1
        elif i == "down":
            y0 -= 1
    tupl = (x0, y0)
    return tupl


print("task 13- ", robot(("up", "up", "left", "left", "hey", "down")))


# 14)Ստուգեք, արդյոք 2 ցուցակները 1-քայլ ցիկլիկ են:
def are_cyclic(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    if arr1[-1] == arr2[0]:
        if all(arr1[i] == arr2[i + 1] for i in range(len(arr1) - 1)):
            return True
    elif arr2[-1] == arr1[0]:
        if all(arr2[i] == arr1[i + 1] for i in range(len(arr1) - 1)):
            return True
    return False


print("task 14-", are_cyclic([1, 2, 3, 4, 5, 6], [6, 1, 2, 3, 4, 5]))
print("task 14-", are_cyclic([6, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]))


# 15) Գրել ծրագիր, որը ստանւմ է թիվ, գտեք առավելագույն թիվը, որը կարող եք ստանալ՝
# ջնջելով տվյալ թվի ուղիղ մեկ թվանշանը:
def max_remaining(n):
    x = str(n)
    maximum = x[:-1]  # removing last digit
    for i in range(0, len(x)):
        t = x  # in order not to lose x
        t = t[0:i] + t[i+1:]
        if t > maximum:
            maximum = t
    return maximum


print("task 15-", max_remaining(152))


# 16)Գրեք ֆուկցիա որը ստանում է tuple տիպի օբյեկտ և վերադարձնում նոր tuple
# բաղկացած միայն առաջին tuple֊ի թվերից։
def tuple_numbers(tupl):
    new_tuple = ()
    for i in tupl:
        if type(i) == int:
            new_tuple += (i,)
    return new_tuple


print("Task 16", tuple_numbers(("hey", 4, True, 3)))


# 17)Գրեք Python ֆուկցիա որը ստանում է tuple և ցանկացաց տիպի օբյեկտ և ավելացնում
# է ստացած արժեքը tuple մեջ։
def tuple_add(tupl, element):
    tupl += (element,)
    return tupl


print("task 17-", tuple_add((1, False, 3, "hey", 7), "Hello"))


# 18)Գրեք Python ֆուկցիա որը ստանում է tuple դարձնում է string։
# Tuplex֊ի էլեմենտները ստրինգում պետք է բաժանված լինեն ‘-’ նշանով։
def tuple_to_string(tupl):
    new_str = ""
    for i in tupl:
        new_str += str(i)
        new_str += "-"
    return new_str[:-1]  # do not need the last '-'


print("task 18-", tuple_to_string((2, 3, 'hey')))


# 19)Գրեք Python ֆուկցիա որը ստանում է list և պետքա գտնել նրա երկարությունը առանց
# len() ֆունկցիա֊ի օգտագորձմամբ։
def list_length(arr):
    count = 0
    for i in arr:
        count += 1
    return count


print("task 19-", list_length([1, 2, 6, 4, 2, 8, 10]))


# 20) Ticket numbers usually consist of an even number of digits.
# A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.
# Given a ticket number n, determine if it's lucky or not. Not using: string, list, tuple, set types.
def is_lucky(n):
    # count of digits
    count = 1
    x = n  # so that we can change
    while x >= 10:
        x //= 10
        count += 1
    # check if lucky
    n1 = n % 10 ** (count/2)  # second half
    n2 = (n - n1) // 10 ** (count/2)  # second half
    sum1 = 0
    sum2 = 0
    i = 0
    while i <= count/2:
        sum1 += n1 % 10
        sum2 += n2 % 10
        n1 //= 10
        n2 //= 10
        i += 1
    if sum1 == sum2:
        return True
    return False


print("task 20 -", is_lucky(1230))


# 21) Euler function is return a count of numbers not greater than N, which are mutualy simple with
# N. Example φ(6)=2, as only 1 and 5 from 1,2,3,4,5 are mutually simple with 6. Write a function
# which return count of numbers mutually simple with given N.

# from the previus class I copied gcd function
def gcd(a, b):  # ամենամեծ ընդհանուր բաժանարարը
    rem = a % b
    while rem != 0:
        a = b
        b = rem
        rem = a % b
    return b


def euler(n):
    count = 0
    for i in range(n):
        if gcd(i, n) == 1:
            count += 1
    return count


print("task 21-", euler(6))


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
