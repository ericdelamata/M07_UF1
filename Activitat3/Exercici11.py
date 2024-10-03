divisas = {
    "Dolar estadounidense":"US$",
    "Euro":"€",
    "Yen japonés":"¥",
    "Libra esterlina":"£",
    "Dolar australiano":"A$",
    "Dolar canadiense":"C$",
    "Franco suizo":"CHF",
    "Renminbi/yuan chino":"元",
    "Dolar de Hong Kong":"HK$",
    "Dolar de Nueva Zelanda":"NZ$",
    "Corona sueca":"kr",
    "Won surcoreano":"₩",
    "Dolar de Singapur":"S$",
    "Corona noruega":"kr",
    "Peso mexicano":"$",
    "Rupia india":"₹",
    "Rublo ruso":"₽",
    "Rand sudafricano":"R",
    "Lira turca":"₺",
    "Real brasileño":"R$",
    "Nuevo dolar taiwanés":"NT$",
    "Corona danesa":"kr",
    "Złoty polaco":"zł",
    "Baht tailandés":"฿",
    "Rupia indonesia":"Rp",
    "Florin hungaro":"Ft",
    "Corona checa":"Kč",
    "Nuevo shekel israelí":"₪",
    "Peso chileno":"CLP$",
    "Peso filipino":"₱",
}
div = input("Pon el nombre de la divisa que quieras saber: ")
if divisas.get(div):
    print(divisas[div])
else:
    print("Esta divisa no esta")