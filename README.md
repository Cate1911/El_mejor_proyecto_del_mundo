# El_mejor_proyecto_del_mundo
Holaaa, bienvenido al repositorio del mejor proyecto del mundo. En este repositorio, quisimos darle solución a una de las problemáticas más grandes para cualquier persona que trabaja en el laboratorio y son los cálculos. Creamos un algoritmo que pudiera hallar magnitudes como la molaridad, el volumen, la densidad. entre otros, así como las incertidumbres de estas medidas. Asimismo, este algoritmo también le permite al usuario la conversión de unidades para facilitar el manejo de las magnitudes en el laboratorio. Como extra, para facilitar el cálculo de la concentración de un analito en una titulación redox, así como...
Este repositorio se divide en tres partes: en la primera parte se explica la parte del programa que calcula las magnitudes, en la segunda parte se explica el apartado de las conversiones de unidades y em la última parte se muestra cómo se realizó el programa para el tratamiento de datos y el cálculo de la presición y la exactitud de datos de laboratorio. 
## Cálculo de medidas experimentales
Para esta parte del programa, quisimos brindar una herramienta para que el usuario pudiera calcular las medidas más utilizadas en el laboratorio con su respectiva incertidumbre. Las medidas que se pueden calcular en este programa son:
+ Densidad relativa.
+ Densidad de una sustancia (m/v).
+ Masa de una sustancia.
+ Promedio de una serie de datos ->aquí se utilizó la librería de numpy.
+ Molaridad.
+ Molalidad.
+ Porcentaje peso a peso (%p/p o %m/m)
+ Porcentaje peso a peso (%p/v o %m/v)
+ Porcentaje volumen a volumen (%v/v)
Para el cálculo de las incertidumbres de las mediciones, nos basamos las siguientes fórmulas:

