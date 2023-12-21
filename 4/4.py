# with open('input.txt') as f:
#     lines = f.readlines()
#     res = 0
#     for i, line in enumerate(lines):
#         line = line.split("|")
#         winning = line[0].split(":")[1].split()
#         you_have = line[1].split()
#         prize = 0
#         for num in you_have:
#             if num in winning:
#                 if prize == 0:
#                     prize = 1
#                 else:
#                     prize = 2 * prize
#         res += prize
#     print(res)

with open('input.txt') as f:
    lines = f.readlines()
    nums = [1 for _ in range(203)]
    res = 0
    for i, line in enumerate(lines):
        line = line.split("|")
        winning = line[0].split(":")[1].split()
        you_have = line[1].split()
        prize = 0
        for num in you_have:
            if num in winning:
                prize += 1
                nums[prize + i] += nums[i]
    print(nums)
    print(sum(nums))