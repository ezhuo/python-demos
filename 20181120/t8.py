def count(n):
    while n > 0:
        print('befour=%d',n)
        yield n     # 生成值: n
        n -= 1
        print('after=%d',n)


c = count(5)
c.__next__()
c.__next__()
