# from enum import IntEnum

# class Type(IntEnum):
#     FIVE_OF_A_KIND = 7
#     FOUR_OF_A_KIND = 6
#     FULL_HOUSE = 5
#     THREE_OF_A_KIND = 4
#     TWO_PAIR = 3
#     ONE_PAIR = 2
#     HIGH_CARD = 1

# strength = "AKQJT98765432"

# def get_type(cards):
#     dictionary = {}
#     for c in cards:
#         dictionary[c] = dictionary.get(c, 0) + 1
#     num_doubles = 0
#     triple = False
#     for c in dictionary.keys():
#         if dictionary[c] == 5:
#             return Type.FIVE_OF_A_KIND
#         elif dictionary[c] == 4:
#             return Type.FOUR_OF_A_KIND
#         elif dictionary[c] == 3:
#             triple = True
#         elif dictionary[c] == 2:
#             num_doubles += 1
    
#     if triple and num_doubles == 1:
#         return Type.FULL_HOUSE
#     elif triple:
#         return Type.THREE_OF_A_KIND
#     elif num_doubles == 2:
#         return Type.TWO_PAIR
#     elif num_doubles == 1:
#         return Type.ONE_PAIR

#     return Type.HIGH_CARD

# def get_value(cards):
#     val = 0
#     for c in cards:
#         val *= 14
#         val += 13 - strength.find(c)
#     return val

# def get_total_value(cards):
#     val = pow(14, 5) * int(get_type(cards)) + get_value(cards)
#     return val


# with open('input.txt') as f:
#     lines = f.readlines()
#     nums = list(map(lambda x: (x.split()[0], x.split()[1]), lines))
#     nums.sort(key=lambda x:get_total_value(x[0]))
#     res = 0
#     i = 1
#     for cards, n in nums:
#         res += i * int(n)
#         i += 1
#     print(res)

from enum import IntEnum

class Type(IntEnum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

strength = "AKQT98765432J"

# def get_type(cards):
#     dictionary = {}
#     for c in cards:
#         dictionary[c] = dictionary.get(c, 0) + 1
#     num_doubles = 0
#     max = 1
#     triple = False
#     for c in dictionary.keys():
#         if c != 'J':
#             if dictionary[c] == 5:
#                 return Type.FIVE_OF_A_KIND
#             elif dictionary[c] == 4:
#                 max = 4
#             elif dictionary[c] == 3:
#                 max = 3
#             elif dictionary[c] == 2:
#                 max = 2
#                 num_doubles += 1
    
#     max += dictionary.get('J', 0)
#     if max >= 5:
#         return Type.FIVE_OF_A_KIND
#     elif max == 4:
#         return Type.FOUR_OF_A_KIND
#     elif max == 3:
#         triple = True

#     if dictionary.get('J', 0) == 0:
#         if triple and num_doubles == 1:
#             return Type.FULL_HOUSE
#         elif triple:
#             return Type.THREE_OF_A_KIND
#         elif num_doubles == 2:
#             return Type.TWO_PAIR
#         elif num_doubles == 1:
#             return Type.ONE_PAIR
#     elif dictionary.get('J', 0) == 1:
#         if num_doubles == 2:
#             return Type.FULL_HOUSE
#         elif num_doubles == 1:
#             return Type.THREE_OF_A_KIND
#         return Type.ONE_PAIR
#     elif dictionary.get('J', 0) == 2:
#         return Type.THREE_OF_A_KIND

#     return Type.HIGH_CARD

def get_type(cards):
    dictionary = {}
    for c in cards:
        dictionary[c] = dictionary.get(c, 0) + 1
    char, max = 'J', 0
    for c in dictionary.keys():
        if c != 'J':
            if dictionary[c] > max:
                max = dictionary[c]
                char = c
    if 'J' in dictionary.keys() and dictionary['J'] != 5:
        dictionary[char] += dictionary.pop('J')

    num_doubles = 0
    triple = False
    for c in dictionary.keys():
        if dictionary[c] == 5:
            return Type.FIVE_OF_A_KIND
        elif dictionary[c] == 4:
            return Type.FOUR_OF_A_KIND
        elif dictionary[c] == 3:
            triple = True
        elif dictionary[c] == 2:
            num_doubles += 1
    
    if triple and num_doubles == 1:
        return Type.FULL_HOUSE
    elif triple:
        return Type.THREE_OF_A_KIND
    elif num_doubles == 2:
        return Type.TWO_PAIR
    elif num_doubles == 1:
        return Type.ONE_PAIR

    return Type.HIGH_CARD

def get_value(cards):
    val = 0
    for c in cards:
        val *= 14
        val += 13 - strength.find(c)
    return val

def get_total_value(cards):
    val = pow(14, 5) * int(get_type(cards)) + get_value(cards)
    return val


with open('input.txt') as f:
    lines = f.readlines()
    nums = list(map(lambda x: (x.split()[0], x.split()[1]), lines))
    nums.sort(key=lambda x:get_total_value(x[0]))
    res = 0
    i = 1
    for cards, n in nums:
        res += i * int(n)
        i += 1
    print(nums)
    print(res)