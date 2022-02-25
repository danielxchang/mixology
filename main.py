from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from cocktail import *


app = Flask(__name__)
Bootstrap(app)


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/cocktails', defaults={'letter': 'a'})
@app.route('/cocktails/<letter>')
def cocktails(letter):
    return render_template('cocktails.html', letter=letter, cocktails=cocktails_dict)


@app.route('/cocktail/<int:cocktail_id>')
def show_cocktail(cocktail_id):
    return render_template('drink.html',
                           cocktail=look_up_cocktail(cocktail_id),
                           column_dict_key_pairs=[("Alcoholic", "strAlcoholic"),
                                                  ("Glass Type", "strGlass"),
                                                  ("Ingredients", "strIngredient"),
                                                  ("Instructions", "strInstructions")],
                           str=str
                           )


@app.route('/random')
def get_random():
    random_cocktail = get_random_cocktail()
    return redirect(url_for("show_cocktail", cocktail_id=random_cocktail['idDrink']))


if __name__ == '__main__':
    cocktails_dict = get_all_cocktails()
    app.run()
