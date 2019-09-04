blood_type = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
count_A = 0
count_O = 0
count_B = 0
count_AB = 0

for i in blood_type:
    if i == 'A':
        count_A += 1

for i in blood_type:
    if i == 'O':
        count_O += 1

for i in blood_type:
    if i == 'B':
        count_B += 1

for i in blood_type:
    if i == 'AB':
        count_AB += 1

print({'A':{count_A}, 'O':{count_O}, 'B':{count_B}, 'AB':{count_AB}})

