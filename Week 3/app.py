# =================================
# ENTERPRISE PASSWORD GENERATOR
# DecodeLabs Project 3
# =================================

import string
import secrets
import math
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "decodelabs_p3_secure_key"


@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    entropy = 0
    strength_label = ""
    strength_class = ""

    if request.method == "POST":
        try:

            length = int(request.form.get("length", 16))
            use_upper = "uppercase" in request.form
            use_lower = "lowercase" in request.form
            use_digits = "digits" in request.form
            use_symbols = "symbols" in request.form

            if not (use_upper or use_lower or use_digits or use_symbols):
                flash("Error: You must select at least one character type.", "error")
                return redirect(url_for("index"))

            if length < 8 or length > 128:
                flash("Error: Length must be between 8 and 128 characters.", "error")
                return redirect(url_for("index"))

            pool = ""
            if use_upper:
                pool += string.ascii_uppercase
            if use_lower:
                pool += string.ascii_lowercase
            if use_digits:
                pool += string.digits
            if use_symbols:
                pool += string.punctuation

            char_list = [secrets.choice(pool) for _ in range(length)]
            password = "".join(char_list)

            pool_size = len(pool)
            entropy = length * math.log2(pool_size)

            if entropy < 50:
                strength_label, strength_class = "Weak (Vulnerable)", "weak"
            elif entropy < 80:
                strength_label, strength_class = "Moderate (Standard)", "moderate"
            elif entropy < 120:
                strength_label, strength_class = "Strong (Secure)", "strong"
            else:
                strength_label, strength_class = (
                    "Uncrackable (Enterprise)",
                    "enterprise",
                )

        except ValueError:
            flash("Invalid input detected. Please try again.", "error")
            return redirect(url_for("index"))

    return render_template(
        "index.html",
        password=password,
        entropy=round(entropy, 2),
        strength_label=strength_label,
        strength_class=strength_class,
    )


if __name__ == "__main__":
    app.run(debug=True)
