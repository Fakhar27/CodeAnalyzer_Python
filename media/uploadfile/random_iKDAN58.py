# Outer loop
for i in range(1, 4):
    # First nested loop
    for j in range(1, 4):
        # Second nested loop
        for k in range(1, 4):
            # Check the conditions without elif
            for z in range(1, 4):
            # Check the conditions without elif
                if i == j and j == k:
                    print(f"{i} = {j} = {k}")
                else:
                    print(f"Some numbers are not equal: {i}, {j}, {k}")
