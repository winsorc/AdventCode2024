
left_vals = []
right_vals = []
distance = 0
sim_score = 0

with open ('input.txt', 'r') as file:
    for line in file:
        values = (line.split())
        left_vals.append(int(values[0]))
        right_vals.append(int(values[1]))
        left_vals.sort()
        right_vals.sort()

    for i in range(len(left_vals)):
        distance += abs(left_vals[i] - right_vals[i])
        num_count = right_vals.count(left_vals[i])
        similar = (left_vals[i] * num_count)
        sim_score += similar

    print(distance)
    print(sim_score)
    


    

