int get_left_side_sum(int A[], int N, int P)
{
    int sum = 0;
    
    if(P <= 0)
    {
        return 0;
    }
    
    for(int i = 0; i < P && i < N; i++)
    {
        sum = sum + A[i];
    }
    
    return sum;
}

int get_right_side_sum(int A[], int N, int P)
{
    int sum = 0;
    
    for(int i = P + 1; i < N; i++)
    {
        sum = sum + A[i];
    }
    
    return sum;
}

int solution(int A[], int N)
{
    /*
        P is the equilibrium index such that:
            0 <= P < N
            sum(0 to P-1) == sum(P+1 to N-1)
    */
    int P = 0;
    
    // Get the initial sums
    int lss = get_left_side_sum(A, N, P);
    int rss = get_right_side_sum(A, N, P);
    
    while(P < N)
    {
        if(lss == rss)
        {
            return P;
        }
        
        P++;
        
        lss = lss + A[P-1];
        
        rss = rss - A[P];
    }
    
    return -1; // no equilibrium index
}