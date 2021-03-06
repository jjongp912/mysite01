from MySQLdb import connect, OperationalError

from MySQLdb.cursors import DictCursor
from django.db import models

def conn():
    return connect(
        user='webdb',
        password='webdb',
        host='localhost',
        port=3306,
        db='webdb',
        charset='utf8')


def findall():
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor(DictCursor)

        # SQL 실행
        sql = '''
            select board.no, board.title, board.contents, board.hit,
                date_format(board.reg_date, '%Y-%m-%d %h:%i:%s') as reg_date,
                board.g_no, board.o_no, board.depth, board.user_no, user.name            
            from board
            left join user
            on board.user_no = user.no
            order by g_no desc,o_no asc, reg_date desc;
            '''
        cursor.execute(sql)

        # 결과 받아오기
        results = cursor.fetchall()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return results

    except OperationalError as e:
        print(f'error: {e}')

def findview(no):
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor(DictCursor)

        # SQL 실행
        sql = '''
            select no,title,contents,user_no          
            from board
            where no = %s;
            '''
        cursor.execute(sql,(no,))

        # 결과 받아오기
        results = cursor.fetchone()  #fetchall() 하면 안됨...

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return results

    except OperationalError as e:
        print(f'error: {e}')



def insert(title, contents, hit, g_no, o_no, depth, user_no):
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor()

        # SQL 실행
        sql = 'insert into board values(null, %s, %s, %s, now(), %s, %s, %s, %s);'
        count = cursor.execute(sql, (title, contents, hit, g_no, o_no, depth, user_no))

        # commit
        # insert, update, delete 후 commit 필요
        db.commit()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return count == 1

    except OperationalError as e:
        print(f'error: {e}')

def delete(no):
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor()

        # SQL 실행
        sql = 'delete from board where no = %s;'

        count = cursor.execute(sql,(no,))

        # commit
        db.commit()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return count == 1

    except OperationalError as e:
         print(f'error: {e}')

def update(title, contents, no):
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor()

        # SQL 실행
        sql = 'update board set title=%s, contents=%s where no=%s'
        count = cursor.execute(sql, (title, contents, no))

        # commit
        # insert, update, delete 후 commit 필요
        db.commit()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return count == 1

    except OperationalError as e:
        print(f'error: {e}')