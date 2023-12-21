# def check_around(lines, row, start, end):
#     h = len(lines)
#     w = len(lines[0])
#     if row != 0:
#         for i in range(max(start - 1, 0), min(end + 1, w - 1)):
#             if check_char(lines, row - 1, i):
#                 return True
#     if row != h - 1:
#         for i in range(max(start - 1, 0), min(end + 1, w - 1)):
#             if check_char(lines, row + 1, i):
#                 return True
#     if start != 0:
#         if check_char(lines, row, start - 1):
#             return True
#     if end != w - 1:
#         if check_char(lines, row, end):
#             return True
#     return False
        
# def check_char(lines, row, col):
#     if lines[row][col].isdigit() or lines[row][col] == '.':
#         return False
#     return True

# with open('input.txt') as f:
#     lines = f.readlines()
#     res = 0
#     for i, line in enumerate(lines):
#         num = 0
#         start = -1
#         for j, c in enumerate(line):
#             if c.isdigit():
#                 num = num * 10 + int(c)
#                 if start == -1:
#                     start = j
#             else:
#                 if start != -1:
#                     end = j
#                     if check_around(lines, i, start, end):
#                         res += num
#                     num = 0
#                     start = -1
#     print(res)

numbers_adjacent = {}

def check_around(lines, row, start, end, num):
    h = len(lines)
    w = len(lines[0])
    if row != 0:
        for i in range(max(start - 1, 0), min(end + 1, w - 1)):
            check_char(lines, row - 1, i, num)
    if row != h - 1:
        for i in range(max(start - 1, 0), min(end + 1, w - 1)):
            check_char(lines, row + 1, i, num)
    if start != 0:
        check_char(lines, row, start - 1, num)
    if end != w - 1:
        check_char(lines, row, end, num)
        
def check_char(lines, row, col, num):
    if lines[row][col] == '*':
        if (row, col) not in numbers_adjacent.keys():
            numbers_adjacent[(row,col)] = [num]
        else:
            numbers_adjacent[(row,col)].append(num)

with open('input.txt') as f:
    lines = f.readlines()
    res = 0
    for i, line in enumerate(lines):
        num = 0
        start = -1
        for j, c in enumerate(line):
            if c.isdigit():
                num = num * 10 + int(c)
                if start == -1:
                    start = j
            else:
                if start != -1:
                    end = j
                    check_around(lines, i, start, end, num)
                    num = 0
                    start = -1
    for _, value in numbers_adjacent.items():
        if len(value) == 2:
            res += value[0] * value[1]
    print(res)