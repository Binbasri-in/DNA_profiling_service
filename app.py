import os


from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, hash_str

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///dna_str_db.db")

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show profile of user"""
    # get the user's id
    user_id = session["user_id"]
    # get the user's info
    user_info = db.execute("SELECT * FROM users WHERE id = ?;", user_id)
    # get the user's DNA STRs from the many-to-many table
    user_strs = db.execute("SELECT * FROM dna_str join dna_str_users on dna_str.id = dna_str_users.dna_str_id WHERE dna_str_users.user_id = ? ORDER BY owner_name;", user_id)

    # print the user's info
    #print(user_info)
    # print the user's DNA STRs
    #print(user_strs)
    # render the profile page
    return render_template("profile.html", user_info=user_info[0], user_strs=user_strs)



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("MISSING USERNAME")

        if not request.form.get("password"):
            return apology("MISSING PASSWORD")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?;", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        if not (username := request.form.get("username")):
            return apology("MISSING USERNAME")

        if not (password := request.form.get("password")):
            return apology("MISSING PASSWORD")

        if not (confirmation := request.form.get("confirmation")):
            return apology("PASSWORD DON'T MATCH")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?;", username)

        # Ensure username not in database
        if len(rows) != 0:
            return apology(f"The username '{username}' already exists. Please choose another name.")

        # Ensure first password and second password are matched
        if password != confirmation:
            return apology("password not matched")

        # Insert all into database
        id = db.execute("INSERT INTO users (username, hash, lab_name, lab_address, lab_city, lab_state, lab_zip, lab_phone, lab_email) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);",
                    username, generate_password_hash(password), request.form.get("lab_name"), 
                    request.form.get("lab_address"), request.form.get("lab_city"), request.form.get("lab_state"), 
                    request.form.get("lab_zip"), request.form.get("lab_phone"), request.form.get("lab_email"))

        # Remember which user has logged in
        session["user_id"] = id

        flash("Registered!")

        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/new", methods=["GET", "POST"])
@login_required
def new():
    """Add new DNA STR to the database"""
    
    if request.method == "POST":
        # when user submit the form
        if not (name := request.form.get("name")):
            return apology("MISSING NAME")

        if not (filename := request.form.get("filename")):
            return apology("MISSING FILENAME")
        STRs = ["AGATC", "TTTTTTCT", "AATG", "TCTAG", "GATA", "TATC", "GAAA", "TCTG"]
        count = []
        # get the STRs to the list
        for STR in STRs:
            count.append(int(request.form.get(STR)))
        # Add the new DNA STR to the database
        try:
            dna_id = db.execute("INSERT INTO dna_str (owner_name, hashed, AGATC, TTTTTTCT, AATG, TCTAG, GATA, TATC, GAAA, TCTG) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                    name, hash_str(count), count[0], count[1], count[2], count[3], count[4], count[5], count[6], count[7])

        except:
            return apology("The name already exists. Please choose another name.")
            
        # linke the user and the DNA STR in dna_str_users table
        db.execute("INSERT INTO dna_str_users (dna_str_id, user_id) VALUES (?, ?);", dna_id, session["user_id"])
        flash(name+" Added!")
        return redirect("/")
    else:
        return render_template("add_new.html")


@app.route("/find", methods=["GET", "POST"])
@login_required
def find():
    """Find the DNA STR in the database"""
    if request.method == "POST":
        # when user submit the form
        if not (filename := request.form.get("filename")):
            return apology("MISSING FILENAME")
        # get the STRs to the list
        STRs = ["AGATC", "TTTTTTCT", "AATG", "TCTAG", "GATA", "TATC", "GAAA", "TCTG"]
        count = []
        for STR in STRs:
            count.append(int(request.form.get(STR)))
        # find the DNA STR in the database
        rows = db.execute("SELECT * FROM dna_str WHERE hashed = ?;",hash_str(count))
        if len(rows) == 0:
            return apology("The DNA STR not found.")
        else:
            return render_template("found.html", row=rows[0])
    else:
        return render_template("find.html")


@app.route("/about", methods=["GET"])
@login_required
def about():
    """About the website"""
    return render_template("about.html")

# delete a given DNA STR
@app.route("/delete", methods=["GET", "POST"])
@login_required
def delete():
    """Delete the DNA STR"""
    if request.method == "POST":
        # when user submit the form
        if not (dna_id := request.form.get("id")):
            return apology("MISSING NAME")
        # delete the DNA STR
        print(dna_id)
        db.execute("DELETE FROM dna_str_users WHERE dna_str_id = ?;", dna_id)
        db.execute("DELETE FROM dna_str WHERE id = ?;", dna_id)
        flash("Deleted!")
        return redirect("/")
    else:
        return redirect("/")
