from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

@app.route("/")
def quote():

    conn = psycopg2.connect(
        host="localhost",
        database="quote",
        user="postgres",
        password="hda182526"
    )
    curs = conn.cursor()
    if request.method == "POST":
        nama = request.form.get("id")
        detail = request.form.get("quote")
        query = f"insert into quote(id, quote) values('{id}', '{quote}')"
        curs.execute(query)
        conn.commit()

    print(request.method)
    query = f"select * from quote order by id desc"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
    return render_template("quote.html", context=data)

if __name__ == "__main__":
    app.run()