from collections import defaultdict, Counter
with open('input.txt') as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

polymer_base = input_data[0]
polymer_insertions = {}

for line in input_data[2:]:
    pattern, insertion = line.split(' -> ')
    polymer_insertions[pattern] = insertion

def run_step(polymer):
    pairs = [polymer[x:x+2] for x in range(len(polymer)-1)]
    new_pairs = []
    for pair in pairs:
        #print(f"Considering pair {pair}")
        sub = polymer_insertions.get(pair, None)
        new_pairs += [f"{pair[0]}{sub}"]
        #print(new_pairs)
    new_pairs += [polymer[-1]]
    return ''.join(new_pairs)

def count_frequency(polymer):
    freq_dict = defaultdict(lambda: 0)
    for k in polymer:
        freq_dict[k] += 1
    return freq_dict

def part_1():
    polymer = polymer_base
    for _ in range(10):
        polymer = run_step(polymer)
    freq_list = count_frequency(polymer)
    max_occur = max(freq_list.values())
    min_occur = min(freq_list.values())
    return max_occur - min_occur

def part_2():
    # Start with an initial count of pairs
    # For each rule, we want to substitute, so if AB mapped to C, we would, increment AC by 1, increment BC by 1
    pairs = [polymer_base[x:x+2] for x in range(len(polymer_base)-1)]
    counter = Counter(pairs)
    for _ in range(40):
        new_counter = Counter()
        for pair, sub in polymer_insertions.items():
            l, r = pair
            a = f"{l}{sub}"
            b = f"{sub}{r}"
            new_counter[a] += counter[pair]
            new_counter[b] += counter[pair]
        counter = new_counter
    # The split of pairs didn't account for the last letter, add it
    counts = Counter(polymer_base[-1])
    for k, v in counter.items():
        a, b = k
        counts[a] += v
        counts[b] += v
    
    max_item = max(counts.values())
    min_item = min(counts.values())
    # Everything is double counted, so we want to divide our answer by 2
    return (max_item - min_item) // 2


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
