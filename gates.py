def orr(A: bool, B: bool) -> bool:
    return A or B
def aand(A: bool, B: bool) -> bool:
    return A and B
def xor(A: bool, B: bool) -> bool:
    return (A and not(B)) or (not(A) and B)