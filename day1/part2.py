
input_data = [int(x) for x in open('input.txt').read().split('\n')]

windows = []

for i in range(len(input_data)):
    if i + 3 > len(input_data):
        break
    windows.append(sum(input_data[i:i+3]))

count = 0
for i in range(len(windows)):
    if i > 0 and windows[i] > windows[i-1]:
        count += 1
print(count)