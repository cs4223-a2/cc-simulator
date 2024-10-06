import os
from .instruction import Instruction

class InstructionSource:
    def __init__(self, file):
        if not os.path.exists(file):
            raise FileNotFoundError(f"{file} does not exist.")

        self.file = file

    # Fetch instructions from source lazily
    def read_instructions(self):
        with open(self.file, 'r') as file:
            for line in file:
                label, value = line.split()
                instruction = Instruction(label, value)
                yield instruction