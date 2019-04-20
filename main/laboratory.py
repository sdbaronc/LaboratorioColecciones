"""
Solución del laboratorio
"""
print("Bienvenido a la plataforma de informacion del Observatorio Nacional de Meteorología UPB.")
import statistics
from custom_functions import temperature_methods

santander=[38,32,34,35,36,32,27,23,31,20,30,28]
narinho=[24,25,23,28,29,29,30,28,32,33,32,27]
guajira=[38,39,40,39,41,39,38,39,40,41,38,43]
nacional=[38,32,34,35,36,32,27,23,31,20,30,28,24,25,23,28,29,29,30,28,32,33,32,27,38,39,40,39,41,39,38,39,40,41,38,43]
mes=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
#parte "a" del problema
proms=temperature_methods.calculate_final_temperature(santander)
promn=temperature_methods.calculate_final_temperature(narinho)
promg=temperature_methods.calculate_final_temperature(guajira)

print("el promedio anual de temperaturas en el departamento de santander fue :" ,proms)
print("el promedio anual de temperaturas en el departamento de nariño  fue :" , promn)
print("el promedio anual de temperaturas en el departamento de la guajira fue :" ,promg )
#parte "b" del problema

promnal=temperature_methods.calculate_final_temperature(nacional)
print("el promedio de temperatura de los tres departamentos fue :" , promnal)
#parte "c" del problema

tempbests=temperature_methods.calculate_best_temperature(santander)
tempbestn=temperature_methods.calculate_best_temperature(narinho)
tempbestg=temperature_methods.calculate_best_temperature(guajira)
mestempbests=santander.index(tempbests)
mestempbestn=narinho.index(tempbestn)
mestempbestg=guajira.index(tempbestg)


print("el mes con mayor temperatura en el departamento de santander fue :" ,mes[mestempbests]," con una temperatura de :", tempbests)
print("el mes con mayor temperatura en el departamento de nariño fue :" , mes[mestempbestn], " con una temperatura de :", tempbestn)
print("el mes con mayor temperatura en el departamento de la guajira fue :",mes[mestempbestg], " con una temperatura de :" , tempbestg)

#parte "d" del problema
list_tempbest=[tempbestg,tempbestn,tempbests]
besttemp=temperature_methods.calculate_final_temperature(list_tempbest)

print("el promedio de las tempeeraturas mas calientes de todos los departamentos es :",besttemp)

#parte "e" del problema
list_bestprom=[proms,promn,promg]
bestprom=temperature_methods.calculate_best_temperature(list_bestprom)
print("el promedio mas caliente de todos los departamentos fue :",bestprom)

#parte "f" del problema
departamento=["guajira","nariño","santander"]
f={0:"enero",1:"febrero",2:"marzo",3:"abril",4:"mayo",5:"junio",6:"julio",7:"agosto",8:"septiembre",9:"octubre",10:"noviembre",11:"diciembre",12:"enero",13:"febrero",14:"marzo",15:"abril",16:"mayo",17:"junio",18:"julio",19:"agosto",20:"septiembre",21:"octubre",22:"noviembre",23:"diciembre",24:"enero",25:"febrero",26:"marzo",27:"abril",28:"mayo",29:"junio",30:"julio",31:"agosto",32:"septiembre",33:"octubre",34:"noviembre",35:"diciembre"}
best_f=temperature_methods.calculate_best_temperature(list_tempbest)
posicion=list_tempbest.index(best_f)
mes_f=nacional.index(best_f)
print("la temperatura mas caliente de tod el año fue : ",best_f , " en el departamento de :" ,departamento[posicion], " en el mes de :",f[mes_f])

#parte "g" del problema
desvia_s=statistics.stdev(santander)
desvia_n=statistics.stdev(narinho)
desvia_g=statistics.stdev(guajira)

print("la desviacion estandar de la temperatura en el departamento de santander fue :",desvia_s)
print("la desviacion estandar de la temperatura en el departamento de nariño fue :",desvia_n)
print("la desviacion estandar  de la temperatura en el departamento de la guajira fue :" ,desvia_g)