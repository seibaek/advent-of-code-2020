input01 = open("input01", "r")
new_list = input01.read().splitlines()
input01.close()

for v in new_list:
    for i in range(len(new_list)):
        for j in range(len(new_list)):
            if int(v) + int(new_list[i]) + int(new_list[j]) == 2020:
                print(int(v) * int(new_list[i]) * int(new_list[j]))