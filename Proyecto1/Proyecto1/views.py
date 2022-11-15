from django.http import HttpResponse
from django.template import Template, Context
import os.path

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates/')

def saludo(request):
	return HttpResponse("Hola Django - Coder")


def probandoTemplate(self):

    miHtml = open(TEMPLATE_PATH+"/template.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)
