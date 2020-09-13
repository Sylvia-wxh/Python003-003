import pandas as pd
import numpy as np

# dates = pd.date_range('20200131', periods=12, freq='M')
# s1 = pd.Series(dates)

df1 = pd.DataFrame([[89, 90, 'gold'],
                    [187, 77, 'gold'],
                    [52, 61, 'silver'],
                    [52, 93, 'bronze'],
                    [3369, 21, 'silver'],
                    [10, 99, 'silver'],
                    [7981, 10, 'gold'],
                    [187, 28, 'bronze'],
                    [187, 98, 'silver'],
                    [349, 56, 'bronze'],
                    [955, 47, 'bronze'],
                    [65577, 1, 'silver']], columns=['id', 'age', 'planet'])

df2 = pd.DataFrame([[89, 'tom', 'tv'],
                    [187, 'jack', 'tv'],
                    [52, 'peter', 'basketball'],
                    [52, 'amy', 'diving'],
                    [3369, 'jenny', 'dance'],
                    [10, 'candy', 'singing'],
                    [7981, 'jason', 'basketball'],
                    [623, 'lilian', 'basketball'],
                    [7, 'tracy', 'diving'],
                    [349, 'yasmeen', 'hiking'],
                    [955, 'frank', 'dance'],
                    [65577, 'wayne', 'sleeping']], columns=['id', 'name', 'hobby'])

# print('原始s1数据：\n{}'.format(s1))
print('原始df1数据：\n{}'.format(df1))
print('原始df2数据：\n{}'.format(df2))

print('SELECT * FROM data的翻译: \n{}'.format(df1))

print('SELECT * FROM data LIMIT 10的翻译: \n{}'.format(df1.head(10)))

print('SELECT id FROM data的翻译: \n{}'.format(df1['id']))

print('SELECT * FROM data WHERE id<1000 AND age>30的翻译: \n{}'.format(
    df1.loc[(df1['id'] < 1000) & (df1['age'] > 30)]))

print('SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id的翻译: \n{}'.format(
    pd.merge(df1, df2, left_on='id', right_on='id', how='inner')))

print(
    'SELECT * FROM table1 UNION SELECT * FROM table2的翻译: \n{}'.format(pd.concat([df1, df2])))

print('DELETE FROM table1 WHERE id=10的翻译: \n{}'.format(df1.drop(df1[df1['id']==10].index)))

print('SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id的翻译: \n{}'.format(
    df1.groupby('id')['planet'].nunique()))

print('ALTER TABLE table1 DROP COLUMN column_name的翻译: \n{}'.format(
    df1.drop('planet', axis=1)))
