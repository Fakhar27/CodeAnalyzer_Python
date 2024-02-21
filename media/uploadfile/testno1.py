total_loops = 0
total_if_else = 0

for i in range(3):
    total_loops += 1
    if i % 2 == 0:
        total_if_else += 1
    else:
        total_if_else += 2
    for k in range(1):
        total_loops += 1
        if k == 0:
            total_if_else += 1
        else:
            total_if_else += 2
            
for i in range(3):
    total_loops += 1
    if i % 2 == 0:
        total_if_else += 1
    else:
        total_if_else += 2
    for k in range(1):
        total_loops += 1
        if k == 0:
            total_if_else += 1
        else:
            total_if_else += 2

for i in range(3):
    total_loops += 1
    if i % 2 == 0:
        total_if_else += 1
    else:
        total_if_else += 2
    for k in range(1):
        total_loops += 1
        if k == 0:
            total_if_else += 1
        else:
            total_if_else += 2
