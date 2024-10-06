from bus import *
from cache import *


class CPU:
    # some self.statistics
    """
    # CPU
    total cycles (self)
    compute cycles (non load/store)
    num of load/store instr
    num of idle cycles

    ## Cache
    cache hit counts
    cache miss counts

    ## Bus
    data_traffic_on_bus (bytes) [only for data, not address]
    num_of_invalidation
    num_of_updates

    Distribution of access to private / shared data [?]

    """

    # connects to a bus

    # has a LRU cache

    # Accept and read a input file
    # Process the instructions as "requested" per time cycle
    def __init__(self, idx: int, cache: Cache, bus: Bus, input_file: str) -> None:
        self.idx = idx
        self.cache = cache
        self.bus = bus
        self.instructions = []
        self.instr_idx = 0
        with open(input_file, "r") as file:
            for l in file:
                # remove new line char
                self.instructions.append(l.strip("\n"))

        # initialize statistics
        self.load_store_instr = 0
        self.idling_cycles = 0
        self.non_load_store_cycles = 0
        self.total_cycle = 0
        self.stalling = 0


    def run_cycle(self) -> bool:
        if self.is_done():
            return False
        
        self.total_cycle += 1
        if self.stalling:
            self.stalling -= 1
        # execute instruction
        instr = self.instructions[self.instr_idx]
        label, value = instr.split()

        # need check if can execute this current instruction (single core just execute)
        self.instr_idx += 1
        
        # cache hit, 1 cycle

        # cache miss 100 cycles

        # 

        # send message to bus if any


        return True

    def receive_message(self, messages):
        # To ensure cache coherence
        # For the bus to call when executing each timestep

        # to update cpu cache if there are any relevant messages
        pass

    def is_done(self):
        return self.instr_idx >= len(self.instructions)
    
    # sanity function
    def print_instructions(self):
        limit = 0
        for i in self.instructions:
            if limit > 10:
                break
            print(i)
            limit += 1

