int num_equal_on_left(int K, int X, int A[], int N)
{
    int num_equal = 0;
    
    if(K <= 0)
    {
        return 0;
    }
    
    for(int i = 0; i < K && i < N; i++)
    {
        if(A[i] == X)
        {
            num_equal++;
        }
    }
    
    return num_equal;
}

int num_diff_on_right(int K, int X, int A[], int N)
{
    int num_diff = 0;
    
    for(int i = K; i < N; i++)
    {
        if(A[i] != X)
        {
            num_diff++;
        }
    }
    
    return num_diff;
}

int solution(int X, int A[], int N)
{
    int K = 0;
    
    int eol = num_equal_on_left(K, X, A, N);
    int dor = num_diff_on_right(K, X, A, N);
    
    while(K <= N)
    {
        if(eol == dor)
        {
            return K;
        }
        
        K++;
        
        // If I add a same to the left, increase eol.
        if(A[K-1] == X)
        {
            eol++;
        }
        // If I add a different to the left, decrease dor.
        else
        {
            dor--;
        }
    }
    
    // This is bad because there is alwasy supposed to be a unique answer for K
    return -1;
}
