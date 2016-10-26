def flatten_list(L):
    flat_list = []
    
    for e in L:
        if isinstance(e, list):
            flat_list += flatten_list(e)
        
        else:
            flat_list.append(e)
    
    return flat_list


def print_result(S, res):
    print('{0} : {1}'.format(S, res))


if __name__ == '__main__':
    L = [1,2,[3],[4,[5,6]],[[7]],8]
    
    print_result(L, flatten_list(L))
    
    L = [1,2,[3],[4,[5,6],5,6],[[7],[8,[9]]],10]
    
    print_result(L, flatten_list(L))
    
    L = [1,2,[3],[4,[5,6],5,6],[[7],[8,[9]]],10,[[[11],12]]]
    
    print_result(L, flatten_list(L))
