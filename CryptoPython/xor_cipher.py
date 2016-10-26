
def toggle_bytes(byte_array, key):
    i = 0
    
    while i < len(byte_array):
        j = 0
        
        while j < len(key):
            if i >= len(byte_array):
                j = len(key)
                continue
            
            byte_array[i] ^= key[j]
            i += 1
            j += 1
    
    return