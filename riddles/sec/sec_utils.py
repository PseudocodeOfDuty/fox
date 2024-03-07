from bitarray import bitarray


def circular_shift(bits, shift):
    return bits[shift:] + bits[:shift]


def hexer(bits):
    bits = "".join(map(str, bits))
    return hex(int(bits, 2))[2:].upper()


def bytes_to_bits(bytes):
    bits = bitarray()
    bits.frombytes(bytes)
    return bits


def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]
