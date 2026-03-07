def fibonaci_series(n):
    a, b = 0, 1
    count = 0
    res = []
    while count < n:
        # print(a, end=' ')
        res.append(a)
        a, b = b, a + b
        count += 1
        
    print(res)
if __name__ == "__main__":
    fibonaci_series(10)