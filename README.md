# hipoteca

Calculadora de Hipoteca Inversa
Este programa es una aplicación web desarrollada con Flask que permite calcular diferentes tipos de hipotecas inversas. Una hipoteca inversa es un producto financiero destinado a personas mayores que les permite obtener un préstamo o crédito utilizando su vivienda como garantía.
Descripción
La Calculadora de Hipoteca Inversa permite al usuario ingresar información como el valor de la vivienda, la edad, la tasa de interés anual y la renta mensual deseada. Con estos datos, el programa calcula el saldo de la deuda según el tipo de hipoteca inversa seleccionada: temporal, vitalicia o única.
Tipos de Hipoteca Inversa

Temporal : En este tipo de hipoteca inversa, el usuario especifica el número de años durante los cuales desea recibir la renta mensual. El programa calcula el saldo de la deuda acumulada durante ese período.
Vitalicia : En este caso, el usuario proporciona su esperanza de vida, y el programa calcula el saldo de la deuda considerando que recibirá la renta mensual durante ese tiempo.
Única : En esta modalidad, el programa calcula el saldo de la deuda final y el número de meses necesarios para que la deuda alcance el valor total de la vivienda.

Los resultados calculados se guardan en una base de datos PostgreSQL y se muestran en una página web.
Estructura del Programa
El programa sigue la estructura de una aplicación web Flask y consta de los siguientes archivos:

App.py: Archivo principal que inicia la aplicación Flask y registra el blueprint main.
Controller.py: Contiene las rutas y la lógica principal de la aplicación, incluyendo la conexión a la base de datos y el manejo de formularios.
Modell.py: Defina la clase HipotecaInversaque contiene los métodos para calcular los diferentes tipos de hipotecas inversas.
Index.HTML: Plantilla HTML que muestra el formulario para ingresar los datos.
Resultado.HTML: Plantilla HTML que muestra los resultados calculados.

uso

Clona este repositorio o descarga los archivos.
Asegúrese de tener Flask y las dependencias necesarias instaladas.
Configure la conexión a la base de datos PostgreSQL en Controller.py.
Ejecute el archivo App.pypara iniciar la aplicación.
Acceda a la aplicación web en su navegador y siga las instrucciones para calcular los diferentes tipos de hipotecas inversas.


Cómo lo hago funcionar?

Tener en cuenta: primeramente debe descargar el repositorio, para hacerlo ten en cuenta los siguientes pasos:

1.	Instalada la aplicación Git. Descargar Git
2.	Copiar el link del repositorio.
3.	Entra a el escritorio de tu computadora, das click derecho y presiona la opción open git bash here.
4.	En la consola de git bash escribe el comando "git clone" y pega el link del repositorio, recuerde que para pegar el link debes presionar click derecho y luego presiona en pegar, despues le das entrer y el repositorio se comenzara a descargar en el escritorio.
NOTA
•	En esta aplicacion la Base de datos funciona unicamente con html

Configuracion Base de datos
1.	Debes ingresar a la pagina Neon. Neon.Tech
2.	Te registrar/logea, una vez registrado debes crear un proyecto, el titulo del proyecto a tu preferencia y el nombre de la base de datos puede porle: "Calculadora hipoteca" y le das es crear proyecto.
3.	Una vez creado el proyecto y la base de datos te dirijes a la opcion Dashboard.
4.	Desplegas el menu donde dice Connection string, alli seleccionas la opcion de Parameters only.
5.	Copias todo lo que se encuentra en el campo de texto y te dirijes donde tienes el repositorio abierto.
6.	En la carpeta del proyecto encontraras una carpeta llamada .env.
7.	En este archivo debes pegar los parametros que copias en el Neon de tu base de datos.
8.	Asegúrese de tener Flask y las dependencias necesarias instaladas, de no tenerla instalada con el comando pip instanll Flask, lo instalas.

Ejecutar por consola
1.	Abra la terminal en su computadora.
2.	En la terminal utilice el comando cd para entrar al escritorio; "cd Escritorio" (depende del nombre que tenga su escritorio o que ruta tiene para llegar a este).
3.	Utilice el mismo comando para entrar a la aplicación "cd hipoteca".
4.	Luego ejecute Python App.py

Créditos
Este programa fue creado por David Zabala y Valentina Carmona.
