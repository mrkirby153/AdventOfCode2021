from queue import Queue
with open('input.txt') as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

def _get_value(p):
    return p.value()

class Packet:
    def __init__(self, version, packet_type, data=None):
        self.version = version
        self.type = packet_type
        self.extra_data = data

    def __repr__(self) -> str:
        return f"v{self.version} [{self.type}]: {self.extra_data}"
    
    def value(self):
        if self.type == 4:
            return self.extra_data
        if self.type == 0:
            return sum(map(_get_value, self.extra_data))
        if self.type == 1:
            product = 1
            for p in self.extra_data:
                product *= p.value()
            return product
        if self.type == 2:
            return min(map(_get_value, self.extra_data))
        if self.type == 3:
            return max(map(_get_value, self.extra_data))
        if self.type == 5:
            first = self.extra_data[0]
            second = self.extra_data[1]
            return 1 if first.value() > second.value() else 0
        if self.type == 6:
            first = self.extra_data[0]
            second = self.extra_data[1]
            return 1 if first.value() < second.value() else 0
        if self.type == 7:
            first = self.extra_data[0]
            second = self.extra_data[1]
            return 1 if first.value() == second.value() else 0

def parse_literal(queue: Queue):
    bin_str = ""
    while True:
        should_continue = queue.get(block=False)
        bin_str += ''.join(_get_multiple(queue, 4))
        if should_continue == '0':
            break
    return binary_to_dec(bin_str)

def parse_operator(queue: Queue):
    mode = queue.get()
    print(f"Operator mode: {mode}")
    results = []
    if mode == '0':
        total_length = ''.join(_get_multiple(queue, 15))
        print(f"Total length is {total_length} {binary_to_dec(total_length)}")
        processed_bits = 0
        sub_packet_count = 0
        while processed_bits < binary_to_dec(total_length):
            sub_packet_count += 1
            print(f"-- Processing sub-packet {sub_packet_count} --")
            start_size = queue.qsize()
            results.append(_parse_packet(queue))
            end_size = queue.qsize()
            consumed_bits = start_size - end_size
            print(f"Processed sub-packet with {consumed_bits} consumed")
            processed_bits += consumed_bits
            print(f"-- Finished processing sub-packet {sub_packet_count} --")
    elif mode == '1':
        total_packets = ''.join(_get_multiple(queue, 11))
        print(f"Total packets are {total_packets} {binary_to_dec(total_packets)}")
        for i in range(binary_to_dec(total_packets)):
            print(f"-- Processing sub-packet {i+1} --")
            results.append(_parse_packet(queue))
            print(f"-- Finished processing sub-packet {i+1} --")
    else:
        raise Exception(f"Unrecognized mode {mode}")
    return results

def hex_to_binary(hex):
    if type(hex) == list or len(hex) > 1:
        bin_str = ""
        for k in hex:
            binary_repr = hex_to_binary(k)
            # print(f"{k} -> {binary_repr}")
            bin_str += binary_repr
        return bin_str
    return bin(int(hex, 16))[2:].zfill(4)

def binary_to_dec(binary):
    return int(binary, 2)

def _get_multiple(queue: Queue, amount: int):
    return [queue.get(block=False) for _ in range(amount)]

def parse_packet(binary: str) -> Packet:
    print(binary)
    data = Queue()
    for char in binary:
        data.put(char)
    return _parse_packet(data)

def _parse_packet(packet_data: Queue) -> Packet:
    ver_bin = ""
    type_bin = ""
    ver_bin = ''.join(_get_multiple(packet_data, 3))
    type_bin = ''.join(_get_multiple(packet_data, 3))
    type_dec = binary_to_dec(type_bin)
    ver_dec = binary_to_dec(ver_bin)
    print(f"Packet Header: ver = {ver_dec}  type = {type_dec}")
    handler = parse_literal if binary_to_dec(type_bin) == 4 else parse_operator
    if handler is None:
        raise Exception(f"No type parser for type {type_dec}")
    print(f"Executing handler {handler}")
    result = handler(packet_data)
    return Packet(ver_dec, type_dec, result)

raw_packet_data = hex_to_binary(input_data)
parsed_packet = parse_packet(raw_packet_data)

def part_1():
    version_sum = 0
    packets = Queue()
    packets.put(parsed_packet)
    while not packets.empty():
        p = packets.get(block=False)
        version_sum += p.version
        if p.type != 4: # If this has sub-packets
            for sub_packet in p.extra_data:
                packets.put(sub_packet)
    return version_sum

def part_2():
    return parsed_packet.value()

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
