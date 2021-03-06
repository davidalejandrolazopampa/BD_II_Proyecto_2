# BD2 - Proyecto 2 - Recuperación de Documentos de Texto
## Integrantes
|  **#** | **Código** | **Apellidos, Nombre** |
| :---: | :---: | :---: |
|  1 | 201810483 | Barrios Silva, Alonso Winston |
|  2 | 201810010 | Lazo Pampa, David Alejandro |
## Objtetivo
- Realiza un proyecto de búsqueda y recuperación, basado en la implementación de un índice invertido para la recuperación de diferentes Tweets.

## Implementación
### Backend
#### Preprocesamiento
Para esta parte, lo primero que se hizo es obtener los __stops words__, esto con ayuda de un archivo proporcionado en laboratorios anteriores. Luego se pasó a recorrer el archivo que tiene los tweets en archivos .json; a cada archivo se recorrienron sus tweets y a cada tweet se tokenizó, primero volviéndolo a minúscula y luego con la ayuda de la librería **nltk** se procedió a tokenizar. Por último, cada palabra tokenizada se comprobó que no estuviera en la lista de **stop words** y se les aplicó la reducción de palabras para de esta manera obtener su raíz. La función retorna una lista de todas las palabras usadas en los tweets ya tokenizadas.
  
#### Indice invertido
Para la construcción se hizo un procedimiento similar al preprocesamiento. Se recorrieron los archivos que tienen la data y se procedieron a tokenizar, una vez se tenía las palabras tokenizadas se procedió a construir el índice invertido, teniendo como atributos: 
- Palabra tokenizada
- Id del tweet
- Document frequency
- Collection frequency

#### Memoria secundaria
En cuanto al manejo de memoría secundaria, se carga el indice invertido a archivos en caso no exista ningún archivo .json, caso contrario se procede a leer el archivo y obtener el indice invertido. Cabe resaltar que el formato utilizado para el manejo de archivo es de tipo json.

#### Consultas
Para la parte de consultas, se tokenizó el query para de esta manera hacer una mejor búsqueda. Luego se calcula los **tfIdf** tanto del query como del índice, una vez se hace el calculo se procede a calcular el score con el coseno.

### Web
Para la parte web se usó la librería Flask de Python, tiene dos archivos: 1 index.html y 1 retrieval.html. En el archivo index se pide al usuario que ingrese los keywords y el rango que se desea obtener los resultados.

![Index](./rmd_img/index.png)

Y por último, al ingresar los datos, el programa retorna un conjunto de tweets, los cuales presentan una mayor similitud con los keywords ingresados.

![Index](./rmd_img/retrieval.png)

## VIDEO
### [Video-Drive](https://drive.google.com/file/d/15C8B0t7vbq2JPLIDcs_AFQTUh9m2KDXU/view?usp=sharing)
### [Youtube](https://www.youtube.com/watch?v=vSqyYzI_YlY&feature=youtu.be)
