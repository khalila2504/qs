from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hewan():

    conn = psycopg2.connect(
        host="localhost",
        database="hewan",
        user="postgres",
        password="hda182526"
    )
    curs = conn.cursor()
    if request.method == "POST":
        nama = request.form.get("nama")
        kingdom = request.form.get("kingdom")
        filum = request.form.get("filum")
        kelas = request.form.get("kelas")
        ordo = request.form.get("ordo")
        famili = request.form.get("famili")
        genus = request.form.get("genus")
        spesies = request.form.get("spesies")
        query = f"insert into taksonomi(nama, kingdom, filum, kelas, ordo, famili, genus, spesies) values('{nama}', '{kingdom}', '{filum}', '{kelas}', '{ordo}', '{famili}', '{genus}', '{spesies}')"
        curs.execute(query)
        conn.commit()

    print(request.method)
    query = f"select * from taksonomi order by id desc"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
    return render_template("cape.html", context=data)
    

@app.route("/delete/<taksonomi_id>")
def delete(taksonomi_id):
    conn = psycopg2.connect(
        host="localhost",
        database="hewan",
        user="postgres",
        password="hda182526"
    )
    curs = conn.cursor()
    query = f"delete from taksonomi where id = {taksonomi_id}"
    curs.execute(query)
    conn.commit()
    curs.close()
    conn.close()
    return redirect("/")

@app.route("/update/<taksonomi_id>", methods=["GET", "POST"])
def update(taksonomi_id):
    conn = psycopg2.connect(
        host="localhost",
        database="hewan",
        user="postgres",
        password="hda182526"
    )
    curs = conn.cursor()
    if request.method == "POST":
        nama = request.form.get("nama")
        kingdom = request.form.get("kingdom")
        filum = request.form.get("filum")
        kelas = request.form.get("kelas")
        ordo = request.form.get("ordo")
        famili = request.form.get("famili")
        genus = request.form.get("genus")
        spesies = request.form.get("spesies")
        query = f"update taksonomi set nama = '{nama}', kingdom = '{kingdom}', filum = '{filum}', kelas = '{kelas}', ordo = '{ordo}', famili = '{famili}', genus = '{genus}', spesies = '{spesies}') values('{nama}', '{kingdom}', '{filum}', '{kelas}', '{ordo}', '{famili}', '{genus}', '{spesies}')"
        curs.execute(query)
        conn.commit()
        return redirect ("/")
 
    query = f"select * from taksonomi where id = {taksonomi_id}"
    curs.execute(query)
    data = curs.fetchone()
    # conn.commit()
    curs.close
    conn.close
    return render_template("update.html", context=data)
if __name__ == "__main__":
    app.run()