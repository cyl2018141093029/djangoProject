import pymysql
from django.db import models

pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()


class FixCharField(models.Field):
    # 自定义的char类型的字段类
    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        super().__init__(max_length=max_length, *args, **kwargs)

    def db_type(self, connection):
        # 限定生成的数据库表字段类型char，长度为max_length指定的值
        # :param connection:
        # :return:
        return 'char(%s)' % self.max_length
