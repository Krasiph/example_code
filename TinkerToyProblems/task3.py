# UP AND RIGHT
def move_right_up(a, b):
    return a + 1, b + 2

def move_up_right(a, b):
    return a + 2, b + 1

# UP AND LEFT
def move_left_up(a, b):
    return a + 1, b - 2

def move_up_left(a, b):
    return a + 2, b - 1

# DOWN AND RIGHT
def move_right_down(a, b):
    return a - 1, b + 2

def move_down_right(a, b):
    return a - 2, b + 1

# DOWN AND LEFT
def move_left_down(a, b):
    return a - 1, b - 2

def move_down_left(a, b):
    return a - 2, b - 1

def solution(A, B):
    if A < -100000000 or B < -100000000 \
    or A > 100000000 or B > 100000000:
        return -1
    
    turns = 0
    
    ca = 0
    cb = 0
    
    while ca != A and cb != B:
        up = False
        right = False
        
        if abs(A - ca) > 3 \
        and abs(B - cb) > 3:
            if A > ca:
                up = True
            
            if B > cb:
                right = True
            
            # double move
            if up:
                if right:
                    ca, cb = move_right_up(ca, cb)
                    ca, cb = move_up_right(ca, cb)
                
                else:
                    ca, cb = move_left_up(ca, cb)
                    ca, cb = move_up_left(ca, cb)
            
            else:
                if right:
                    ca, cb = move_right_down(ca, cb)
                    ca, cb = move_down_right(ca, cb)
                
                else:
                    ca, cb = move_left_down(ca, cb)
                    ca, cb = move_down_left(ca, cb)
            
            # extra turn for double move
            turns += 1
        
        else:
            if A > ca:
                up = True
            
            if B > cb:
                right = True
            
            if up:
                if right:
                    if abs(A - ca) < abs(B - cb):
                        ca, cb = move_right_up(ca, cb)
                    
                    else:
                        ca, cb = move_up_right(ca, cb)
                
                else:
                    if abs(A - ca) < abs(B - cb):
                        ca, cb = move_left_up(ca, cb)
                    
                    else:
                        ca, cb = move_up_left(ca, cb)
            
            else:
                if right:
                    if abs(A - ca) < abs(B - cb):
                        ca, cb = move_right_down(ca, cb)
                    
                    else:
                        ca, cb = move_down_right(ca, cb)
                
                else:
                    if abs(A - ca) < abs(B - cb):
                        ca, cb = move_left_down(ca, cb)
                    
                    else:
                        ca, cb = move_down_left(ca, cb)
        
        turns += 1
        
        # can't get there? return -1
        # @TODO how do I detect this?
        
        if turns > 100000000:
            return -2
    # end while
    
    return turns
