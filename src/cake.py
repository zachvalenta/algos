###
# ARRAYS
###


def mtg_merge(mtgs):
    """
    ref: https://www.interviewcake.com/question/python3/merging-ranges
    desc: take list of meetings and merge into blocks when possible
    time: O(n log n) - Timsort (n log n) my sort (n); 不明觉厉
    space: O(n) bc return list could be same size as input list
    notes: list of meetings not sorted but meeting start/end are
    """
    mtgs.sort()
    blocks = [mtgs[0]]
    for ind, mtg in enumerate(mtgs[1:]):
        # DSL
        mtg_start = mtg[0]
        mtg_end = mtg[1]
        block_start = blocks[-1][0]
        block_end = blocks[-1][1]
        # logic
        if block_end >= mtg_start:
            if block_end >= mtg_end:
                blocks.pop()
                blocks.append((block_start, block_end))
            else:
                blocks.pop()
                blocks.append((block_start, mtg_end))
        else:
            blocks.append((mtg_start, mtg_end))
    return blocks


def reverse_out_of_place_imperative(qd):
    """
    time: O(n)
    space: O(n)
    """
    new_qd = []
    for i in reversed(qd):
        new_qd.append(i)
    return new_qd


def reverse_out_of_place_pythonic(qd):
    """
    time: O(n)
    space: O(n)
    """
    return qd[::-1]


def reverse_in_place_imperative(qd):
    """
    time: O(n)
    space: O(1)
    """
    if not qd:
        return qd
    start = 0
    end = len(qd) - 1
    for ind, el in enumerate(qd):
        if ind == len(qd) // 2:
            return qd
        qd[start], qd[end] = qd[end], qd[start]
        start += 1
        end -= 1


def reverse_in_place_pythonic(qd):
    """
    time: O(n)
    space: O(1)
    """
    qd.reverse()
    return qd


def reverse_sentence(qd):
    """
    ref: https://www.interviewcake.com/question/python3/reverse-words
    desc: in-place
    time: O(n)
    space: O(n)
    """
    start = 0
    rev = list()
    # empty or one-word sentence
    if not qd or " " not in qd:
        return qd
    for ind, val in enumerate(qd):
        # add word
        if val == " ":
            rev.append("".join(qd[start : ind + 1]))
            start = ind + 1
        # last word
        if ind == len(qd) - 1:
            rev.append("".join(qd[start : ind + 1]))
    rev.reverse()
    # add/trim white space for first/last words
    rev[0], rev[-1] = rev[0] + " ", rev[-1][:-1]
    return list("".join(rev))
