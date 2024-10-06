from enum import Enum


class InstructionType(Enum):
    LOAD_ = 0    # Load (read)
    STORE = 1    # Store (write)
    OTHER = 2    # Other (computation, etc.)

class Instruction:
    # Instruction Type: LOAD/STORE/OTHER
    # Value: Memory Location / Cycles

    def __init__(self, label, value):
        self.instruction_type = InstructionType(int(label))
        self.value = int(value, 0)

    def __str__(self):
        return f"{self.instruction_type.name} | {hex(self.value)}"
    
    def __repr__(self):
        return self.__str__()
    
    def getInstructionType(self):
        return self.instruction_type
    
    def getValue(self):
        return self.value