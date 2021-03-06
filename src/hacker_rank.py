def ransom_note(magazine, note):
    """
    https://www.hackerrank.com/challenges/ctci-ransom-note
    * problem: does 'magazine' contain same substrings (and same number) as 'note' ?
    * my initial solution that doesn't handle dupes:
    * they want you to print to stdout instead of returning bool ¯\_(ツ)_/¯
    # NOQA return True if (set(magazine.split(' ')) & set(note.split(' '))) == set(note.split(' ')) else False
    """
    note_map = dict()
    for word in note:
        if word in note_map:
            note_map[word] = note_map[word] + 1
        else:
            note_map[word] = 1
    magazine_map = dict()
    for word in magazine:
        if note_map == magazine_map:
            return True
        if word in note_map:
            if word in magazine_map and magazine_map[word] < note_map[word]:
                magazine_map[word] = magazine_map[word] + 1
            else:
                magazine_map[word] = 1
    return note_map == magazine_map


def sum_hourglass(arr):
    """https://www.hackerrank.com/challenges/2d-array"""
    global_high = 0
    for ind, two_d in list(enumerate(arr))[:4]:
        for sy, el in list(enumerate(two_d))[:4]:
            local_high = 0
            top_sum = sum(two_d[sy : sy + 3])
            mid_sum = arr[ind + 1][sy + 1]
            btm_sum = sum(arr[ind + 2][sy : sy + 3])
            local_high += top_sum + mid_sum + btm_sum
            if (
                ind == 0 and sy == 0
            ) or local_high >= global_high:  # solves if all sums negative
                global_high = local_high
    return global_high


def counting_valleys(s):
    """
    https://www.hackerrank.com/challenges/counting-valleys
    * count number of time you go below and then return to sea level
    * scratch the phrase 'consecutive steps' from the problem statement
    """
    sea_level = 0
    valleys = 0
    for i, v in list(enumerate(s)):
        current_sea_level = sea_level
        if v == "U":
            sea_level += 1
        else:
            sea_level -= 1
        if current_sea_level == 0 and sea_level < 0:
            valleys += 1
    return valleys


def jump_clouds(c):
    """
    https://www.hackerrank.com/challenges/jumping-on-the-clouds
    * input is list of 0s and 1s
    * get to last index in as few moves as possible
    * can move to index that is is either 1 or 2 greater than current
     index i.e. at index 2, can move to indices 3 or 4
    * cannot move to index where value is 1
    """

    jumps = 0
    pairs = [x for x in enumerate(c)]
    index = 0
    index_end = len(c) - 1

    while index != index_end:
        if pairs[index + 1][0] == index_end:
            jumps += 1
            break
        if pairs[index + 2][1] != 1:
            jumps += 1
            index += 2
        else:
            jumps += 1
            index += 1
    return jumps


def repeated_string(s, n):
    """
    https://www.hackerrank.com/challenges/repeated-string
    """
    whole = n // len(s)
    remainder = n % len(s)
    base_count = whole * s.count("a")
    return base_count + s[:remainder].count("a")


def sock_merchant(ar):
    """
    https://www.hackerrank.com/challenges/sock-merchant
    sample input:
    n - 9
    ar - 10, 20, 20, 10, 10, 30, 50, 10, 20

    sample output:
    3
    """
    pairs = dict()
    tally = 0
    for el in ar:
        if el not in pairs:
            pairs[el] = 1
        else:
            pairs.update({el: pairs[el] + 1})
        if pairs[el] == 2:
            tally += 1
            pairs.update({el: 0})
    return tally
