from flask import Flask  # klassen Flask brukes til å lage vår webapplikasjon
from flask import request  # brukes for å hente data/info fra http requestene.
from flask import render_template # For å generere html fra template fil.
import webbrowser

#   --  Lager en flask webapp.  --
app = Flask(__name__)


#   Denne instansen (app) brukes nedover for å knytte
#   de enkelte sidenes urler til en python funksjon.
#   
#   Python funksjonen tar imot requests for hver sin url
#   og har ansvar for å lage en html streng som returneres. 
#   Html-strengen er det vi får som svar i browseren vår.
#   Det er flere måter å generere html-sidene på:
#       - som vanlig streng. 
#       - fra template fil



###############################################################################
#
#       URL --> Funksjon 
#
###############################################################################


# Binder urler til python funksjoner  her blir urlen  localhost:5000
@app.route("/")
def index():
    """  
        Hello Web!  
        Her vises den enkleste måten å bruke flask på til å generere 
        hovedsiden vår. 
    """
    return "<h1> Hei bloggen</h1>"t


# URL: localhost:5000/cat
@app.route("/cat")
def cats():
    """ 
        Samme som ovenfor, men her viser man et bilde av en katt på en 
        annen url. 
    """
    return "<img src='https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTB5LeeuewHrocxsNFy4qrem1PBZvhLZElzAt8hYt0N0iDpWsmGba0qjA'>"


@app.route("/greetings/<name>")
def greetings(name):
    """
        Her demonstreres variabler i urlen. 
        
        :param name: Navnet på den man skal si hello til
        
        eksempler på urler som alle vil havne i denne funksjonen:
        localhost:5000/greetings/Silje
        localhost:5000/greetings/Lars
        localhost:5000/greetings/Ingeborg

    """
    return "Hello there %s" % name


#############################################################
#   
#       GET variabler
#
#############################################################

@app.route("/summer")
def summer():
    """
        Eksempel på å hente data fra query delen av urlen  (GET argumeneter)

        eksempler på urler som alle vil havne i denne funksjonen:
        localhost:5000/summmer?a=10&b=20
    """
    # Får inn to tall fra url-ens query del / GET argumenter. 
    a = request.args.get("a")
    b = request.args.get("b")
    # Kalkulasjoner utføres, vent litt...
    summen = int(a) + int(b)
    # Returnere en streng med resultatet
    return " %d + %d = %d" % (a, b, summen)



############################################################
#
#   TEMPLATE  -- Generere html fra template fil
#
############################################################

@app.route("/comment")
def comment():
    """ 
        Eksempel på å bruke render_template funksjonen for å genere 
        et kommentarfelt. HTML koden ligger i filen 
        kommentarfelt.html  som ligger i mappen templates.
    """
    return render_template("kommentarfelt.html")


# Spesifisere at denne funksjonen skal kunne ta imot POST og GET requests.
@app.route("/new-comment", methods=['POST', 'GET'])
def new_comment():
    """
        Eksempel på å ta imot en kommentar fra kommentarfeltet i forrige 
        funksjon. 

        Her demonstreres både Hvordan man 

    """
    if request.method == 'POST':
        # Henter navn og kommentar fra formen.
        name = request.form.get("name")
        comment = request.form.get("comment")
    # denne funksjonen vil nå ikke fungere dersom vi prøver å bruke GET
    # til å nå urlen localhost:5000/new-comment.
    # Vi kunne evt brukt:
    #
    # elif request.method == 'GET': 
    #   return "<b>Du må fylle ut en kommentar!</b>"
    # for å returnere noe html om man ikke har POSTet en kommentar. 

    # Legg merke til at vi sender inn variabler til templaten.
    return render_template("kommentar.html", name=name, comment=comment)


if __name__ == "__main__":
    # Åpner browseren DIN :).
    webbrowser.open("http://127.0.0.1:5000")
    # Starter en lokal webserver som er ment for testing og utvikling.
    # Den egner seg ikke til å kjøre siden "på ordentlig".
    app.run(debug=True)



