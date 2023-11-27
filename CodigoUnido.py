import math   #se importa maths 
import numpy as np # se importa numpy como "np"

#Tratamiento de datos por método Tukey
#importar bibliotecas
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd



#################### De aqui en adelante se definen cada una de las funciones para realizar conversión de unidades antes de realizar calculos mas avanzados

def MolaGramos(NumeroDeMoles: float, MasaMolar: float) -> float: #definimos la función para conversion mol a gramos
    molagramos = NumeroDeMoles * MasaMolar
    return molagramos

def GramosaMol(NumeroDeGramos: float, MasaMolar: float) -> float: #definimos la función para conversion gramos a mol
    gramosamol = NumeroDeGramos / MasaMolar
    return gramosamol

def LitroAMililitro(L: float) -> float: #definimos la función para conversion litro a mililitro
    LitroAMililitro = L * 1000
    return LitroAMililitro

def MililitroALitro(mL: float) -> float: #definimos la función para conversion mililitro a litro
    MililitroALitro = mL / 1000
    return MililitroALitro

def LitroAMetroCubico(L: float) -> float: #definimos la función para conversion litro a metro cubico
    LitroAMetroCubico = L / 1000
    return LitroAMetroCubico

def MetroCubicoAMililitro(m3: float) -> float: #definimos la función para conversion metro cubico a mililitro
    MetroCubicoAMililitro = m3 * 1000000
    return MetroCubicoAMililitro

def GramoAKilogramo(Gramos: float)->float: #definimos la función para conversion gramo a kilogramo
    GramoAKilogramo = Gramos / 1000
    return GramoAKilogramo

def KilogramoAGramo(Kilogramos: float)->float: #definimos la función para conversion kilogramo a gramo
    KilogramoAGramo = Kilogramos*1000
    return KilogramoAGramo

def GramoALibra(Gramos: float)->float: #definimos la función para conversion gramo a libra
    GramoALibra= Gramos/453.592
    return GramoALibra

def KilogramoALibras(Kilogramos: float)->float: #definimos la función para conversion kilogramo a libra
    KilogramoALibras = Kilogramos*2,204
    return KilogramoALibras

def AtmAmmHg(Atm: float)->float:
    AtmAmmHg = Atm*760
    return AtmAmmHg

def mmHgAAtm(mmHg: float)->float:
    mmHgAAtm = mmHg/760
    return mmHgAAtm

def KelvinAFahrenheit(Kelvin: float)->float:
    KelvinAFahrenheit = ((9/5)*(Kelvin-273.15)) + 32
    return KelvinAFahrenheit

def KelvinACelsius(Kelvin: float)->float:
    KelvinACelsius = Kelvin - 273.15
    return KelvinACelsius

def CelsiusAKelvin(Celsius: float)->float:
    CelsiusAKelvin = Celsius + 273.15
    return CelsiusAKelvin

def CelsiusAFahrenheit(Celsius: float)->float:
    CelsiusAFahrenheit =  ((9/5)*Celsius + 32)
    return CelsiusAFahrenheit

def FahrenheitACelsius(Fahrenheit: float)->float:
    FahrenheitACelsius = ((5/9)*(Fahrenheit-32))
    return FahrenheitACelsius

def FahrenheitAKelvin(Fahrenheit: float)->float:
    FahrenheitAKelvin =   ((Fahrenheit - 32)*(5/9)) + 273.15
    return FahrenheitAKelvin

def calcular_masa_compuesto(): #definir una función para calcular la masa del compuesto
    masas_molares ={
                    "H":1.01, "He":4.00, "Li":6.94, "Be": 9.01, "B":10.81, "C": 12.01, "N":14.00, "O": 16.00, "F": 19.00, "Ne": 20.18, 
                    "Na":23.00, "Mg": 24.30, "Al": 26.98, "Si": 28.09, "P": 30.97, "S":32.07, "Cl": 35.45, "Ar": 39.95, "K":39.10, 
                    "Ca": 40.08, "Sc": 44.96, "Ti": 47.87, "V": 50.94, "Cr":52.00, "Mn": 54.94, "Fe": 55.85, "Co": 58.93, "Ni": 58.69, 
                    "Cu": 63.55, "Zn": 65.41, "Ga": 69.72, "Ge": 72.61, "As":74.92, "Se": 78.96, "Br": 79.90, "Kr":83.80, "Rb":85.47, 
                    "Sr":87.62, "Y": 88.91, "Zr": 91.22, "Nb":92.91,"Mo":95.94, "Tc": 98.00, "Ru":101.07,"Rh": 102.91, "Pd": 106.42, 
                    "Ag": 107.87, "Cd": 112.41, "In": 114.82, "Sn":118.71, "Sb": 121.76, "Te":127.60, "I":126.90, "Xe":131.29, "Cs":132.90, 
                    "Ba": 137.33, "La": 138.90, "Ce":140.12, "Pr": 140.41, "Nd":144.24, "Pm":145.00, "Sm":150.36, "Eu": 151.96, "Gd": 157.25, 
                    "Tb": 158.92, "Dy": 162.50,"Ho":164.93, "Er": 167.26, "Tm": 168.93, "Yb": 173.04, "Hf": 178.49, "Ta": 180.95, "W": 183.84,
                    "Re": 186.21, "Os":190.23, "Ir": 192.22, "Pt":195.08, "Au": 196.97, "Hg":200.59, "Tl": 204.38, "Pb": 207.20, "Bi": 208.98, 
                    "Po": 208.98, "At": 209.99, "Rn": 222.02, "Fr":223.02, "Ra": 226.02, "Ac": 227.03,"Rf":261.11, "Db": 263.11, "Sg":263.11,
                      "Sg": 263.12, "Bh":263.12,"Hs":264.00, "Mt": 266.13, "Ds": 269.00, "Rg":272.00,"Cn": 277.00, "Nh":284.00,"Fl": 289.00,
                      "Mc":288.00, "Lv": 292.00, "Th": 332.04, "Pa":331.04, "U": 238.03 } #crear diccionario con las masas de los elementos
    suma = 0 #inicializar la variable suma como 0
    
    while True: #usar ciclo while
        elemento = input("Ingrese el símbolo del elemento presente en el compuesto: ") #pedirle al usuario que ingrese el símbolo del elemento
        if elemento in masas_molares: #condición si el símbolo del elemento se encuentra en el diccionario
            veces = float(input("Ingrese la cantidad de átomos de este elemento presentes en la molécula: ")) #ingresar el número de veces que el elemento aparece en el compuesto
            masa_elemento = masas_molares[elemento] * veces #multiplicar el número de veces con la masa molar del elemento
            suma += masa_elemento #sumar las masas de los elementos
        else: #condición para salir del bucle
            break
    return suma


