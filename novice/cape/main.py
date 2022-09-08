from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def cape():

    conn = psycopg2.connect(
        host="localhost",
        database="cape",
        user="postgres",
        password="hda182526"
    )
    curs = conn.cursor()
    if request.method == "POST":
        nama = request.form.get("nama")
        actions = request.form.get("actions")
        query = f"insert into cape(nama, actions) values('{nama}', '{actions}')"
        curs.execute(query)
        conn.commit()

    print(request.method)
    query = f"select * from cape order by id desc"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
    return render_template("cape.html", context=data)
    
@app.route("/detail/<cape_id>") 
def detail(cape_id):
    conn = psycopg2.connect(
        host="localhost",
        database="cape",
        user="postgres",
        password="hda182526"
    )
    curs = conn.cursor()
    query = f"select * from cape where id = {cape_id}"
    curs.execute(query)
    data = curs.fetchone()
    curs.close()
    conn.close()
    print(data)
    return render_template("detail.html", context=data)

@app.route("/delete/<cape_id>")
def delete(cape_id):
    conn = psycopg2.connect(
        host="localhost",
        database="cape",
        user="postgres",
        password="hda182526"
    )
    curs = conn.cursor()
    query = f"delete from cape where id = {cape_id}"
    curs.execute(query)
    conn.commit()
    curs.close()
    conn.close()
    return redirect("/")

@app.route("/update/<cape_id>", methods=["GET", "POST"])
def update(cape_id):
    conn = psycopg2.connect(
        host="localhost",
        database="cape",
        user="postgres",
        password="hda182526"
    )
    curs = conn.cursor()
    if request.method == "POST":
        nama = request.form.get("nama")
        actions = request.form.get("actions")
        query = f"update cape set nama ='{nama}', actions = '{masalah}' where id = {cape_id}"
        curs.execute(query)
        conn.commit()
        return redirect("/")
    
    query = f"select * from cape where id = {cape_id}"
    curs.execute(query)
    data = curs.fetchone()
    # conn.commit()
    curs.close
    conn.close
    return render_template("update.html", context=data)
if __name__ == "__main__":
    app.run()