from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1/flower'
db = SQLAlchemy(app)

@app.route("/test")
def hello():
    from sqlalchemy import text
    sql = text("select * from user")
    result = db.engine.execute(sql)
    for row in result:
        app.logger.info(row)
    return "hello"
if __name__ == '__main__':
    app.run(debug=True)