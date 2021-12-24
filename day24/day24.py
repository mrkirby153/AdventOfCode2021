import math
import itertools
import sys

with open('input.txt') as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))


class ALU:

    def __init__(self) -> None:
        self.memory = {
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0
        }
        self.instructions = []
        self.input_buffer = []
        self.buffer_index = 0

    def reset(self):
        for k in self.memory.keys():
            self.memory[k] = 0
        self.buffer_index = 0

    def inp(self, var):
        """
        Reads input from the input buffer
        """
        if self.buffer_index > len(self.input_buffer):
            raise Exception(f"Invalid instruction: imp {var} {self.memory}; Empty input buffer")
        if var not in self.memory:
            raise Exception(f"Invalid instruction: imp {var} {self.memory}; Variable not found")
        value = self.input_buffer[self.buffer_index]
        self.buffer_index += 1
        self.memory[var] = value

    def get_value(self, mem):
        """
        Returns the value from memory if it's in memory, else an int of the number
        """
        return self.memory[mem] if mem in self.memory else int(mem)
    
    def add(self, var_a, var_b):
        var_a_val = self.get_value(var_a)
        var_b_val = self.get_value(var_b)
        res = var_a_val + var_b_val
        self.memory[var_a] = res
    
    def mul(self, var_a, var_b):
        var_a_val = self.get_value(var_a)
        var_b_val = self.get_value(var_b)
        res = var_a_val * var_b_val
        self.memory[var_a] = res
    
    def div(self, var_a, var_b):
        var_a_val = self.get_value(var_a)
        var_b_val = self.get_value(var_b)
        if var_b_val == 0:
            raise Exception(f"Invalid instruction: div {var_a}, {var_b} {self.memory}; Divide by zero")
        res = math.floor(var_a_val / var_b_val)
        self.memory[var_a] = res
    
    def mod(self, var_a, var_b):
        var_a_val = self.get_value(var_a)
        var_b_val = self.get_value(var_b)
        if var_a_val < 0:
            raise Exception(f"Invalid instruction: mod {var_a}, {var_b} {self.memory}; {var_a} < 0")
        if var_b_val <= 0:
            raise Exception(f"Invalid instruction: mod {var_a}, {var_b} {self.memory}; {var_b} <= 0")
        res = var_a_val % var_b_val
        self.memory[var_a] = res
    
    def eql(self, var_a, var_b):
        var_a_val = self.get_value(var_a)
        var_b_val = self.get_value(var_b)
        self.memory[var_a] = 1 if var_a_val == var_b_val else 0
    
    def load(self, instructions):
        for ins in instructions:
            parts = ins.split(' ')
            ins = parts[0]
            args = parts[1:]
            self.instructions.append((ins, args))
    
    def evaluate(self, input_buffer, debug=False):
        def sprint(*args, **kwargs):
            if debug:
                print(*args, **kwargs)
        self.input_buffer = input_buffer
        for instruction in self.instructions:
            # sprint(f"Executing instruction {instruction}")
            method, args = instruction
            to_call = getattr(self, method, None)
            if to_call is None:
                raise Exception(f"Error processing instruction {instruction}. No handler found")
            to_call(*args)
            sprint(f"Memory: {self.memory}")
        return self.memory


def generate_all_valid_digits(length=14):
    return [int(''.join(map(str, x))) for x in itertools.product(range(1, 10), repeat=length)]

# def part_1():
#     alu = ALU()
#     alu.load(input_data)
#     input_str = [int(x) for x in "99999999999999"]
#     print(input_str)
#     print(alu.evaluate(input_str)["z"])
        

# def part_2():
#     pass

# print(f"Part 1: {part_1()}")
# # print(f"Part 2: {part_2()}")
if len(sys.argv) != 2:
    exit(-1)
num = sys.argv[1]
alu = ALU()
alu.load(input_data)
input_buff = [int(x) for x in num]
print(input_buff)
print(alu.evaluate(input_buff)["z"] == 0)