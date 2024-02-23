from gates import aand, orr, xor

def one_bit_half_adder(A: bool, B:bool) -> ("carry", "sum"):
    return (aand(A,B), xor(A,B))

def one_bit_full_adder(carry_in: bool, A: bool, B: bool) -> ("carry", "sum"):
    data1 = one_bit_half_adder(A, B)
    carry_out1 = data1[0]
    sum1 = data1[1]
    data2 = one_bit_half_adder(sum1, carry_in)
    carry_out = orr(carry_out1,data2[0])
    sum = data2[1]
    return (carry_out, sum)

def inverter(bits: tuple[bool]):
    return [not(x) for x in bits]
    
def eight_bit_full_adder(carry_in: bool, bits1: tuple[bool], bits2: tuple[bool]) -> ("carry", list):
    data = [0, [0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(7, -1, -1):
        var = one_bit_full_adder(carry_in, bits1[i], bits2[i])
        data[1][i] = bool(var[1])
        carry_in = var[0]
    data[0] = carry_in
    return data

def eight_bit_full_substractor(bits1: tuple[bool], bits2: tuple[bool]) -> ("carry", list):
    return eight_bit_full_adder(True, bits1, inverter(bits2))


# print(eight_bit_full_adder(0, (0,0,1,0,1,1,1,0), (0,1,1,0,0,1,0,1)))
# print(eight_bit_full_adder(0, (0,0,0,0,0,0,0,1), (0,0,0,0,0,0,0,1)))
# print(eight_bit_full_substractor((0,1,1,1,0,1,0,1), (0,0,0,1,1,0,0,0)))
