#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'heway'

import pymongo
from conf import starts

connection = pymongo.Connection('10.77.30.62', 27017)

#选择sina数据库
db_sina = connection.sina

#选择weibo_user文档集
col_weibo_user = db_sina.weibo_user

#对于本次的每一个种子用户，读取其粉丝和关注，选出双向关注的用户，作为下一批的种子用户
with open('expand_uid', 'w') as uid_file:
    for uid in starts:
        weibo_user = col_weibo_user.find_one({"uid": uid})
        fan_uids = set([fan['uid'] for fan in weibo_user['fans']])
        follow_uids = set([follow['uid'] for follow in weibo_user['follows']])
        co_uids = fan_uids&follow_uids
        print '实际粉丝数和关注数：', weibo_user['info']['n_fans'], weibo_user['info']['n_follows']
        print '爬取粉丝数和关注数：', len(fan_uids),len(follow_uids)
        print '相互关注数为：',len(co_uids)
        for co_uid in co_uids:
            uid_file.write(co_uid + '\n')

