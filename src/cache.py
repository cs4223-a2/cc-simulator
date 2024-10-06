import math
from collections import OrderedDict
from cache_block import CacheBlock

#https://cache-calculator.yahyasohail.com/

class Cache:
    def __init__(self, size: int, associativity: int, block_size: int, word_size: int = 32):
        self.size = size
        self.associativity = associativity
        self.block_size = block_size

        self.sets = size // (associativity * block_size)
        self.offset_bits = (block_size.bit_length() - 1)
        self.index_bits = (self.sets.bit_length() - 1) 
        self.tag_bits = word_size - self.offset_bits - self.index_bits

        print('==cache info==')
        print(f'sets: {self.sets}, offset_nbits: {self.offset_bits}, index_nbits: {self.index_bits}, tag_nbits: {self.tag_bits}')
        print()

        # Cache statistics
        self.hits = 0
        self.misses = 0

    def get_tag_index_offset(self, address):
        offset_mask = (1 << self.offset_bits) - 1
        offset = address & offset_mask
        
        index_mask = (1 << self.index_bits) - 1
        index = (address >> self.offset_bits) & index_mask
        
        tag = address >> (self.offset_bits + self.index_bits)
        
        return tag, index, offset

    # Access C[Address]
    def access(self, address):
        pass
    
    # Store C[Address]
    def store(self, address):
        pass