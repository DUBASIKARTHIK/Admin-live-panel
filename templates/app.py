from flask import Flask, render_template

app = Flask(__name__)



url = "https://kgmvprtxxvkaavqziwpx.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtnbXZwcnR4eHZrYWF2cXppd3B4Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3MTM0MTIyMCwiZXhwIjoyMDg2OTE3MjIwfQ.3N3nLWx7ZnfvSCdQOAbCn9TWByxCTep5Ycm3HVUigfI"
# ===============================
# USER WEBSITE ROUTES
# ===============================

# Login page
@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")


# User dashboard (matches list)
@app.route("/dashboard")
def dashboard():
    return render_template("admin_dashboard.html")


# ⭐ ADMIN MATCH SCORING PAGE (NEXT STEP READY)
@app.route("/admin/match/<int:match_id>")
def admin_match(match_id):
    return render_template("admin_match.html", match_id=match_id)




# ===============================
# RUN APP
# ===============================
if __name__ == "__main__":
    app.run(debug=True)
