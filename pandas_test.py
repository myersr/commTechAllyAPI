# This file is a graveyard of tries and fails. Not relevant to the running server

import pandas as pd
import json
from glom import glom

obj = {}
with open('election_data.json') as infile:
    obj = json.loads(infile.read())
for x in obj.keys():
    for y in obj[x].keys():
        df = pd.DataFrame(obj[x][y])
        print(df)
# df = pd.read_json('election_data.json')
#
# # df.pivot(columns=df.head())
# ma_keys = [x for x in df.keys()]
# dd = pd.read_json('election_data.json', orient='values')
# print(df.info())
# print(dd.info())
# for x in ma_keys:
#     print(pd.json_normalize(df[x]))
#
#
# print('---------------------------')
# print(df)

summ = 0
# for x in df.keys():
#     print(x)
#     print(pd.DataFrame(df[x]))


# huuh = pd.DataFrame(df['Vermont']['Lake Adam'])
# hooh = pd.DataFrame(df['New Hampshire'])
# print(huuh.info())
# print(hooh.info())
# # scheme = pd.Series(pd.json_normalize(huuh['Republican']))
# # print(scheme.info())
# scheme2 = pd.Series(huuh['Democrat'])
# print(scheme2.info())
# # out = df['Vermont'].apply(lambda row: glom(row, 'Republicans.Strickland'))
#
# print(out)
# print(out.info)