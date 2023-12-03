color_limit = {"red": 12, "green" : 13, "blue" : 14}

# with open('input.txt') as f:
#     lines = f.readlines()
#     res = 0
#     for line in lines:
#         game, rest = line.split(":")
#         _, game_number = game.split()
#         sets = rest.split(";")
#         exit = False
#         for set in sets:
#             cubes = set.split(",")
#             for cube in cubes:
#                 num, color = cube.split()
#                 if color_limit[color] < int(num):
#                     res += int(game_number)
#                     exit = True
#                     break
#             if exit:
#                 break

#     print(res)
#     print(5050 - res)

with open('input.txt') as f:
    lines = f.readlines()
    res = 0
    for line in lines:
        color_limit = {"red": 0, "green" : 0, "blue" : 0}
        game, rest = line.split(":")
        _, game_number = game.split()
        sets = rest.split(";")
        for set in sets:
            cubes = set.split(",")
            for cube in cubes:
                num, color = cube.split()
                color_limit[color] = max(int(num), color_limit[color])
        res += color_limit["red"] * color_limit["green"] * color_limit["blue"]

    print(res)