from flask import Flask, render_template

from data import title, unitList, unit_table

app = Flask(__name__)

#Render main page
@app.route("/")
def template():
    return render_template('index.html',
                           title=title,
                           unitlist=unitList)

#Render clothes type page
@app.route("/<unit_type>/")
def render_page(unit_type):
    drawData = unit_table(unit_type)
    return render_template('index.html',
                           title=title,
                           unit_type=unit_type,
                           unitlist=unitList,
                           drawData=drawData)

#Render simple ERROR page
@app.errorhandler(404)
def render_not_found(error):
    return "Sorry, error 404."

@app.errorhandler(500)
def render_server_error(error):
    return "Sorry, error 500. Something gone wrong, PLEASE RELOAD THIS PAGE."

# Launch server
if __name__ == '__main__':
    app.run()