def simple_text_editor(options: list[str]) -> str:
    s = ""
    q = []
    for item in options:
        option = item.split(" ")
        if option[0] == "1":
            # append
            q.append(s)
            s += option[1]
        elif option[0] == "2":
            # delete last k character
            q.append(s)
            s = s[: len(s) - int(option[1])]
        elif option[0] == "3":
            # print n last position
            print(s[int(option[1]) - 1])
        else:
            s = q.pop()


if __name__ == '__main__':
    # get input
    num_ops = input()
    ops_list = []
    for row in range(int(num_ops)):
        ops_list.append(input())

    # run function
    simple_text_editor(ops_list)