import sys

from bus import *
from cache import *
from cpu import *

def main():
    # read in arguments in the future
    if len(sys.argv) != 6:
        print("Usage: python3 main.py <protocol> <input_file> <cache_size> <associativitiy> <block_size> ")
        print("E.g.: python3 main.py MESI bodytrack 1024 1 16\n")
        print("Arguments Received: ", " ".join(sys.argv))
        return
    
    # sys.argv
    protocol = sys.argv[1]
    input_file = sys.argv[2]
    cache_size = int(sys.argv[3])
    associativity = int(sys.argv[4])
    block_size = int(sys.argv[5])


    # TODO: Proper initialization of bus and cache
    bus = Bus()
    cpu_list: list[CPU] = []
    for i in range(1):
        cache = Cache()
        cpu = CPU(i, cache, bus, f"input/{input_file}_{i}.data")
        cpu_list.append(cpu)

    # Uncomment for sanity check
    # for c in cpu_list:
    #     c.print_instructions()
    
    # Run the cpu until instructions are exhausted
    runnable = True
    while runnable:
        runnable = False
        for c in cpu_list:
            runnable |= c.run_cycle()
        # bus operations?
    
    # print cpu statistics, cache statistics
    # bus statistics
    # for c in cpu_list:
    #     print(c)


main()