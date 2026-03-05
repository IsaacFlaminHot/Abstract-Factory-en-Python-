# Abstract Factory Pattern en Python

Este proyecto implementa el patrón de diseño **Abstract Factory** usando Python.

## Descripción

El programa simula un sistema que genera materiales educativos dependiendo de la modalidad de estudio.

Se manejan tres modalidades:

- Presencial
- Virtual
- Semipresencial

Cada modalidad genera una familia de objetos:

| Modalidad | Guía | Examen |
|------|------|------|
| Presencial | Guía impresa | Examen en papel |
| Virtual | Guía PDF | Examen en línea |
| Semipresencial | Guía Mixta | Examen Mixto |

El patrón Abstract Factory permite crear estos objetos sin que el cliente conozca las clases concretas.



## Estructura del proyecto


### Ejecución

Para ejecutar el programa:

"python Ejercicio_1_Abstract_Factory.py" para windows o en su caso para sistemas macOS es "python3 Ejercicio_1_Abstract_Factory.py"

### Salida Esperada 

Mostrando guia impresa
Aplicando examen en papel

Mostrando guia en formato PDF
Se aplica el examen en Linea

Mostrando guia en formato PDF e impresa
Aplicando examen en papel y en Linea


## Patrón utilizado

Se utiliza el patrón **Abstract Factory**, que permite:

- Crear familias de objetos relacionados
- Desacoplar la creación de objetos del código cliente
- Facilitar la extensión del sistema

## Conclusión 

Se me hace interesante ver como en este simple codigo, al momento de implementar otra modalidad, simplemente agregamos más clases, en vez de modificar el código ya existente.
