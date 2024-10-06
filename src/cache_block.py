class CacheBlock:
    def __init__(self, address):
        self.address = address          # The starting address of the block
        self.valid = False              # Valid bit
        self.dirty = False              # Dirty bit

    def __repr__(self):
        return f"CacheBlock(addr={self.address}, valid={self.valid}, dirty={self.dirty})"
