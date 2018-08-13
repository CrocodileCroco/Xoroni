import pyttsx3
import webbrowser
engine = pyttsx3.init()

#engine.say("test 1")
#engine.runAndWait()
#engine.say("test 2")
#engine.runAndWait()
def dire(texte):
    print(texte)
    engine.say(texte)
    engine.runAndWait()

def urlie(siteinternet):
    webbrowser.open(siteinternet, new=2)


dire("Bonjour, je suis xoroni, une intelligence artificielle créé par LL Productions FR")
dire("J'ai été créé dans le but de prouver qu'il est possible de faire une i a comme cortana")
dire("Donnez moi quelque chose a faire, je vous aiderai")
dire("Que voulez vous?")
while True:
    xoroc = input("Votre Commande : ")
    if xoroc.startswith("tu es") or xoroc.startswith("Tu es"):
        dire("Je ne savais pas ça! Cool!")

    if xoroc == "truelle":
        dire("que la truelle soit en vous!")

    if xoroc == "ora":
        dire("ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ")

    if xoroc == "joue de la musique" or xoroc == "Joue de la musique":
        dire("tata tatatita tatata")

    if xoroc == "dadyday":
        dire("la 3d de dadyday, elle est vraiment meilleure, en marché, en livré, puis enfin de mes mains, la 3d de dadyday, a moitié déguisé")

    if xoroc.startswith("z0r "):
        z0rde = xoroc
        z0rde = z0rde[4:]
        dire("Ok, j'ouvre zor " + z0rde + " pour vous")
        urlie("https://z0r.de/" + z0rde)

    if xoroc.startswith("dire "):
        moidire = xoroc
        moidire = moidire[5:]
        dire(moidire)