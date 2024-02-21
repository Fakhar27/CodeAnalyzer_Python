for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            if i == j and j == k:
                print(f"{i} = {j} = {k}")
            elif i != j and j != k and i != k:
                print(f"{i} != {j} != {k}")
            else:
                print(f"Some numbers are equal: {i}, {j}, {k}")