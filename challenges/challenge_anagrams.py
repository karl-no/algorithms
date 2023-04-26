def merge_sort(word, start=0, end=None):
    if end is None:
        end = len(word)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(word, start, mid)
        merge_sort(word, mid, end)
        merge(word, start, mid, end)


def merge(word, start, mid, end):
    left = word[start:mid]
    right = word[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            word[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            word[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            word[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            word[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    first_word = first_string
    first_list = list(first_word.lower())
    merge_sort(first_list)

    second_word = second_string
    second_list = list(second_word.lower())
    merge_sort(second_list)

    if not first_string or not second_string:
        return ("".join(first_list), "".join(second_list), False)
    else:
        return ("".join(first_list),
                "".join(second_list), first_list == second_list)
