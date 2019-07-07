import pymysql

import secret
import config
from models.base_model import SQLModel
from models.comment import Comment
from models.test_model import Test
from models.session import Session
from models.user_role import UserRole
from models.user import User
from models.todo_ajax import TodoAjax
from models.weibo import Weibo
from utils import log


def recreate_table(cursor):
    cursor.execute(Test.sql_create)
    cursor.execute(User.sql_create)
    cursor.execute(Session.sql_create)
    cursor.execute(TodoAjax.sql_create)
    cursor.execute(Weibo.sql_create)
    cursor.execute(Comment.sql_create)


def recreate_database():

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password=secret.mysql_password,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        with connection.cursor() as cursor:

            cursor.execute(
                'DROP DATABASE IF EXISTS `{}`'.format(
                    config.db_name
                )
            )
            cursor.execute(
                'CREATE DATABASE `{}` DEFAULT CHARACTER SET utf8mb4'.format(
                    config.db_name
                )
            )
            cursor.execute('USE `{}`'.format(config.db_name))
            recreate_table(cursor)


        connection.commit()
    finally:
        connection.close()


def fake_data():
    log('fake data')
    SQLModel.init_db()

    Test.new({})

    form1 = dict(
        username='zjt',
        password='123',
        role=UserRole.normal,
    )
    form2 = dict(
        username='abc',
        password='abc',
        role=UserRole.normal,
    )
    u2, result = User.register(form1)
    u1, result = User.register(form2)

    Session.add(u1.id)
    Session.add(u2.id)

    form = dict(
        title='test todo ajax',
    )
    t = TodoAjax.add(form, u1.id)

    # weibo
    form1 = dict(
        content="weibo test user zjt",
        user_id=u1.id,
    )
    form2 = dict(
        content="weibo test user abc",
        user_id=u2.id,
    )
    w1 = Weibo.add(form1, u1.id).id
    w2 = Weibo.add(form2, u2.id).id
    w1 = Weibo.add(form1, u2.id).id
    w2 = Weibo.add(form2, u1.id).id

    # comment
    form1 = dict(
        content="weibo test user zjt",
        user_id=u1.id,
        weibo_id=w1,
    )
    form2 = dict(
        content="weibo test user abc",
        user_id=u2.id,
        weibo_id=w1,
    )
    # comment
    form3 = dict(
        content="weibo test user zjt",
        user_id=u1.id,
        weibo_id=w2,
    )
    form4 = dict(
        content="weibo test user abc",
        user_id=u2.id,
        weibo_id=w2,
    )
    Comment.new(form1)
    Comment.new(form2)
    Comment.new(form3)
    Comment.new(form4)


    SQLModel.connection.close()

if __name__ == '__main__':
    recreate_database()
    fake_data()
