from collections import defaultdict
from math import prod


devices = dict()
flipflops = defaultdict(int)
conjuctions = defaultdict(dict)

for line in open("input.txt"):
    source, _, *destinations = line.replace(",", "").split()
    type, source = (source[0], source[1:]) if source[0] in "%&" else ("", source)

    devices[source] = type, destinations

    for destination in destinations:
        conjuctions[destination][source] = 0
        if destination == "rx": rx = source

rx_ins = {source: 0 for source in conjuctions[rx]}

presses = 0
counts = [0, 0]

while True:
    if presses == 1000:
        print("part 1:", prod(counts))
    presses += 1

    if all(rx_ins.values()):
        print("part 2:", prod(rx_ins.values()))
        break

    queue = [(None, "broadcaster", 0)]
    while queue:
        source, mod, pulse_in = queue.pop(0)
        counts[pulse_in] += 1

        if mod not in devices: continue
        type, nexts = devices[mod]

        match type, pulse_in:
            case "", _:
                pulse_out = pulse_in
            case "%", 0:
                pulse_out = flipflops[mod] = not flipflops[mod]
            case "&", _:
                conjuctions[mod][source] = pulse_in
                pulse_out = not all(conjuctions[mod].values())

                if "rx" in nexts:
                    for k, v in conjuctions[mod].items():
                        if v: rx_ins[k] = presses
            case _,_: continue

        for n in nexts:
            queue.append((mod, n, pulse_out))
