gameoflife
==========
El juego de la vida es un autómata celular diseñado por el matemático británico John Horton Conway en 1970.

El juego de la vida es en realidad un juego de cero jugadores, lo que quiere decir que su evolución está determinada por el estado inicial y no necesita ninguna entrada de datos posterior.

https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

<h2>Description:</h2>

  1. El "tablero de juego" es una malla formada por cuadrados ("células") que se extiende por el infinito en todas las direcciones.

  2. Cada célula tiene 8 células vecinas, que son las que están próximas a ella, incluso en las diagonales.

  3. Las células tienen dos estados: están "vivas" o "muertas" (o "encendidas" y "apagadas").

  4. El estado de la malla evoluciona a lo largo de unidades de tiempo discretas (se podría decir que por turnos).

  5. El estado de todas las células se tiene en cuenta para calcular el estado de las mismas al turno siguiente.
    Todas las células se actualizan simultáneamente.

<h2>Reglas:</h2>

1. Una célula muerta con exactamente 3 células vecinas vivas "nace" (al turno siguiente estará viva).
2. Una célula viva con 2 ó 3 células vecinas vivas sigue viva, en otro caso muere o permanece muerta (por "soledad" o "superpoblación").
