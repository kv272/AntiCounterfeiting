def maximize_gems(n, d):
    d.sort()
    s_min, s_max = 0, 0
    g_min, g_max = d[0][1], d[0][1]

    for i in range(1, n):
        if d[i][0] == d[i - 1][0] + 1:
            g_min = min(g_min, d[i][1])
            g_max = max(g_max, d[i][1])
        else:
            s_min += g_min
            s_max += g_max
            g_min = d[i][1]
            g_max = d[i][1]

    s_min += g_min
    s_max += g_max
    return max(s_min, s_max)

if __name__ == "__main__":
    d = []
    n = int(input())
    aise = list(input().split())
    for _ in aise:
        day, gems = map(int, _.split(':'))
        d.append((day, gems))

    result = maximize_gems(n, d)
    print(result)
