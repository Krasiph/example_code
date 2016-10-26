def match_length(S, i):
    matches = 1
    
    while (i + 1) < len(S):
        current_domino = S[i].split('-')
        
        next_domino = S[i+1].split('-')
        
        if current_domino[1] != next_domino[0]:
            break
        
        else:
            matches += 1
        
        i += 1
    
    return matches


def domino(S):
    if len(S) > 0:
        largest_match = 1
    
    else:
        largest_match = 0
    
    dominos = S.split(',')
    
    for i in range(len(dominos)):
        ml = match_length(dominos, i)
        
        if ml > largest_match:
            largest_match = ml
    
    return largest_match


def print_result(S, res):
    print('{0} : {1}'.format(S, res))


if __name__ == '__main__':
    S = '1-1'
    
    print_result(S, domino(S))
    
    S = '1-2,2-1'
    
    print_result(S, domino(S))
    
    S = '3-2,2-1,1-4,4-4,5-4,4-2,2-1'
    
    print_result(S, domino(S))
    
    S = '5-5,5-5,4-4,5-5,5-5,5-5,5-5,5-5,5-5,5-5'
    
    print_result(S, domino(S))
    
