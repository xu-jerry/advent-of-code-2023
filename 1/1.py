# with open('input.txt') as f:
#     lines = f.readlines()
#     res = 0
#     for line in lines:
#         num1 = 0
#         num2 = 0
#         for c in line:
#             if c.isdigit():
#                 num1 = int(c)
#                 break
#         for c in line[::-1]:
#             if c.isdigit():
#                 num2 = int(c)
#                 break
#         res += 10 * num1 + num2
#         print(10 * num1 + num2)
#     print(res)

numbers = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

with open('input.txt') as f:
    lines = f.readlines()
    res = 0
    for line in lines:
        num1 = 0
        num2 = 0
        index = 0
        while index < len(line):
            if line[index].isdigit():
                num1 = int(line[index])
                break
            elif index+3 < len(line) and line[index:index+3] in numbers.keys():
                num1 = numbers[line[index:index+3]]
                break
            elif index+4 < len(line) and line[index:index+4] in numbers.keys():
                num1 = numbers[line[index:index+4]]
                break
            elif index+5 < len(line) and line[index:index+5] in numbers.keys():
                num1 = numbers[line[index:index+5]]
                break
            index += 1
        index = len(line) - 1
        while index >= 0:
            if line[index].isdigit():
                num2 = int(line[index])
                break
            elif index-3 >= 0 and line[index-3:index] in numbers.keys():
                num2 = numbers[line[index-3:index]]
                break
            elif index-4 >= 0 and line[index-4:index] in numbers.keys():
                num2 = numbers[line[index-4:index]]
                break
            elif index-5 >= 0 and line[index-5:index] in numbers.keys():
                num2 = numbers[line[index-5:index]]
                break
            index -= 1
        res += 10 * num1 + num2
    print(res)