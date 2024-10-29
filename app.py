from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        number = request.form.get("number")
        
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contacts (name, number) VALUES (?, ?)", (name, number))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))
    
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search():
    search_name = request.args.get("search_name")
    search_result = None
    
    if search_name:
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        cursor.execute("SELECT number FROM contacts WHERE name = ?", (search_name,))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            search_result = result[0]
    
    return render_template("index.html", search_result=search_result, search_name=search_name)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)