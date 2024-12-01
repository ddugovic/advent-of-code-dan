"""
--- Day 16: Packet Decoder ---
https://adventofcode.com/2021/day/16
"""
import math
from aocd import data

def pop(bits, length):
    """Pop first length bits from binary string"""
    return (bits[0:length], bits[length:])

def popint(bits, length):
    """Pop first length bits from binary string"""
    return (int(bits[0:length], 2), bits[length:])

def poprun(bits):
    """Pop run from binary string"""
    number = ""
    while bits[0] == '1':
        number, bits = number + bits[1:5], bits[5:]
    number, bits = number + bits[1:5], bits[5:]
    return (int(number, 2), bits)

def parse(bits):
    """Parse bits as packets"""
    packets = []
    version, bits = popint(bits, 3)
    typeid, bits = popint(bits, 3)
    if typeid == 4:
        value, bits = poprun(bits)
        packets.append((version, value))
    else:
        bit, bits = pop(bits, 1)
        if bit == '0':
            length, bits = popint(bits, 15)
            run, bits = pop(bits, length)
            while len(run) >= 6:
                packet, run = parse(run)
                packets.extend(packet)
        else:
            number, bits = popint(bits, 11)
            for _ in range(number):
                packet, bits = parse(bits)
                packets.extend(packet)
        if typeid == 0:
            value = sum([packet[1] for packet in packets])
        elif typeid == 1:
            value = math.prod([packet[1] for packet in packets])
        elif typeid == 2:
            value = min([packet[1] for packet in packets])
        elif typeid == 3:
            value = max([packet[1] for packet in packets])
        elif typeid == 5:
            value = 1 if packets[0][1] > packets[1][1] else 0
        elif typeid == 6:
            value = 1 if packets[0][1] < packets[1][1] else 0
        elif typeid == 7:
            value = 1 if packets[0][1] == packets[1][1] else 0
        version += sum([packet[0] for packet in packets])
        packets = [(version, value)]
    return (tuple(packets), bits)

def solve():
    """Decode the structure of your hexadecimal-encoded BITS transmission; what do you get if you add up the version numbers in all packets?

    What do you get if you evaluate the expression represented by your hexadecimal-encoded BITS transmission?"""

    packets = []
    for line in data.splitlines():
        bits = ''.join(bin(int(ch, 16))[2:].zfill(4) for ch in line)
        packets.extend(parse(bits)[0])

    print("part a:", sum(packet[0] for packet in packets))
    print("part b:", packets[-1][1])

if __name__ == "__main__":
    solve()
