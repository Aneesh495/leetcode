func countValidSequences(n int, k int) int {
    const mod int64 = 1000000007
    factorial := make([]int64,n)
    factorial[0] = 1
    for i := 1; i < n; i++ { factorial[i] = factorial[i-1]*int64(i)%mod }
    choose := func(total, picked int) int64 {
        denominator := factorial[picked]*factorial[total-picked]%mod
        inverse := int64(1)
        for exponent := mod-2; exponent > 0; exponent >>= 1 {
            if exponent&1 != 0 { inverse = inverse*denominator%mod }
            denominator = denominator*denominator%mod
        }
        return factorial[total]*inverse%mod
    }
    total := choose(n-1,k-1)
    // Remove all-odd compositions by writing each selected value as 2a+1.
    if (n-k)%2 == 0 { total -= choose((n-k)/2+k-1,k-1) }
    return int((total+mod)%mod)
}