#################### De aqui en adelante se define cada una de las funciones para realizar calculos teoricos 

def calcular_densidad_relativa(masa_agua:float, masa_sustancia_desconocida:float, densidad_agua:float) -> float: #crear función para calcular la medida
    densidad_relativa_sustancia_desconocida = (densidad_agua / masa_agua) * masa_sustancia_desconocida #calcular densidad relativa
    return densidad_relativa_sustancia_desconocida 

def calcular_densidad_comun(masa_sustancia:float, volumen:float) -> float: #crear función para calcular la medida
    densidad_normal = (masa_sustancia / volumen) #calcular densidad
    return densidad_normal

def calcular_volumen_solido_con_liquido(volumen_s_a_probeta:float, volumen_a_probeta:float) -> float: #crear la función para calcular el volumen del sólido
    volumen_1 = abs(volumen_s_a_probeta - volumen_a_probeta) #calcular volumen del sólido
    return volumen_1

def calculo_molaridad(moles_soluto:float, litros_solucion:float) -> float: #crear una función para calcular la molaridad
    molaridad = moles_soluto / (litros_solucion / 1000)
    return molaridad

def calculo_molalidad(moles_soluto:float, gramos_solucion:float) -> float: #crear una función para calcular la molalidad
    molalidad = moles_soluto / (gramos_solucion / 1000)
    return molalidad

def calcular_porcentaje_masa_volumen(masa_sustancia_1:float, volumen_sustancia_1:float) -> float: #crear una función para calcular el % m/v
    porcentaje_masa_volumen = (masa_sustancia_1 / volumen_sustancia_1) * 100 #calcular % masa/volumen
    return porcentaje_masa_volumen

def calcular_peso_a_peso(masa_soluto:float, masa_solucion:float) -> float: #definir una función para calcular el %m/m
    m_m_i = (masa_soluto) / masa_solucion
    m_m_f = (m_m_i) * 100
    return m_m_f

def calcular_porcentaje_volumen_volumen(volumen_soluto:float, volumen_disolucion:float) -> float: #crear una función para calcular el % v/v
    porcentaje_volumen_volumen = (volumen_soluto / volumen_disolucion) * 100 #calcular % volumen/volumen
    return porcentaje_volumen_volumen

####################  De aqui en adelnate se define cada una de las funciones para realizar calculo con su incertidumbre 

def calcular_incertidumbre_densidad_relativa(masa_agua:float, masa_sustancia_desconocida:float, densidad_agua:float, densidad_relativa:float, incertidumbre_balanza:float) -> float: #crear función para calcular la incertidumbre
    datos = [masa_agua, masa_sustancia_desconocida] #crear un arreglo con los datos que tienen incertidumbre
    terminos_incertidumbres = [] #crear arreglo para calcular la incertidumbre final
    suma = 0 #inicializar la variable suma como 0
    for dato in datos: #usar ciclo for para todas las medidas con incertidumbre
        #hallar la incertidumbre de cada dato
        incertidumbre_previa = (incertidumbre_balanza / dato) * 100
        incertidumbre_previa_f = incertidumbre_previa ** 2
        terminos_incertidumbres.append(incertidumbre_previa_f)
        
        for t in terminos_incertidumbres: #sumar los porcentajes de incertidumbres
            suma += t
    #calcular la incertidumbre de la medida
    incertidumbre_0 = math.sqrt(suma)
    incertidumbre = (incertidumbre_0 * densidad_relativa) / 100
    return incertidumbre

def calcular_incertidumbre_densidad_comun(masa_sustancia:float, volumen:float, incertidumbre_volumen_1:float, densidad:float, incertidumbre_balanza:float) -> float: #crear función para calcular la incertidumbre
    datos = [masa_sustancia, volumen] #crear un arreglo con los datos que tienen incertidumbre
    incertidumbres = [incertidumbre_balanza, incertidumbre_volumen_1] #crear arreglo para las incertidumbres de cada medida
    terminos_incertidumbres = [] #crear arreglo para calcular la incertidumbre final
    suma = 0 #inicializar la variable suma como 0
    for dato in datos: #usar ciclo for para todas las medidas con incertidumbre
        for i in incertidumbres:
            #hallar la incertidumbre de cada dato
            incertidumbre_previa = (i / dato) * 100
            incertidumbre_previa_f = incertidumbre_previa ** 2
            terminos_incertidumbres.append(incertidumbre_previa_f)
        
        for t in terminos_incertidumbres: #sumar los porcentajes de incertidumbres
            suma += t
    #calcular la incertidumbre de la medida
    incertidumbre_0 = math.sqrt(suma)
    incertidumbre = (incertidumbre_0 * densidad) / 100
    return incertidumbre

def calcular_incertidumbre_volumen_s_a_probeta(incertidumbre_volumen_b:float): #crear función para calcular la incertidumbre del volumen
    incertidumbre_volumen_2 = incertidumbre_volumen_b / 2
    incertidumbre_previa = ((incertidumbre_volumen_2 ** 2) * 2) #hallar el porcentaje de incertidumbre de la medida
    incertidumbre = math.sqrt(incertidumbre_previa)
    return incertidumbre

def calcular_masa(masa_objeto_medicion:float, masa_sustancia_y_objeto:float) -> float: #definir función para calcular la masa de la sustancia
    masa_sustancia_1 = masa_sustancia_y_objeto - masa_objeto_medicion
    return masa_sustancia_1

def calcular_incertidumbre_masa_medicion(masa_objeto_medicion:float) -> float:
    parte_entera_1 = int(masa_objeto_medicion) #extraer la parte entera del dato
    parte_decimal_1 = masa_objeto_medicion - parte_entera_1 #obtener la parte decimal del dato
    #convertir en cadena el dato
    parte_decimal = str(parte_decimal_1)

    for decimal in range(2,len(parte_decimal)-1): #usar ciclo for para que me reemplace todos los dígitos de la parte decimal por 0, menos el último
        parte_decimal.replace(parte_decimal[decimal], "0")
        
        parte_decimal.replace(parte_decimal[len(parte_decimal)-1], "1") #reemplazar el último dígito de la parte decimal por 1
        
        parte_final = float(parte_decimal) #declarar e inicializar la variable de la parte final como la cadena de la incertidumbre obtenida convertida en un número real
        incertidumbre_0 = (parte_final ** 2) * 2
        incertidumbre = math.sqrt(incertidumbre_0)
    return incertidumbre

