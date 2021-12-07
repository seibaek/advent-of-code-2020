aoc_input = open("input02", "r")
new_list = aoc_input.read().splitlines()
aoc_input.close()

counter = 0

def valid_pass(prange, pchar, pword):
    global counter
    if pword[int(prange[0]) - 1] == pchar and pword[int(prange[1]) - 1] != pchar:
        counter += 1
    if pword[int(prange[0]) - 1] != pchar and pword[int(prange[1]) - 1] == pchar:
        counter += 1

for v in new_list:
    pass_check = v.split(" ")
    pass_range = pass_check[0].split('-')
    pass_char = pass_check[1][0]
    pass_word = pass_check[2]
    valid_pass(pass_range, pass_char, pass_word)

print(counter)