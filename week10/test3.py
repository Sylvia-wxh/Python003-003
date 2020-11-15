from snownlp import SnowNLP
import pandas as pd
import numpy as np

data = {'date':['11/13/2020', '11/14/2020', '11/14/2020', '11/14/2020'],
        'name':['test1', 'prod2', 'prod2', 'abc'],
        'comment':['好难买到', '我退单了', '抢到了吗', '再来一个'],}
df = pd.DataFrame(data)

comment = df[['comment']]
print(type(comment))

# for i in range(len(comment)):
#     s = comment[i]
#     print(s)
    # ana = SnowNLP(s)
    # print(list(ana.tags))