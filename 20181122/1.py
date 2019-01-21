def yield_test(n):
    for i in range(n):
        print('yield before=')
        yield call(i)
        print('yield after=',"i=", i)
    # 做一些其它的事情
    print("do something.")
    print("end.")


def call(i):
    print('call=',i)
    return i*2


# 使用for循环
for i in yield_test(2):
    print('for i = ',i, "," , '=====================================')