def calcular_promedio(datos_promedio) -> float: #crear la función para calcular el promedio de los datos
    #calcular promedio de los datos
    promedio_d = np.mean(datos_promedio)
    return promedio_d

def calcular_incertidumbre_promedio(incertidumbres) -> float: #crear la función para calcular el promedio de las incertidumbres
    #calcular promedio de las incertidumbres de los datos
    promedio_i = np.mean(incertidumbres)
    return promedio_i

def calcular_incertidumbre_molaridad(moles_soluto:float, litros_solucion:float, incertidumbre_moles:float, incertidumbre_litros:float, molaridad_final:float) -> float: #crear función para calcular la incertidumbre de la molaridad
    #calcular el porcentaje de incertidumbre de los moles
    termino_1 = (incertidumbre_moles / moles_soluto) * 100
    #calcular el porcentaje de incertidumbre del volumen de la solución
    termino_2 = (incertidumbre_litros * 100 / litros_solucion) * 100
    #sumar los porcentajes de incertidumbre
    suma_cuadrados_terminos = termino_1**2 + termino_2**2
    #hallar la incertidumbre de la molaridad
    incertidumbre_0 = math.sqrt(suma_cuadrados_terminos)
    incertidumbre = (molaridad_final * incertidumbre_0) / 100
    return incertidumbre

def calcular_incertidumbre_molalidad(moles_soluto:float, gramos_solucion:float, incertidumbre_moles:float, incertidumbre_gramos:float, molalidad_final:float) -> float: #crear función para calcular la incertidumbre de la molaridad
    #calcular el porcentaje de incertidumbre de los moles
    termino_1 = (incertidumbre_moles / moles_soluto) * 100
    #calcular el porcentaje de incertidumbre de la masa de la solución
    termino_2 = (incertidumbre_gramos / (gramos_solucion / 1000)) * 100
    #sumar los porcentajes de incertidumbre
    suma_cuadrados_terminos = termino_1**2 + termino_2**2
    #hallar la incertidumbre de la molaridad
    incertidumbre_0 = math.sqrt(suma_cuadrados_terminos)
    incertidumbre = (molalidad_final * incertidumbre_0) / 100
    return incertidumbre

def calcular_incertidumbre_masa_volumen(masa_sustancia_1:float, volumen_sustancia_1:float, incertidumbre_volumen_1:float, incertidumbre_masa_soluto:float) -> float: #definir una fnción para calcular la incertidumbre de la medida
    #calcular el porcentaje de incertidumbre de cada medida
    termino_1 = (incertidumbre_masa_soluto / masa_sustancia_1) * 100
    termino_2 = (incertidumbre_volumen_1 / volumen_sustancia_1) * 100
    #calcular el porcentaje de incertidumbre de la medida en general
    suma_terminos = termino_1 ** 2 + termino_2 ** 2
    porcentaje_incertidumbre = math.sqrt(suma_terminos)
    #calcular incertidumbre de la medida
    incertidumbre_m_v = porcentaje_incertidumbre * porcentaje_1 / 100
    porcentaje_1 = calcular_porcentaje_masa_volumen(masa_sustancia_1, volumen_sustancia_1)
    return incertidumbre_m_v

def calcular_incertidumbre_masa_masa(masa_soluto:float, masa_solucion:float, i_masa_soluto:float, i_masa_solucion:float) -> float: #definir una función para calcular la incertidumbre del %m/m
    t_1 = (i_masa_soluto / masa_soluto) * 100 #hallar el porcentaje de incertidumbre de la masa del soluto
    t_2 = (i_masa_solucion / masa_solucion) * 100 #hallar el porcentaje de incertidumbre de la masa de la solución
    #calcular la incertidumbre del porcentaje masa/masa
    incertidumbre_i = t_1**2 + t_2**2
    incertidumbre_f = math.sqrt(incertidumbre_i)
    return incertidumbre_f

def calcular_incertidumbre_volumen_volumen(volumen_soluto:float, volumen_disolucion:float, incertidumbre_volumen_1:float, incertidumbre_volumen_soluto:float) -> float: #definir una fnción para calcular la incertidumbre de la medida
    #calcular el porcentaje de incertidumbre de cada medida
    termino_1 = (incertidumbre_volumen_soluto / volumen_soluto) * 100
    termino_2 = (incertidumbre_volumen_1 / volumen_disolucion) * 100
    #calcular el porcentaje de incertidumbre de la medida en general
    suma_terminos = termino_1 ** 2 + termino_2 ** 2
    porcentaje_incertidumbre = math.sqrt(suma_terminos)
    #calcular incertidumbre de la medida
    incertidumbre_v_v = porcentaje_incertidumbre * porcentaje_2 / 100
    porcentaje_2 = calcular_porcentaje_volumen_volumen( volumen_soluto, volumen_disolucion)
    return incertidumbre_v_v


#################### De aqui en adelante se definen cada una de las funciones para el tratamiento de datos 


def tratar_datos_por_tukey(datos_muestra): #definir una función para el tratamiento de datos
    diagrama_caja = sns.boxplot(x=datos_muestra, color="plum")#crear un diagrama de caja con Seaborn
    
    #Mostrar estadísticas de resumen utilizando Pandas
    df = pd.DataFrame(datos_muestra, columns=["Datos"])
    descripcion = df.describe()

    # Calcular y mostrar valores atípicos
    cuartil_1 = descripcion.at["25%", "Datos"] #calcular el cuartil 1 de los datos
    cuartil_3 = descripcion.at["75%", "Datos"] #calcular el cuartil 3 de los datos
    rango_intercuartil = cuartil_3 - cuartil_1

    atipicos = [valor for valor in datos_muestra if valor < cuartil_1 - 1.5 * rango_intercuartil or valor > cuartil_3 + 1.5 * rango_intercuartil] #crear un arreglo que incluya datos que esten por encima del rango intercuartílico extendido
    
    if atipicos: #condición si hay valores atípicos
        print("Valores atípicos:", atipicos)
    else: #condición si no hay valores atípicos
        print("No hay valores atípicos.")
    return diagrama_caja

