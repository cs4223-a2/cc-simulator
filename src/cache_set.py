from collections import OrderedDict

from cache_block import CacheBlock

class Cache_set:
    # index of cache blocks in a cache set is the same
    def __init__(self, associativity: int, block_size: int, word_size: int):
        self.cache = OrderedDict()
        self.capacity = associativity
        self.block_size = block_size
        self.word_size = word_size

    # return number of cycles required, if it is a cache hit
    # addr == tag here, since the offset & index is taken cared of in the cache
    def get(self, tag):
        if tag not in self.cache:
            # cache miss
            return self.put(self, tag)
        else:
            # cache hit
            self.cache.move_to_end(tag)
            return 1, True

    def put(self, tag):
        # write allocate
        cycles = 1
        is_cache_hit = True
        if tag not in self.cache:
            cache_block = CacheBlock(tag)
            self.cache[tag] = cache_block
            cycles += 100
            is_cache_hit = False
        else:
            # update dirty bit
            self.cache[tag].dirty = True # need to set valid to false? This part kind of dependant on the protocol

        self.cache.move_to_end(tag)
        if len(self.cache) > self.capacity:
            # write back logic? involving bus
            self.cache.popitem(last=False)
        return cycles, is_cache_hit