![image](https://github.com/Cate1911/El_mejor_proyecto_del_mundo/assets/141857246/a37f8c28-29bf-495f-8918-b86e9a982886)

Mientras que, para las incertidumbres de los instrumentos y las medidas que no necesitaban un cálculo, tuvimos en cuenta que:
a. La incertidumbre de un instrumento digital es la mínima cifra decimal que puede aportar. Por ejemplo, una balanza que aporta 6 cifras significativas, tiene como incertidumbre ±0.0001g.
b. La incertidumbre de un instrumento que presenta escalas o divisiones (como la regla o una bureta graduada), es igual a la mitad de la mínima cifra que puede aportar. Por ejemplo, la mínima cifra que puede aportar una regla es 0.1 cm, por tanto, su incertidumbre es ±0.05cm.
c. Los instrumentos aforados reportan una incertidumbre dada por el fabricante.
d. Los datos teóricos no presentan incertidumbre.

Este apartado se puede ver más a fondo en el archivo llamado "calculos.ipynb". Sin embargo, aquí hay algunos ejemplos de la aplicación del código:

**Ejemplo del cálculo de la densidad relativa de una sustancia**

![image](https://github.com/Cate1911/El_mejor_proyecto_del_mundo/assets/141857246/a7da1c66-0c53-486a-a0ad-136399a10a80)
![image](https://github.com/Cate1911/El_mejor_proyecto_del_mundo/assets/141857246/b6d5ffc5-798d-432f-a4a4-385f41c25c87)

**Ejemplo del cálculo del porcentaje peso a peso de una solución**

![image](https://github.com/Cate1911/El_mejor_proyecto_del_mundo/assets/141857246/b1a1f053-c46f-4e3b-aedb-0462aa1870fc)

## Conversión de unidades
## Tratamiento de datos 
### Tratamiento de datos por el método Tukey
El método Tukey, o diagrama de caja y bigotes, identifica valores atípicos en un conjunto de datos mediante el cálculo del rango intercuartílico (IQR). Los valores atípicos son aquellos que están fuera del rango Q1-1.5*IQR y Q3+1.5×IQR. Este método proporciona una representación visual de la distribución de los datos, así como también permite el descarte de datos para que no sean tomados en cuenta al momento de calcular exactitudes o presiciones de una muestra.
Partiendo de lo anterior, se desarrolló una función que le permite al usuario ingresar una serie de datos y evaluar cuáles de esos datos no están dentro del rango intercuartílico (atípicos), así como también le muestra un diagrama de caja de la distribución de esos datos. Para realizar este diagrama, utilizamos la biblioteca de Seaborn, Mathplot.lib y la de Pandas.
    
  ![Tukey](https://github.com/Cate1911/El_mejor_proyecto_del_mundo/assets/141857246/03d6614b-5001-439b-a9e2-64baa411e5b5)
A continuación, se presenta un ejemplo de la aplicación de esta función del programa:
  
![image](https://github.com/Cate1911/El_mejor_proyecto_del_mundo/assets/141857246/a1a6e878-ad37-4d29-8e68-a83a7728b049)

  Como se puede ver, el programa muestra tanto los datos atípicos, así como el gráfico que representa los valores que están dentro del rango explicado anteriormente.

**_Explicación más detallada:_**
El programa funciona de la siguiente manera:
+ import seaborn as sns: Importa la biblioteca Seaborn, que se utiliza para la visualización de datos estadísticos, incluyendo diagramas de caja (boxplot).
+ import matplotlib.pyplot as plt: Importa la biblioteca Matplotlib para la creación del gráfico y su visualizaciones.
+ import pandas as pd: Importa la biblioteca Pandas para el manejo y análisis de datos.
+ def tratar_datos_por_tukey(datos_muestra): Define una función llamada tratar_datos_por_tukey que toma una muestra de datos como argumento.
+ diagrama_caja = sns.boxplot(x=datos_muestra, color="plum"): Crea un diagrama de caja con Seaborn, visualizando la distribución de los datos. El color de la caja se establece en "plum".
+ df = pd.DataFrame(datos_muestra, columns=["Datos"]): Convierte la muestra de datos en un DataFrame de Pandas para facilitar el cálculo de estadísticas.
+ descripcion = df.describe(): Calcula estadísticas descriptivas sobre la muestra, como el promedio, la desviación estándar y los cuartiles.
+ cuartil_1 = descripcion.at["25%", "Datos"]: Obtiene el primer cuartil (Q1) de los datos.
+ cuartil_3 = descripcion.at["75%", "Datos"]: Obtiene el tercer cuartil (Q3) de los datos.
+ rango_intercuartil = cuartil_3 - cuartil_1: Calcula el rango intercuartil (IQR).
+ atipicos = [valor for valor in datos_muestra if valor < cuartil_1 - 1.5 * rango_intercuartil or valor > cuartil_3 + 1.5 * rango_intercuartil]: Identifica valores atípicos basados en el método Tukey y los almacena en la lista atipicos.
+ if atipicos:: Verifica si hay valores atípicos.
+ print("Valores atípicos:", atipicos): Imprime los valores atípicos si los hay.
+ else:: En caso contrario,
+ print("No hay valores atípicos."): Imprime que no hay valores atípicos.
+ return diagrama_caja: Retorna el objeto del diagrama de caja.
+ if __name__ == "__main__":: Inicia el bloque principal del programa.
+ nombre_diagrama_caja = input("Ingrese el nombre que le quiere dar al diagrama de caja: "): Solicita al usuario ingresar un nombre para el diagrama de caja.
+ datos_muestra = []: Inicializa un arreglo vacío que contendrá la muestra de datos a tratar.
+ while True:: Inicia un bucle infinito para que el usuario pueda ingresar datos hasta que decida salir ingresando 0.
+ diagrama = tratar_datos_por_tukey(datos_muestra): Llama a la función tratar_datos_por_tukey para realizar el tratamiento de los datos y almacena el objeto del diagrama de caja en diagrama.
+ plt.title(nombre_diagrama_caja, color="orchid"): Establece el título del diagrama de caja con el nombre ingresado por el usuario y le asigna un color "orchid".
+ plt.show(diagrama): Muestra el diagrama de caja.
+ print("Datos evaluados:" + str(datos_muestra)): Imprime en la consola la muestra de datos evaluada.
### Cálculo de la presición y la exactitud de una serie de datos de una muestra
  La precisión y la exactitud son esenciales para garantizar la confiabilidad de los datos y las mediciones en una variedad de campos, desde la investigación científica hasta la producción industrial y el sector médico. Ayudan a asegurar que las decisiones y los resultados  sean datos confiables. Es por eso, que se hace imperativa la evaluación de las medidas de una muestra, lo cual, se realizó en el siguiente código:
  
![exactitud_y_precision](https://github.com/Cate1911/El_mejor_proyecto_del_mundo/assets/141857246/b5ea389c-26d5-4f49-8e6f-4c273d7ec704)

**_Explicación más detallada:_**
  + Utilizamos el import numpy as np para importar la biblioteca NumPy con el alias np, que se utiliza para cálculos numéricos más eficientes en cuanto a cuestiones de tiempo y líneas de código.
  + def calcular_precision(datos_muestra_1): Define una función llamada calcular_precision que toma una muestra de datos como argumento y calcula la desviación estándar de esos datos utilizando NumPy.
  + def calcular_exactitud(datos_muestra_1, valor_real:float): Define una función llamada calcular_exactitud que toma una muestra de datos y un valor real como argumentos. Calcula el promedio de la muestra, el error absoluto, el error relativo y el error porcentual en comparación con el valor real.
  + if __name__ == "__main__":: Inicia el bloque principal del programa.
  + datos_muestra_1 = []: Inicializa un arreglo vacío que contendrá la muestra de datos a evaluar.
  + while True:: Inicia un bucle infinito para que el usuario pueda ingresar datos hasta que decida salir ingresando 0.
  + dato = float(input("Ingrese el dato de la muestra o ingrese 0 para salir: ")): Solicita al usuario ingresar un dato de la muestra como entrada.
  + datos_muestra_1.append(dato): Añade el dato ingresado al arreglo de datos de la muestra.
  + if dato == 0:: Verifica si el usuario ingresó 0, en cuyo caso se sale del bucle y elimina el 0 del arreglo.
  + valor_real = float(input("Ingrese el valor real: ")): Solicita al usuario ingresar el valor real con el que se compararán los datos.
  + unidad = input("Ingrese la unidad de medida de sus datos: "): Solicita al usuario ingresar la unidad de medida de los datos.
  + precision = calcular_precision(datos_muestra_1): Calcula la precisión llamando a la función calcular_precision con la muestra de datos y almacena el resultado en la variable precision.
  + exactitud = calcular_exactitud(datos_muestra_1, valor_real): Calcula la exactitud llamando a la función calcular_exactitud con la muestra de datos y el valor real, y almacena el resultado en la variable exactitud.
  + Los print imprimen los resultados, tanto la exactitud de los datos como su precisión.

**Referencias adicionales:**
+ divcode. (2023, 3 enero). Como INSTALAR NUMPY en Python Visual Studio Code 🚀 [Vídeo]. YouTube. https://www.youtube.com/watch?v=lYMWw_HO-Qs
+ Estadística Salud, [POR LAS RAMAS]2.1.1 Datos atípicos en Excel. (2019).
+ Python, R. (2023, 21 julio). Python plotting with Matplotlib (Guide). https://realpython.com/python-matplotlib-guide/
+ Specifying colors — Matplotlib 3.8.2 documentation. (s. f.). https://matplotlib.org/stable/users/explain/colors/colors.html
