#!/usr/bin/env python3
# -*- coding:utf-8 -*--
broker_url = 'sqla+sqlite:///celerydb.sqlite'

# 使用pymysql连接数据库
result_backend = 'db+mysql+pymysql://root:123456@127.0.0.1:3306/drmp_db_2022'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Asia/Shanghai'
enable_utc = False
result_expires = 60 * 60 * 24 * 7  # 存储结果过期时间（默认7天）