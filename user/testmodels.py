from user import models


def test_models_inert():
    models.insert('마이콜,'michol@gmail.com','1234,'male')

def test_models_findby_email_and_password():
    result = models_findby_email_and_password('michol@gmail.com')
