
input_data = [int(x) for x in open('input.txt').read().split('\n')]

increments = 0
for i in range(len(input_data)):
    if i > 0 and input_data[i] > input_data[i-1]:
        increments += 1
print(increments)