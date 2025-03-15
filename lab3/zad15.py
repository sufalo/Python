def najdluzszy_wspolny_podciag(napis1, napis2):
    n = len(napis1)
    m = len(napis2)
    
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if napis1[i - 1] == napis2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    wynik = ""
    i, j = n, m
    
    while i > 0 and j > 0:
        if napis1[i - 1] == napis2[j - 1]:
            wynik = napis1[i - 1] + wynik
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return wynik

s1 = "abcbdab"
s2 = "bdcabb"
print(najdluzszy_wspolny_podciag(s1, s2))
