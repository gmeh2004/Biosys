#from pyairtable import Api
from pyairtable.orm import Model
from pyairtable.orm import fields


class Usuario(Model):
    clave=fields.TextField("clave")
    contra=fields.TextField("contra")
    nombre=fields.TextField("nombre")
    admin=fields.IntegerField("admin")

    class Meta:
        api_key="patexiSeAkNWrp1RI.23421ca4c84c65d5eef0ca65fcd9c08321d1f5cb07740523e61b2f7661bb156d"
        base_id="app7BQmX4AUxmErad"
        table_name="usuario"

class Bioenergia(Model):
    cultivo=fields.TextField("cultivo")
    parte=fields.TextField("parte")
    cantidad=fields.FloatField("cantidad")
    area=fields.FloatField("area")
    energia=fields.FloatField("energia")
    municipio=fields.SelectField("municipio")
    latitud=fields.FloatField("latitud")
    longitud=fields.FloatField("longitud")


    class Meta:
        api_key="patexiSeAkNWrp1RI.23421ca4c84c65d5eef0ca65fcd9c08321d1f5cb07740523e61b2f7661bb156d"
        base_id="app7BQmX4AUxmErad"
        table_name="bioenergia"

#cacao=Bioenergia(
    #cultivo="Cacao",
    #parte="Bagazo",
    #cantidad=35.0,
    #area=123.0,
    #energia=5.0,
  #  municipio="Cunduacan",
  #  latitud=18.076169,
 #   longitud=19.04321
#)
#cacao.save()

#
#api=Api("patexiSeAkNWrp1RI.23421ca4c84c65d5eef0ca65fcd9c08321d1f5cb07740523e61b2f7661bb156d")
#tabla=api.table("app7BQmX4AUxmErad","usuario")

#Altas
#yo={'clave': 'estrada',
 #'contra': 'estrada', 
 #'nombre': 'Gloria Estrada',
 # 'admin': 1
#}
#tabla.create(yo)

#Consultas
#registros=tabla.all()
#for r in registros:
#    print(r["fields"])