+++
title = "Factorización"
weight = 20
+++

La noción clásica de divisibilidad se comporta de manera inesperada en presencia de divisores de cero. Aquí evitaremos estos problemas y estudiaremos la divisibilidad en dominios. Pondremos especial énfasis en el estudio de anillos donde el sea posible generalizar el teorema fundamental de la aritmética. Este teorema, ya conocido para los números enteros y más generalmente para los dominios euclídeos, nos dice que todo número no nulo que no sea una unidad factoriza como producto de primos de manera esencialmente única. Veremos además cómo estos anillos son de utilidad a la hora de resolver ecuaciones diofánticas.

## Divisores

\Begin{definition} 
En un dominio $R$, decimos que $a$ **divide** a $b$, o que $b$ es un **múltiplo** de $a$, y escribimos $a|b$, si $b=aq$ para cierto $q\in R$, que llamaremos **cociente**. Decimos que $a$ es un **divisor propio** de $b$ si además ni $a$ ni $q$ son unidades. Un elemento no trivial de $R$ es **irreducible** si no tiene divisores propios ni es una unidad. Dos elementos $a$ y $a'$ son **asociados** si tanto $a| a'$ como $a'|a$. 
 \End{definition}


\Begin{watch} 
El cero solo divide al cero, por tanto el cero es el único asociado del cero. Es más, si $a\neq 0$ y $a|b$ el cociente es único, es decir, solo hay un $q\in R$ tal que $b=qa$ pues si $b=q'a$ entonces $qa=q'a$ y por la propiedad cancelativa $q=q'$.
 \End{watch}


\Begin{proposition} 
En un dominio $R$:

* $a|b \Leftrightarrow (a)\supset (b)$.

