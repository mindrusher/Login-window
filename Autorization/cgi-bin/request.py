#!/usr/bin/env python3
import pyodbc

class Request:
    def __init__(self):
        self.conn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=DESKTOP-CS77PCT;"
        "Database=Test;"
        "Trusted_Connection=yes;"
    )

    def get_log_pas(self, log, pas):
        cursor = self.conn.cursor()
        cursor.execute("select * from tab")
        rows = cursor.fetchall()
        for row in rows:
            login = row[0].replace(' ', '')
            password = row[1].replace(' ', '')
            if log == login and pas == password:
                self.conn.close()
                success = """<!DOCTYPE HTML>
<html>
<head>
    <meta charset="utf-8">
    <title>Обработка данных форм</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <div class="container">
        <div class="form-row">
            <div class="alert alert-success alert-message text-center" role="alert">
                <h4 class="alert-heading">{}, Авторизация прошла успешно!</h4>
                <hr>
                <p class="mb-0">Вы будете переведены на другую страницу.</p>
            </div>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>""".format(login)
                return success

            else:
                fail = """<!DOCTYPE HTML>
<html>
<head>
    <meta charset="utf-8">
    <title>Обработка данных форм</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <div class="container">
        <div class="form-row">
            <div class="alert alert-danger text-center" role="alert">
                <h4 class="alert-heading">Неправильный логин или пароль</h4>
            </div>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>"""
        self.conn.close()
        return fail 

# req = Request()
# a = req.get_log_pas('1q', '2w')
# print(a)





