from flask import Blueprint
from flask import render_template, request
from jinja2 import TemplateNotFound
import random

import apps.crypto.classic.shift as shiftcipher
import apps.crypto.classic.substitution as substitutioncipher
import apps.crypto.classic.affine as affinecipher
import apps.crypto.classic.vigenere as vigenerecipher
import apps.crypto.classic.hill as hillcipher
import apps.crypto.classic.permutation as permutationcipher

import apps.crypto.analysis as analysis

bp = Blueprint("routes", __name__)


@bp.route("/")
def route_default():
    return render_template("routes/index.html", segment="index")


@bp.route("/shift", methods=["POST", "GET"])
def shift():

    if "criptoanalisis" in request.form:

        texto_cifrado = request.form["texto_cifrado"]

        frequency = analysis.frequency(request.form["texto_cifrado"])
        bigrams = analysis.bigrams(request.form["texto_cifrado"])
        trigrams = analysis.trigrams(request.form["texto_cifrado"])

        return render_template(
            "routes/shift.html",
            texto_cifrado=texto_cifrado,
            frequency=frequency,
            bigrams=bigrams,
            trigrams=trigrams,
            segment="shift",
            tab="criptoanalisis",
        )

    if "ataque" in request.form:

        texto_cifrado = request.form["texto_cifrado"]

        return render_template(
            "routes/shift.html",
            texto_cifrado=texto_cifrado,
            segment="shift",
            tab="ataque",
        )

    clave = request.form["clave"]

    if clave != "":

        if "cifrar" in request.form:

            texto_claro = request.form["texto_claro"]
            texto_cifrado = shiftcipher.cifrar(request.form["texto_claro"], clave)

        elif "descifrar" in request.form:

            texto_claro = shiftcipher.descifrar(request.form["texto_cifrado"], clave)
            texto_cifrado = request.form["texto_cifrado"]

    else:
        texto_claro = request.form["texto_claro"]
        texto_cifrado = request.form["texto_cifrado"]

    if "generar-clave" in request.form:

        texto_claro = request.form["texto_claro"]
        texto_cifrado = request.form["texto_cifrado"]
        clave = random.choice(range(0, 26))

    elif "limpiar" in request.form:

        texto_claro = ""
        texto_cifrado = ""
        clave = ""

    return render_template(
        "routes/shift.html",
        texto_claro=texto_claro,
        clave=clave,
        texto_cifrado=texto_cifrado,
        segment="shift",
        tab="primary",
    )


@bp.route("/substitution", methods=["POST", "GET"])
def substitution():

    if "criptoanalisis" in request.form:

        texto_cifrado = request.form["texto_cifrado"]

        frequency = analysis.frequency(request.form["texto_cifrado"])
        bigrams = analysis.bigrams(request.form["texto_cifrado"])
        trigrams = analysis.trigrams(request.form["texto_cifrado"])

        return render_template(
            "routes/substitution.html",
            texto_cifrado=texto_cifrado,
            frequency=frequency,
            bigrams=bigrams,
            trigrams=trigrams,
            segment="substitution",
            tab="criptoanalisis",
        )

    if "ataque" in request.form:

        texto_cifrado = request.form["texto_cifrado"]

        return render_template(
            "routes/substitution.html",
            texto_cifrado=texto_cifrado,
            segment="substitution",
            tab="ataque",
        )

    clave = request.form["clave"]

    if clave != "":

        if "cifrar" in request.form:

            texto_claro = request.form["texto_claro"]
            texto_cifrado = substitutioncipher.cifrar(
                request.form["texto_claro"], clave
            )

        elif "descifrar" in request.form:

            texto_claro = substitutioncipher.descifrar(
                request.form["texto_cifrado"], clave
            )
            texto_cifrado = request.form["texto_cifrado"]

    else:
        texto_claro = request.form["texto_claro"]
        texto_cifrado = request.form["texto_cifrado"]

    if "generar-clave" in request.form:

        texto_claro = request.form["texto_claro"]
        texto_cifrado = request.form["texto_cifrado"]
        abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        clave = "".join(random.sample(abc, len(abc)))

    elif "limpiar" in request.form:

        texto_claro = ""
        texto_cifrado = ""
        clave = ""

    return render_template(
        "routes/substitution.html",
        texto_claro=texto_claro,
        clave=clave,
        texto_cifrado=texto_cifrado,
        segment="substitution",
        tab="primary",
    )


