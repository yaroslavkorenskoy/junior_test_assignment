from flask import Flask, render_template

from data import title, unitList, unit_table

app = Flask(__name__)


# Render main page
@app.route("/")
def template():
    return render_template('index.html',
                           title=title,
                           unitlist=unitList)


# Render clothes type page
@app.route("/<unit_type>/")
def render_page(unit_type):
    draw_data = unit_table(unit_type)
    return render_template('index.html',
                           title=title,
                           unit_type=unit_type,
                           unitlist=unitList,
                           drawData=draw_data)


# Render simple ERROR page
@app.errorhandler(404)
def render_not_found(error):
    return render_template('error.html',
                           title=title,
                           unit_type=unit_type,
                           error=error)


@app.errorhandler(500)
def render_server_error(error):
    return render_template('error.html',
                           title=title,
                           unitlist=unitList,
                           error=error)


if __name__ == '__main__':
    app.run()