def calcular_precision(datos_muestra_1): #definir la función para calcular la precisión
    desviacion_estandar = np.std(datos_muestra_1) #calcular desviación estándar
    return desviacion_estandar

def calcular_exactitud(datos_muestra_1, valor_real:float): #definir la función para calcular la exactitud
    promedio_1 = np.mean(datos_muestra_1) #calcular el promedio de los datos
    error_absoluto = abs(valor_real - promedio_1) #calcular el error absoluto
    error_relativo = error_absoluto / valor_real #calcular el error relativo
    error_porcentual = error_relativo * 100 #calcular el error porcentual
    return error_porcentual


#################### Aqui se calcula algo importante o no?

def CalcularSIpasasProgramacion(NotaExamen1: float, NotaExamen2_3: float, NotaAvancesProyecto: float, NotaProyectoFinal: float, NotaTalleres: float, NotaRetos: float  )->float:
    PasasProgramacion = ((NotaExamen1)*0.1) + ((NotaExamen2_3)*0.25) + ((NotaAvancesProyecto)*0.1) + ((NotaProyectoFinal)*0.25) + (NotaTalleres*(0.1)) + (NotaRetos*(0.2))
    return PasasProgramacion


#################### Aqui se define la funcion principal, en la que se basa todo el codigo 