@bp.route("/affine", methods=["POST", "GET"])
def affine():

    if "criptoanalisis" in request.form:

        texto_cifrado = request.form["texto_cifrado"]

        frequency = analysis.frequency(request.form["texto_cifrado"])
        bigrams = analysis.bigrams(request.form["texto_cifrado"])
        trigrams = analysis.trigrams(request.form["texto_cifrado"])

        return render_template(
            "routes/affine.html",
            texto_cifrado=texto_cifrado,
            frequency=frequency,
            bigrams=bigrams,
            trigrams=trigrams,
            segment="affine",
            tab="criptoanalisis",
        )

    if "ataque" in request.form:

        texto_cifrado = request.form["texto_cifrado"]

        return render_template(
            "routes/affine.html",
            texto_cifrado=texto_cifrado,
            segment="affine",
            tab="ataque",
        )

    clave_a = request.form["clave_a"]
    clave_b = request.form["clave_b"]

    if "" not in [clave_a, clave_b]:
        if "cifrar" in request.form:

            texto_claro = request.form["texto_claro"]
            texto_cifrado = affinecipher.cifrar(
                request.form["texto_claro"], clave_a, clave_b
            )
            print(analysis.occurrence(texto_cifrado))
            print("asdf")

        elif "descifrar" in request.form:

            texto_claro = affinecipher.descifrar(
                request.form["texto_cifrado"], clave_a, clave_b
            )
            texto_cifrado = request.form["texto_cifrado"]

    else:
        texto_claro = request.form["texto_claro"]
        texto_cifrado = request.form["texto_cifrado"]

    if "generar-clave" in request.form:

        texto_claro = request.form["texto_claro"]
        texto_cifrado = request.form["texto_cifrado"]
        clave_a = random.choice([1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25])
        clave_b = random.choice(range(0, 26))

    elif "limpiar" in request.form:

        texto_claro = ""
        texto_cifrado = ""
        clave_a = ""
        clave_b = ""

    return render_template(
        "routes/affine.html",
        texto_claro=texto_claro,
        clave_a=clave_a,
        clave_b=clave_b,
        texto_cifrado=texto_cifrado,
        segment="affine",
        tab="primary",
    )


@bp.route("/vigenere", methods=["POST", "GET"])
def vigenere():

    if "criptoanalisis" in request.form:

        texto_cifrado = request.form["texto_cifrado"]

        frequency = analysis.frequency(request.form["texto_cifrado"])
        bigrams = analysis.bigrams(request.form["texto_cifrado"])
        trigrams = analysis.trigrams(request.form["texto_cifrado"])

        return render_template(
            "routes/vigenere.html",
            texto_cifrado=texto_cifrado,
            frequency=frequency,
            bigrams=bigrams,
            trigrams=trigrams,
            segment="vigenere",
            tab="criptoanalisis",
        )

    if "ataque" in request.form:

        texto_cifrado = request.form["texto_cifrado"]

        return render_template(
            "routes/vigenere.html",
            texto_cifrado=texto_cifrado,
            segment="vigenere",
            tab="ataque",
        )

    clave = request.form["clave"]

    if clave != "":

        if "cifrar" in request.form:

            texto_claro = request.form["texto_claro"]
            texto_cifrado = vigenerecipher.cifrar(request.form["texto_claro"], clave)

        elif "descifrar" in request.form:

            texto_claro = vigenerecipher.descifrar(request.form["texto_cifrado"], clave)
            texto_cifrado = request.form["texto_cifrado"]

    else:
        texto_claro = request.form["texto_claro"]
        texto_cifrado = request.form["texto_cifrado"]

    if "limpiar" in request.form:

        texto_claro = ""
        texto_cifrado = ""
        clave = ""

    return render_template(
        "routes/vigenere.html",
        texto_claro=texto_claro,
        clave=clave,
        texto_cifrado=texto_cifrado,
        segment="vigenere",
        tab="primary",
    )


