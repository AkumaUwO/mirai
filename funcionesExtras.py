import wikipedia

def normalize(texto):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        texto = texto.replace(a, b).replace(a.upper(), b.upper())
    return texto

def funcionPrincipal(respuestaIA, entradaUsuario):

	keywords = ['busca', 'significado', 'de', 'en', 'el', 'wikipedia']
	if 'wikipedia:' in respuestaIA:
		try:
			lista = entradaUsuario.split(' ')
			for i in keywords:
				lista = list(filter((i).__ne__, lista))
			search = ' '.join(lista)
			buscar = normalize(search)
			print(buscar)
			wikipedia.set_lang("es")
			wiki = wikipedia.summary(buscar.lower(), 1)
			return respuestaIA + wiki
		except:
			return "Lo siento no encontre esa información"
	else:
		return respuestaIA

