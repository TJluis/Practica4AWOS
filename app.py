from flask import flask, render_template, request, jsonify, make_response, session
app = Flask(__name__)

@app.route('/producto')
def productos():
    import mysql.connector
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="concencionario"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM concencionaria")
    myresult = mycursor.fetchall()
    return make_response(jsonify(myresult))

