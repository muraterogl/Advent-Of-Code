from math import prod
with open('day16/input.txt') as f:q=f.readlines()

def parse(inp):
	global p1
	packetVersion, typeId, rest = inp[:3], inp[3:6], inp[6:]
	typeId = int(typeId, 2)
	p1 += int(packetVersion, 2)
	subpackets = []
	if typeId == 4: #literal value
		binaryValue = ""
		while rest[0] != "0":
			currentPacket, rest = rest[1:5], rest[5:]
			binaryValue += currentPacket
		currentPacket, rest = rest[1:5], rest[5:]
		binaryValue += currentPacket
		return int(binaryValue, 2), rest
	else:
		lengthTypeId, rest = rest[0], rest[1:]

		if lengthTypeId == "0":
			lengthOfPackets, rest = rest[:15], rest[15:]
			lengthOfPackets = int(lengthOfPackets, 2)
			originalRest = rest
			while len(originalRest)-len(rest)< lengthOfPackets:
				subpacket, rest = parse(rest)
				subpackets.append(subpacket)
		else:
			numOfPackets, rest = rest[:11], rest[11:]
			numOfPackets = int(numOfPackets, 2)
			for _ in range(numOfPackets):
				subpacket, rest = parse(rest)
				subpackets.append(subpacket)
		if typeId == 0:
			subpackets = sum(subpackets)
		elif typeId == 1:
			subpackets = prod(subpackets)
		elif typeId == 2:
			subpackets = min(subpackets)
		elif typeId == 3:
			subpackets = max(subpackets)
		elif typeId == 5:
			subpackets = 1 if subpackets[0] > subpackets[1] else 0
		elif typeId == 6:
			subpackets = 1 if subpackets[0] < subpackets[1] else 0
		elif typeId == 7:
			subpackets = 1 if subpackets[0] == subpackets[1] else 0
		return subpackets, rest

packet = q[0].rstrip()
packetBinary = "".join(bin(int(c,16))[2:].rjust(4, "0")for c in packet)

p1 = 0
p2 = parse(packetBinary)

print(f"part1: {p1}")
print(f"part2: {p2[0]}")