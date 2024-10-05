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
    def __init__(self, cache: Cache, bus: Bus, input_file: str) -> None:
        self.cache = cache
        self.bus = bus


    def run_cycle(self):
        if self.is_done():
            return
        
        self.total_cycle += 1
        if self.stalling:
            self.idle += 1
            self.stalling -= 1
        # execute instruction

        # cache hit, 1 cycle

        # cache miss 100 cycles

        # 

        # send message to bus if any

    def receive_message(self, messages):
        # To ensure cache coherence
        # For the bus to call when executing each timestep

        # to update cpu cache if there are any relevant messages
        pass

    def is_done(self):
        return True

