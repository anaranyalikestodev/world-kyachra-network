from flask import request, session, redirect, url_for, render_template
from flask import current_app,Blueprint,flash
auth_bp = Blueprint("auth_bp", __name__, template_folder="templates")

@auth_bp.route("/login/<chapter>",methods=["GET","POST"])
def login(chapter):

    if request.method=="POST":
        key=request.form.get("key")
        if key==current_app.config.get("ADMIN_KEY"): 
            session["admin"] = True
            return redirect(url_for("notice_bp.index"))
        else:
            flash('Invalid admin key','danger')
    if chapter=='wkn1':
        return render_template("login.html", chapter=chapter)
    elif chapter=='wkn2':
        return render_template("login.html", chapter=chapter)