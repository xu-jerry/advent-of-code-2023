def overlap(start1, len1, start2, len2):
    end1 = start1 + len1
    end2 = start2 + len2
    if start2 > end1:
        return False
    if start1 > end2:
        return False
    return True
    

with open('input.txt') as f:
    lines = f.readlines()
    seeds = [int(num) for num in lines[0].split(":")[1].split()]
    i = 0
    seeds_copy = seeds[:]
    seeds = []
    while i < len(seeds_copy):
        start = seeds_copy[i]
        length = seeds_copy[i+1]
        seeds.append((start, length))
        i+=2
    res = []

    maps = []
    cur_map = []
    for line in lines[2:]:
        if len(line) == 1:
            maps.append(cur_map)
            cur_map = []
        else:
            nums = line.split()
            if len(nums) == 3:
                cur_map.append((int(nums[0]), int(nums[1]), int(nums[2])))
    maps.append(cur_map)
    
    # for seed, length in seeds:
        # cur_loc = seed
    for cur_map in maps:
        seeds_copy = seeds[:]
        seeds = []
        print("seeds")
        print(seeds_copy)
        for seed, length in seeds_copy:
            beginning = [(seed, length)]
            end = []

            for (dest_start, source_start, range_length) in cur_map:
                beginning_copy = beginning[:]
                beginning = []
                for s, l in beginning_copy:
                    if overlap(s, l, source_start, range_length):
                        overlap_start = max(s, source_start) - source_start
                        overlap_end = min(s + l, source_start + range_length) - source_start
                        # print(overlap_start, overlap_end)
                        end.append((overlap_start + dest_start, overlap_end - overlap_start))
                        if overlap_start + source_start > s:
                            beginning.append((s, overlap_start + source_start - s))
                        if overlap_end + source_start < s + l:
                            beginning.append((overlap_end + source_start, s + l - (overlap_end + source_start)))
                    else:
                        beginning.append((s, l))
                # print("beginning end")
                # print(beginning, end)
            # print(beginning, end)
            for i in beginning:
                end.append(i)
            for i in end:
                seeds.append(i)

        # print(seeds)
    print(seeds)
    print(min(map(lambda x: x[0], seeds)))