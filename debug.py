import pysnooper
import numpy as np

@pysnooper.snoop()
def multi_matmul(times):
    x = np.random.rand(2, 2)
    w = np.random.rand(2, 2)

    for i in range(times):
        x = np.matmul(x, w)
    return x

multi_matmul(3)

#作者：七月在线 七仔
#链接：https://www.zhihu.com/question/62220477/answer/677734227
#来源：知乎
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
