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
col_micro_blog = db_sina.micro_blog

def expand_next():
    #对于本次的每一个种子用户，读取其粉丝。
    # 过滤掉粉丝太多的，以防网络过渡膨胀，可能是公共账号；过滤掉关注太多，可能是类僵尸粉
    with open('expand_uid', 'w') as uid_file:
        for uid in starts:
            weibo_user = col_weibo_user.find_one({"uid": uid})
            fans = weibo_user['fans']

            count = 0
            not_count = 0
            for fan in fans:
                if int(fan['n_fans']) > 1000 or int(fan['n_fans']) < 50\
                                or int(fan['n_follows']) > 1000\
                                or int(fan['n_weibos']) < 100:
                    not_count += 1
                    print fan['nickname'].encode('utf-8'),  fan['n_follows'], fan['n_fans'],fan['n_weibos']
                else:
                    count += 1
                    uid_file.write(fan['uid'] + '\n')  # '    - uid: ' + fan['uid'] + '\n'

            print '\n输出个数 粉丝数过多个数', count, not_count

def expand_follow():
    out_mb = open('data/weibo', 'w')
    out_follower = open('data/follower', 'w')
    out_info = open('data/info', 'w')
    out_expand = open('expand_uid', 'w')
    weibo_users = col_weibo_user.find({"fans":{"$ne":[]}})
    for user in weibo_users:

    print weibo_users

if __name__ == "__main__":
    expand_follow()


