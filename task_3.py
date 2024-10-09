import timeit
from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search

with open("data/стаття 1.txt", "r") as file:
    text1 = file.read()
with open("data/стаття 2.txt", "r") as file:
    text2 = file.read()


def get_real_sub_str(text: str) -> str:
    return text[int(len(text) / 2):int(len(text) / 2) + 10]


# rea
sub_strl_1_real = get_real_sub_str(text1)
sub_strl_2_real = get_real_sub_str(text2)
non_existing_substring = "Non_existng_sub_str"

# Вимірювання часу для кожного алгоритму та підрядка
algorithms = [
    ("Boyer-Moore", boyer_moore_search),
    ("KMP", kmp_search),
    ("Rabin-Karp", rabin_karp_search)
]

test_setup = [
    {
        "text_name": "стаття 1",
        "text": text1,
        "data_for_test": [
            ("Existing", sub_strl_1_real),
            ("Existing small", sub_strl_1_real[0: 4]),
            ("Non-existing", non_existing_substring)
        ]
    },
    {
        "text_name": "стаття 2",
        "text": text2,
        "data_for_test": [
            ("Existing", sub_strl_2_real),
            ("Existing smll", sub_strl_2_real[0: 4]),
            ("Non-existing", non_existing_substring)
        ]
    }

]

results = []
for test in test_setup:
    for substring_name, substring in test['data_for_test']:
        for alg_name, alg_func in algorithms:
            time_taken = timeit.timeit(lambda: alg_func(test['text'], substring), number=100)
            results.append((test['text_name'], substring_name, alg_name, time_taken))

# Виведення результатів
for result in results:
    text_name, substring_name, alg_name, time_taken = result
    print(f"{text_name} - {substring_name} Substring - {alg_name}: {time_taken:.6f} seconds")