* $(a)=(a')\Leftrightarrow$ $a$ y $a'$ son asociados $\Leftrightarrow  a'=ua$ para cierta unidad $u$.

* $u$ es una unidad $\Leftrightarrow (u)=(1)$.

* $a$ es un divisor propio de $b \Leftrightarrow (1)\supsetneq (a)\supsetneq (b)$.

 \End{proposition}


\Begin{proof} 

* $(a)\supset (b)\Leftrightarrow (a)\ni b\Leftrightarrow a|b$.

* La primera equivalencia se sigue del apartado anterior. Para la segunda, $\Leftarrow$ es obvio pues también $a=u^{-1}a'$. Veamos $\Rightarrow$. Si $a$ y $a'$ son asociados entonces $a'=qa$ y $a=q'a'$, luego $a=q'qa$. Si $a=0$ entonces $a'=0$ y podemos tomar $u=1$. En caso contrario, por la propiedad cancelativa $1=q'q$, luego $q'$ y $q$ son unidades y podemos tomar $u=q$.

* $\Rightarrow$ se ha visto antes. $\Leftarrow$ si $(u)=(1)$ entonces existe $r\in R$ tal que $ru=1$, con lo que $u$ es una unidad.

* Es consecuencia de los tres apartados anteriores. 

 \End{proof}


\Begin{remark} 
Si $a\in R$ no es nulo ni una unidad, un divisor de $a$  es bien propio, bien asociado, o bien una unidad, pero no puede ser dos de estas cosas a la vez. En particular, si $a$ y $a'$ son irreducibles y $a|a'$ entonces $a$ y $a'$ son asociados.  Los divisores de una unidad son las unidades. La primera caracterización de los asociados es especialmente interesante porque demuestra que cualquier propiedad de elementos de $R$ que pueda enunciarse en términos de sus correspondientes ideales principales es también válida para los elementos asociados.
 \End{remark}



## Factorizaciones      

En un dominio $R$, si $a\in R$ es un elemento no trivial que no es una unidad ni tampoco irreducible, entonces podemos descomponerlo como producto de dos divisores propios $a=bc$. Lo mismo podemos hacer con $b$ y con $c$, y así sucesivamente. Este procedimiento puede acabar en una descomposición de $a=b\_1\cdots b\_n$ como producto de elementos irreducibles $b_i\in R$, $1\leq i\leq n$, pero también podría no acabar nunca.

\Begin{definition} 
Decimos que **existen factorizaciones** en un dominio $R$ si el anterior proceso de factorización acaba para todo elemento no nulo que no sea una unidad.
 \End{definition}


\Begin{proposition} 
En un dominio $R$ existen factorizaciones $\Leftrightarrow$ no existe ninguna sucesión estrictamente creciente de ideales principales $(a_1)\subsetneq(a_2)\subsetneq(a_3)\subsetneq\cdots$.
 \End{proposition}


\Begin{proof} 
$\Rightarrow$ En lugar de A $\Rightarrow$ B demostraremos (no A) $\Leftarrow$ (no B). Tomamos pues una sucesión $(a_1)\subsetneq(a_2)\subsetneq(a_3)\subsetneq\cdots$. Podemos suponer que $a\_1\neq 0$ ya que en caso contrario la inclusión estricta $(a\_1)\subsetneq(a\_2)$ implicaría que $a\_2\neq 0$ y bastaría reindexar. Observa que $(a\_n)\subsetneq (1)$ para todo $n\geq 1$, ya que la sucesión es estrictamente creciente y $(1)=R$ es el ideal total. Las inclusiones $(a\_n)\subsetneq (a\_{n+1})\subsetneq(1)$ nos dicen entonces que $a_n$ se puede descomponer como producto de divisores propios $a\_n=q\_{n+1}a\_{n+1}$, por tanto el proceso de factorización no termina para
$$\begin{array}{rcl}
a\_1&=& q\_2a\_2\cr
&=& q\_2q\_3a\_3\cr
&=&q\_2q\_3q\_4a\_4\cr
&=&\cdots,
\end{array}$$
lo cual es una contradicción.

$\Leftarrow$ Como antes, en lugar de A $\Leftarrow$ B demostraremos (no A) $\Rightarrow$ (no B). Probaremos pues que si no existen factorizaciones entonces podemos encontrar una sucesión $(a_1)\subsetneq(a_2)\subsetneq(a_3)\subsetneq\cdots$. Sea $a\_1\in R$ un elemento no nulo que no sea una unidad para el cual el proceso de factorización no termina. Entonces podemos descomponerlo como producto de divisores propios $a\_1=q\_2a\_2$ de modo que alguno de los dos no es irreducible. Como el producto es conmutativo podemos suponer que es $a_2$ el que no es irreducible. Por tanto este también se puede descomponer como producto de dos divisores propios $a\_2=q\_3a\_3$ alguno de los cuales no es irreducible. Una vez más podemos suponer que es $a\_3$ el no irreducible y continuar indefinidamente con el proceso. Por construcción, esto nos da una sucesión creciente $(a_1)\subsetneq(a_2)\subsetneq(a_3)\subsetneq\cdots$ que es estricta porque todas las descomposiciones anteriores son como producto de dos divisores propios. 
 \End{proof}

La condición de la derecha del enunciado de la proposición anterior se suele denominar **condición de cadena ascendente** para ideales principales. Las condiciones de cadena juegan un papel muy importante en el álgebra moderna. Los anillos que satisfacen la condición de cadena ascendente para ideales cualesquiera se denominan **noetherianos**, por [Emmy Noether](https://es.wikipedia.org/wiki/Emmy_Noether). Los que cumplen la **condición de cadena descendente** para ideales arbitrarios se llaman **artinianos**, por [Emil Artin](https://es.wikipedia.org/wiki/Emil_Artin), padre de Michael, el autor del libro que estamos siguiendo. 


\Begin{example}\textrm{\normalfont (Un dominio sin factorizaciones)} 
No es fácil construir dominios donde no existan factorizaciones. El ejemplo más sencillo es el cociente $R/I$, donde $$R=k[x\_1,x\_2,x\_3,\dots]$$ es un anillo de polinomios sobre un cuerpo $k$ en una sucesión infinita de variables $\\{x\_n\\}_{n\geq 1}$ e $$I=(x\_1-x\_2^2, x\_2-x\_3^2, x\_3-x\_4^2,\dots)$$ es un ideal infinitamente generado que fuerza las relaciones $\bar x\_n=\bar x\_{n+1}^2\in R/I$, $n\geq 1$. En este cociente $$(\bar x\_1)\subsetneq(\bar x\_2)\subsetneq(\bar x\_3)\subsetneq\cdots.$$ Más concretamente, el proceso $\bar x\_1=\bar x\_2\bar x\_2=\bar x\_2\bar x\_3\bar x\_3=\bar x\_2\bar x\_3\bar x\_4\bar x\_4=\cdots$ no termina.

En rigor, es necesario probar que ningún $\bar{x}\_i$ es una unidad. Esto es cierto porque de lo contrario existiría algún polinomio $f\in R$ tal que $\bar{x}\_i\bar{f}=1$, o equivalentemente $x_if-1\in I$. Esto es imposible porque los elementos de $I$, al ser combinaciones lineales de sus generadores, no tienen término independiente.
 \End{example}


\Begin{definition} 
Un **dominio de factorización única** (también **DFU** o **UFD**) es un dominio donde existen factorizaciones y tal que dos factorizaciones de un mismo elemento coinciden salvo orden y asociados, es decir si $$b\_1\cdots b\_s=c\_1\cdots c\_t$$ son productos de irreducibles entonces $s=t$ y existe una permutación $\sigma\in S\_s$ de $s$ elementos tal que $b\_i$ y $c\_{\sigma(i)}$ son asociados, $1\leq i\leq s$.
 \End{definition}


\Begin{example}\textrm{\normalfont (Un dominio con factorizaciones que no son únicas)} 
En $\mathbb Z[\sqrt{-5}]\subset\mathbb C$, $$9=3^2=(2+\sqrt{-5})(2-\sqrt{-5}).$$
Todo elemento de $\mathbb Z[\sqrt{-5}]$ es de la forma $$z=a+b\sqrt{-5}=a+ib\sqrt{5}$$ donde $a,b\in\mathbb Z$. El cuadrado del módulo de tal elemento es $$|z|^2=|a+b\sqrt{-5}|=a^2+5b^2\in\mathbb Z.$$ Como $$|z_1z_2|^2=|z_1|^2\cdot|z_2|^2,$$ si $z\in \mathbb Z[\sqrt{-5}]$ es una unidad entonces $1=|z|^2\cdot|z^{-1}|^2$, así que $|z|^2\in\mathbb Z$ es invertible (y positivo), luego $|z|^2=1$. La única posibilidad de que esto ocurra es que $z=\pm 1$, por tanto las unidades de nuestro anillo son $\\{\pm1\\}$. Es más, las no unidades tienen módulo al cuadrado $>1$, así que si $z_1$ es un divisor propio de $z_2$ entonces $|z_1|^2<|z_2|^2$.

En $\mathbb Z[\sqrt{-5}]$ existen factorizaciones. En efecto, si hubiera una cadena $(z_1)\subsetneq(z_2)\subsetneq(z_3)\subsetneq\cdots$ entonces tendríamos que $|z_1|^2>|z_2|^2>|z_3|^2>\cdots\geq 0$, pero esto es imposible, no hay sucesiones infinitas estrictamente decrecientes de enteros no negativos.

Veamos que $3$ es irreducible. Si $3=z_1z_2$ es una factorización como producto de divisores propios entonces $3^2=|z_1|^2|z_2|^2$. No puede ser que $|z_i|^2=1$ ya que $z_i$ no es una unidad para ningún $i\in\\{1,2\\}$, luego, por el teorema fundamental de la aritmética para números enteros, $|z_1|^2=|z_2|^2=3$, pero no hay ningún elemento en $\mathbb Z[\sqrt{-5}]$ que tenga este cuadrado de módulo. Análogamente, $2\pm\sqrt{-5}$ es irreducible pues si $2\pm\sqrt{-5}=z_1z_2$ entonces de nuevo $|2\pm\sqrt{-5}|^2=3^2=|z_1|^2|z_2|^2$.

Por último, el $3$ no es un asociado de $2\pm\sqrt{-5}$ porque las únicas unidades de $\mathbb Z[\sqrt{-5}]$ son $\pm1$, luego las dos factorizaciones anteriores de $9$ como producto de irreducibles son esencialmente distintas.
 \End{example}


Con el objetivo de caracterizar los DFU, introducimos un nuevo tipo de elemento.

\Begin{definition} 
Un elemento de un dominio $p\in R$ es **primo** si no es nulo ni una unidad y además si $p|ab$ entonces bien $p|a$ o bien $p|b$. 
 \End{definition}


\Begin{remark} 
En términos de ideales, un elemento $p\in R$ no nulo es primo si y solo si $(p)\subset R$ es un ideal primo.
 \End{remark}


\Begin{proposition} 
En un dominio, todo elemento primo $p\in R$ es irreducible.
 \End{proposition}


\Begin{proof} 
El primo no es una unidad porque los ideales primos son distintos del total, $(p)\neq (1)$. Veamos que no tiene divisores propios. Para ello supongamos que $p=ab$ y demostremos que $a$ o $b$ es una unidad. Como $p|ab$, entonces $p|a$ o $p|b$. Si $p|a$ entonces $a=pq$, luego $p=ab=pqb$. Como los primos no son nulos y estamos en un dominio esto implica que $1=qb$, por tanto $b$ es una unidad. Si $p|b$ deducimos del mismo modo que $a$ tendría que ser una unidad.
 \End{proof}


\Begin{example}\textrm{\normalfont (Un irreducible que no es primo)} 
Continuando con el ejemplo anterior, el irreducible $3\in \mathbb Z[\sqrt{-5}]$ no es primo porque $3|(2+\sqrt{-5})(2-\sqrt{-5})$ pero $3\nmid 2\pm \sqrt{-5}$ porque ambos son irreducibles pero no asociados.
 \End{example}



\Begin{theorem} 
Un dominio $R$ es de factorización única $\Leftrightarrow$ existen factorizaciones y todo irreducible es primo.
 \End{theorem}


\Begin{proof} 
$\Rightarrow$ Basta ver que los irreducibles son primos. Sea $c\in R$ irreducible. Para ver que es primo, supongamos que $c|ab$. Hay que probar que $c|a$ o $c|b$. Como $c|ab$, entonces $ab=cd$ para cierto $d\in R$. Si $a=0$ entonces $c|a$ y si $b=0$, $c|b$. Si $a$ es una unidad, entonces despejando vemos que $c|b$, y si $b$ es una unidad $c|a$. Supongamos en adelante que $a$ y $b$ no son nulos ni unidades. Entonces $d$ no puede ser una unidad, ya que de lo contrario podriamos despejarla y $c=(d^{-1}a)b$ no sería irreducible, pues estaría descompuesto como producto de dos divisores propios. Por tanto $a$, $b$ y $d$ factorizan como productos de irreducibles,
$$\begin{array}{rcl}
a&=&a\_1\cdots a\_r,\cr
b&=&b\_1\cdots b\_s,\cr
d&=&d\_1\cdots d\_t.
\end{array}$$
Tenemos pues que
$$a\_1\cdots a\_rb\_1\cdots b\_s=cd\_1\cdots d\_t$$ son dos descomposiciones de un mismo elemento como producto de irreducibles. Por la unicidad, $c$ ha de ser asociado de algún $a_i$ o $b_j$, por tanto $c$ divide a $a$ o a $b$.

$\Leftarrow$ Veamos primero que si un primo $p$ divide a un producto de irreducibles $a_1\cdots a_r$ entonces $p$ es asociado de algún $a_i$. Procedemos por inducción en $r$. Para $r=1$, como $p|a_1$ y ambos elementos son irreducibles, han de ser asociados, según hemos visto anteriormente. Para $r>1$, como $p|a_1(a_2\cdots a_r)$, bien $p|a_1$ o bien $p|a_2\cdots a_r$. En el primer caso, ya tratado, $p$ es asociado de $a_1$, y en el segundo, por hipótesis de inducción, $p$ es asociado de algún otro $a_i$.

Consideramos ahora dos productos de irreducibles (primos) que son iguales
$$a\_1\cdots a\_r=b\_1\cdots b\_s.$$
Supongamos sin pérdida de generalidad que $1\leq r\leq s$. Procedemos por inducción en $r$. Si $r=1$ entonces $s=1$ puesto que un irreducible no tiene divisores propios. En este caso no hay nada que probar pues $a_1=b_1$. Sea $r>1$. Como $a_1|b_1\cdots b_s$ y $a_1$ es primo, $a_1$ es asociado de algún $b_i$, es decir $b_i=ua_1$ para cierta unidad $u\in R$. Por la propiedad cancelativa
$$a\_2\cdots a\_r=ub\_1\cdots\widehat{b}_i\cdots b\_s.$$
Observa que $b_1$ y $ub_1$ son asociados. 
Por hipótesis de inducción, las últimas factorizaciones coinciden salvo orden y asociados, por tanto las anteriores también. 
 \End{proof}


\Begin{proposition} 
En un DFU, un producto de irreducibles $a_1\cdots a_r$ divide a otro $b_1\cdots b_s$ si y solo si $r\leq s$ y, salvo reordenamiento, $a_i$ y $b_i$ son asociados $1\leq i\leq r$.
 \End{proposition}


\Begin{proof} 
Como el primer producto divide al segundo, existe $c\in R$ tal que $a_1\cdots a_rc=b_1\cdots b_s$. Si $c$ no es una unidad, lo factorizamos como producto de irreducibles $c=c_1\cdots c_t$, $$a_1\cdots a_rc_1\cdots c_t=b_1\cdots b_s.$$ Por la unicidad de las factorizaciones, cada $a_i$ es asociado a un $b_j$ distinto, y salvo reordenamiento podemos suponer que son los $r$ primeros. Si $c$ fuera una unidad, la unicidad de las factorizaciones demostraría directamente que $r=s$ y que cada $a_i$ es asociado de un $b_j$ distinto.
 \End{proof}


\Begin{corollary} 
Dados dos elementos no nulos de un DFU, $a,b\in R$, existe un **divisor común máximo** $d\in R$, que es un elemento que satisface:

* $d|a$ y $d|b$.

* si $d'|a$ y $d'|b$ entonces $d'|d$.

El divisor común máximo es único salvo asociados y se denota $\operatorname{mcd}(a,b)$ o $\gcd(a,b)$.
 \End{corollary}


\Begin{proof} 
Si $a$ o $b$ fuera una unidad, cualquier unidad sería un divisor común máximo puesto los divisores de una unidad son las unidades. En caso contrario, basta factorizar ambos elementos $a=a_1\cdots a_r$ y $b=b_1\cdots b_s$ como producto de primos y tomar $d$ como el producto del mayor subconjunto de los factores de $a$ que tienen asociados distintos entre los factores de $b$. La unicidad salvo asociados se deduce de que si $d$ y $d'$ son divisores comunes máximos de $a$ y $b$ entonces por definición $d|d'$ y $d'|d$.
 \End{proof}


\Begin{remark} 
 Si $a$ o $b$ es una unidad $\operatorname{mcd}(a,b)=1$. A diferencia de los dominios euclídeos, en un DFU un divisor común máximo no tiene por qué satisfacer una identidad de Bézout, es decir, $\operatorname{mcd}(a,b)$ no tiene por qué estar en el ideal $(a,b)$. Veremos ejemplos más adelante.
 \End{remark}


\Begin{corollary} 
Dados dos elementos no nulos de un DFU, $a,b\in R$, existe un **múltiplo común mínimo** $m\in R$, que es un elemento que satisface:

* $a|m$ y $b|m$.

* si $a|m'$ y $b|m'$ entonces $m|m'$.

El múltiplo común mínimo es único salvo asociados y se denota $\operatorname{mcm}(a,b)$ o $\operatorname{lcm}(a,b)$.
 \End{corollary}


\Begin{proof} 
Si $d$ es un divisor común máximo entonces $m=\frac{ab}{d}=a\frac{b}{d}=\frac{a}{d}b$ es un múltiplo común mínimo. En efecto, la primera propiedad es obvia. Comprobemos la segunda. Si $a|m'$ y $b|m'$ entonces $d|m'$. Es más, $\frac{a}{d}|\frac{m'}{d}$ y $\frac{b}{d}|\frac{m'}{d}$. Como $\frac{a}{d}$ y $\frac{b}{d}$ no tienen factores primos asociados, su múltiplo común mínimo es el producto $\frac{ab}{d^2}$, así que $\frac{ab}{d^2}|\frac{m'}{d}$. Multiplicando por $d$ deducimos que $m=\frac{ab}{d}|m'$. La unicidad salvo asociados se deduce como en el caso del divisor común máximo.
 \End{proof}


\Begin{lemma} 
Dada una sucesión creciente de ideales $I\_1\subset I\_2\subset I\_3\subset\cdots$ en un anillo $R$, su unión $I\_\infty=\cup\_{n\geq 1}I\_n$ es un ideal.
 \End{lemma}


\Begin{proof} 
Por un lado, $0\in I\_1\subset I\_{\infty}$. Por otro, dados $a,b\in I\_\infty$ es obvio que $a,b\in I\_n$ para cierto $n\geq 1$, por tanto $a+b$, $-a$ y $ra$, $r\in R$, pertenecen a $I\_n\subset I\_\infty$.
 \End{proof}


\Begin{proposition} 
Todo DIP es un DFU.
 \End{proposition}


\Begin{proof} 

Sea $R$ un DIP. Veamos por reducción al absurdo que no puede existir una sucesión estrictamente creciente de ideales principales
$$(a_1)\subsetneq(a_2)\subsetneq(a_3)\subsetneq\cdots.$$
Al estar en un DIP, $\cup\_{n\geq 1}(a\_n)=(b)$ para cierto $b\in R$. Como $b\in \cup\_{n\geq 1}(a\_n)$ este elemento ha de estar en cierto término de la sucesión, $b\in (a\_n)$. Si esto es así $(b)\subset (a\_n)\subsetneq (a\_{n+1})\subset (b)$, lo cual es una contradicción.

Veamos ahora que todo irreducible $a\in R$ es primo. Probaremos por reducción al absurdo que el ideal $(a)$ es maximal y por tanto primo. Si $(a)$, que es un ideal propio y no trivial, no fuera maximal podríamos encontrar un ideal $I$ tal que $(a)\subsetneq I\subsetneq R$. Como $R$ es un DIP, $I=(b)$ para cierto $b\in I$. Entonces tenemos que $(a)\subsetneq(b)\subsetneq(1)$. Esto quiere decir que $b$ es un divisor propio de $a$, lo cual es una contradicción. 
 \End{proof}


Más adelante veremos ejemplos de DFU que no son DIP.

\Begin{proposition} 
En un DIP, dados $a,b\in R$, cualquier $d\in R$ tal que $(a,b)=(d)$ es un $\operatorname{mcd}(a,b)$.
 \End{proposition}


\Begin{proof} 
Como $a,b\in (a,b)=(d)$, $d$ es un divisor común. Si $d'|a$ y $d'|b$ entonces $a,b\in (d')$, luego $(d)=(a,b)\subset (d')$ y por tanto $d'|d$.
 \End{proof}


Acabamos de demostrar que en un DIP todo divisor común máximo satisface una **identidad de Bézout**.



\Begin{definition} 
Un **dominio euclídeo** es un dominio $R$ equipado con una función $$\delta\colon R\setminus\\{0\\}\longrightarrow\\{0,1,2\dots\\},$$ llamada **función de tamaño** o **euclídea**, tal que dados $D,d\in R$ con $d\neq 0$, denominados **dividendo** y **divisor**, respectivamente, existen $c,r\in R$, **cociente** y **resto**, de modo que $$D=dc+r$$ y bien $r=0$ o bien $\delta( r )<\delta(d)$.
 \End{definition}


\Begin{remark} 
Sabemos que $\mathbb Z$ y $k[x]$, con $k$ un cuerpo, son dominios euclídeos con función de tamaño el valor absoluto y el grado, respectivamente. En general, el cociente y el resto no están determinados de manera única por el dividendo y el divisor, por ejemplo $$13=4\cdot 3+1=5\cdot 3+(-2).$$ Los dominios euclídeos son dominios de ideales principales. Todo ideal no trivial está generado por cualquiera de sus elementos no nulos de menor tamaño.
 \End{remark}


\Begin{example}\textrm{\normalfont (Los enteros de Gauss)} 
Vamos a ver que $\mathbb{Z}[i]$ con el cuadrado del módulo como función euclídea es un dominio euclídeo. Tomamos $D,d\in\mathbb{Z}[i]$, este último no nulo,$$\begin{array}{rcl}D&=&a+ib,\cr d&=& x+iy.\cr \end{array}$$ Encontrar un cociente euclídeo se reduce a hallar un múltiplo de $d$ en el interior del círculo de centro $D$ y radio $|d|$. Vamos a ver cómo hacerlo de manera analítica. Consideramos el número complejo $$\frac{D}{d}=u+iv.$$ Aquí $u$ y $v$ son números reales, de hecho racionales, pero no necesariamente enteros. Aproximamos el anterior número complejo por un entero de Gauss $$c=u_0+iv_0\in\mathbb Z[i]$$ de modo que sus partes real e imaginaria estén lo más cerca posible de las del complejo $\frac{D}{d}$, $$\begin{array}{rcl} |u-u_0|&\leq &\frac{1}{2},\cr |v-v_0|&\leq &\frac{1}{2}. \end{array}$$ De este modo $$\left|\frac{D}{d}-c\right|=\sqrt{(u-u_0)^2+(v-v_0)^2}\leq \frac{1}{\sqrt{2}}.$$ Veamos que $c$ es el cociente de una división euclídea. El resto sería $r=D-dc$ y su módulo es $$|r|=|D-dc|=|d|\cdot \left|\frac{D}{d}-c\right|\leq \frac{|d|}{\sqrt{2}}<|d|.$$ 
 \End{example}



\Begin{example}\textrm{\normalfont (Enteros cuadráticos)} 
Un entero $n\in\mathbb Z$ es **libre de cuadrados** no es divisible por el cuadrado de ningún primo, es decir, si entre sus factores primos no podemos encontrar dos asociados. Por ejemplo, $-4=2(-2)$ no es libre de cuadrados pero $6=2\cdot 3$ y $-1$ sí. Los **cuerpos de números cuadráticos** son $\mathbb Q[\sqrt{n}]\subset\mathbb C$ donde $n$ es un entero libre de cuadrados. Su **anillo de enteros** $R\subset\mathbb Q[\sqrt{n}]$ está formado por los elementos que son raíces de un polinomio mónico en $\mathbb Z[x]$. Se puede comprobar que $R=\mathbb Z[\sqrt{n}]$ si $n\equiv 2,3$ mod $4$ y $R=\mathbb Z[\frac{1+\sqrt{n}}{2}]$ si $n\equiv 1$ mod $4$. Decimos que $R$ es un **anillo de enteros cuadráticos imaginarios** si $n{<}0$. Los anillos de enteros cuadráticos imaginarios que son DIPs se obtienen para $$n=−1, −2, −3, −7, −11, −19, −43, −67, −163.$$ De estos, son dominios euclídeos para $$n=−1, −2, −3, −7, −11.$$ En todos estos casos podemos además tomar el cuadrado del módulo como función de tamaño. El resto de anillos de enteros cuadráticos imaginarios no son ni siquiera DFUs. Para $n{>}0$, obtenemos dominios euclídeos con la 'norma' $N(a+b\sqrt{n})=a^2-b^2n$ para $$n=2, 3, 5, 6, 7, 11, 13, 17, 19, 21, 29, 33, 37, 41, 57, 73.$$ Para $n=69$, $R=\mathbb Z[\frac{1+\sqrt{69}}{2}]$ es también un dominio euclídeo pero no con una función de tamaño distinta de $N$.
 \End{example}

La siguiente aplicación interactiva te permite explorar la posibilidad de realizar divisiones euclídeas respecto del cuadrado del módulo complejo en el anillo de enteros cuadráticos imaginarios $R\subset\mathbb Q[\sqrt{-n}]$ para ciertos valores positivos de $n$. Para $n=1$ tenemos los enteros de Gauss. Puedes seleccionar los coeficientes del dividendo $D=a+b\sqrt{-n}$ y del divisor $d=x+y\sqrt{-n}$, si $-n\not\equiv 1$ mod $4$. Si $-n\equiv 1$ mod $4$, el dividendo y el divisor son de la forma $D=a+b\frac{1+\sqrt{-n}}{2}$ y $d=x+y\frac{1+\sqrt{-n}}{2}$, respectivamente. Los coeficientes del dividendo pueden estar en $[-10,10]$ y los del divisor en $[-5,5]$. Aparece un círculo amarillo centrado en $D$ de radio $|d|$. Los puntos verdes son elementos del anillo y los azules son además múltiplos del divisor. Cada punto azul en el _interior_ del círculo representa una división euclídea. La aplicación da la lista de todos los pares $(c,r)$ que producen divisiones euclídeas $D=d\cdot c+r$.

<div class="sage">
  <script type="text/x-sage">
from sage.plot.circle import Circle
@interact(layout={'top': [['parameter'],['dividend_x', 'divisor_x'],['dividend_y','divisor_y']]})
def _(parameter=selector([1,2,3,5,6,7,10,11], label="n=", buttons=True), dividend_x=slider(-10,10, step_size=1, default = 0, label="a="), dividend_y=slider(-10,10, step_size=1, default = 0, label="b="), divisor_x=slider(-5,5, step_size=1, default = 1, label="x="), divisor_y=slider(-5,5, step_size=1, default = 0, label="y=")):
    if ((divisor_x,divisor_y) == (0,0)):
        show("NO SE PUEDE DIVIDIR POR CERO. ESCOJE UN DIVISOR NO NULO.")
    else:
        if (-parameter % 4 != 1):
            dividend = dividend_x+I*dividend_y*sqrt(parameter)
            divisor = divisor_x+I*divisor_y*sqrt(parameter)
            radius = N(abs(divisor))
            bound_x = floor(radius)+1
            bound_y = floor(radius/sqrt(parameter))+1
            interval_lattice_x = [dividend.real()-bound_x .. dividend.real()+bound_x]
            interval_lattice_y = [dividend.imag()+y*sqrt(parameter) for y in [-bound_y .. bound_y]]
            lattice = cartesian_product([interval_lattice_x,interval_lattice_y]).list()
            multiples = [z for z in lattice if ((((z[0]+I*z[1])/divisor).real()).is_integer() and (((z[0]+I*z[1])/divisor).imag()/sqrt(parameter)).is_integer())]
        else:
            dividend = dividend_x+dividend_y*(1+I*sqrt(parameter))/2
            divisor = divisor_x+divisor_y*(1+I*sqrt(parameter))/2
            radius = N(abs(divisor))
            bound_x = floor(radius)+1
            bound_y = floor(2*radius/sqrt(parameter))+1
            lattice = [(dividend.real()+x+1/2*is_odd(y), dividend.imag()+y*sqrt(parameter)/2) for y in [-bound_y .. bound_y] for x in [-bound_x .. bound_x]]
            def integer_odd(x,y):
                if x.is_integer():
                    return (y+1/2*ZZ(x).mod(2)).is_integer()
                else:
                    return False
            multiples = [z for z in lattice if integer_odd(((z[0]+I*z[1])/divisor).imag()*2/sqrt(parameter),((z[0]+I*z[1])/divisor).real())]
        divisions = [z for z in multiples if abs(divisor)-abs(dividend - (z[0]+I*z[1])) > 0]
        if len(divisions) == 0:
            show("NO HAY DIVISIONES EUCLÍDEAS.")
        else:
            for z in divisions:
                show((expand((z[0]+I*z[1])*divisor.conjugate()/(divisor.real()^2+divisor.imag()^2)), dividend-(z[0]+I*z[1])))
        lattice_plot = point(lattice, rgbcolor='green')
        multiples_plot = point(multiples, rgbcolor='blue', size=50)
        circ = circle((dividend.real(), dividend.imag()), radius, alpha=.4, fill = True, facecolor='yellow', thickness=0)
        if (dividend.real(),dividend.imag()) in multiples:
            cent = point([(dividend.real(),dividend.imag())], rgbcolor='blue', size=200)
        else:
            cent = point([(dividend.real(),dividend.imag())], rgbcolor='green', size=200)
        return show(circ+lattice_plot+multiples_plot+cent, aspect_ratio=1)
  </script>
</div>


## Polinomios

En este epígrafe demostraremos que los anillos de polinomios con coeficients en un DFU son también DFUs. En adelante $R$ denotará un DFU y $k=Q( R )$ su cuerpo de fracciones.

\Begin{definition} 
Un polinomio no nulo $f=f(x)=a_nx^n+\cdots+a_1x+a_0\in R[x]$ es **primitivo** si el divisor común máximo de sus coeficientes es $1$, es decir, si no existe ningún primo $p\in R$ tal que $p|a_i$ para todo $1\leq i\leq n$. 
 \End{definition}

Los únicos polinomios constantes primitivos son las unidades de $R$.

\Begin{lemma} 
Dado $f=f(x)=a_nx^n+\cdots+a_1x+a_0\in k[x]$ no nulo existe una constante $c\in k$, llamada **contenido**, y un polinomio primitivo $f_0(x)\in R[x]$ tal que $$f(x)=c\cdot f_0(x).$$ Además $c$ y $f_0(x)$ son únicos salvo producto por unidades de $R$. Denotaremos $c=\operatorname{cont}(f)$. 
 \End{lemma}


\Begin{proof} 

Veamos la existencia. Podemos quitar denominadores de los coeficientes de $f(x)$ multiplicando por una constante $d\in R$ no nula, $$d\cdot f(x)\in R[x].$$ Si $e$ es el divisor común máximo de los coeficientes de $d\cdot f(x)$ vemos que podemos tomar
$$\begin{array}{rcl}
f_0&=&\frac{d}{e}\cdot f(x),\cr
c&=&\frac{e}{d}.
\end{array}$$

Probemos ahora la unicidad. Supongamos que $c\cdot f_0(x)=c'\cdot f'\_0(x)$ siendo $f_0(x),f'\_0(x)\in R[x]$ primitivos. Podemos además suponer sin pérdida de generalidad que $c,c'\in R$, multiplicando por un denominador común si fuera necesario. Como el divisor común máximo de los coeficientesde $f_0(x)$ es $1$, el divisor común máximo de los coeficientes de $c\cdot f_0(x)$ es $c$. Análogamente el divisor común máximo de los coeficientes de $c'\cdot f'\_0(x)$ es $c'$. Por la unicidad del divisor común máximo, $c$ y $c'$ son asociados, es decir $c'=u\cdot c$ donde $u\in R$ es una unidad. Por tanto, por la propiedad cancelativa, $f_0(x)=u\cdot f\_0'(x)$.
    \End{proof}


\Begin{remark} 
Si el contenido de un polinomio $f(x)\in k[x]$ está en $R$ entonces $f(x)\in R[x]$. Recíprocamente, el contenido de un polinomio $f(x)\in R[x]$ es el divisor común máximo de sus coeficientes, en particular $\operatorname{cont}(f)\in R$. Es más, dada una constante $a\in R$ tenemos que $a|f(x)$ si y solo si $a|\operatorname{cont}(f)$. Un polinomio $f(x)\in R[x]$ es primitivo si y solo si $\operatorname{cont}(f)=1$.
 \End{remark}


\Begin{theorem}\textrm{\normalfont (Lema de Gauss)} 
El producto de polinomios primitivos en $R[x]$ es primitivo. 
 \End{theorem}


\Begin{proof} 
 Dado un primo $p\in R$, consideramos el homomorfismo de **reducción módulo $p$** $$\phi_p\colon R[x]\longrightarrow (R/(p))[x]$$ definido en las constantes como $\phi_p(a)=\bar a$, $a\in R$, tal que $\phi_p(x)=x$. Es decir, $$\phi_p(a_nx^n+\cdots+a_1x+a_0)=\bar a_nx^n+\cdots+\bar a_1x+\bar a_0.$$ El homomorfismo $\phi_p$ consiste simplemente en reducir los coeficientes módulo $(p)$. En particular $f\in \ker \phi_p$ si y solo si $p$ divide a todos los coeficientes de $f$. Por tanto $f\in R[x]$ es primitivo si y solo si $\phi_p(f)\neq 0$ para todo $p\in R$ primo. Si $f,g\in R[x]$ son primitivos entonces $$\phi_p(f\cdot g)=\phi_p(f)\cdot \phi_p(g)\neq 0$$ para todo $p\in R$ primo ya que $(R/(p))[x]$ es un dominio. Es decir, $f\cdot g$ también es primitivo.
 \End{proof}


\Begin{corollary} 
Dados $f,g\in k[x]$ tenemos que $\operatorname{cont}(f\cdot g)=\operatorname{cont}(f)\cdot \operatorname{cont}(g)$. 
 \End{corollary}


\Begin{proof} 
 Tomamos $f,g\in k[x]$ y los descomponemos  $$\begin{array}{rcl} f&=&c\cdot f_0,\cr g&=&d\cdot g_0, \end{array}$$ con $c,d\in k$ y $f_0,g_0\in R[x]$ primitivos. Entonces $$f\cdot g=(c\cdot d)\cdot (f_0\cdot g_0).$$ Como $f_0\cdot g_0$ es primitivo por el Lema de Gauss, esta es una descomposición válida del producto $f\cdot g$, así que $c\cdot d$ es su contenido.
 \End{proof}


\Begin{proposition} 
Dados $f,g\in R[x]$, si $g|f$ en $k[x]$ y $g$ es primitivo entonces $g|f$ en $R[x]$. 
 \End{proposition}


\Begin{proof} 
 Supongamos que $f=g\cdot q$ en $k[x]$. Como $g$ es primitivo, $$\operatorname{cont}(f)=\operatorname{cont}(g)\operatorname{cont}(q)=\operatorname{cont}(q).$$ Como $f\in R[x]$ su contenido está en $R$, y como este coindice con el de $q$, entonces $q\in R[x]$, por lo que $g|f$ en $R[x]$.
 \End{proof}


\Begin{proposition} 
Un polinomio $f\in R[x]$ no constante es irreducible en $R[x]$ $\Leftrightarrow$ $f$ es primitivo e irreducible en $k[x]$. 
 \End{proposition}


\Begin{proof} 

$\Leftarrow$ Supongamos que por reducción al absurdo que $f$ no es irreducible en $R[x]$. Lo descomponemos como producto de divisores propios $f=gh$ en $R[x]$. Si $g$ fuera constante entonces dividiría al contenido de $f$, que es $1$, por tanto $g$ sería una unidad, lo cual entra en contradicción con que sea un divisor propio. Lo mismo ocurriría si $h$ fuera constante. Si $g$ y $h$ no son constantes entonces también son divisores propios de $f$ en $k[x]$, pues no podrían ser unidades, luego $f$ no sería irreducible.

$\Rightarrow$ Si $f$ no fuera primitivo tampoco sería irreducible en $R[x]$ pues su contenido sería un divisor propio. Supongamos por reducción al absurdo que $f$ tiene un divisor propio $g$ en $k[x]$. Aquí ser un divisor propio significa que $0<$ grado de $g<$ grado de $f$.  Multiplicando por una constante no nula de $k$ si fuera necesario (por el inverso del contenido), podemos suponer que $g\in R[x]$ y es primitivo. Por la proposción anterior $g$ también divide a $f$ en $R[x]$ y por tanto es un divisor propio por cuestión de grados.
 \End{proof}


\Begin{remark} 
Una constante $a\in R$ es irreducible en $R[x]$ si y solo si lo es en $R$.
 \End{remark}


\Begin{theorem} 
$R[x]$ es un DFU.
 \End{theorem}


\Begin{proof} 

Primero probamos que existen factorizaciones en $R[x]$. Supongamos por reducción al absurdo que tenemos una sucesión estrictamente creciente de ideales principales (que podemos suponer no nulos) en este anillo, $$(f\_1)\subsetneq (f\_2)\subsetneq (f\_3)\subsetneq\cdots.$$ Ningún $(f\_n)$ puede ser el ideal total porque la sucesión estabilizaría necesariamente a partir de este punto. Por tanto, cada $f\_{n+1}$ es un divisor propio de $f\_{n}$, $n\geq 1$. En particular grado de $0\leq$ grado de $f\_{n+1}\leq$ grado de $f\_{n}$, es decir, los grados de los generadores forman una sucesion decreciente de enteros no negativos. Esta sucesión de enteros no nulos ha de estabilizar a partir de cierto punto, es decir, ha de existir cierto $n\_0\geq 1$ tal que grado de $f\_{n+1}=$ grado de $f\_{n}$ para todo $n\geq n\_0$, o equivalentemente $f\_n=c\_{n+1}f\_{n+1}$ para cierto $c\_{n+1}\in R$ que no puede ser una unidad ni tampoco nulo.
Si llamamos $d\_n=\operatorname{cont}(f\_n)$ tenemos que $d\_n=c\_{n+1}d\_{n+1}$. Ningún contenido $d\_n$ puede ser una unidad porque es divisible por $c\_{n+1}$ así que por tanto $d\_n=c\_{n+1}d\_{n+1}$ es una factorización como producto de divisores propios. Sustituyendo reiteradamente vemos que
$$
\begin{array}{rcl}
d\_{n\_0}&=& c\_{n\_0+1}d\_{n\_0+1}\cr
&=& c\_{n\_0+1}c\_{n\_0+2}d\_{n\_0+2}\cr
&=& c\_{n\_0+1}c\_{n\_0+2}c\_{n\_0+3}d\_{n\_0+3}\cr
&=&\cdots
\end{array}
$$
Por tanto el proceso no termina para $d\_{n\_0}$, lo que contradice la existencia de factorizaciones en $R$.

Veamos que todo elemento irreducible de $R[x]$ es primo. Consideraremos primero el caso en el que nuestro irreducible es un polinomio $f\in R[x]$ no constante. Supongamos que $f|gh$ en $R[x]$. Como $f$ también es irreducible en $k[x]$, que es un DFU, entonces $f$ es primo en $k[x]$ y por tanto $f|g$ o $f|h$ en $k[x]$. Los tres polinomios están en $R[x]$ y al ser $f$ irreducible en este anillo ha de ser primitivo, así que entonces $f|g$ o $f|h$ en $R[x]$.

Supongamos ahora que  $a\in R\subset  R[x]$ es una constante irreducible y que $a|gh$ en $R[x]$. Esto último equivale adecir que $a|\operatorname{cont}(gh)=\operatorname{cont}(g)\operatorname{cont}(h)$. Como $R$ es un DFU, el irreducible $a$ es primo en $R$, así que $a|\operatorname{cont}(f)$ o $a|\operatorname{cont}(g)$, es decir, $a|g$ o $a|h$.
 \End{proof}
 

\Begin{corollary} 
$R[x_1,\dots, x_n]$ es un DFU para todo $n\geq 0$.
 \End{corollary}


\Begin{example}\textrm{\normalfont (El anillo $\mathbb Z[x]$)} 
Este anillo es un DFU pero no es un DIP. Para comprobarlo basta ver que la identidad de Bézout para el divisor común máximo no siempre se da. Tanto $2$ como $x$ son primos en $\mathbb Z[x]$ según criterios vistos anteriormente. Como no son asociados, $\operatorname{mcd}(2,x)=1$, pero $1\notin (2,x)$ ya que todo elemento de este ideal es de la forma $2g+xh$ para ciertos $g,h\in \mathbb Z[x]$, así que su término independiente ha de ser par. Por tanto no hay una identidad de Bézout en este caso. El ideal $(2,x)\subset \mathbb Z[x]$ es de hecho un ejemplo de ideal que no es principal.
 \End{example}

Tenemos que $R[x]\subset k[x]$. El siguiente resultado nos permite calcular cómo se ven los ideales del segundo dentro del primero.

\Begin{proposition} 
Si $(f)\subset k[x]$ es un ideal no nulo entonces $(f)\cap R[x]=(f_0)$, donde $f=c\cdot f_0$ con $c\in k$ el contenido y $f_0 \in R[x]$ primitivo. 
 \End{proposition}

\Begin{proof} 
La intersección $(f)\cap R[x]$ es un ideal ya que es la imagen inversa de $(f)\subset k[x]$ a través de la inclusión $R[x]\hookrightarrow k[x]$. Veamos la igualdad de ideales por doble inclusión.

$\supset$ Como $f_0 \in R[x]$ y $f_0 =c^{-1}f \in (f)\subset k[x]$, tenemos que $f_0 \in (f)\cap R[x]$, lo cual demuestra esta inclusión.

$\subset$ Todo elemento $p \in (f)$ es de la forma $p =g\cdot f =(g \cdot c)\cdot f_0$. Si $p \in R[x]$, como $f_0 |p$ en $k[x]$ y $f_0$ es primitivo, $f_0 |p$ también en $R[x]$, así que $g \cdot c\in R[x]$ y por tanto $p \in (f_0)\subset R[x]$.
 \End{proof}

El siguiente resultado nos demuestra con rigor que las dos posibles maneras de añadirle a $R$ raíces de polinomios irreducibles dan resultados isomorfos.

\Begin{theorem} 
Dado un polinomio irreducible $f\in R[x]$, un cuerpo $K$ que contiene al cuerpo de fracciones, $k\subset K$, y una raíz $\alpha\in K$ de $f$, hay un único isomorfismo $R[x]/(f)\cong R[\alpha]\subset K$ que se comporta sobre $R$ como la identidad y que envía $\bar{x}$ a $\alpha$.
 \End{theorem}

\Begin{proof} 
Por el principio de sustitución, hay un único homomorfismo $g\colon R[x]\rightarrow K$ que se restringe a la inclusón $R\subset k\subset K$ sobre el dominio de coeficientes y que satisface $g(x)=\alpha$. La imagen de $g$ es $R[\alpha]$ por definición. Por el primer teorema de isomorfía, basta probar que $\ker g=(f)\subset R[x]$. Para ello, consideramos la extensión $\bar g\colon k[x]\rightarrow K$ de $g$ que se define como la inclusión $k\subset K$ sobre el cuerpo de coeficientes y que cumple $\bar{g}(x)=\alpha$. Veamos que $\ker\bar{g}=(f)\subset k[x]$.
 
El ideal $\ker\bar{g}\subset k[x]$ está formado por todos los polinomios que tienen a $\alpha$ como raíz. Al ser $k[x]$ un dominio euclídeo, $\ker\bar{g}=(\tilde f)$ donde $\tilde f\in k[x]$ es cualquier polinomio no nulo de grado mínimo en este ideal. Realizamos la división euclídea en $k[x]$, $f(x)=c(x)\tilde{f}(x)+r(x)$. Si $r$ no fuera trivial, su grado sería menor que el de $\tilde{f}$, pero $r(x)=f(x)-c(x)\tilde{f}(x)$, por tanto $r(\alpha)=f(\alpha)-c(\alpha)\tilde{f}(\alpha)=0-c(\alpha)0=0$. Esto es imposible porque $\tilde{f}$ es de grado mínimo. Por tanto $r=0$ y $f(x)=c(x)\tilde{f}(x)$. El polinomio $c(x)$ ha de ser constante porque $f$ es también irreducible en $k[x]$, así que $f$ y $\tilde{f}$ son asociados, luego generan el mismo ideal, $\ker\bar{g}=(f)\subset k[x]$.

Como $g=\bar{g}|_{R[x]}$, $\ker g=\ker\bar{g}\cap R[x]=(f)\subset R[x]$ en virtud de la proposición anterior, pues $f\in R[x]$, al ser irreducible, es primitivo. Esto concluye la demostración.
 \End{proof}

\Begin{remark} 
Recuerda que, dado un cuerpo $k$, un polinomio $f\in k[x]$ de grado $\leq 3$ es irreducible si y solo si no tiene raíces en $k$.
 \End{remark}

\Begin{example}\textrm{\normalfont (Añadiendo elementos)} 
El polinomio $x^2+1\in\mathbb{Z}[x]$ es irreducible ya que es primitivo e irreducible en $\mathbb{Q}[x]$ pues su grado es $\leq 3$ y no tiene raíces racionales. Por tanto el resultado anterior se aplica a la inclusión $\mathbb Q\subset\mathbb C$ y a la raíz compleja $i\in\mathbb C$ de $x^2+1$ y obtenemos un isomorfismo con los enteros de Gauss,
$$
\begin{array}{rcl}
\mathbb Z[x]/(x^2+1)&\cong&\mathbb Z[i],\cr
 \bar{x}&\mapsto& i.
\end{array}
$$

Análogamente obtenemos por ejemplo 
$$
\begin{array}{rcl}
\mathbb Z[x]/(x^2-2)&\cong&\mathbb Z[\sqrt{2}],\cr
 \bar{x}&\mapsto& \sqrt{2}.
\end{array}
$$
Vimos que todo elemento de $\mathbb Z[x]/(x^2-2)$ se podía expresar de manera única como $a\_1\bar x+a\_0$, $a\_0,a\_1\in\mathbb Z$, así que todo elemento de $\mathbb Z[\sqrt{2}]$ se puede escribir de manera única como $a\_1 \sqrt{2}+a\_0$, $a\_0,a\_1\in\mathbb Z$.
 \End{example}

Finalmente veremos un par de condiciones suficientes más avanzadas para la irreducibilidad de un polinomio.

\Begin{proposition} 
Si $f=a\_nx^n+\cdots+a\_1x+a\_0\in R[x]$ es un polinomio primitivo de grado $n>0$, $p\in R$ es un primo que no divide $a\_n$ y la reducción de $f$ módulo $p$ es irreducible en $(R/(p))[x]$, entonces $f$ es irreducible en $R[x]$. 
 \End{proposition}


\Begin{proof} 
 Usaremos el homomorfismo $\phi_p\colon R[x]\rightarrow (R/(p))[x]$ de reducción módulo $p$ introducido en la demostración del Lema de Gauss. En general, $$\operatorname{grado}(\phi_p(f))\leq \operatorname{grado}(f).$$ La condición sobre $a_n$ equivale a decir que concretamente para el polinomio $f$ del enunciado $$\operatorname{grado}(\phi_p(f))= \operatorname{grado}(f).$$ Reduzcamos al absurdo. Si $f$ fuera reducible se descompondría como producto de dos divisores propios $f=gh$. Como $f$ es primitivo, ni $g$ ni $h$ puede ser constante, es decir $$\operatorname{grado}(g),\operatorname{grado}(h)>0.$$ Al ser $\phi_p$ un homomorfismo, $$\phi_p(f)=\phi_p(g)\phi_p(h).$$ Ninguna de las desigualdades  $$\begin{array}{rcl} \operatorname{grado}(\phi_p(g))&\leq &\operatorname{grado}(g),\cr \operatorname{grado}(\phi_p(h))&\leq &\operatorname{grado}(h), \end{array}$$ puede ser estricta ya que de ser así $$\operatorname{grado}(\phi_p(f))=\operatorname{grado}(\phi_p(g))+\operatorname{grado}(\phi_p(h))<\operatorname{grado}(g)+\operatorname{grado}(h)=\operatorname{grado}(f),$$ pero $\operatorname{grado}(\phi_p(f))=\operatorname{grado}(f)$. Las dos igualdades de la ecuación anterior son ciertas porque tanto $R$ como $R/(p)$ son dominios, el segundo por ser $p$ primo. Por tanto, $$\operatorname{grado}(\phi_p(g)),\operatorname{grado}(\phi_p(h))>0$$ y tanto $\phi_p(g)$ como $\phi_p(h)$ serían divisores propios de $\phi_p(f)$, que no sería irreducible.
 \End{proof}


\Begin{theorem}\textrm{\normalfont (Criterio de Eisenstein)}\label{eisenstein} 
Si $f=a\_nx^n+\cdots+a\_1x+a\_0\in R[x]$ es un polinomio primitivo de grado $n>0$ y $p\in R$ es un primo tal que: 

* $p$ no divide $a\_n$,

* $p$ divide a $a\_{n-1},\dots,a\_0$,

* $p^2$ no divide a $a_0$,

entonces $f$ es irreducible en $R[x]$. 
 \End{theorem}


\Begin{proof} 
Esta demostración transcurre de manera exactamente igual que la anterior hasta la última frase, que no es válida en este caso. A partir de ahí continuamos del siguiente modo. Si $b_0, c_0\in R$ son los términos independientes de $g$ y $h$ entonces $a_0=b_0c_0$. Como $p|a_0$ y $p$ es primo, $p|b_0$ o $p|c_0$, pero no puede dividir a ambos a la vez ya que $p^2$ no divide a $a_0$. Esto prueba que bien $\phi_p(g)$ o bien $\phi_p(h)$ tiene término independiente no nulo. Por las condiciones del enunciado, $\phi_p(f)=\bar a_nx^n$ con $\bar a_n\neq 0$. Al ser $\phi_p(f)=\phi_p(g)\phi_p(h)$ un monomio y $R/(p)$ es un dominio, también $\phi_p(g)$ y $\phi_p(h)$ han de ser monomios. Como uno de ellos tiene término independiente no nulo, entonces ha de tener grado $0$, lo que contradice el cálculo al que se llega en la última ecuación de la demostración anterior.   
 \End{proof}



## Enteros de Gauss

Vamos a estudiar los primos y las factorizaciones en el anillo $\mathbb Z[i]$, que es un DFU y un DIP por ser un DE. En nuestros argumentos haremos uso de la conjugación compleja, del módulo y de su cuadrado. Recordemos que el cero es el único elemento de módulo cero y las unidades $\\{\pm1,\pm i\\}$ son los elementos de módulo $1$.

\Begin{proposition} 
Si $\pi\in\mathbb Z[i]$ es primo entonces su conjugado $\bar\pi$ también.
 \End{proposition}


\Begin{proof} 
Como la conjugación preserva productos, si $\bar\pi|ab$ entonces $\pi|\bar a\bar b$ luego $\pi|\bar a$ o $\pi|\bar b$, es decir $\bar\pi|a$ o $\bar\pi|b$.
 \End{proof}


Necesitaremos la siguiente observación sobre enteros primos.

\Begin{lemma} 
Todo entero primo $p\in\mathbb Z$ satisface una y solo una de las siguientes ecuaciones:

* $p\equiv 1$ mod $4$.

* $p\equiv 3$ mod $4$.

* $p=\pm2$.

 \End{lemma}


\Begin{proof} 
Si $p\equiv 0$ mod $4$ entonces $p$ sería un múltiplo de $4$, con lo cual no sería primo. Si $p\equiv 2$ mod $4$ entonces $p=2+4n=2(1+2n)$ para cierto $n\in\mathbb Z$, que solo es primo si $1+2n$ es invertible en $\mathbb Z$, es decir si y solo si $p=\pm2$.
 \End{proof}

Los primos 5, 13, 17, 29, 37, 41, 53, 61... son 1 mod 4, y 3, 7, 11, 19, 23, 31, 43, 47... son 3 mod 4.

\Begin{exercise} 
Demuestra que hay una cantidad infinita de primos que satisfacen tanto la primera como la segunda ecuación.
 \End{exercise}


\Begin{proposition} 
Si $\pi\in\mathbb Z[i]$ es tal que $|\pi|^2=p\in\mathbb Z$ es un entero primo entonces $\pi$ es primo en los enteros de Gauss y además bien $p=2$ o bien $p\equiv 1$ mod $4$.
 \End{proposition}


\Begin{proof} 
Supongamos que $\pi$ se descompone como $\pi=z_1z_2$ en $\mathbb Z[i]$. Entonces tenemos la ecuación $|z_1|^2|z_2|^2=|\pi|^2=p$ de números enteros. Como $p$ es primo en los enteros, necesariamente $|z_i|^2=1$ para algún $i\in\\{1,2\\}$, es decir, algún $z_i$ tendría que ser una unidad. Esto prueba que el entero de Gauss $\pi$ es irreducible, luego primo.

Veamos la ecuación en congruencias. Si $\pi=a+ib$ entonces $p=|\pi|^2=a^2+b^2$. En $\mathbb Z/4$ los únicos elementos que son cuadrados de otros son $0,1\in\mathbb Z$, por tanto $p=a^2+b^2$ puede ser $0$, $1$ o $2$ módulo $4$. La primera posibilidad queda descartada por el lema anterior y la tercera solo se da cuando $p=2$.
 \End{proof}


De este modo vemos que $1+i$, $2+i$, $3+2i$, $4+i$, $5+2i$, $6+i$, $5+4i$, $7+2i$, $6+5i$... son primos en los enteros de Gauss, así como sus conjugados y asociados. En particular $5=(2+i)(2-i)$ es una factorización como producto de primos en $\mathbb Z[i]$.


\Begin{proposition} 
Si $p\in\mathbb Z$ es un entero primo tal que $p\equiv 3$ mod $4$ entonces $p$ también es primo en los enteros de Gauss.
 \End{proposition}


\Begin{proof} 
Supongamos por reducción al absurdo que $p$ se descompone como producto de divisores propios $p=z_1z_2$, entonces tenemos la ecuación $p^2=|z_1|^2|z_2|^2$ en los enteros. Como ningún $z_i$ es una unidad, necesariamente $|z_1|^2=|z_2|^2=p$. Como $p\equiv 3$ mod $4$, esto es imposible por la proposición anterior.
 \End{proof}



\Begin{proposition} 
Salvo asociados, $1+i\in\mathbb Z[i]$ es el único primo cuyo módulo al cuadrado es $2$.
 \End{proposition}


\Begin{proof} 
Si $\pi=a+ib$ y $2=|\pi|^2=a^2+b^2$ es fácil observar que $a^2=b^2=1$, es decir $a=\pm1=b$. Esto nos da
$$\begin{array}{rcl}
1+i,&&\cr
1-i&=&(-i)(1+i),\cr
-1+i&=&i(1+i),\cr
-1-i&=&(-1)(1+i).
\end{array}$$
   \End{proof}

\Begin{remark} 
La factorización del $2$ como producto de primos en $\mathbb Z[i]$ es $2=(1+i)(1-i)$. Los dos primos que aparecen en esta factorización son asociados.
 \End{remark}

Veamos que para el resto de enteros primos $p\equiv 1$ mod $4$ también hay primos en los enteros de Gauss que lo tienen como móldulo al cuadrado y que son de hecho los factores primos de $p$ en $\mathbb Z[i]$. Para ello necesitamos resultados técnicos sobre enteros primos.

\Begin{lemma} 
Todo entero primo $p\in\mathbb Z$ no negativo satisface la ecuación $(p-1)!\equiv -1$ mod $p$.
 \End{lemma}


\Begin{proof} 
El resultado es obvio para $p=2$. Supongamos que $p>2$. 
Observemos la definición del factorial $$(p-1)!=1\underbrace{2\cdots (p-2)}(p-1).$$ Como $p$ es primo, $\mathbb Z/(p)$ es un cuerpo y todo elemento no nulo es una unidad. Ningún factor de la definición de $(p-1)!$ es divisible por $p$, porque es menor. Por tanto todos son unidades módulo $p$. En $\mathbb Z/(p)$ las únicas unidades que son inversas de sí mismas son $\pm 1$ ya que estas son las únicas raíces del polinomio $x^2-1=(x-1)(x+1)$. El primer factor de $(p-1)!$ es $1$ y el último es $p-1\equiv -1$ mod $p$, por tanto, todos los factores de en medio tienen una inversa diferente, que es otro elemento del mismo producto. Dicho de otro modo, el producto de los $p-3$ factores centrales se puede dividir en $(p-3)/2$ pares de elementos mutuamente inversos módulo $p$, con lo que este producto es congruente con $1$ módulo $p$, así que $(p-1)!\equiv 1(p-1)\equiv -1$ mod $p$.
 \End{proof}


\Begin{lemma} 
Si $p\in\mathbb Z$ es un  entero primo tal que $p\equiv 1$ mod $4$ entonces $p|(m^2+1)$ para cierto $m\in\mathbb Z$.
 \End{lemma}


\Begin{proof} 
Podemos suponer sin pérdida de genralidad que $p\geq 0$. Por el lema anterior, basta ver que $(p-1)!$ es un cuadrado módulo $p$. Como $p=4n+1$ entonces $$\begin{array}{rcl}(p-1)!&=&1\cdot 2\cdots (4n-1)\cdot (4n)\cr &=& \underbrace{1\cdot 2\cdots (2n-1)\cdot (2n)}\cdot \underbrace{(2n+1)\cdot (2n+2)\cdots (4n-1)\cdot (4n)}.\end{array}$$ Para todo $1\leq i\leq 2n$, en $\mathbb Z/(p)$ el $i$-ésimo factor de la primera mitad es el opuesto por el signo del $i$-ésimo factor de la segunda mitad empezando por el final ya que ambos suman $4n+1=p\equiv 0$ mod $p$. Por tanto, módulo $p$, $$\begin{array}{rcl}(p-1)!&\equiv& \underbrace{1\cdot 2\cdots (2n-1)\cdot (2n)}\cdot \underbrace{(-2n)\cdot (-2n-1)\cdots (-2)\cdot (-1)}\cr&\equiv&(-1)^{2n}\cdot 1^2\cdot 2^2\cdots (2n-1)^2 (2n)^2\cr &=&m^2\end{array}$$
para $m=(2n)!$. 
 \End{proof}


\Begin{remark} 
En la demostración hemos visto que si $p=4n+1\geq 0$ podemos tomar $m=(2n)!$, pero en general se pueden usar números más pequeños, concretamente siempre hay un $0{<}m{<}p$ adecuado ya que simplemente se trata de resolver la ecuación $x^2+1\equiv 0$ mod $p$. Este $m$ es el resto de dividir $(2n)!$ por $p$. Por ejemplo, para $p=13=4\cdot 3+1$, $(2\cdot 3)!=720$ pero podemos tomar $m=5$.
 \End{remark}


\Begin{proposition} 
Si $p\in\mathbb Z$ es un entero primo tal que $p\equiv 1$ mod $4$ entonces $p$ no es primo en los enteros de Gauss.
 \End{proposition}


\Begin{proof} 
Sabemos que $p|(m^2+1)$ para cierto $m\in\mathbb Z$, es decir $p|(m+i)(m-i)$ pero $p$ no divide a $m\pm i$ ya que no divide a su parte imaginaria. Por tanto $p$ no es primo en $\mathbb Z[i]$.
 \End{proof}



\Begin{theorem} 
Si $p\in\mathbb Z$ es un entero primo tal que $p\equiv 1$ mod $4$ entonces, salvo asociados, hay exactamente dos primos en los enteros de Gauss cuyo módulo al cuadrado es $p$. Además estos dos primos son conjugados $\pi,\bar\pi\in\mathbb Z[i]$.
 \End{theorem}


\Begin{proof} 
Como $p$ no es primo en $\mathbb Z[i]$ podemos descomponerlo como producto de dos divisores propios $p=z_1z_2$. Tenemos la ecuación $p^2=|z_1|^2|z_2|^2$ en los enteros. Como ningún $z_i$ es una unidad, necesariamente $|z_1|^2=|z_2|^2=p$. Según hemos visto antes estos $z_i$ son primos en $\mathbb Z[i]$. Es más $z_1\bar z_1=|z_1|^2=p=z_1z_2$, por tanto $z_2=\bar z_1$.

Llamemos $\pi=z_1=a+ib$. Veamos que $\pi$ y $\bar\pi$ no son asociados. Los asociados de $\pi$ son
$$\begin{array}{rcl}
a+ib,&&\cr
(-1)(a+ib)&=&-a-ib,\cr
i(a+ib)&=&-b+ia,\cr
(-i)(a+ib)&=&b-ia.
\end{array}$$
Veamos que ninguno de estos enteros de Gauss puede ser $\bar\pi=a-ib$. Si fuera el primero tendríamos que $b=0$, pero entonces $p=|\pi|^2=a^2$, lo cual es una contradicción. Si fuera el segundo tendríamos que $a=0$ y llegaríamos a la contradicción $p=|\pi|^2=b^2$. Si fuera el tercero tendríamos que $a=-b$, con lo que $\pi=a(1-i)$, que solo es primo si $a$ es una unidad, pero en este caso $p=|\pi|^2=2\not\equiv 1$ mod $4$. Análogamiente si fuera el último tendríamos que $a=b$ y $\pi=a(1+i)$, incurriendo en la misma contradicción que en el caso anterior.

Finalmente, comprobemos no puede haber más que estos primos de Gauss y sus asociados con módulo al cuadrado $p$. En efecto, si $\pi'\in\mathbb Z[i]$ satisficiera $p=|\pi'|^2=\pi'\bar\pi'$ entonces como $\pi'|p=\pi\bar\pi$ tendríamos que bien $\pi'|\pi$ o bien $\pi'|\bar\pi$, es decir, como estos tres elementos son primos, $\pi'$ es asociado a $\pi$ o a $\bar\pi$.
   \End{proof}


\Begin{remark} 
 En las condiciones del enunciado anterior, la factorización de $p$ en $\mathbb Z[i]$ es $p=\pi\bar\pi$. Para $p=5$ los dos primos de Gauss son $\pi=2+i$ y $\bar\pi=2-i$. Los asociados de $\pi$ son $2+i$, $-2-i$, $-1+2i$ y $1-2i$. Los asociados de $\bar\pi$ son los conjugados de los anteriores, $2-i$, $-2+i$, $-1-2i$ y $1+2i$.
 \End{remark}





\Begin{example}\textrm{\normalfont (Factores de $p\equiv 1$ mod $4$)}\label{exm:prime1mod4} 
Dado un entero primo $p\in\mathbb Z$ tal que $p\equiv 1$ mod $4$, podemos hallar su factorización como producto de primos $p=\pi\bar\pi$ en $\mathbb Z[i]$ del siguiente modo. Primero encontramos un $m\in\mathbb Z$ tal que $p|(m^2+1)$. Hemos visto en una demostración anterior que $p$ no divide a $m\pm i$, pero $\pi|p$ y $p|(m^2+1)=(m+i)(m-i)$, por tanto el primo de Gauss $\pi$ divide a $m+i$ o a su conjugado, y análogamente $\bar\pi$. Deducimos que $\pi$ y $\bar \pi$ son $\operatorname{mcd}(p,m+i)$ y $\operatorname{mcd}(p,m-i)$.

Por ejemplo, para $p=13$ hemos visto que podemos tomar $m=5$. Calculamos $\operatorname{mcd}(13, 5+i)$, mediante el algoritmo de Euclides. Como el módulo de $13$ es mayor que el de $5+i$, comenzamos realizando la división euclídea del primero por el segundo, $$13=(5+i)\cdot 3+(-2-3i).$$ Ahora dividimos $5+i$ por el resto de la anterior división, $$(5+i)=(-2-3i)(-1+i)+0.$$
El resto de esta división es $0$. El divisor común máximo es el último resto no nulo, $$\pi=-2-3i.$$
 \End{example}


Hasta el momento hemos conseguido factorizar los primos enteros en $\mathbb{Z}[i]$ y por tanto calcular aquellos primos de Gauss que son factores de un primo entero. Veamos que estos son todos los primos de Gauss posibles y que por tanto hemos dado ya una descripción completa de todos los primos en $\mathbb Z[i]$.

\Begin{proposition} 
Todo primo en $\mathbb Z[i]$ divide a un primo en $\mathbb Z$.
 \End{proposition}


\Begin{proof} 
Sea $\pi\in\mathbb Z[i]$ un primo. Factorizamos $|\pi|^2\in\mathbb Z$ como producto de primos enteros $|\pi|^2=p_1\cdots p_n$. Como $|\pi|^2=\pi\bar\pi$ entonces $\pi|p_1\cdots p_n$ así que $\pi|p_i$ para cierto $1\leq i\leq n$.
 \End{proof}

\Begin{remark} 
Recapitulando, los primos de Gauss son los siguientes, salvo asociados:

* $1+i$.

* Los primos enteros $p\in \mathbb{Z}$, $p > 0$, tales que $p\equiv 3$ mod $4$.

* Para cada primo entero $p\in\mathbb{Z}$, $p > 0$, tal que $p\equiv 1$ mod $4$, dos primos de Gauss conjugados $\pi$ y $\bar{\pi}$ tales que $p=\pi\bar{\pi}$, cuyo cálculo se ha explicado en un [ejemplo anterior](#exm:prime1mod4).

Hay una cantidad infinita de primos de Gauss tanto del segundo tipo como del tercer tipo. 
En $\mathbb{Z}[i]$, los asociados de un elemento se obtienen multiplicándolo por las unidades $\\{\pm1,\pm i\\}$.
 \End{remark}

\Begin{example}\textrm{\normalfont (Factorizar un entero en $\mathbb Z[i]$)}\label{exm:integer} 
Para factorizar $n\in\mathbb{Z}$, $n\neq 0,\pm1$, como producto de primos en $\mathbb{Z}[i]$, primero lo factorizamos como producto de primos en $\mathbb{Z}$, $n=p_1\cdots p_r$, y luego factorizamos cada $p_i\in\mathbb{Z}$ como producto de primos en $\mathbb{Z}[i]$. Recuerda que si $p_i\equiv 3$ mod $4$ entonces ya es primo de Gauss, la factorización del $2$  como producto de primos de Gauss es $2=(1+i)(1-i)$, y el caso $p_i\equiv 1$ mod $4$ se ha tratado [más arriba.](#exm:prime1mod4) Por ejemplo, 
$$
\begin{array}{rcl}
n&=&1350\cr
&=&2\cdot 3^3\cdot 5^2\cr
&=&(1+i)\cdot(1-i)\cdot 3^3\cdot(2+i)^2\cdot(2-i)^2.
\end{array}
$$
 \End{example}

\Begin{definition} 
Diremos que un entero de Gauss $z=a+ib$ no tiene *parte entera* si $a\neq 0\neq b$ y $\operatorname{mcd}(a,b)=1$. 
 \End{definition}

\Begin{remark} 
Un entero de Gauss no tiene parte entera si y solo no es divisible por ningún entero distinto de $\pm1$.
 \End{remark}

\Begin{lemma} 
Sea $z$ un entero de Gauss sin parte entera y $\pi$ un primo de Gauss tal que $|\pi|^2=p$ es un entero primo $p\equiv 1$ mod $4$. Si $\pi|z$ entonces $\bar{\pi}\nmid z$.
 \End{lemma}

\Begin{proof} 
Por reducción al absurdo, si también $\bar{\pi}\mid p$ entonces $\operatorname{mcm}(\pi,\bar{\pi})|z$. Como $\pi$ y $\bar{\pi}$ son primos no asociados, $\operatorname{mcm}(\pi,\bar{\pi})=\pi\bar{\pi}=p$, por tanto $p|z$ y $z$ tendría parte entera.
 \End{proof}

\Begin{example}\textrm{\normalfont (Factorización de enteros de Gauss sin parte entera)}\label{exm:nointeger} 
Sea $z\in\mathbb{Z}[i]$ sin parte entera. Supongamos que $z=\pi_1\cdots\pi_r$ es su factorización como producto de primos de Gauss. Como $z$ no tiene parte entera, ningún $\pi_i$ es un primo entero $p\equiv 3$ mod $4$, así que $|\pi_i|^2=2$, y en dicho caso $\pi_i$ es asociado de $1+i$, o bien $|\pi_i|^2=p$ es un primo entero $p\equiv 1$ mod $4$. Es más, en este último caso ni $\bar{\pi}_i$ ni ninguno de sus asociados puede aparecer en la factorización.

Por tanto, para factorizar $z$ en $\mathbb{Z}[i]$ podemos proceder del siguiente modo. Primero, factorizamos $|z|^2$ como producto de potencias de primos enteros positivos, 
$$|z|^2 = p_1^{n_1}\cdots p_s^{n_s}.$$
Entonces 
$$z=u\pi_1^{n_1}\cdots \pi_s^{n_s}$$
donde:

* Si $p_i=2$ entonces $\pi_i=1+i$.

* Si $p_i\equiv 1$ mod $4$, entonces $\pi_i|p$. Para calcularlo, factorizamos $p_i$ como producto de primos de Gauss, $p_i=\pi\bar{\pi}$, según el [ejemplo anterior](#exm:prime1mod4) y dividimos $\frac{z}{\pi}$ en $\mathbb{C}$. Si $\frac{z}{\pi}$ resulta ser un entero de Gauss entonces $\pi_i=\pi$, y si no $\pi_i=\bar{\pi}$.

* $u$ es una unidad, $u\in\\{\pm1,\pm i\\}$, que se determina a posteriori.

Veámoslo en el caso particular $z=201-43i$. En este caso
$$|z|^2=201^2+43^2=42250=2\cdot 5^3 \cdot 13^2.$$
Las factorizaciones de $5$ y de $13$ en $\mathbb{Z}[i]$ son $3=(2+i)(2-i)$ y $13=(3+2i)(3-2i)$, por tanto
$$z=u(1+i)(2\pm i)^3(3\pm 2i)^2.$$
Para determinar qué factor del $5$ aparece realmente, dividimos $z$ por uno de ellos en $\mathbb{C}$, por ejemplo
$$
\begin{array}{rcl}
\frac{z}{2+i}&=&\frac{(201-43i)(2-i)}{(2+i)(2-i)}\cr
&=&\frac{359}{5}-\frac{287}{5}i.
\end{array}
$$
Como no es un entero de Gauss, $2+i\nmid z$, así que $2-i\mid z$, luego
$$z=u(1+i)(2-i)^3(3\pm 2i)^2.$$
Ahora, para hallar qué factor del $13$ aparece realmente, dividimos $z$ por uno de ellos en $\mathbb{C}$,
$$
\begin{array}{rcl}
\frac{z}{3-2i}&=&\frac{(201-43i)(3+2i)}{(3-2i)(3+2i)}\cr
&=&23+21i.
\end{array}
$$
Este sí es un entero de Gauss, por tanto $3-2i\mid z$ y
$$z=u(1+i)(2-i)^3(3- 2i)^2.$$
Para hallar la unidad, calculamos el producto de la derecha
$$
(1+i)(2-i)^3(3- 2i)^2=-43-201i,
$$
así que $u=i$,
$$z=i(1+i)(2+i)^3(3\pm 2i)^2.$$
La unidad $i$ se puede incorporar a cualquier factor primo, por ejemplo al primero, $i(1+i)=-1+i$, y en conclusión
$$z=(-1+i)(2+i)^3(3\pm 2i)^2$$
es una factorización de $z$ como producto de primos de Gauss.
 \End{example}

\Begin{example}\textrm{\normalfont (Factorización en $\mathbb Z[i]$)} 
En general, todo entero de Gauss $z=a+ib\in\mathbb{Z}[i]$ se puede descomponer como $z=n\cdot z'$, con $n=\operatorname{mcd}(a,b)$ y $z'\in\mathbb{Z}[i]$ sin parte entera. La factorización de $z$ como producto de primos de Gauss se obtiene multiplicando las correspondientes factorizaciones de $n$ y $z'$, que se realizan según indicamos [aquí](#exm:integer) y [aquí](#exm:nointeger).

Por ejemplo, $z=15+45i=15(1+3i)$. Por un lado $n=15=3\cdot 5=3\cdot(2+i)\cdot (2-i)$. Por otro lado $z'=1+3i$, $|z'|^2=1^2+3^2=10=2\cdot 5$. Por tanto 
$$z'=u(1+i)(2\pm i).$$
Para saber qué factor de $5=(2+i)\cdot (2-i)$ divide a $z'$ realizamos la siguiente operación en $\mathbb{C}$,
$$
\begin{array}{rcl}
\frac{1+3i}{2+i}&=&\frac{(1+3i)(2-i)}{(2+i)(2-i)}\cr
&=&1+i.
\end{array}
$$
Por tanto
$$z'=u(1+i)(2+ i).$$
De hecho, el cálculo anterior nos demuestra que la unidad es $u=1$, así que
$$z'=(1+i)(2+ i),$$
luego
$$
\begin{array}{rcl}
z&=&n\cdot z'\cr
&=&3\cdot(2+i)\cdot (2-i)\cdot(1+i)\cdot (2+ i)\cr
&=&3\cdot(2+i)^2\cdot (2-i)\cdot(1+i).
\end{array}
$$
 \End{example}


El siguiente gráfico nos muestra la distribución de los primos cercanos al origen en los enteros de Gauss. 

![Primos de Gauss](../../images/gaussian_primes.png)

Puedes también usar la siguiente aplicación interactiva para explorar la distribución de los primos de Gauss en cuadrados de diferente tamaño centrados en el origen. Los lados del cuadrado tienen tamaño $2n$. Los puntos rojos son los primos de Gauss de módulo al cuadrado 2. En azul están los que son enteros. El resto, en verde.

<div class="sage">
  <script type="text/x-sage">
@interact
def _(n=slider(3,100, step_size=1, default = 5, label="n=")):
    lattice1 = []
    lattice2 = [[1,1], [1,-1], [-1,1], [-1,-1]]
    lattice3 = []
    for x in [-n .. n]:
        for y in [-n .. n]:
            if is_prime(x^2+y^2) and (x^2+y^2).mod(4) == 1:
                lattice1 = lattice1 + [[x,y]]
    for z in list(primes(3,n+1)):
        lattice3 = lattice3 + [[z,0], [-z,0]]
    lattice1_plot = point(lattice1, rgbcolor='green', size=400/n)
    lattice2_plot = point(lattice2, rgbcolor='red', size=800/n)
    lattice3_plot = point(lattice3, rgbcolor='blue', size=800/n)
    return show(lattice1_plot+lattice2_plot+lattice3_plot, aspect_ratio=1)
  </script>
</div>



## Ecuaciones diofánticas

A modo de ejemplo, vamos a estudiar aquí un par de ecuaciones diofánticas cuyas soluciones pasan por el estudio de los enteros de Gauss realizado anteriormente.

Al comienzo del tema de anillos nos habíamos planteado como motivación el solucionar la ecuación diofántica $$x^2+y^2=5.$$ Ahora reemplazaremos el término independiente con un entero positivo $>1$ cualquiera.

\Begin{theorem} 
Dado $n\geq 2$, la ecuación diofántica $$x^2+y^2=n$$ tiene solución si y solo si cualquier primo $p\equiv 3$ mod $4$ tiene exponente par en la factorización de  $n$. Además, en dicho caso el número de soluciones es finito.
 \End{theorem}


\Begin{proof} 
La ecuación planteada equivale a encontrar los enteros de Gauss $x+iy$ tales que $|x+iy|^2=n$. Si $x+iy=\pi_1\cdots\pi_n$ es una factorización en $\mathbb Z[i]$ entonces $|x+iy|^2=|\pi_1|^2\cdots|\pi_n|^2$. Sabemos además, por la clasificación de los primos de Gauss, que $|\pi_i|^2$ puede ser $2$, un entero primo $p\equiv 1$ mod $4$ o $p^2$ donde $p\equiv 3$ mod $4$. Esto demuestra la necesidad de la condición del enunciado. También la suficiencia porque, si se cumple, basta tomar $x+iy$ como el producto de:

* Un factor $1+i$ por cada $2$ que aparezca en la factorización de $n$.

* Si $p\equiv 1$ mod $4$, un factor $\pi$ con $|\pi|^2=p$ por cada factor $p$ de $n$.

* Si $p\equiv 3$ mod $4$, un factor $p$ por *cada dos* factores $p$ de $n$.

El conjunto de todas las soluciones se obtiene permitiendo reemplazar los $\pi$ del segundo apartado por sus conjugados y tomando los asociados de todas las soluciones particulares así obtenidas. En particular hay un número finito de soluciones.
 \End{proof}


\Begin{example}\textrm{\normalfont ($x^2+y^2=1170$)} 
En este caso concreto $1170=2\cdot 3^2\cdot 5\cdot 13$. El único primo que vale $3$ módulo $4$ y que aparece en esta factorización es el propio $3$, con exponente par, por lo que la ecuación tiene solución. Una solución se corresponde con el entero de Gauss $x+iy$ obtenido al multiplicar los siguientes factores:

* $1+i$ por aparecer un $2$.

* $2+i$ por haber un $5$ y $2+3i$ por haber un $13$.

* $3$ por el $3^2$ que aparece.

Es decir,
$$(1+i)(2+i)(2+3i)3=-21+27i.$$
Otras soluciones concretas se obtienen permitiendo reemplazar los factores del segundo apartado por sus conjugados,
$$\begin{array}{rcl}
(1+i)(2-i)(2+3i)3&=&9+33i,\cr
(1+i)(2+i)(2-3i)3&=&33+9i,\cr
(1+i)(2-i)(2-3i)3&=&27-21i.
\end{array}$$
El conjunto de todas las soluciones $x+iy$ son las cuatro anteriores y sus asociados, 16 en total:
$$
\begin{array}{rrrr}
-21+27i,&9+33i,&33+9i,&27-21i,\cr
-27-21i,&-33+9i,&-9+33i,&21+27i,\cr
21-27i,&-9-33i,&-33-9i,&-27+21i,\cr
27+21i,&33-9i,&9-33i,&-21-27i.
\end{array}
$$

 \End{example}


La otra ecuación diofántica que vamos a considerar en este epígrafe es la **ecuación de Pitágoras** $$x^2+y^2=z^2.$$
Sus soluciones positivas $x,y,z>0$ se denominan **ternas pitagóricas** y parametrizan los triángulos rectángulos con lados de medida entera.

![Teorema de Pitágoras](../../images/pythagorean.png)

Los papeles de $x$ e $y$ en la ecuación de Pitágoras son intercambiables, por lo que $(x,y,z)$ es una solución si y solo si lo es
$$(y,x,z).$$
Los signos de las soluciones son irrelevantes, es decir si $(x,y,z)$ es una solución entonces también lo son $$(\pm x,\pm y,\pm z).$$
Las soluciones triviales son las de la forma $(x,0,\pm x)$ o $(0,y,\pm y)$. Por tanto basta estudiar las ternas pitagóricas.

No hay ternas pitagóricas con $x$ e $y$ impares porque en ese caso $x\equiv\pm 1$ e $y\equiv \pm1$ mod $4$, así que $z^2=x^2+y^2\equiv 1+1=2$ mod $4$. Esto es imposible porque los únicos cuadrados en $\mathbb Z/(4)$ son $0$ y $1$.

Si $(x,y,z)$ es una terna pitagórica y $d=\operatorname{mcd}(x,y)$ entonces $d^2|x^2$ y $d^2|y^2$ por lo que $d^2|z^2$. Por tanto $d|z$ y $$\left(\frac{x}{d},\frac{y}{d},\frac{z}{d}\right)$$ es otra terna pitagórica con $\operatorname{mcd}(\frac{x}{d},\frac{y}{d})=1$. En definitiva, podemos centrarnos en buscar las ternas pitagóricas $(x,y,z)$ tales $\operatorname{mcd}(x,y)=1$. Estas se denominan **ternas pitagóricas primitivas**. Las que no son primitivas se obtienen a partir de las primitivas multiplicando por enteros positivos. En una terna pitagórica primitiva $x$ e $y$ no pueden ser ambos pares. A la luz del párrafo anterior, $x$ ha de ser par e $y$ impar, o viceversa, es decir, $$x\not\equiv y \mod 2.$$
Podemos pues suponer que $x$ es impar e $y$ es par, el resto de ternas pitagóricas primitivas se obtendrán intercambiando la $x$ y la $y$.

La conexión de la ecuación de Pitágoras con los enteros de Gauss proviene de que esta ecuación equivale a
$$(x+iy)(x-iy)=z^2.$$

\Begin{lemma} 
Dados $x,y\in\mathbb Z$ no nulos, tenemos que $x\equiv y$ mod $2$ $\Leftrightarrow$ $(1+i)|(x+iy)$.
 \End{lemma}


\Begin{proof} 
$\Rightarrow$ Si $x\equiv y$ mod $2$ entonces $x$ e $y$ son ambos pares o ambos impares. Si son ambos pares entonces $2|(x+iy)$ y ya sabemos que $(1+i)|2$ con lo que $(1+i)|(x+iy)$. Si son ambos impares entonces $y\pm x$ es par y tenemos la siguiente ecuación en $\mathbb Z[i]$, $$x+iy=(1+i)\left(\frac{y+x}{2}+i\frac{y-x}{2}\right).$$

$\Leftarrow$ Si $(1+i)|(x+iy)$ entonces  $$x+iy=(1+i)(x'+iy')=(x'-y')+(x'+y')i$$ y por tanto $$x=x'-y'\equiv x'+y'=y \mod 2.$$   
 \End{proof}


En el siguiente lema caracterizamos en términos de los enteros de Gauss la condición sobre $x$ e $y$ que caracteriza las ternas pitagóricas que son primitivas.

\Begin{lemma}\label{lem:mcdconj} 
Dados $x,y\in\mathbb Z$ no nulos, tenemos que $\operatorname{mcd}(x,y)=1$ y $x\not\equiv y$ mod $2$ $\Leftrightarrow$ $\operatorname{mcd}(x+iy,x-iy)=1$.
 \End{lemma}


\Begin{proof} 
$\Rightarrow$ Por reducción al absurdo. Si $\pi\in\mathbb Z[i]$ es un primo de Gauss tal que $\pi|(x+iy)$ y $\pi|(x-iy)$ entonces $$\begin{array}{rcl}\pi\;|\;[(x+iy)+(x-iy)]&=&2x,\cr \pi\;|\;[(x+iy)-(x-iy)]&=&2yi.\end{array}$$ 
El primo $\pi$ no puede dividir simultáneamente a $x$ y a $y$ ya que $\operatorname{mcd}(x,y)=1$, y el divisor común máximo de dos enteros es el mismo calculado en $\mathbb{Z}$ o en $\mathbb{Z}[i]$. De aquí deducimos que $\pi|2$, es decir $\pi=1+i$ (o un asociado). Por tanto $(1+i)|(x+iy)$, así que por el lema anterior $x\equiv y$ mod $2$, lo cual es una contradicción.

$\Leftarrow$ Cualquier divisor común de $x$ e $y$ divide tanto a $x+iy$ como a $x-iy$, por tanto $\operatorname{mcd}(x,y)=1$. Además $x\not\equiv y$ mod $2$ ya que en caso contrario, por el lema anterior, $(1+i)|(x+iy)$ y por tanto $(1-i)|(x-iy)$. Como $1+i$ y $1-i$ son asociados, ambos dividirían tanto a $x+iy$ como a $x-iy$, que no podrían ser coprimos.
   \End{proof}


\Begin{lemma}\label{lem:DFU} 
En un DFU $R$, las soluciones no nulas de la ecuación $xy=z^2$ tales $\operatorname{mcd}(x,y)=1$ son, salvo asociados, todas de la forma $x=a^2$, $y=b^2$ y $z=ab$ con $a,b\in R$, $\operatorname{mcd}(a,b)=1$.
 \End{lemma}


\Begin{proof} 
Si $z$ fuera una unidad, entonces también lo tendrían que ser $z^2$, $x$ e $y$, por tanto, salvo asociados, $x=y=z=1=1^2$. Supongamos ahora que $z$ no es una unidad. Sea $z=p_1\cdots p_n$ una factorización como producto de primos. Como $xy=z^2=p_1^2\cdots p_n^2$, por la unicidad de las factorizaciones en $R$ los factores primos de $z^2$ se han de repartir entre $x$ e $y$, salvo asociados. Además, como $\operatorname{mcd}(x,y)=1$, los dos factores de cada $p_i^2$ tienen que quedar del mismo lado, por lo que tanto $x$ como $y$ son cuadrados, $x=a^2$ e $y=b^2$, y $z=ab$, de nuevo salvo asociados. Además $\operatorname{mcd}(a,b)=1$ porque $1=\operatorname{mcd}(x,y)=\operatorname{mcd}(a,b)^2$.
 \End{proof}



\Begin{theorem} 
Las ternas pitagóricas primitivas con segunda coordenada par son las de la forma $(a^2-b^2, 2ab, a^2+b^2)$ con $a,b\in\mathbb Z$, $a>b>0$, $\operatorname{mcd}(a,b)=1$, $a\not\equiv b$ mod $2$.
 \End{theorem}


\Begin{proof} 
La ecuación de Pitágoras, vista en $\mathbb Z[i]$, es $$(x+iy)(x-iy)=z^2.$$ 
Según hemos visto [mas arriba](#lem:mcdconj), la condición de que una terna pitagórica sea primitiva equivale a $\operatorname{mcd}(x+iy,x-iy)=1$. Por el [lema anterior](#lem:DFU), tanto $x+iy$ como $x-iy$ son cuadrados, o asociados de cuadrados, necesariamente conjugados. Es decir, $x+iy=u(a+ib)^2$ para cierto $u=1,-1,i,-i$. Esto da lugar a las siguientes posibilidades:
$$
(x,y)=\left\\{\begin{array}{l}
(a^2-b^2,2ab),\cr
(b^2-a^2,-2ab),\cr
(-2ab,a^2-b^2),\cr
(2ab,b^2-a^2).
\end{array}\right.
$$
Las dos últimas no dan lugar al tipo de terna pitagórica primitiva que estamos considerando, pues $x$ sería par. La primera sí, siempre que $a>b>0$, pues $x,y>0$. También si $ a < b < 0$, pero por este camino llegaríamos a las mismas ternas. La segunda posibilidad también da lugar a las mismas ternas que la primera. Así que podemos suponer que $x+iy=(a+ib)^2$ con $a>b>0$ y por tanto $x-iy=(a-ib)^2$.

De nuevo por el [lema anterior](#lem:DFU), $$z=u(a+ib)(a-ib)=u(a^2+b^2)$$ para cierta unidad $u\in\\{\pm1,\pm i\\}$. Como la ecuación $(x+iy)(x-iy)=z^2$ ha de satisfacerse, la unidad ha de ser tal que $u^2=1$, con lo que $u=\pm 1$. El caso $u=-1$ lo excluimos ya que entonces $z=-(a^2+b^2)<0$, por tanto $z=a^2+b^2$. Además, una vez más por el [lema anterior](#lem:DFU), $\operatorname{mcd}(a+ib,a-ib)=1$, es decir $\operatorname{mcd}(a,b)=1$ y $a\not\equiv b$ mod $2$, usando el [lema de más arriba](#lem:mcdconj). Esto reduce todas las posibilidades a las que aparecen en el enunciado del teorema. Veamos que todas ellas son en efecto ternas pitagóricas primitivas. 

Claramente, las ternas del enunciado resuelven la ecuación de Pitágoras, es decir,
$$(a^2-b^2)^2+(2ab)^2=(a^2+b^2)^2.$$
Las tres coordenadas son positivas, pues $a>b>0$. La segunda coordenada es claramente par. Solo queda comprobar que las dos primeras son coprimas. Para ello, demostraremos que la primera no es divisible por $2$ ni por ningún factor primo de $a$ o de $b$. Como $n\equiv n^2$ mod $2$ para todo $n\in\mathbb{Z}$, $a^2-b^2\equiv a-b\not\equiv 0$ mod $2$, pues $a\not\equiv b$ mod $2$, así que $a^2-b^2$ es impar. Sea $p\in\mathbb{Z}$ un primo. Si $p\mid a$ entonces $p\mid a^2$. Si fuera cierto que $p\mid (a^2-b^2)$ entonces tendriamos que $p\mid b^2$ y por tanto $p\mid b$. Esto contradeciría que $\operatorname{mcd}(a,b)=1$, luego en realidad  $p\nmid (a^2-b^2)$. Análogamente se prueba que si $p\mid b$ entonces $p\nmid (a^2-b^2)$. Esto concluye la demostración.
 \End{proof}


El siguiente gráfico muestra los pares $(x,y)$ que forman parte de una terna pitagórica cualquiera con $x,y\leq 4500$.

![Ternas pitagóricas](../../images/Pythagorean_triple_scatterplot.png)

La siguiente aplicación muestra los pares $(x,y)$ que forman parte de una terna pitagórica primitiva con $x$ impar y $x,y\leq n$, donde $n$ puede ser cualquier múltiplo de $10$ comprendido entre $10$ y $3000$.

<div class="sage">
  <script type="text/x-sage">
@interact
def _(n=slider(10,3000, step_size=10, default = 100, label="n=")):
    octant = [[a,b] for a in [1..floor(n/2)] for b in [1..(a-1)]]
    parameters = []
    for x in octant:
        if gcd(x[0],x[1]) == 1 and x[0].mod(2) != x[1].mod(2):
            parameters.append(x)
    big_list = [[y[0]^2-y[1]^2,2*y[0]*y[1]] for y in parameters]
    small_list = []
    for z in big_list:
        if z[0] <= n and z[1] <= n and z[0] > 0:
            small_list.append(z)
    return show(point(small_list, rgbcolor='green', size=min(max(30,2*3000/n),100), aspect_ratio=1))
  </script>
</div>