def FuncionPrincipal():

    operacion = (input("Seleccione la operación a realizar\n"
                   "\n"
                   "La linea de 1 es para realizar conversión de unidades antes de calculos mas avanzados:\n"
                   "\n"
                   "1.1 Moles a gramos\n"
                   "1.2 Gramos a moles\n"
                   "1.3 Litros a mililitros\n"
                   "1.4 Mililitros a litros\n"
                   "1.5 Litros a metros cúbicos\n"
                   "1.6 Metros cúbicos a mililitros\n"
                   "1.7 Gramo a Kilogramo \n"
                   "1.8 Kilogramo a gramo \n"
                   "1.9 Gramo a libras\n"
                   "1.10 Kilogramos a libras \n"
                   "1.11 Atm a mmHg\n"
                   "1.12 mmHg a Atm\n"
                   "1.13 Conversiones de temperatura\n"
                   "\n"
                   "La linea de 2 es para realizar calculos con teoricos:\n"
                   "\n"
                   "2.1 densidad relativa\n"
                   "2.2 densidad comun "
                   "2.3 volumen de un solido\n "
                   "2.4 molaridad de una sustancia \n "
                   "2.5 molalidad de una sustancia \n "
                   "2.6 porcentaje masa/volumen\n"
                   "2.7 porcentaje peso/peso\n"
                   "2.8 porcentaje volumen/volumen\n"
                   "2.9 Calcular masa molaer de un compuesto\n"
                   "\n"
                   "La linea de 3 es para realizar calculos con su incertidumbre \n"
                   "\n"
                   "3.1 densidad relativa con su incertidumbre \n"
                   "3.2 densidad comun con su incertidumbre \n"
                   "3.3 volumen de un solido con su incertidumbre \n "
                   "3.4 masa de una sustancia con incertidumbres \n "
                   "3.5 promedio de los datos con su incertidumbre\n"
                   "3.6 molaridad con su incertidumbre \n "
                   "3.7 molalidad con su incertidumbre \n "
                   "3.8 porcentaje masa/volumen con su incertidumbre\n"
                   "3.9 porcentaje peso/peso con su incertidumbre \n"
                   "3.10 porcentaje volumen/volumen con su incertidumbre \n"
                   "\n"
                   "La linea de 4 es para tratamiento de datos \n"
                   "\n"
                   "4.1 tratamiento de datos por el metodo de tukey\n"
                   "4.2 calcular precision y exactitud \n"
                   "\n"
                   "5 para calcular algo importante :)\n"
                   "Ingrese el número de la operación: " ))
                   
                   
                    

    if operacion == "1.1": # Moles a gramos
        NumeroDeMoles: float = float(input("Ingrese la cantidad de moles: "))
        MasaMolar: float = float(input("Ingrese la masa molar: "))
        resultado = MolaGramos(NumeroDeMoles, MasaMolar)
        print(f"la coversion de {NumeroDeMoles} moles a gramos es {resultado}")
        
    elif operacion == "1.2": # Gramos a moles
        NumeroDeGramos: float = float(input("Ingrese la cantidad de gramos: "))
        MasaMolar: float = float(input("Ingrese la masa molar: "))
        resultado = GramosaMol(NumeroDeGramos, MasaMolar)
        print(f"La conversión de {NumeroDeGramos} gramos a moles es {resultado}")

    elif operacion == "1.3":
        Litros: float = float(input("Ingrese la cantidad de litros: "))
        resultado = LitroAMililitro(Litros)
        print(f"La conversión de {Litros} litros a mililitros es {resultado}")

    elif operacion == "1.4":
        Mililitros: float = float(input("Ingrese la cantidad de mililitros: "))
        resultado = MililitroALitro(Mililitros)
        print(f"La conversión de {Mililitros} mililitros a litros es {resultado}")

    elif operacion == "1.5":
        Litros: float = float(input("Ingrese la cantidad de litros: "))
        resultado = LitroAMetroCubico(Litros)
        print(f"La conversión de {Litros} litros a metros cúbicos es {resultado} ")

    elif operacion == "1.6":
        MetrosCubicos: float = float(input("Ingrese la cantidad de metros cúbicos: "))
        resultado = MetroCubicoAMililitro(MetrosCubicos)
        print(f"La coversión de {MetrosCubicos} metros cúbicos a litros es {resultado}")

    elif operacion == "1.7":
        Gramos:float=float(input("Ingrese el numero de gramos: "))
        Kilogramos:float=float(input("Ingrese los kilogramos: "))
        GramoAKilogramo1 = GramoAKilogramo(Gramos, Kilogramos)
        print(f"{Gramos} gramos a Kilogramos son {GramoAKilogramo1}")

    elif operacion == "1.8":
        Gramos:float=float(input("Ingrese el numero de gramos: "))
        Kilogramos:float=float(input("Ingrese los kilogramos: "))
        KilogramoAGramo1 = KilogramoAGramo(Gramos, Kilogramos)
        print(f"{Kilogramos} kilogramos a gramos son {KilogramoAGramo1}")

    elif operacion == "1.9":
    
        Gramos:float=float(input("Ingrese el numero de gramos: "))
        Kilogramos:float=float(input("Ingrese los kilogramos: "))
        GramoALibra1 = GramoALibra(Gramos)
        print(f"{Gramos} gramos a libras son  {GramoALibra1}")

    elif operacion == "1.10":
        Gramos:float=float(input("Ingrese el numero de gramos: "))
        Kilogramos:float=float(input("Ingrese los kilogramos: "))
        KilogramoALibras1 = KilogramoALibras(Kilogramos)
        print(f"{Kilogramos} kilogramos  a libras son {KilogramoALibras1}")

    elif operacion == "1.11":
        Atm:float=float(input("Ingrese el numero de Atmosferas: "))
        mmHg: float=float(input("Ingrese el número de milimetros de mercurio: "))  
        AtmAmmHg1 = AtmAmmHg(Atm)
        print(f"{Atm} Atm a mmHg son {AtmAmmHg1}")
    
    elif operacion == "1.12":
        Atm:float=float(input("Ingrese el numero de Atmosferas: "))
        mmHg: float=float(input("Ingrese el número de milimetros de mercurio: "))
        mmHgAAtm1 = mmHgAAtm(mmHg)
        print(f"{mmHg} mmHg a Atm son {mmHgAAtm1}")
    
    elif operacion == "1.13":
        Kelvin:float=float(input("Ingrese la temperatura en kelvin: "))
        Celsius:float=float(input("Ingrese la temperatura en Celsius: "))
        Fahrenheit:float=float(input("Ingrese la temperatura en Fahrenheit: "))
        KelvinAFahrenheit1 = KelvinAFahrenheit(Kelvin)
        KelvinACelsius1 =  KelvinACelsius(Kelvin)
        CelsiusAKelvin1 = CelsiusAKelvin(Celsius)
        CelsiusAFahrenheit1 = CelsiusAFahrenheit(Celsius)
        FahrenheitACelsius1 = FahrenheitACelsius(Fahrenheit)
        FahrenheitAKelvin1 = FahrenheitAKelvin(Fahrenheit)
        print(f"{Kelvin}K a Fahrenheit son {KelvinAFahrenheit1}°F")
        print(f"{Kelvin}K a celsius son {KelvinACelsius1}°C")
        print(f"{Celsius}°C a Kelvin son {CelsiusAKelvin1}K")
        print(f"{Celsius}°C a Fahrenheit son {CelsiusAFahrenheit1}°F")
        print(f"{Fahrenheit}°F a celsius son {FahrenheitACelsius1}°C")
        print(f"{Fahrenheit}°F a kelvin son {FahrenheitAKelvin1}K")


    

    elif operacion == "2.1":
        #pedirle al usuario los datos necesarios para calcular la densidad relativa
        masa_agua: float = float(input("Ingrese la masa del agua en gramos: "))
        masa_sustancia_desconocida: float = float(input("Ingrese la masa de la sustancia (con densidad desconocida) en gramos: "))
        densidad_agua: float = float(input("Ingrese la densidad del agua en g/cm^3 (a la temperatura de trabajo): "))
        #llamar a las funciones declarando e inicializando las variables de la densidad relativa 
        densidad_relativa = calcular_densidad_relativa(masa_agua, masa_sustancia_desconocida, densidad_agua)
        print(f"La densidad relativa de la sustancia es de {densidad_relativa}")#imprimir resultados

    elif operacion == "2.2":
        masa_sustancia = float(input("Ingrese la masa de la sustancia: "))
        volumen = float(input("Ingrese el volumen de la sustancia en cm^3: "))
        densidad = calcular_densidad_comun(masa_sustancia, volumen)
        print(f"La densidad de la sustancia es de {densidad} ")#imprimir resultados

    elif operacion == "2.3":
        #pedirle al usuario los datos necesarios para calcular el volumen de un sólido
        volumen_a_probeta = float(input("Ingrese el volumen de agua registrado en la probeta en mL: "))
        volumen_s_a_probeta = float(input("Ingrese el volumen registrado en la probeta del volumen de agua + el sólido en mL: "))
        #llamar a las funciones declarando e inicializando las variables del volumen de un sólido y la incertidumbre
        volumen_solido_probeta = calcular_volumen_solido_con_liquido(volumen_a_probeta, volumen_s_a_probeta)

    elif operacion == "2.4":
        moles_soluto = float(input("Ingrese los moles del soluto: "))
        litros_solucion = float(input("Ingrese el volumen de la solución en mL: "))
        molaridad_final = calculo_molaridad(moles_soluto, litros_solucion)
        print(f"La molaridad de la solución es {molaridad_final} ")#imprimir resultados

    elif operacion == "2.5":

        moles_soluto = float(input("Ingrese los moles del soluto: "))
        gramos_solucion = float(input("Ingrese la masa de la solución en gramos: "))
        molalidad_final = calculo_molalidad(moles_soluto, gramos_solucion)
        print(f"La molalidad de la solución es {molaridad_final} ")#imprimir resultados

    elif operacion == "2.6":
        masa_sustancia_1 = float(input("Ingrese la masa del soluto en gramos: "))
        incertidumbre_masa_soluto = float(input("Ingrese la incertidumbre de la masa del soluto: "))
        volumen_sustancia_1 = float(input("Ingrese el volumen de la solución en mL/cm^3: "))
        porcentaje_1 = calcular_porcentaje_masa_volumen(masa_sustancia_1, volumen_sustancia_1)
        print(f"El % masa/volumen (%m/v) de la sustancia es {porcentaje_1} ") #imprimir resultados

    elif operacion == "2.7":
        masa_soluto = float(input("Ingrese la masa del soluto en gramos: "))
        masa_solucion = float(input("Ingrese los gramos de solución: "))
        porcentaje_masa_masa = calcular_peso_a_peso(masa_soluto, masa_solucion)

        print(f"El porcentaje peso a peso o masa a masa (%m/m) de la solución es {porcentaje_masa_masa} ") #imprimir resultados

    elif operacion == "2.8": 
        #pedirle al usuario que ingrese los datos necesarios para calcular la incertidumbre del %v/v
        volumen_soluto = float(input("Ingrese el volumen del soluto en mL/cm^3: "))
        volumen_disolucion = float(input("Ingrese el volumen de la solución en mL/cm^3: "))
        porcentaje_2 = calcular_porcentaje_volumen_volumen( volumen_soluto, volumen_disolucion)

        print(f"El % volumen/volumen (%volumen/v) de la sustancia es {porcentaje_2}") #imprimir resultados

    elif operacion == "2.9":
        masa_compuesto = calcular_masa_compuesto() #llamar a la función

        print(f"La masa molar del compuesto es {masa_compuesto}") #imprimir resultados
    




     
    elif operacion == "3.1":
        #pedirle al usuario los datos necesarios para calcular la densidad relativa con su incertidumbre 
        masa_agua = float(input("Ingrese la masa del agua en gramos: "))
        masa_sustancia_desconocida = float(input("Ingrese la masa de la sustancia (con densidad desconocida) en gramos: "))
        densidad_agua = float(input("Ingrese la densidad del agua en g/cm^3 (a la temperatura de trabajo): "))
        incertidumbre_balanza = float(input("Ingrese el decimal más pequeño que puede mostrar la balanza: "))
        #llamar a las funciones declarando e inicializando las variables de la densidad relativa y la incertidumbre
        densidad_relativa = calcular_densidad_relativa(masa_agua, masa_sustancia_desconocida, densidad_agua)
        incertidumbre_medida_1 = calcular_incertidumbre_densidad_relativa(masa_agua, masa_sustancia_desconocida, densidad_agua, densidad_relativa, incertidumbre_balanza)
        print(f"La densidad relativa de la sustancia es de {densidad_relativa} ±{incertidumbre_medida_1} g/cm^3.")#imprimir resultados
    
    elif operacion == "3.2":
    #pedirle al usuario los datos necesarios para calcular la densidad con su incertidumbre 
        masa_sustancia = float(input("Ingrese la masa de la sustancia: "))
        incertidumbre_balanza = float(input("Ingrese el decimal más pequeño que puede mostrar la balanza: "))
        volumen = float(input("Ingrese el volumen de la sustancia en cm^3: "))
    
        while True: #usar ciclo while para que se ingrese una opción válida cuando se pregunta por la incertidumbre del instrumento con el que se midió el volumen
            incertidumbre_volumen_o = input("¿Midió el volumen con un instrumento aforado o graduado? (Ingrese 1 si es aforado, 2 si es graduado y 3 si la medida no tiene incertidumbre): ")

            if incertidumbre_volumen_o.isdigit(): #condición si el usuario ingresó un dígito
                incertidumbre_volumen_o = int(incertidumbre_volumen_o)

                if incertidumbre_volumen_o == 1: #condición si el usuario señaló que el instrumento era aforado
                    incertidumbre_volumen_1 = float(input("Ingrese la incertidumbre reportada por el fabricante: ")) #pedirle al usuario que ingrese la incertidumbre reportada por el fabricante
                    break
                elif incertidumbre_volumen_o == 2: #condición si el usuario señaló que el instrumento era graduado
                    #calcular la incertidumbre de un instrumento que presenta una escala
                    incertidumbre_volumen_a = float(input("Ingrese la división más fina de la escala: "))
                    incertidumbre_volumen_1 = incertidumbre_volumen_a / 2
                    break
                elif incertidumbre_volumen_o == 3: #condición si el usuario reportó que la medida no tenía incertidumbre
                    incertidumbre_volumen_1 = 0 #tomar incertidumbre como 0
                    break
                else: #condición si el usuario no ingresó una opción válida
                    print("Por favor ingrese una opción válida.")
            else: #condición si el usuario no ingresó un dígito
                print("Por favor ingrese un número válido.")

        #llamar a las funciones declarando e inicializando las variables de la densidad y la incertidumbre
        densidad = calcular_densidad_comun(masa_sustancia, volumen)
        incertidumbre_medida_2 = calcular_incertidumbre_densidad_comun(masa_sustancia, volumen, incertidumbre_volumen_1, densidad, incertidumbre_balanza)
        print(f"La densidad de la sustancia es de {densidad} ±{incertidumbre_medida_2} g/cm^3.")#imprimir resultados

    elif operacion == "3.3":
        #pedirle al usuario los datos necesarios para calcular el volumen de un sólido
        volumen_a_probeta = float(input("Ingrese el volumen de agua registrado en la probeta en mL: "))
        volumen_s_a_probeta = float(input("Ingrese el volumen registrado en la probeta del volumen de agua + el sólido en mL: "))
        incertidumbre_volumen_b = float(input("Ingrese la división más fina de la escala de la probeta: "))
        #llamar a las funciones declarando e inicializando las variables del volumen de un sólido y la incertidumbre
        volumen_solido_probeta = calcular_volumen_solido_con_liquido(volumen_a_probeta, volumen_s_a_probeta)
        incertidumbre_medida_4 = calcular_incertidumbre_volumen_s_a_probeta(incertidumbre_volumen_b)
        print(f"El volumen del sólido es {volumen_solido_probeta} ±{incertidumbre_medida_4} mL.")#imprimir resultados

    elif operacion == "3.4":
        #pedirle al usuario que ingrese los datos necesarios para calcular la masa de la sustancia
        masa_objeto_medicion = float(input("Ingrese la masa del instrumento en donde peso la sustancia (en gramos): "))
        masa_sustancia_y_objeto = float(input("Ingrese la masa del instrumento con la sustancia (en gramos): "))
        #llamar a las funciones
        masa_final = calcular_masa(masa_objeto_medicion, masa_sustancia_y_objeto)
        incertidumbre_medida_5 = calcular_incertidumbre_masa_medicion(masa_objeto_medicion)
        print(f"La masa de la sustancia es de {masa_final} ±{incertidumbre_medida_5} gramos.") #imprimir resultados

    elif operacion == "3.5":
        #crear arreglos vacíos
        datos_promedio = []
        incertidumbres = []
    
        while True: #pedirle al usuario los datos que quiere promediar con el ciclo for hasta que ponga un 0 como dato
            dato = float(input("Ingrese el dato para hallar el promedio o ingrese 0 para salir: "))
            datos_promedio.append(dato) #añadir el dato al arreglo
            i = float(input("Ingrese la incertidumbre del dato. Ingrese 0 si el dato no tiene incertidumbre: "))
            incertidumbres.append(i)
            if dato == 0: #cuando el usuario ingrese 0 en el dato, el ciclo termina
                break
        medida = input("Ingrese la unidad de medida de los datos: ") #pedirle al usuario que ingrese la unidad de medida de los datos
        #llamar a la función declarando e inicializando las variables del promedio y la incertidumbre del promedio
        promedio = calcular_promedio(datos_promedio)
        incertidumbre_promedio = calcular_incertidumbre_promedio(incertidumbres)
        print(f"El promedio de los datos es {promedio} ±{incertidumbre_promedio} {medida}.")#imprimir resultados

    elif operacion == "3.6":
        #pedirle al usuario los datos necesarios para calcular la molaridad
        moles_soluto = float(input("Ingrese los moles del soluto: "))
        incertidumbre_moles = float(input("Ingrese la incertidumbre de los moles: "))
        litros_solucion = float(input("Ingrese el volumen de la solución en mL: "))
        while True: #usar ciclo while para que se ingrese una opción válida cuando se pregunta por la incertidumbre del instrumento con el que se midió el volumen
            incertidumbre_volumen_o = input("¿Midió el volumen de la solución con un instrumento aforado o graduado? (Ingrese 1 si es aforado, 2 si es graduado y 3 si la medida no tiene incertidumbre): ")

            if incertidumbre_volumen_o.isdigit(): #condición si el usuario ingresó un dígito
                incertidumbre_volumen_o = int(incertidumbre_volumen_o)

                if incertidumbre_volumen_o == 1: #condición si el usuario señaló que el instrumento era aforado
                    incertidumbre_litros = float(input("Ingrese la incertidumbre reportada por el fabricante: ")) #pedirle al usuario que ingrese la incertidumbre reportada por el fabricante
                    break
                elif incertidumbre_volumen_o == 2: #condición si el usuario señaló que el instrumento era graduado
                    #calcular la incertidumbre de un instrumento que presenta una escala
                    incertidumbre_volumen_a = float(input("Ingrese la división más fina de la escala: "))
                    incertidumbre_litros = incertidumbre_volumen_a / 2
                    break
                elif incertidumbre_volumen_o == 3: #condición si el usuario reportó que la medida no tenía incertidumbre
                    incertidumbre_litros = 0 #tomar incertidumbre como 0
                    break
                else: #condición si el usuario no ingresó una opción válida
                    print("Por favor ingrese una opción válida.")
            else: #condición si el usuario no ingresó un dígito
                print("Por favor ingrese un número válido.")
      
        #llamar a las funciones declarando e inicializando las variables de la molaridad y la incertidumbre
        molaridad_final = calculo_molaridad(moles_soluto, litros_solucion)
        incertidumbre_medida_6 = calcular_incertidumbre_molaridad(moles_soluto, litros_solucion, incertidumbre_litros, incertidumbre_moles, molaridad_final)
        print(f"La molaridad de la solución es {molaridad_final} ±{incertidumbre_medida_6} mol/L.")#imprimir resultados

    elif operacion == "3.7":
        #pedirle al usuario los datos necesarios para calcular la molaridad
        moles_soluto = float(input("Ingrese los moles del soluto: "))
        incertidumbre_moles = float(input("Ingrese la incertidumbre de los moles: "))
        gramos_solucion = float(input("Ingrese la masa de la solución en gramos: "))
        incertidumbre_gramos = float(input("Ingrese la incertidumbre de la masa de la solución: "))

        #llamar a las funciones declarando e inicializando las variables de la molaridad y la incertidumbre
        molalidad_final = calculo_molalidad(moles_soluto, gramos_solucion)
        incertidumbre_medida_7 = calcular_incertidumbre_molalidad(moles_soluto, gramos_solucion, incertidumbre_gramos, incertidumbre_moles, molalidad_final)
    
        print(f"La molalidad de la solución es {molaridad_final} ±{incertidumbre_medida_7} mol/kg.")#imprimir resultados

    elif operacion == "3.8":

        #pedirle al usuario que ingrese los datos necesarios para calcular el %m/v de la solución
        masa_sustancia_1 = float(input("Ingrese la masa del soluto en gramos: "))
        incertidumbre_masa_soluto = float(input("Ingrese la incertidumbre de la masa del soluto: "))
        volumen_sustancia_1 = float(input("Ingrese el volumen de la solución en mL/cm^3: "))

        while True: #usar ciclo while para que se ingrese una opción válida cuando se pregunta por la incertidumbre del instrumento con el que se midió el volumen
            incertidumbre_volumen_o = input("¿Midió el volumen de la solución con un instrumento aforado o graduado? (Ingrese 1 si es aforado, 2 si es graduado y 3 si la medida no tiene incertidumbre): ")

            if incertidumbre_volumen_o.isdigit(): #condición si el usuario ingresó un dígito
                incertidumbre_volumen_o = int(incertidumbre_volumen_o)

                if incertidumbre_volumen_o == 1: #condición si el usuario señaló que el instrumento era aforado
                    incertidumbre_volumen_1 = float(input("Ingrese la incertidumbre reportada por el fabricante: ")) #pedirle al usuario que ingrese la incertidumbre reportada por el fabricante
                    break
                elif incertidumbre_volumen_o == 2: #condición si el usuario señaló que el instrumento era graduado
                    #calcular la incertidumbre de un instrumento que presenta una escala
                    incertidumbre_volumen_a = float(input("Ingrese la división más fina de la escala: "))
                    incertidumbre_volumen_1 = incertidumbre_volumen_a / 2
                    break
                elif incertidumbre_volumen_o == 3: #condición si el usuario reportó que la medida no tenía incertidumbre
                    incertidumbre_volumen_1 = 0 #tomar incertidumbre como 0
                    break
                else: #condición si el usuario no ingresó una opción válida
                    print("Por favor ingrese una opción válida.")
            else: #condición si el usuario no ingresó un dígito
                print("Por favor ingrese un número válido.")
    
        #llamar a las funciones
        porcentaje_1 = calcular_porcentaje_masa_volumen(masa_sustancia_1, volumen_sustancia_1)
        i_masa_volumen = calcular_incertidumbre_masa_volumen(masa_sustancia_1, volumen_sustancia_1, incertidumbre_volumen_1, incertidumbre_masa_soluto)

        print(f"El % masa/volumen (%m/v) de la sustancia es {porcentaje_1} ± {i_masa_volumen}%") #imprimir resultados

    elif operacion == "3.9": 

        #pedirle al usuario que ingrese los datos necesarios para calcular el %m/m
        masa_soluto = float(input("Ingrese la masa del soluto en gramos: "))
        i_masa_soluto = float(input("Ingrese la incertidumbre de la masa del soluto: "))
        masa_solucion = float(input("Ingrese los gramos de solución: "))
        i_masa_solucion = float(input("Ingrese la incertidumbre de la masa de la solución: "))
        #llamar a las funciones
        incertidumbre_medida_8 = calcular_incertidumbre_masa_masa(masa_soluto, masa_solucion, i_masa_solucion, i_masa_soluto)

        print(f"El porcentaje peso a peso o masa a masa (%m/m) de la solución es {porcentaje_masa_masa} ± {incertidumbre_medida_8}%") #imprimir resultados

    elif operacion == "3.10":
            #pedirle al usuario que ingrese los datos necesarios para calcular la incertidumbre del %v/v
        volumen_soluto = float(input("Ingrese el volumen del soluto en mL/cm^3: "))
        incertidumbre_volumen_soluto = float(input("Ingrese la incertidumbre del volumen del soluto: "))
        volumen_disolucion = float(input("Ingrese el volumen de la solución en mL/cm^3: "))

        while True: #usar ciclo while para que se ingrese una opción válida cuando se pregunta por la incertidumbre del instrumento con el que se midió el volumen
            incertidumbre_volumen_o = input("¿Midió el volumen de la solución con un instrumento aforado o graduado? (Ingrese 1 si es aforado, 2 si es graduado y 3 si la medida no tiene incertidumbre): ")

            if incertidumbre_volumen_o.isdigit(): #condición si el usuario ingresó un dígito
                incertidumbre_volumen_o = int(incertidumbre_volumen_o)

                if incertidumbre_volumen_o == 1: #condición si el usuario señaló que el instrumento era aforado
                    incertidumbre_volumen_1 = float(input("Ingrese la incertidumbre reportada por el fabricante: ")) #pedirle al usuario que ingrese la incertidumbre reportada por el fabricante
                    break
                elif incertidumbre_volumen_o == 2: #condición si el usuario señaló que el instrumento era graduado
                    #calcular la incertidumbre de un instrumento que presenta una escala
                    incertidumbre_volumen_a = float(input("Ingrese la división más fina de la escala: "))
                    incertidumbre_volumen_1 = incertidumbre_volumen_a / 2
                    break
                elif incertidumbre_volumen_o == 3: #condición si el usuario reportó que la medida no tenía incertidumbre
                    incertidumbre_volumen_1 = 0 #tomar incertidumbre como 0
                    break
                else: #condición si el usuario no ingresó una opción válida
                    print("Por favor ingrese una opción válida.")
            else: #condición si el usuario no ingresó un dígito
                print("Por favor ingrese un número válido.")
    
        #llamar a las funciones
        porcentaje_2 = calcular_porcentaje_volumen_volumen( volumen_soluto, volumen_disolucion)
        i_volumen_volumen = calcular_incertidumbre_volumen_volumen(volumen_soluto, volumen_disolucion, incertidumbre_volumen_1, incertidumbre_volumen_soluto)

        print(f"El % volumen/volumen (%volumen/v) de la sustancia es {porcentaje_2} ± {i_volumen_volumen}%") #imprimir resultados

    elif operacion == "4.1":
        nombre_diagrama_caja = input("Ingrese el nombre que le quiere dar al diagrama de caja: ")
        #crear arreglo vacío con los datos que necesitan ser tratados
        datos_muestra = []
    
        while True: #pedirle al usuario los datos que quiere tratar con el ciclo for hasta que ponga un 0 como dato
            dato = float(input("Ingrese el dato de la muestra o ingrese 0 para salir: "))
            datos_muestra.append(dato) #añadir el dato al arreglo
            if dato == 0: #cuando el usuario ingrese 0 en el dato, el ciclo termina
                datos_muestra.pop(-1) #eliminar el 0 del arreglo
                break
    
        diagrama = tratar_datos_por_tukey(datos_muestra)#llamar a la función que realiza el tratamiento de los datos
    
        plt.title(nombre_diagrama_caja, color="orchid")
        plt.show(diagrama)#mostrar diagrama de caja
        print("Datos evaluados:"+str(datos_muestra)) #imprimir arreglo con los datos evaluados

    elif operacion == "4.2":

        #crear arreglo vacío con los datos que van a evaluarse
        datos_muestra_1 = []
    
        while True: #pedirle al usuario los datos que quiere evaluar con el ciclo for hasta que ponga un 0 como dato
            dato = float(input("Ingrese el dato de la muestra o ingrese 0 para salir: "))
            datos_muestra_1.append(dato) #añadir el dato al arreglo
            if dato == 0: #cuando el usuario ingrese 0 en el dato, el ciclo termina
                datos_muestra_1.pop(-1) #eliminar el 0 del arreglo
                break
    
        valor_real = float(input("Ingrese el valor real: "))
        unidad = input("Ingrese la unidad de medida de sus datos: ")

        precision = calcular_precision(datos_muestra_1) #llamar a la función que realiza el cálculo de la precisión
        exactitud = calcular_exactitud(datos_muestra_1, valor_real) #llamar a la función que realiza el cálculo de la exactitud
    
        print(f"La precisión de los datos es de {precision} {unidad}.")
        print(f"La exactitud de los datos es de un {exactitud}%")

    elif operacion == "5":
        NotaExamen1 = float(input("Ingrese NotaExamen1: "))
        NotaExamen2_3 = float(input("Ingrese NotaExamen2_3 : "))
        NotaAvancesProyecto = float(input("Ingrese NotaAvancesProyecto : "))
        NotaProyectoFinal = float(input("Ingrese NotaProyectoFinal: "))
        NotaTalleres = float(input("Ingrese NotaTalleres: "))
        NotaRetos = float(input("Ingrese NotaRetos : "))
        Calculo = CalcularSIpasasProgramacion(NotaExamen1, NotaExamen2_3, NotaAvancesProyecto, NotaProyectoFinal, NotaTalleres, NotaRetos)


        if Calculo <= 2.9999999999999:
          print(f"Su nota final es {Calculo}, y recuerde, lo importante en esta clase es la actitud, asi que no se preocupe")
        elif Calculo == 3.0 : 
          print(f"Su nota final es {Calculo}, y recuerde, 3 es nota, lo demas es avaricia ")
        elif 3.01 <=  Calculo  <= 5:
          print(f"Su nota final es {Calculo}, y recuerde, con esta nota su PAPA y PAPPI van para arriba  ")
        elif Calculo > 5:
          print(f"{Calculo}, ESTA NOTA ESTA COMO RARA NO?")

    else:
        print("Opción no válida")
        return


if __name__ == "__main__":
    FuncionPrincipal()