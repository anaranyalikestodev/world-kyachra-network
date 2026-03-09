from flask import Blueprint, render_template, redirect, url_for, flash
from flask import abort,request,jsonify,session

from models.wkn1.notice import db, Notice
from flask_login import current_user

notice_bp = Blueprint("notice_bp", __name__, template_folder="templates")

@notice_bp.before_request
def protect_notices():
    if not session.get("admin"):
        return redirect("auth/login")
        
# READ (Home Page)
@notice_bp.route("/")
def index():
    notices = Notice.query.order_by(Notice.issued_at.desc()).all()
    return render_template("wkn1/noticeboard.html", notices=notices, title="House of Kyachra")

# CREATE
@notice_bp.route("/create", methods=["GET", "POST"])
def create_notice():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        issued_by=request.form.get("issued_by").strip()
        # Validation
        if not title or not content or not issued_by:
            flash("Fields cannot be empty", "danger")
            return render_template(
                "wkn1/cu.html",
                title="Create Notice",
                title_value=title,
                content_value=content,issued_by=issued_by
            )

        new_notice = Notice(title=title, content=content,issued_by=issued_by)
        db.session.add(new_notice)
        db.session.commit()

        flash("Notice created successfully!", "success")
        return redirect(url_for("notice_bp.index"))

    return render_template("wkn1/cu.html", title="Create Notice")

# EDIT
@notice_bp.route("/edit/<int:id>", methods=["GET"])
def edit(id):
    notice = Notice.query.get_or_404(id)
    return render_template(
        "wkn1/cu.html",
        title="Edit Notice",
        notice=notice
    )

# UPDATE
@notice_bp.route("/update/<int:id>", methods=["POST"])
def update_notice(id):
    notice = Notice.query.get_or_404(id)

    title = request.form.get("title", "").strip()
    content = request.form.get("content", "").strip()

    if not title or not content:
        flash("Fields cannot be empty", "danger")
        return render_template(
            "wkn1/cu.html",
            title="Edit Notice",
            notice=notice
        )

    notice.title = title
    notice.content = content
    db.session.commit()

    flash("Notice updated successfully!", "success")
    return redirect(url_for("notice_bp.index"))

# DELETE
@notice_bp.route("/delete/<int:id>", methods=["POST"])
def delete_notice(id):
    notice = Notice.query.get_or_404(id)
    db.session.delete(notice)
    db.session.commit()

    flash("Notice deleted successfully!", "success")
    return redirect(url_for("notice_bp.index"))