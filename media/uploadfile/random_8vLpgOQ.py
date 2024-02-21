for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            for z in range(1, 4):
                if i == j and j == k:
                    print(f"{i} = {j} = {k}")
                else:
                    print(f"Some numbers are not equal: {i}, {j}, {k}")
                    
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            if i == j and j == k:
                print(f"{i} = {j} = {k}")
            else:
                print(f"Some numbers are not equal: {i}, {j}, {k}")
