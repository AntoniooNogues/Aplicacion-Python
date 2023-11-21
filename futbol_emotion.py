import requests
import bs4
productos_plantilla = {
        "nombre": "",
        "marca": "",
        "precio": "",
        "imagen": "",
        "url": "",
        "descripcion": "",
        "tipo_suela": "",
    }
productos_finales = []


def obtener_contenido_web():
    pagina_web = requests.get("https://www.futbolemotion.com/es/categoria/futbol-sala/zapatillas-de-futbol-sala").content
    soup = bs4.BeautifulSoup(pagina_web, "html.parser")
    return soup
def extraer_informacion():
    soup = obtener_contenido_web()
    elemento_principal = soup.find_all("article", {"class": "col-12 col-md-8 col-xxl-6 my-3 producto-listado position-relative px-1"})
    for elemento in elemento_principal:
        nombre = elemento.find("h3", {"class": "producto-listado-nombre fw-bold m-0 font-size-weight-bold"}).text
        imagen = elemento.find("img")["src"]
        marca = elemento.find("div", {"class": "producto-listado-marca position-absolute blend-multiply"}).find("img")["alt"]
        url = elemento.find("a", {"class": "text-secondary d-block"})["href"]
        """if nombre == "Zapatilla Mundial" or nombre == "Zapatilla React Gato" or nombre =="Zapatilla Street Gato" or nombre =="Zapatilla Lunar Gato II" or nombre == "Zapatilla Street Gato Niño" or nombre=="Zapatilla Zoom Mercurial Vapor 15 Academy IC Niño" or nombre=="Zapatilla Legend 10 Academy IC" or nombre=="Zapatilla Copa Gloro IN" or imagen=="https://www.futbolemotion.com/imagesarticulos/216366/medianas/zapatilla-kelme-precision-rojo-azul-1.jpg" or nombre=="Zapatilla FS Reactive":
            precio = float(elemento.find("div", {"class": "precio fw-bolder fs-5 font-style-currency"}).text.replace("€", "").replace(",", ".").strip())
        else:
            precio = float(elemento.find("div", {"class": "precio-rebajado fw-bolder fs-5 text-danger font-style-currency"}).text.replace("€", "").replace(",", ".").strip())"""

        #Sacar informacion detallada de cada producto
        pagina_detalles = requests.get(url).content
        soup_detalles = bs4.BeautifulSoup(pagina_detalles, "html.parser")
        descripcion = soup_detalles.find("p", {"class": "descripcion"}).text.replace("\n","")

        if nombre == "Zapatilla Copa Gloro IN":
            continue
        else:
            tipo_suela = soup_detalles.find("div", {"class": "col-lg-12 media my-4 align-items-center row m-0"}).find("p", {"class": "mt-2"}).text

        #Meter en el diccionario la informacion del producto.
        productos = productos_plantilla.copy()
        productos["nombre"] = nombre
        productos["marca"] = marca
        productos["imagen"] = imagen
        productos["url"] = url
        productos["descripcion"] = descripcion
        productos["tipo_suela"] = tipo_suela

        productos_finales.append(productos)
    #Devolver la lista de los productos con toda su informacion
    return productos_finales

#Quitar la llamada a la hora de llamar al script para la bdd
