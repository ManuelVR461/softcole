<p>Test</p>
<p>Un colegio necesita un sistema para administrar sus cursos. El sistema tiene que soportar que
se ingresen varios cursos. Cada curso tendrá un profesor a cargo y una serie de alumnos
inscritos. Cada profesor, así como cada alumno puede estar en más de un curso. Además cada
curso tendrá una cantidad no determinada de pruebas, y el sistema debe permitir ingresar la
nota para cada alumno en cada prueba. Todas las pruebas valen lo mismo.</p>
<p>Modelo de datos</p>
<p>Escriba a continuación las tablas que utilizaría para resolver este problema con los campos y
llaves de éstas. Intente hacer el sistema lo más robusto posible, pero sin incluir datos
adicionales a los que se plantean acá.</p>
<p>SQL</p>
<p>Considerando el enunciado anterior conteste las siguientes preguntas:</p>
<ul>
 <li>Escriba una Query que entregue la lista de alumnos para el curso "programación"</li>
 <li>Escriba una Query que calcule el promedio de notas de un alumno en un curso.</li>
 <li>Escriba una Query que entregue a los alumnos y el promedio que tiene en cada ramo.</li>
 <li>Escriba una Query que lista a todos los alumnos con más de un ramo con promedio rojo.</li> 
</ul>

 <p>Dejando de lado el problema del cólegio se tiene una tabla con información de jugadores de tenis:</p>
 <br>
 <p>PLAYERS(Nombre, Pais, Ranking). Suponga que Ranking es un número de 1 a 100 que es distinto para cada jugador. Si la tabla en un momento dado tiene solo 20  tuplas, indique cuantas tuplas tiene la tabla que resulta de la siguiente consulta:</p>
 
 <pre> SELECT c1.Nombre, c2.Nombre FROM PLAYERS c1, PLAYERS c2 WHERE c1.Ranking > c2.Ranking</pre>

<p><Seleccione las respuestas correctas:</p>
<ul>
 <li>a) 400</li>
 <li>b) 190</li>
 <li>c) 20</li>
 <li>d) imposible saberlo</li>
 </ul>
 <br>
 <p>Diseño de software</p>
 <br>
<p>Backend<p>
 <br>
<p>Si usted estuviera resolviendo el problema del colegio implementando una aplicación web que incluya las siguientes funcionalidades:</p>
<ul>
 <li>CRUD alumnos, cursos, pruebas y notas.</li>
 <li>Listar a los alumnos junto a su promedio de notas.</li>
 <li>Filtar a todos los alumnos con más de un ramo con promedio rojo.</li>
 </ul>
 <br>
 <p>Puede utilizar alguno de estos frameworks:</p>
 <ul>
  <li>Laravel</li>
  <li>Django</li>
  <li>Ruby on Rails</li>
 </ul>
<p>Nota: La aplicación debe incluir un archivo README.md explicando como instalar las dependencias del proyecto y todos los supuestos considerados.</p>
 <p>Frontend</p>
<p>Construya una función o clase en JS que recibiendo el siguiente JSON por parámetro, permita renderear una agenda semanal en html y con bloques de 30 minutos como la siguiente:</p>
 <pre>
{
 "monday": [
 {"name": "Jorge", "start_time": "08:00", "end_time": "09:00"},
 {"name": "Jorge", "start_time": "09:30", "end_time": "11:00"},
 {"name": "Jorge", "start_time": "15:00", "end_time": "16:00"},
 {"name": "Jorge", "start_time": "17:00", "end_time": "19:30"}
 ],
 "tuesday": [
 {"name": "Jorge", "start_time": "08:00", "end_time": "09:00"},
 {"name": "Jorge", "start_time": "11:30", "end_time": "12:00"},
 {"name": "Jorge", "start_time": "15:00", "end_time": "16:00"},
 {"name": "Jorge", "start_time": "17:00", "end_time": "19:30"}
 ],
 "wednesday": [
 {"name": "Jorge", "start_time": "08:00", "end_time": "09:00"},
 {"name": "Jorge", "start_time": "10:30", "end_time": "12:00"},
 {"name": "Jorge", "start_time": "15:00", "end_time": "16:00"},
 {"name": "Jorge", "start_time": "17:00", "end_time": "19:30"}
 ],
 "thursday": [
 {"name": "Jorge", "start_time": "08:00", "end_time": "09:00"},
 {"name": "Jorge", "start_time": "09:30", "end_time": "12:00"},
 {"name": "Jorge", "start_time": "15:00", "end_time": "16:00"},
 {"name": "Jorge", "start_time": "17:00", "end_time": "19:30"}
 ],
 "friday": [
 {"name": "Jorge", "start_time": "08:00", "end_time": "09:00"},
 {"name": "Jorge", "start_time": "09:30", "end_time": "12:00"},
 {"name": "Jorge", "start_time": "15:00", "end_time": "16:00"},
 {"name": "Jorge", "start_time": "17:00", "end_time": "19:30"}
 ]
}
</pre>
 <br>
 <p>La agenda debe contener los distintos bloques y pintar con el nombre del paciente, las horas que
  están tomadas.</p>
 <p>Nota:</p>
<ul>
 <li>La agenda NO debe tener interacción solo dibujarse en la pantalla</li>
 <li>No utilizar tablas, sólo DIVS</li>
 <li>La agenda debe tener un ancho de 960px y esta centrada en la pantalla</li>
 </ul>
