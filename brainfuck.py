import sys
from unicodedata import decimal

def increment_pointer(data, data_pointer):
    data_pointer += 1
    return data_pointer

def decrement_pointer(data, data_pointer):
    data_pointer -= 1
    return data_pointer

def increment_byte(data, data_pointer):
    data[data_pointer] += 1

def decrement_byte(data, data_pointer):
    data[data_pointer] -= 1

def output(data, data_pointer):
    print(data[data_pointer], end="")

def get_input():
    input()

def while_loop(data_pointer, ops):
    while data_pointer > 0:
        for op in ops:
            op()

def parse(file):
    parsed = []
    with open(file) as f:
        contents = [char for char in f.read()]
    parsed = list(filter(lambda x : x in "+-<>.,[]", contents))
    return parsed

def group_while(parsed):
    new_parsed = []
    for parse in parsed:
        if parse != "[":

    
def create_op_list(parsed):
    ops = []
    for parse in parsed:
        if parse == ">":
            ops.append(increment_pointer)
        if parse == "<":
            ops.append(decrement_pointer)
        if parse == "+":
            ops.append(increment_byte)
        if parse == "-":
            ops.append(decrement_byte)
        if parse == ".":
            ops.append(output)
        if parse == ",":
            ops.append(get_input)
    return ops

def run(op_list, data, data_pointer):
    for op in op_list:
        new_data = op(data, data_pointer)
        if new_data is not None:
            data_pointer = new_data


if __name__ == "__main__":
    data = [0] * 10
    data_pointer = 0
    file = sys.argv[1]
    parsed = parse(file)
    op_list = create_op_list(parsed)
    run(op_list, data, data_pointer)
    print(data)
    print(data_pointer)