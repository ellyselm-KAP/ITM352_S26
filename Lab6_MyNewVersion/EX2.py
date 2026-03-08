values = [3, "hi", 9.5, True, None, {"a": 1}]  # change this however you want

n = len(values)

if n < 5:
    print(f"List has {n} elements: fewer than 5.")
elif 5 <= n <= 10:
    print(f"List has {n} elements: between 5 and 10 (inclusive).")
else:
    print(f"List has {n} elements: more than 10.")



test_cases = [
    [],                                 # length 0  -> fewer than 5
    [1, 2, 3, 4],                        # length 4  -> fewer than 5
    [1, 2, 3, 4, 5],                     # length 5  -> between 5 and 10
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],     # length 10 -> between 5 and 10
    list(range(11)),                     # length 11 -> more than 10
]

for case in test_cases:
    n = len(case)
    if n < 5:
        msg = "fewer than 5"
    elif 5 <= n <= 10:
        msg = "between 5 and 10 (inclusive)"
    else:
        msg = "more than 10"

    print(f"len={n} -> {msg}")

if describe_list_size(lst):
    n = len(lst)
    if n < 5:
        return "fewer than 5"
    elif n <= 10:
        return "between 5 and 10 (inclusive)"
    else:
        return "more than 10"

for case in test_cases:
    print(f"len={len(case)} -> {describe_list_size(case)}")


