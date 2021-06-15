from flask import Blueprint, g, render_template, request, session, url_for, redirect


admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("")
    else:
        admin_id = request.form['admin_id']
        admin_pw = request.form['admin_pw']

        if admin_id == "test" and admin_pw == "test":
            return redirect(url_for("index"))
        else:
            return render_template('admin/login.html')


@admin_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))
