

# the dictionary class implementation
class Dict2:
    def __init__(self):
        self.keys = []
        self.values = []
    
    def __setitem__(self, key, value):
        if key in self.keys:
            index = self.keys.index(key)
            self.values[index] = value
        else:
            self.keys.append(key)
            self.values.append(value)
    
    def __getitem__(self, key):
        if key in self.keys:
            index = self.keys.index(key)
            return self.values[index]
        else:
            raise KeyNotFoundException(f"Key '{key}' not found")
    
    def __iter__(self):
        return iter(self.keys)



# the custom exception class
class KeyNotFoundException(Exception):
    pass


