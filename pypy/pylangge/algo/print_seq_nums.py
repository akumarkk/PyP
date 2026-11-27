if __name__ == "__main__":
    n = int(input())
    ret = 1
    m = 10
    for i in range(1, n+1):
        if i >= m:
            m = m*10
        ret = (ret * m) + i
        print(ret)
    print(ret)