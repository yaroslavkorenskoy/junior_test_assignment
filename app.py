from flask import Flask, render_template

from data import title, subtitle, description, unitList, unit_table, database

app = Flask(__name__)

#Render main
@app.route("/")
def template():
    return render_template('index.html',
                           title=title,
                           subtitle=subtitle,
                           description=description,
                           unitlist=unitList,
                           database=database)

#Render page
@app.route("/<unit_type>/")
def render_page(unit_type):
    drawData = unit_table(unit_type)
    return render_template('index.html',
                           title=title,
                           unit_type=unit_type,
                           subtitle=subtitle,
                           description=description,
                           unitlist=unitList,
                           database=database,
                           drawData=drawData)

#Render ERROR
@app.errorhandler(404)
def render_not_found(error):
    return "Увы, ошибка 404. Ничего не нашлось! Вот неудача, отправляйтесь на главную!"

@app.errorhandler(500)
def render_server_error(error):
    return "Жаль, ошибка 500. Что-то не так, но мы все починим"

#Launch server
# if __name__ == '__main__':
#     app.run()
app.run()