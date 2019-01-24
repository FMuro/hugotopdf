+++
title = "Anillos"
weight = 10
+++

Consideremos la ecuación 

$$x^2-y^2=25.$$

Nos proponemos hallar todas sus soluciones enteras. El miembro de la izquierda se puede factorizar como producto de dos enteros y el de la derecha como producto de primos,

$$(x+y)(x-y)=5^2.$$

El **teorema fundamental de la aritméica** asegura que todo entero se descompone como producto de primos de manera única salvo signo. Por tanto, para que esta última ecuación sea cierta es necesario que los factores primos de $25$ se repartan entre los dos términos de la izquierda, de nuevo salvo signo. Es decir, las soluciones a nuestro problema son las soluciones enteras de los siguientes seis sistemas de ecuaciones lineales,

$$\left\\{
\begin{array}{rccccccc}
x+y&=&1,&-1,&5,&-5,&25,&-25;\cr
x-y&=&25,&-25,&5,&-5,&1,&-1.
\end{array}
\right.$$

Todos ellos son compatibles determinados y su solución es entera,

$$\begin{array}{rcl}
(x,y)&=&(13,-12),\, (-13,12),\, (5,0),\cr 
&&(-5,0),\, (13,12),\, (-13,-12).
\end{array}$$

Ahora introduciremos ligeros cambios en nuestra ecuación y consideraremos 

$$x^2+y^2=5.$$

En este caso no podemos obtener una factorización general no trivial del término de la izquierda como producto de dos enteros. Podemos sin embargo considerar factorizaciones en el **anillo** $\mathbb Z[i]$ de los números complejos con partes real e imaginaria enteras, denominados **enteros de Gauss**. Aquí los miembros de la ecuación factorizan como 

$$(x+iy)(x-iy)=(2+i)(2-i).$$

En este capítulo veremos, entre otras muchas cosas, que el teorema fundamental de la aritmética también tiene sentido en $\mathbb Z[i]$. Cualquier entero de Gauss se descompone como producto de primos de manera única, no solo salvo signo sino salvo producto por $\\{\pm 1,\pm i\\}$, que son los enteros de Gauss invertibles. Además, $5$ no es primo en $\mathbb Z[i]$ y su descomposición como producto de primos es el término de la derecha de la última ecuación. 

El razonamiento anterior nos conduce a que las soluciones de la ecuación que nos ocupa son las soluciones enteras de los siguientes dieciséis sistemas de ecuaciones lineales,

$$\left\\{
\begin{array}{rccccccc}
x+iy&=&1,&-1,&i,&-i,\cr
x-iy&=&5,&-5,&-i5,&i5,
\end{array}
\right.$$ 

$$\left\\{
\begin{array}{rccccccc}
x+iy&=&(2+i),&-(2+i),&i(2+i),&-i(2+i),\cr
x-iy&=&(2-i),&-(2-i),&-i(2-i),&i(2-i),
\end{array}
\right.$$

$$\left\\{
\begin{array}{rccccccc}
x+iy&=&(2-i),&-(2-i),&i(2-i),&-i(2-i),\cr
x-iy&=&(2+i),&-(2+i),&-i(2+i),&i(2+i),
\end{array}
\right.$$

$$\left\\{
\begin{array}{rccccccc}
x+iy&=&5,&-5,& i5,& -i5;\cr
x-iy&=&1,&-1,& -i,& i.
\end{array}
\right.$$

Como los térmios de la izquierda, $x+iy$ y $x-iy$, son conjugados, podemos descartar de plano los sistemas cuyos términos independientes no los sean, es decir, los cuatro primeros y los cuatro últimos. Las soluciones del resto, y de nuestro problema, son

$$\begin{array}{rcl}
(x,y)&=&(2,1),\,(-2,-1),\,(-1,2),\,(1,-2),\cr 
&&(2,-1),\,(-2,1),\,(1,2),\,(-1,-2).
\end{array}$$

Obviamente nuestra segunda ecuación se puede resolver fácilmente por métodos elementales, pero los métodos expuestos en este ejemplo, y otros aún más sofisticados, nos permitirán resolver otras ecuaciones que ahora no están realmente a nuestro alcance.
