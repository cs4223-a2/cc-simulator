import argparse

class SimulationParameters:
    def __init__(self, protocol, input_file, cache_size, associativity, block_size):
        self.protocol = protocol
        self.input_file = input_file
        self.cache_size = cache_size
        self.associativity = associativity
        self.block_size = block_size

    def __str__(self):
        return (f"Simulation Parameters\n"
                f"  Protocol: {self.protocol}\n"
                f"  Input File: {self.input_file}\n"
                f"  Cache Size: {self.cache_size} bytes\n"
                f"  Associativity: {self.associativity}-way\n"
                f"  Block Size: {self.block_size} bytes")

def parse_args():
    parser = argparse.ArgumentParser(description="Cache Coherence Simulator")

    DEFAULT_ASSOCIATIVITY = 2
    DEFAULT_CACHE_BLOCK_SIZE = 32   # unit: bytes
    DEFAULT_WORD_SIZE = 32          # unit: bits
    DEFAULT_CACHE_SIZE = 4 * 1024   # unit: bytes

    parser.add_argument("protocol", choices=["MESI", "Dragon"], help="Cache coherence protocol")
    parser.add_argument("input_file", help="Input benchmark file name")
    parser.add_argument("cache_size", type=int, nargs='?', default=DEFAULT_CACHE_SIZE, help="Cache size in bytes")
    parser.add_argument("associativity", type=int, nargs='?', default=DEFAULT_ASSOCIATIVITY, help="Cache associativity")
    parser.add_argument("block_size", type=int, nargs='?', default=DEFAULT_CACHE_BLOCK_SIZE, help="Cache block size in bytes")

    args = parser.parse_args()
    return SimulationParameters(args.protocol, args.input_file, args.cache_size, args.associativity, args.block_size)
