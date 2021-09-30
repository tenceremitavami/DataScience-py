def reversing(li):
    reversed_list = [elem[::-1] for elem in li][::-1]
    print(reversed_list)


inp = [[1, 2], [3, 4], [5, 6, 7]]
reversing(inp)
