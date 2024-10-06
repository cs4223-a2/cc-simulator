
from enum import Enum
from itertools import islice
import os
import sys

from bus import *
from cache import *
from cpu import *

import argparse

from instructions import Instruction, InstructionType
from instructions.instruction_source import InstructionSource
from simulation import parse_args

class dev_CPU:
    def __init__(self, sim_params):
        self.cycle_counter = 0
        self.compute_cycles = 0
        self.cache = Cache(sim_params.cache_size, sim_params.associativity, sim_params.block_size)

    def execute_instruction(self, instruction: Instruction):
        if instruction.getInstructionType() == InstructionType.OTHER:
            self.cycle_counter += instruction.getValue()
            self.compute_cycles += instruction.getValue()
        elif instruction.getInstructionType() == InstructionType.LOAD_:
            address = instruction.getValue()
            print(self.cache.get_tag_index_offset(address))

            if not self.cache.access(address):
                print(f"Cache miss for LOAD at address {address:#x}")



def main():
    _DEBUG_MAX_INSTRUCTIONS = 6

    sim_params = parse_args()
    reader = InstructionSource(sim_params.input_file)
    instructions = reader.read_instructions()
    
    cpu = dev_CPU(sim_params)

    for i in islice(instructions, _DEBUG_MAX_INSTRUCTIONS):
        print(i)
        cpu.execute_instruction(i)

    print(cpu.cycle_counter)
    print(cpu.compute_cycles)



    # # TODO: Proper initialization of bus and cache
    # bus = Bus()
    # cpu_list: list[CPU] = []
    # for i in range(1):
    #     cache = Cache()
    #     cpu = CPU(i, cache, bus, f"input/{input_file}_{i}.data")
    #     cpu_list.append(cpu)

    # # Uncomment for sanity check
    # # for c in cpu_list:
    # #     c.print_instructions()
    
    # # Run the cpu until instructions are exhausted
    # runnable = True
    # while runnable:
    #     runnable = False
    #     for c in cpu_list:
    #         runnable |= c.run_cycle()
    #     # bus operations?
    
    # # print cpu statistics, cache statistics
    # # bus statistics
    # # for c in cpu_list:
    # #     print(c)


if __name__ == "__main__":
    main()