@bp.route("/hill", methods=["POST", "GET"])
def hill():

    if "criptoanalisis" in request.form:

        texto_cifrado = request.form["texto_cifrado"]

        frequency = analysis.frequency(request.form["texto_cifrado"])
        bigrams = analysis.bigrams(request.form["texto_cifrado"])
        trigrams = analysis.trigrams(request.form["texto_cifrado"])

        return render_template(
            "routes/hill.html",
            texto_cifrado=texto_cifrado,
            frequency=frequency,
            bigrams=bigrams,
            trigrams=trigrams,
            segment="hill",
            tab="criptoanalisis",
        )

    if "ataque" in request.form:

        texto_cifrado = request.form["texto_cifrado"]

        return render_template(
            "routes/hill.html",
            texto_cifrado=texto_cifrado,
            segment="hill",
            tab="ataque",
        )

    clave_00 = request.form["clave_00"]
    clave_01 = request.form["clave_01"]
    clave_02 = request.form["clave_02"]
    clave_03 = request.form["clave_03"]
    clave_04 = request.form["clave_04"]
    clave_10 = request.form["clave_10"]
    clave_11 = request.form["clave_11"]
    clave_12 = request.form["clave_12"]
    clave_13 = request.form["clave_13"]
    clave_14 = request.form["clave_14"]
    clave_20 = request.form["clave_20"]
    clave_21 = request.form["clave_21"]
    clave_22 = request.form["clave_22"]
    clave_23 = request.form["clave_23"]
    clave_24 = request.form["clave_24"]
    clave_30 = request.form["clave_30"]
    clave_31 = request.form["clave_31"]
    clave_32 = request.form["clave_32"]
    clave_33 = request.form["clave_33"]
    clave_34 = request.form["clave_34"]
    clave_40 = request.form["clave_40"]
    clave_41 = request.form["clave_41"]
    clave_42 = request.form["clave_42"]
    clave_43 = request.form["clave_43"]
    clave_44 = request.form["clave_44"]

    matrix = [
        [clave_00, clave_01, clave_02, clave_03, clave_04],
        [clave_10, clave_11, clave_12, clave_13, clave_14],
        [clave_20, clave_21, clave_22, clave_23, clave_24],
        [clave_30, clave_31, clave_32, clave_33, clave_34],
        [clave_40, clave_41, clave_42, clave_43, clave_44],
    ]

    matrix = [x for x in [[int(j) for j in i if j != ""] for i in matrix] if x != []]

    if clave_00 != "" and all(len(row) == len(matrix) for row in matrix):

        if "cifrar" in request.form:

            texto_claro = request.form["texto_claro"]
            texto_cifrado = hillcipher.cifrar(request.form["texto_claro"], matrix)

        elif "descifrar" in request.form:

            texto_claro = hillcipher.descifrar(request.form["texto_cifrado"], matrix)
            texto_cifrado = request.form["texto_cifrado"]

    else:
        texto_claro = request.form["texto_claro"]
        texto_cifrado = request.form["texto_cifrado"]

    if "limpiar" in request.form:

        texto_claro = ""
        texto_cifrado = ""
        clave_00 = ""
        clave_01 = ""
        clave_02 = ""
        clave_03 = ""
        clave_04 = ""
        clave_10 = ""
        clave_11 = ""
        clave_12 = ""
        clave_13 = ""
        clave_14 = ""
        clave_20 = ""
        clave_21 = ""
        clave_22 = ""
        clave_23 = ""
        clave_24 = ""
        clave_30 = ""
        clave_31 = ""
        clave_32 = ""
        clave_33 = ""
        clave_34 = ""
        clave_40 = ""
        clave_41 = ""
        clave_42 = ""
        clave_43 = ""
        clave_44 = ""

    return render_template(
        "routes/hill.html",
        texto_claro=texto_claro,
        clave_00=clave_00,
        clave_01=clave_01,
        clave_02=clave_02,
        clave_03=clave_03,
        clave_04=clave_04,
        clave_10=clave_10,
        clave_11=clave_11,
        clave_12=clave_12,
        clave_13=clave_13,
        clave_14=clave_14,
        clave_20=clave_20,
        clave_21=clave_21,
        clave_22=clave_22,
        clave_23=clave_23,
        clave_24=clave_24,
        clave_30=clave_30,
        clave_31=clave_31,
        clave_32=clave_32,
        clave_33=clave_33,
        clave_34=clave_34,
        clave_40=clave_40,
        clave_41=clave_41,
        clave_42=clave_42,
        clave_43=clave_43,
        clave_44=clave_44,
        texto_cifrado=texto_cifrado,
        segment="hill",
        tab="primary",
    )


@bp.route("/permutation", methods=["POST", "GET"])
def permutation():

    if "criptoanalisis" in request.form:

        texto_cifrado = request.form["texto_cifrado"]

        frequency = analysis.frequency(request.form["texto_cifrado"])
        bigrams = analysis.bigrams(request.form["texto_cifrado"])
        trigrams = analysis.trigrams(request.form["texto_cifrado"])

        return render_template(
            "routes/permutation.html",
            texto_cifrado=texto_cifrado,
            frequency=frequency,
            bigrams=bigrams,
            trigrams=trigrams,
            segment="permutation",
            tab="criptoanalisis",
        )

    if "ataque" in request.form:

        texto_cifrado = request.form["texto_cifrado"]

        return render_template(
            "routes/permutation.html",
            texto_cifrado=texto_cifrado,
            segment="permutation",
            tab="ataque",
        )

    clave = request.form["clave"]

    if clave != "":

        if "cifrar" in request.form:

            texto_claro = request.form["texto_claro"]
            texto_cifrado = permutationcipher.cifrar(request.form["texto_claro"], clave)

        elif "descifrar" in request.form:

            texto_claro = permutationcipher.descifrar(
                request.form["texto_cifrado"], clave
            )
            texto_cifrado = request.form["texto_cifrado"]

    else:
        texto_claro = request.form["texto_claro"]
        texto_cifrado = request.form["texto_cifrado"]

    if "generar-clave" in request.form:

        texto_claro = request.form["texto_claro"]
        texto_cifrado = request.form["texto_cifrado"]
        m = random.randrange(10)
        clave = ",".join([str(i) for i in random.sample(range(m), m)])

    elif "limpiar" in request.form:

        texto_claro = ""
        texto_cifrado = ""
        clave = ""

    return render_template(
        "routes/permutation.html",
        texto_claro=texto_claro,
        clave=clave,
        texto_cifrado=texto_cifrado,
        segment="permutation",
        tab="primary",
    )


@bp.route("/<template>")
def route_template(template):

    try:

        if not template.endswith(".html"):
            template += ".html"

        # Detect the current page
        segment = request.path.split("/")[-1]

        # Serve the file (if exists) from app/templates/routes/*.html
        return render_template("routes/" + template, segment=segment, tab="primary")

    except TemplateNotFound:
        return render_template("routes/page-404.html"), 404

    except:
        return render_template("routes/page-500.html"), 500
