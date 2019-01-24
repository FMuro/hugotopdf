+++
title = "Módulos"
weight = 20
+++

¿Cómo es el álgebra lineal que resulta al reemplazar el papel de los cuerpos por anillos más generales? El objeto de estudio de esta álgebra lineal generalizada son los módulos. Un módulo $M$ es a un anillo $R$ lo que un espacio vectorial es a un cuerpo. Es decir, el módulo $M$ está dotado de las siguientes operaciones:

* Suma.

* Resta.

* Producto por escalares de $R$. 

Estas operaciones deben satisfacer las propiedades habituales. Además el módulo ha de contener el siguiente elemento:

* Cero $0$.

Tanto este $0\in M$ como el $1\in R$ han de satisfacer las propiedades habituales con respecto a la suma y la multiplicación.

Los módulos sobre el anillo $\mathbb Z$ son simplemente los grupos abelianos. Los espacios vectoriales sobre un cuerpo cualquiera están clasificados por su dimensión. Es decir, dos espacios vectoriales son isomorfos si y solo si tienen la misma dimensión. En este tema estudiaremos fundamentalmente la clasificación de los módulos finitamente generados sobre un dominio de ideales principales. En particular la clasificación de los grupos abelianos finitamente generados. Aplicaremos estos resultados a la resolución de sistemas de ecuaciones lineales diofánticas y al estudio de un tema de álgebra lineal clásica: los endomorfismos de espacios vectoriales de dimensión finita.

## Definición

\Begin{definition} 

Dado un anillo $R$, un **$R$-módulo** es un conjunto $M$ equipado con dos aplicaciones, llamadas *suma* y *producto por escalares*,
$$
\begin{array}{ccc}
M\times M\rightarrow M, &\qquad& R\times M\rightarrow M,\cr
(a,b)\mapsto a+b;&&(r,a) \mapsto ra;
\end{array}
$$
que satisfacen las siguientes propiedades, donde $a,b,c\in M$ y $r,s\in R$:

* Asociativa: $$a+(b+c)=(a+b)+c,\qquad r(sa)=(rs)a.$$

* Conmutativa: $$a+b=b+a.$$

* Distributiva:
$$r(a+b)=ra+rb,\qquad (r+s)a=ra+sa.$$

* Existencia de *elemento neutro* $0\in M$ para la suma y comportamiento del $1\in R$ como elemento neutro para el producto por escalares:
$$0+a=a,\qquad 1a=a.$$

* Existencia de un *elemento opuesto* para la suma $-a\in M$ para todo $a\in M$ de modo que $$a+(-a)=0.$$

 \End{definition}


\Begin{remark} 
 Cuando quede claro por el contexto o no sea relevante especificarlo, omitiremos $R$ de la notación. La suma en un módulo lo dota de estructura de grupo abeliano. Recordemos que el elemento neutro de un grupo es único, no puede haber dos distintos que satisfagan la misma propiedad. Los opuestos para la suma también. Restar es sumar el elemento opuesto $a-b=a+(-b)$. Además $0a=0=r0$ y $r(-a)=-ra=(-r)a$. Si $R=k$ es un cuerpo la noción de $R$-módulo coincide con la de $k$-espacio vectorial.
 \End{remark}



\Begin{example}\textrm{\normalfont (El módulo trivial)} 

El conjunto unitario $\\{0\\}$, dotado de las únicas operaciones suma y producto por escalares posibles, es un módulo sobre cualquier anillo $R$. 

 \End{example}


\Begin{example}\textrm{\normalfont ($R^n$)} 
 Sus elementos son vectores conlumna con entradas en $R$, aunque a veces, cuando convenga, se denotarán por filas. La suma se define coordenada a coordenada, y el producto por escalares se define multiplicando el escalar por todas las coordenadas: $$\left(\begin{array}{c}a_1\cr\vdots\cr a_n\end{array}\right)+\left(\begin{array}{c}b_1\cr\vdots\cr b_n\end{array}\right)=\left(\begin{array}{c}a_1+b_1\cr\vdots\cr a_n+b_n\end{array}\right),\qquad r\left(\begin{array}{c}a_1\cr\vdots\cr a_n\end{array}\right)=\left(\begin{array}{c}ra_1\cr\vdots\cr ra_n\end{array}\right).$$ Para $n=1$ observamos que el propio $R$ puede considerarse como un $R$-módulo. Para $n=0$ obtenemos el módulo trivial.
 \End{example}


\Begin{example}\textrm{\normalfont (Producto de módulos)} 
Dados dos $R$-módulos $M$ y $N$, su **producto** cartesiano $M\times N$ posee una estructura de $R$-módulo con las siguientes operaciones: $$\begin{array}{rcl}(a\_1,b\_1)+(a\_2,b\_2)&=&(a\_1+a\_2,b\_1+b\_2),\cr r(a,b)&=&(ra,rb).\end{array}$$ ¿Cuál es el elemento neutro para la suma? ¿Cuáles son los opuestos?
 \End{example}


\Begin{proposition} 
 Todo grupo abeliano $A$ posee una única estructura de $\mathbb Z$-módulo. 
 \End{proposition}


\Begin{proof} 

Dado $a\in A$, si $n>0$ en $\mathbb Z$, estaríamos forzados a definir:
$$\begin{array}{rcl}
n a&=&(1+\stackrel{n}{\cdots}+1)a\cr&=&1a+\stackrel{n}{\cdots}+1a\cr&=&a+\stackrel{n}{\cdots}+a,\cr
(-n)a&=&-na,\cr
0a&=&0.
\end{array}$$
Es fácil comprobar que estas fórmulas definen una estructra de $\mathbb Z$-módulo en $A$, necesariamente única.  
 \End{proof}



\Begin{definition} 
Un subconjunto $N\subset M$ de un $R$-módulo $M$ es un **submódulo** si:

* $0\in N$.

* $a+b\in N$ para todo $a,b\in N$.

* $-a\in N$ para todo $a\in N$.

* $ra\in N$ para todo $r\in R$ y $a\in N$.

 \End{definition}



\Begin{remark} 
Un submódulo $N\subset M$ es un módulo por derecho propio con la suma y el producto por escalares heredados de $M$. El módulo trivial $\\{0\\}$ es un submódulo de cualquier otro. Los submódulos de $R$ coinciden con los ideales del anillo. 
 \End{remark}



## Homomorfismos

Los homomorfismos de módulos son aplicaciones que preservan la estructura, es decir, la suma y el producto por escalares.

\Begin{definition} 
Dados dos $R$-módulos $M$ y $N$, un **homomorfismo** $f\colon M\rightarrow N$ es una aplicación tal que, para todo $r\in R$ y $a,b\in M$, $$\begin{array}{rcl} f(a+b)&=&f(a)+f(b),\cr f(ra)&=&rf(a).\end{array}$$ Un **isomorfismo** es un homomorfismo biyectivo. Un **automorfismo** es un isomorfismo de un $R$-módulo en sí mismo.
 \End{definition}


\Begin{remark} 
Los homomorfismos satisfacen $f(-a)=-f(a)$ y $f(0)=0$. La identidad $\operatorname{id}_M\colon M\rightarrow M$ es un isomorfismo. Comprueba que si $$M\stackrel{f}\longrightarrow N\stackrel{g}\longrightarrow P$$ son homomorfismos entonces la composición $g\circ f\colon M\rightarrow P$ también. Lo mismo es cierto para isomorfismos. Es más, demuestra que si $f\colon M\rightarrow N$ es un isomorfismo entonces su aplicación inversa $f^{-1}\colon N\rightarrow M$ también. El símbolo $\cong$ se usará para denotar la relación de ser isomorfos $M\cong N$. Prueba que esta relación es de equivalencia. 
 \End{remark}



\Begin{example}\textrm{\normalfont (La inclusión)} 
Si $M$ es un módulo y $P\subset M$ es un submódulo, la **inclusión** $i\colon P\hookrightarrow M$, $i(a)=a$, es un homomorfismo. ¿Qué diferencia a la inclusión de la identidad?
 \End{example}


\Begin{example}\textrm{\normalfont (Objeto cero)} 
Todo módulo $M$ admite homomorfismos únicos desde $\\{0\\}\rightarrow M$ y hasta $M\rightarrow \\{0\\}$ el módulo trivial. 
 \End{example}


\Begin{example}\textrm{\normalfont (Homomorfismo trivial)} 
Dados dos $R$-módulos cualesquiera $M$ y $N$, la aplicación $M\rightarrow N$ definida como $x\mapsto 0$ para todo $x\in M$ es un homomorfismo, el **homomorfismo trivial**. ¿Puede ser un isomorfismo? 
 \End{example}


\Begin{example}\textrm{\normalfont (Producto por escalares)} 
Dado un $R$-módulo $M$ y $r\in R$, la aplicación $M\stackrel{r\cdot}\rightarrow M$ definida como $x\mapsto r\cdot x$ es un homomorfismo. ¿Puede ser un isomorfismo?
 \End{example}


\Begin{example}\textrm{\normalfont (Inclusiones y proyecciones de un producto)} 
Dados dos $R$-módulos $M$ y $N$, definimos dos homomorfismos de **inclusión** $$i\_1\colon M\longrightarrow M\times N,\qquad i\_2\colon N\longrightarrow M\times N,$$ mediante las fórmulas $$i\_1(a)=(a,0),\qquad i\_2(b)=(0,b),$$ y otros dos de **proyección** $$p\_1\colon M\times N\longrightarrow M,\qquad p\_2\colon M\times N\longrightarrow N,$$ como $$p\_1(a,b)=a,\qquad p\_2(a,b)=b.$$ Comprueba que $p\_1\circ i\_1=\operatorname{id}\_M$ y $p\_2\circ i\_2=\operatorname{id}\_N$. ¿Son estos homomorfismos isomorfismos? 
 \End{example}


\Begin{example}\textrm{\normalfont (Conmutatividad del producto)} 
El producto de $R$-módulos es conmutativo salvo isomorfismo. Dados dos $R$-módulos $M$ y $N$ tenemos un isomorfismo $$\begin{array}{rcl}M\times N&\stackrel{\cong}\longrightarrow&N\times M,\cr (a,b)&\mapsto&(b,a).\end{array}$$ ¿Cuál es su inverso? 
 \End{example}


\Begin{example}\textrm{\normalfont (Matrices)} 
Toda matriz $B$ de tamaño $m\times n$ con entradas en $R$ da lugar a un homomorfismo definido por la multiplicación de matrices: $$\begin{array}{rcl} R^n&\stackrel{B\cdot}\longrightarrow&R^m,\cr \left(\begin{smallmatrix}a_1\cr\vdots\cr a_n\end{smallmatrix}\right)&\mapsto& B\left(\begin{smallmatrix}a_1\cr\vdots\cr a_n\end{smallmatrix}\right). \end{array}$$ La composición de este tipo de homomorfismos es el producto de matrices. En particular $B$ define un isomorfismo si y solo si es una matriz invertible. Cualquier homomorfismo $f\colon R^n\rightarrow R^m$ es de este tipo. En efecto, si para cada $1\leq i\leq n$ consideramos el elemento $$e\_i=\left(\begin{smallmatrix}0\cr\vdots\cr1\cr\vdots\cr0\end{smallmatrix}\right)\in R^n$$ cuya única coordenada no trivial es la $i$-ésima, que vale $1$, puedes comprobar la matriz que define $f\colon R^n\rightarrow R^m$ es aquella cuyas columnas son los $f(e\_i)$, $$\left(f(e\_1)\mid\cdots\mid f(e\_n)\right).$$
 \End{example}


\Begin{exercise} 
 Demuestra que si $M\cong M'$ y $N\cong N'$ entonces $M\times N\cong M'\times N'$.
 \End{exercise}



\Begin{proposition} 
Si $M$ es un $R$-módulo y $S=\\{a\_1,\dots,a\_n\\}\subset M$ un subconjunto cualquiera, existe un único homomorfismo $\phi=\phi_{S}\colon R^n\rightarrow M$ tal quie $\phi(e_i)=a_i$.
 \End{proposition}

\Begin{proof} 
Todo $x=(x\_1,\dots,x\_n)\in R^n$ se puede escribir como $x=\sum\_{i=1}^nx\_ie\_i$. Por tanto, si existiera $\phi$ tendría que cumplir que 
$$
\begin{array}{rcl}
\phi(x)&=&\phi(\sum\_{i=1}^nx\_ie\_i)\cr
&=&\sum\_{i=1}^nx\_i\phi(e\_i)\cr
&=&\sum\_{i=1}^nx\_ia\_i.
\end{array}
$$
Esto demostraría la unicidad, caso de que existiera. Es más, es fácil comprobar que la fórmula $\phi(x)=\sum_{i=1}^nx_ia_i$ define un homomorfismo, luego existe.
 \End{proof}

\Begin{proposition} 
Dado un homomorfismo $f\colon M\rightarrow N$, su **imagen** $\operatorname{im} f\subset N$ es un submódulo. 
 \End{proposition}


\Begin{proof} 

* $0=f(0)\in \operatorname{im} f$.

* $f(a)+f(b)=f(a+b)\in \operatorname{im} f$ para $a,b\in M$.

* $-f(a)=f(-a)\in \operatorname{im} f$ para todo $a\in M$.

* $rf(a)=f(ra)\in \operatorname{im} f$ para todo $r\in R$ y $a\in M$.
 
 \End{proof}

La siguiente proposición posee un análogo para anillos que [ya ha sido demostrado](/estalg/rings/definitions/#factorimage).

\Begin{proposition}\label{factorimagemodules} 
Dado un homomorfismo $f\colon M\rightarrow N$ y un submódulo $U\subset N$, si $\operatorname{im} f\subset U$ entonces $f$ factoriza de manera única a través de la inclusión, es decir, existe un único homomorfismo $g\colon M\rightarrow U$ tal que $f=i\circ g$, $$f\colon M\stackrel{g}\rightarrow U\stackrel{i}\hookrightarrow N.$$ 
 \End{proposition}


\Begin{proof} 
Si $f=i\circ g$ entonces tendríamos $$f(a)=(i\circ g)(a)=i(g(a))=g(a).$$ La unicidad de $g$ sería consecuencia de esta fórmula ya que fuerza su definición. Definimos pues la aplicación $g\colon M\rightarrow U$ como $g(a)=f(a)$. Tiene sentido porque $\operatorname{im}f\subset U$. La aplicación $g$ es un homomorfismo pues está definida por la misma fórmula que el homomorfismo $f$.  
 \End{proof}

\Begin{remark} 
 En la proposición anterior podemos siempre tomar $U=\operatorname{im} f$. 
 \End{remark}


\Begin{proposition} 
El **núcleo** de un homomorfismo $f\colon M\rightarrow N$, $$\ker f=\\{a\in M\mid f(a)=0\\},$$ es un submódulo $\ker f\subset M$.
 \End{proposition}


\Begin{proof} 

* $0\in\ker f$ pues $f(0)=0$.

* Si $a,b\in\ker f$ entonces $a+b\in \ker f$ puesto que $f(a+b)=f(a)+f(b)=0+0=0$.

* Si $a\in\ker f$ entonces $-a\in \ker f$ puesto que $f(-a)=-f(a)=0$.

* Si $a\in\ker f$ y $r\in R$ entonces $ra\in \ker f$ pues $f(ra)=rf(a)=r0=0$.
 
 \End{proof}


\Begin{remark} 
 Como ocurre con los grupos y con los anillos, un homomorfismo de módulos $f\colon M\rightarrow N$ es inyectivo si y solo si $\ker f=\\{0\\}$. De otro modo, la inyectividad de $f$ equivale a que si $a\in M$ es tal que $f(a)=0$ entonces $a=0$.
 \End{remark}


## Módulos libres

\Begin{definition} 
Sea $M$ un $R$-módulo y $S=\\{a\_1,\dots,a\_n\\}\subset M$ un subconjunto. Decimos que $S$ **genera** $M$ si todo elemento de $x\in M$ es **combinación lineal** de $S$, es decir, de la forma $$x=r\_1a\_1+\cdots+r\_na\_n$$ para ciertos $r\_1,\dots,r\_n\in R$. Decimos que $S$ es **linealmente independiente** si la única combinación lineal de $S$ que da como resultado $0$ es aquella que tiene todos los cieficientes nulos, es decir si $r\_1,\dots,r\_n\in R$ son tales que $$r\_1a\_1+\cdots+r\_na\_n=0$$ entonces $r\_1=\cdots=r\_n=0$. Decimos además que $S$ es una **base** de $M$ si lo genera y es linealmente independiente. Un $R$-módulo es **finitamente generado** si posee un subconjunto finito que genera, y es **libre** si posee una base.
 \End{definition}



\Begin{remark} 
Si $R=k$ es un cuerpo todo $R$-módulo es libre puesto que todo $k$-espacio vectorial posee una base. Los $k$-espacios vectoriales finitamente generados se denominan también de dimensión finita. Es posible considerar bases de módulos no finitamente generados, pero aquí no lo haremos.
 \End{remark}


\Begin{example}\textrm{\normalfont ($R^n$ es libre)} 
 El sub conjunto $\\{e\_1,\dots,e\_n\\}\subset R^n$ es una base denominada **canónica**.
 \End{example}

Podemos definir un submódulo con un conjunto prefijado de generadores al igual que lo hicimos con los [ideales](/estalg/rings/definitions/#generators).

\Begin{definition} 
El **submódulo generado por** un conjunto finto de elementos $a_1,\dots,a_n\in M$ está formado por todas las combinaciones lineales de los generadores con coeficientes en el anillo:  $$(a_1,\dots,a_n)=\\{r_1a_1+\dots+r_na_n\;|\; r_1,\dots,r_n\in R\\}\subset M.$$ Un **módulo cíclico** es uno que está generado por un único elemento $(a)=\\{ra\,|\, r\in R\\}$ y que por tanto está formado por sus múltiplos. 
 \End{definition}


\Begin{exercise} 
Comprueba que $(a_1,\dots,a_n)\subset M$ es en efecto un submódulo. Observa que $a_1,\dots,a_n\in (a_1,\dots, a_n)$. Es más, demuestra que si $N\subset M$ es un submódulo y $a_1,\dots,a_n\in N$ entonces $(a_1,\dots,a_n)\subset N$. Intenta dar una definición razonable de ideal generado por un conjunto infinito de elementos que satisfaga las propiedades análogas al caso finito. 
 \End{exercise}


\Begin{remark} 
En términos del homomorfismo $$\phi\_S\colon R^n\longrightarrow M$$ definido antes, podemos afirmar lo siguiente sobre el conjunto $S=\\{a\_1,\dots,a\_n\\}\subset M$: 

* $S$ genera si y solo si $\phi\_S$ es sobreyectivo. 

En particular, $(a\_1,\dots,a\_n)=\operatorname{im} \phi\_S$.

* $S$ es linealmente independiente si y solo si $\phi\_S$ es inyectivo. 

* $S$ es una base si y solo si $\phi\_S$ es un isomorfismo. 

En particular, si $S$ es una base de $M$ entonces para todo $x\in M$ existe un único $(r\_1,\dots,r\_n)\in R^n$ tal que $$x=\phi\_S(r\_1,\dots,r\_n)=r\_1a\_1+\cdots+r\_na\_n.$$ 
Decimos entonces que $(r\_1,\dots,r\_n)$ son las **coordenadas** de $x$ respecto de $S$. Es más, la aplicación que envía cada elemento a sus coordenadas respecto de $S$ es $$\phi\_S^{-1}\colon M\longrightarrow R^n,$$ que es un isomorfismo, por tanto la asignación de coordenadas respecto de una base preserva sumas y productos por escalares. 
 \End{remark}



\Begin{remark} 
 Sea $f\colon M\rightarrow N$ es un homomorfismo de $R$-módulos y $S=\\{a\_1,\dots,a\_n\\}\subset M$. Los siguientes enunciados son consecuencia de las observaciones anteriores: 

* Si $S\subset M$ genera y $f$ es sobreyectivo $\Rightarrow$ $f(S)\subset N$ genera.

* Si $S\subset M$ es linealmente independiente y $f$ es inyectivo $\Rightarrow$ $f(S)\subset N$ es linealmente independiente.

* Si $S\subset M$ es una base y $f$ es biyectivo $\Rightarrow$ $f(S)\subset N$ es una base.

* Si $S\subset M$ genera entonces $f(S)\subset\operatorname{im}f$ genera.

Concluimos que un $R$-módulo es libre si y solo si es isomorfo a algún $R^n$.
 \End{remark}


Seguidamente definimos la noción de determinante para matrices sobre un anillo igual que se hacía para los cuerpos.

\Begin{definition} 
El **determinante** $|A|$ de una matriz cuadrada $A=(a\_{ij})$ de tamaño $n\times n$ con entradas en un anillo conmutativo $R$ se define como $$|A|=\sum\_{\sigma\in S\_n}\operatorname{signo}(\sigma)a\_{1\sigma(1)}\cdots a\_{n\sigma(n)}.$$ Aquí $S_n$ denota el grupo de permutaciones de $n$ elementos.
 \End{definition}


\Begin{remark} 
Los determinantes de matrices con entradas en un anillo conmutativo satisfacen las siguientes propiedades habituales. Puedes comprobarlas como ejercicio.

* El determinante de la matriz identidad es $|I|=1$. 

* Si $A$ tiene una fila de ceros entonces $|A|=0$. 

* Una matriz $A$ y su traspuesta $A^t$ tienen el mismo determinante, $|A|=|A^t|$. 

* El determinante preserva productos, $|AB|=|A||B|$. 

* Las fórmulas del desarrollo de un determinante por los adjuntos de una fila o columna también son válidas en este contexto. 

* Si $A$ es una matriz cuadrada invertible entonces $|A|\in R^{\times}$ es una unidad y $|A^{-1}|=|A|^{-1}$.

* Recíprocamente, si $A$ es cuadrada y $|A|\in R^{\times}$ es una unidad entonces $A$ es invertible. Su inversa es la matriz traspuesta de la adjunta de $A$ dividida por $|A|$. 

Las matrices invertibles son necesariamente cuadradas si $R$ no es el anillo trivial. Esto se comprueba por reducción al absurdo. En efecto, sean $A$ y $B$ matrices tales que $AB=I$ y $BA=I$. Como las matrices identidad $I$ son cuadradas, si $A$ tiene tamaño $m\times n$ entonces el tamaño de $B$ tiene que ser $n\times m$. Podemos suponer sin pérdida de generalidad que $m>n$. Completamos la columnas de $A$ y las filas de $B$ con ceros hasta formar matrices cuadradas y observamos que $$\left(\begin{array}{c|c}A&0\end{array}\right)\left(\begin{array}{c}B\cr \hline 0\end{array}\right)=AB+0=AB=I,$$ pero esto es imposible porque los determinantes de las matrices de la izquierda son $0$, pues contienen alguna fila o columna de ceros, pero el determinante de $I$ es $1$.
 \End{remark}




\Begin{proposition} 
Todas las bases de un mismo $R$-módulo libre $M$ tiene el mismo número de elementos. 
 \End{proposition}


\Begin{proof} 
 Si $S$ y $S'$ son bases con $n$ y $m$ elementos, respectivamente, cada una de ellas define un isomorfismo $\phi\_S\colon R^n\rightarrow M$, $\phi\_{S'}\colon R^m\rightarrow M$. Componiendo el primero con el inverso del segundo obtenemos un isomorfismo $\phi\_{S'}^{-1}\circ\phi\_S\colon R^n\rightarrow R^m$. Este isomorfismo tiene que estar definido por una matriz $A$ de tamaño $m\times n$ invertible. Como las matrices invertibles son cuadradas deducimos que $m=n$.
 \End{proof}



\Begin{definition} 
El **rango** de un $R$-módulo libre $M$ es el número de elementos de una base. 
 \End{definition}


Cuando $R=k$ es un cuerpo, el rango de un $k$-espacio vectorial se denomina dimensión.


\Begin{remark} 
 Si $S=\\{a\_1,\dots,a\_n\\}$ y $S'=\\{a\_1',\dots,a\_n'\\}$ son bases de un mismo $R$-módulo libre de rango $n$, el isomorfismo $\phi\_{S'}^{-1}\circ\phi\_S\colon R^n\rightarrow R^n$ considerado en la demostración anterior está definido por una matriz $B=(b_{ij})$ invertible $n\times n$ sobre $R$, que es la única que satisface las siguientes ecuaciones para todo $1\leq i\leq n$, $$a\_i=b\_{1i}a\_1'+\cdots+b\_{ni}a\_n'.$$ Es decir, las columnas de $B$ son las coordenadas de los elementos de $S$ respecto de la base $S'$. Si $x\in M$ tiene coordenadas $(r\_1,\dots, r\_n)$ respecto de $S$ y $(r\_1',\dots, r\_n')$ respecto de $S'$ entonces se satisface que $$B\left(\begin{smallmatrix}r\_1\cr\vdots\cr r\_n\end{smallmatrix}\right)=\left(\begin{smallmatrix}r\_1'\cr\vdots\cr r\_n'\end{smallmatrix}\right).$$ Por eso $B$ se denomina **matriz de cambio de base** de $S$ a $S'$. 
 \End{remark}



\Begin{example}\textrm{\normalfont (No todos los módulos son libres)} 
 El $\mathbb Z$-módulo $\mathbb Z/(2)$ está generado por el conjunto $S=\\{\bar 1\\}$ pero $S$ no es linealmente independiente porque $2\cdot\bar 1=\bar 2=\bar 0$ y $0\neq 2\in\mathbb Z$. De hecho el $\mathbb Z$-módulo $\mathbb Z/(2)$ no puede tener ninguna base ya que los subconjuntos de $\mathbb Z/(2)$ son $\varnothing$, $\\{\bar 0\\}$, $\\{\bar 1\\}$ y $\\{\bar 0,\bar 1\\}$, los dos primeros no generan y los dos últimos no son linealmente independientes. Este argumento, por elemental, es algo complejo. Es más sencillo observar que los $\mathbb Z$-módulos libres poseen un único elemento, $\mathbb Z^0=\\{0\\}$, o infinitos, $\mathbb Z^n$ con $n>0$, por tanto $\mathbb Z/2$, que tiene dos elementos, no puede ser libre.
 \End{example}


## Torsión

En este apartado $R$ denotará siempre un dominio.

\Begin{definition} 
Dado un $R$-módulo $M$, decimos que $a\in M$ es un elemento de **torsion** si existe algún $r\in R$ no nulo, $r\neq 0$, tal que $ra=0$. 
 \End{definition}


\Begin{remark} 
El $0\in M$ es siempre un elemento de torsión ya que $1\neq 0$ y $1\cdot 0 = 0$. Dado un entero no nulo $0\neq n\in\mathbb Z$, todo elemento $\bar a$ del $\mathbb Z$-módulo $\mathbb Z/(n)$ es de torsión puesto que $n\bar a=\overline{na}=\bar 0$. Más generalmente, si $I\subset R$ es un ideal no nulo entonces todo elemento de $R/I$ es de torsión, pues existe $0\neq a\in I$ y dado $\bar r\in R/I$, $a\bar r=\overline{ar}=0$. Como $R$ no tiene divisores de cero, $T( {R} )=\\{0\\}$, y más generalmente $T(R^n)=\\{0\\}$, $n\geq 0$.
 \End{remark}


Veamos una condición suficiente, aunque no necesaria, para que un módulo no sea libre.

\Begin{proposition} 
Si $M$ es un $R$-módulo que tiene elementos no triviales de torsión entonces $M$ no es libre. 
 \End{proposition}


\Begin{proof} 
 Supongamos por reducción al absurdo que $\\{a\_1,\dots,a\_n\\}\subset M$ fuera una base. Tomamos un elemento no trivial de torsión $0\neq x\in M$ y lo escribimos como $$x=r\_1a\_1+\cdots+r\_na\_n$$ con $r\_1,\dots,r\_n\in R$. Ha de haber algún $r_i\neq 0$ para cierto $1\leq i\leq n$ ya que $x\neq 0$. Como $x\in M$ es de torsión existe $0\neq s\in R$ tal que $$0=sx=sr\_1a\_1+\cdots+sr\_na\_n.$$ Uno de los coeficientes de esta combinación lineal es $sr\_i\neq 0$ que es no nulo porque $R$ es un dominio. Esto contradice la independencia lineal.
 \End{proof}


\Begin{remark} 
 El $\mathbb Z$-módulo $\mathbb Q$ no tiene torsión, pero se puede comprobar que no es libre, es decir, no posee niguna base, ni finita ni infinita. 
 \End{remark}


Los elementos de torsión forman un submódulo.
\Begin{proposition} 
 Si $M$ es un $R$-módulo, el subconjunto $T(M)\subset M$ formado por los elementos de torsión es un submódulo.
 \End{proposition}


\Begin{proof} 
  
Dados $a,b\in T(M)$ existen $s,t\in R$ no nulos, $s\neq 0\neq t$, tales que $sa=0=tb$. 

* $0\in T(M)$ tal como hemos visto antes.

* $a+b\in T(M)$ pues $st\neq 0$ y $st(a+b)=t(sa)+s(tb)=0$.

* $-a\in T(M)$ pues $s(-a)=-sa=0$.

* Dado $r\in R$, $ra\in T(M)$ pues $s(ra)=r(sa)=0$.

 \End{proof}


Los homomorfismos preservan la torsión.

\Begin{proposition}\label{homotorsion} 
 Si $f\colon M\rightarrow N$ es un homomorfismo de $R$-módulos entonces $f(T(M))\subset T(N)$. Si $f$ es un isomorfismo entonces $f(T(M))= T(N)$. 
 \End{proposition}


\Begin{proof} 
Dado $a\in T(M)$ existe $0\neq r\in R$ tal que $ra=0$ luego $rf(a)=f(ra)=f(0)=0$ y por tanto $f(a)$ es de torsión. Esto prueba la inclusión. Si $f$ además es un isomorfismo entonces podemos aplicarle la parte ya probada a $f^{-1}\colon N\rightarrow M$, con lo que tenemos $f^{-1}(T(N))\subset T(M)$, lo cual equivale a la otra inclusión $T(N)\subset f(T(M))$.
 \End{proof}


\Begin{corollary}\label{torsionquotient} 
Si dos módulos son isomorfos $M\cong N$ entonces sus submódulos de torsión también $T(M)\cong T(N)$, y los correspondientes cocientes $M/T(M)\cong N/T(N)$.
 \End{corollary}


La torsión preserva productos.

\Begin{proposition}\label{torsionproduct} 
 Dados dos $R$-módulos $M$ y $N$, tenemos que $T(M\times N)=T(M)\times T(N)$ .
 \End{proposition}


\Begin{proof} 
 Veamos primero $\subset$. Si $(a,b)\in T(M\times N)$ existe $0\neq r\in R$ tal que $r(a,b)=(ra,rb)=(0,0)$, es decir $ra=0$ y $rb=0$, por lo que $a\in T(M)$ y $b\in T(N)$, o dicho de otro modo $(a,b)\in T(M)\times T(N)$. 

Veamos ahora $\supset$. Si $(a,b)\in T(M)\times T(N)$, es decir $a\in T(M)$ y $b\in T(N)$, entonces existen $r,s\in R$ no nulos tales que $ra=0$ y $sb=0$, por tanto $rs\neq 0$ y $rs(a,b)=(s(ra),r(sb))=(0,0)$, luego $(a,b)\in T(M\times N)$.
 \End{proof}


  
## Cocientes

\Begin{definition} 
Dado un $R$-módulo $M$ y un submódulo $N\subset M$, el **$R$-módulo cociente** $M/N$ es el cociente de los grupos abelianos subyacentes dotado del producto por escalares $$r(a+N)=(ra)+N.$$
 \End{definition}


\Begin{remark} 
 Recordemos que $M/N=\\{a+N\,|\, a\in M\\}$ de modo que $a+N=b+N$ si y solo si $a-b\in N$. En particular $a+N=0+N$ si y solo si $a\in N$. El elemento $a+N$ del cociente se denomina **clase** de $a$ **módulo** $N$. Cuando el submódulo $N$ se sobreentiende se escribe simplemente $$a+N=\bar a=[a].$$ La suma en el cociente se define como $(a+N)+(b+N)=(a+b)+N$. El cero en el cociente es $0+N$. Comprueba que $M/M$ es el módulo trivial y $M/\\{0\\}\cong M$. Si $R$ es un dominio y $0\neq x\in R$ todo elemento del $R$-módulo cociente $\bar a\in R/(x)$ es de torsión pues $x\bar a=\overline{xa}=0$. 
 \End{remark}


\Begin{theorem} 
El $R$-módulo cociente $M/N$ está bien definido. Su estructura es la única que hace que la **proyección natural** $p\colon M\twoheadrightarrow M/N$, $p(a)=a+N$, sea un homomorfismo. El núcleo de esta proyección es $\ker p=N$. 
 \End{theorem}


\Begin{proof} 
Para ver que la producto por escalares está bien definido hay que comprobar que 
$$
a+N=a'+N\Rightarrow(ra)+N=(ra')+N.
$$ 
Esto equivale a 
$$
a-a'\in N\Rightarrow ra-ra'= r(a-a')\in N.
$$ 
Las propiedades que la suma y el producto por escalares deben satisfacer se cumplen obviamente pues se derivan de las correspondientes propiedades de $M$.

Probemos la unicidad. Si $p\colon M\rightarrow M/N$ es un homomorfismo entonces
$$\begin{array}{rcl}
p(a+b)&=&p(a)+p(b),\cr p(ra)&=&rp(a),
\end{array}$$
lo cual equivale a
$$\begin{array}{rcl}
(a+b)+N&=&(a+N)+(b+N),\cr (ra)+N&=&r(a+N).
\end{array}$$

El núcleo de la proyección natural es $$\ker p =\\{a\in M\;|\; p(a)=0\\},$$ pero $p(a)=a+N$ y $a+N=0+N$ si y solo si $a\in N$, luego $\ker p=N$.  
 \End{proof}

\Begin{example}\textrm{\normalfont ($R[x]/(p(x))$ como $R$-módulo)} 
Sea $R$ un anillo y $p(x)\in R[x]$ un polinomio mónico de grado $n$. El $R[x]$-módulo cociente $R[x]/(p(x))$ es también un $R$-módulo, restringiendo el producto por escalares al subanillo $R\subset R[x]$. Hemos [visto](../rings/definitions/#uniquerep) que todo elemento del cociente está representado por un único polinomio de grado $<n$. Es decir, todo elemento de $R[x]/(p(x))$ se puede escribir como combinación lineal de $S=\\{1,\bar{x},\dots,\bar{x}^{n-1}\\}$ de manera única. Por tanto, $R[x]/(p(x))$ es libre como $R$-módulo y $S$ es una base. Recuerda que, sin embargo, cuando estudiamos la torsión vimos que, si $R$ es un dominio, $R[x]/(p(x))$ no es libre como $R[x]$-módulo.
 \End{example}

La siguiente proposición también tiene un análogo para anillos [ya demostrado](/estalg/rings/definitions/#factorquotient).

\Begin{proposition}\label{factorquotientmodules} 
Dado un submódulo $N\subset M$ y un homomorfismo $f\colon M\rightarrow P$ tal que $N\subset \ker f$, $f$ factoriza de manera única a través de la proyección natural, es decir existe un único homomorfismo $g\colon M/N\rightarrow P$ tal que $f=g\circ p$, $$f\colon M\stackrel{p}\twoheadrightarrow M/N\stackrel{g}\rightarrow P.$$
 \End{proposition}


\Begin{proof} 
Si $f=g\circ p$ entonces tendríamos $$f(a)=(g\circ p)(a)=g(p(a))=g(a+N).$$ Definimos la aplicación $g\colon M/N\rightarrow P$ como $$g(a+N)=f(a).$$ Veamos que en efecto está bien definida. La unicidad se seguirá de la primera fórmula.

Si $a+N=a'+N$ entonces $a-a'\in N\subset\ker f$ luego $$0=f(a-a')=f(a)-f(a').$$ Por tanto $$g(a+N)=f(a)=f(a')=g(a'+N).$$ Claramente $g$ es un homomorfismo pues se definie como el homomorfismo $f$ en los representantes.  
 \End{proof}


\Begin{remark} 
 En la proposición anterior podemos tomar siempre $N=\ker f$. 
 \End{remark}

El siguiente resultado es una versión para módulos del primer teorema de isomoría, [ya visto para anillos](/estalg/rings/definitions/#primer).

\Begin{theorem}\textrm{\normalfont (Primer Teorema de Isomorfía)}\label{isomodules} 
Dado un homomorfismo $f\colon M\rightarrow N$, existe un único homomorfismo $\bar f\colon M/\ker f\rightarrow \operatorname{im}f$ tal que $f$ factoriza como $f=i\circ\bar f\circ p$, es decir, $f$ encaja en el siguente **diagrama conmutativo**, 

![Primer teorema de isomorfía](../images/isomorfiamodulos.png)

Aquí $p$ es la proyección natural e $i$ es la inclusión. Además $\bar f$ es un isomorfismo.
 \End{theorem}

\Begin{proof} 
[Por un lado](#factorimagemodules) podemos factorizar $f\\colon M\\rightarrow N$ de manera única como $f=i\circ g$, $$f\colon M\stackrel{g}\rightarrow \operatorname{im} f\stackrel{i}\hookrightarrow N,$$ donde $g(a)=f(a)$. En particular $$\ker g = \ker f.$$

[Por otro lado](#factorquotientmodules) podemos factorizar $g\colon M\rightarrow \operatorname{im} f$ de manera única como $g=\bar f\circ p$, $$g\colon M\stackrel{p}\twoheadrightarrow N/\ker f\stackrel{\overline{f}}\rightarrow \operatorname{im} f,$$ donde $\bar f(\bar{a})=g(a)=f(a)$. 

Por tanto $f=i\circ g= i\circ(\overline{f}\circ i)$, como queríamos. La unicidad de $\bar f$ se deduce de esta fórmula, ya que fuerza su definición:
$$
\begin{array}{rcl}
f(a)&=&(i\circ\bar f\circ p)(a)\cr
&=&i(\bar{f}(p(a)))\cr
&=&i(\bar{f}(\bar{a}))\cr
\bar{f}(\bar{a}).
\end{array}
$$

Veamos que $\bar f\colon M/\ker f\rightarrow \operatorname{im} f$ es un isomorfismo. Comenzamos probando que es inyectivo. Sea $\bar{a}\in M/\ker f$ tal que $\bar f(\bar{a})=0$. Como $\bar f(\bar{a})=f(a)$, deducimos que $a\in \ker f$, por lo que $\bar{a}=\bar{0}$.

Veamos que $\bar f\colon M/\ker f\rightarrow \operatorname{im} f$ es sobreyectiva. Dado $b\in\operatorname{im} f$ existe $a\in M$ tal que $f(a)=b$. Por tanto $\bar f(\bar{a})=f(a)=b$.  
 \End{proof}

\Begin{example}\textrm{\normalfont (El cociente de un producto por un factor)} 
Recordemos que dados dos $R$-módulos $M$ y $N$ podemos considerar el $R$-módulos producto $M\times N$ y los homomorfismos de inclusión $i\_1\colon M\rightarrow M\times N$, $i\_1(a)=(a,0)$, y proyección $p\_2\colon M\times N\rightarrow N$, $p\_2(a,b)=b$. El primero es inyectivo y el segundo sobreyectivo. Claramente $\operatorname{im}i\_1=M\times\\{0\\}=\ker p\_2$, por tanto el teorema anterior nos proporciona isomorfismos
$$\begin{array}{rclrcl}
\frac{M\times N}{M\times\\{0\\}}&\stackrel{\cong}\longrightarrow&N,&\qquad M&\stackrel{\cong}\longrightarrow&M\times\\{0\\},\cr 
[(a,b)]&\mapsto& b,&a&\mapsto&(a,0).\end{array}$$
Además, el homomorfismo inyectivo $i_1$ induce un isomorfismo $M\cong M\times\\{0\\}$. 
Análogamente podemos obtener isomorfismos
$$\begin{array}{rclrcl}
\frac{M\times N}{\\{0\\}\times N}&\stackrel{\cong}\longrightarrow&M,&\qquad N&\stackrel{\cong}\longrightarrow&\\{0\\}\times N,\cr 
[(a,b)]&\mapsto& a,&b&\mapsto&(0,b).\end{array}$$
 \End{example}

Recordemos que un $R$-módulo es *cíclico* si se puede generar por un solo elemento.


\Begin{proposition} 
Un $R$-módulo $M$ es cíclico $\Leftrightarrow$ $M\cong R/I$ para algún ideal $I\subset R$. 
 \End{proposition}


\Begin{proof} 
$\Leftarrow$ El módulo $R/I$ es cíclico pues $\\{\\bar 1\\}\subset R/I$ genera, así que cualquier módulo isomorfo a $R/I$ será también cíclico. 

$\Rightarrow$ Sea $\\{a\\}\subset M$ un generador. El homomorfismo $\phi\_{\\{a\\}}\colon R\rightarrow M$ que envía $1\mapsto a$ es por tanto sobreyectivo, así que por el primer [teorema](#isomodules) de isomorfía, $R/\ker \phi\_{\\{a\\}}\cong M$, con lo que podemos tomar $I=\ker \phi\_{\\{a\\}}$.   
 \End{proof}


\Begin{proposition} 
Dado un $R$-módulo $M$ y un submódulo $N\subset M$, si $N$ y $M/N$ son finitamente generados entonces $M$ también lo es. 
 \End{proposition}


\Begin{proof} 
Sean $\\{\bar a\_1,\dots,\bar a\_p\\}\subset M/N$ y $\\{b\_1,\dots,b\_q\\}\subset N$ conjuntos de generadores. Veamos que $S=\\{ a\_1,\dots, a\_p,b\_1,\dots,b\_q\\}\subset M$ genera. Dado $x\in M$, consideramos $\bar x\in M/N$ y lo escribimos como combinación lineal de los generadores de $M/N$ con coeficientes en $R$
$$\begin{array}{rcl}\bar x&=&r\_1\bar a\_1+\cdots+r\_p\bar a\_p\cr
&=&\overline{r\_1a\_1+\cdots+r\_pa\_p}.
\end{array}$$
Tenemos entonces que $$x-(r\_1a\_1+\cdots+r\_pa\_p)\in N$$
así que lo podemos escribir como combinación lineal de los geberadores  de $N$ con coeficientes en $R$,
$$x-(r\_1a\_1+\cdots+r\_pa\_p)=s\_1b\_1+\cdots+s\_qb\_q.$$
Despejando vemos que $x$ es combinación lineal de $S$, y por tanto $S$ genera $M$.  
 \End{proof}

\Begin{remark} 
Si $M$ es finitamente generado, $M/N$ también lo es, porque si $\\{a\_1,\dots, a\_n\\}\subset M$ genera entonces $\\{\bar{a}\_1,\dots, \bar{a}\_n\\}$ genera $M/N$. En cambio, en general, $N$ podría no ser finitamente generado.
 \End{remark}


\Begin{corollary} 
Dado un dominio de ideales principales $R$, un $R$-módulo libre finitamente generado $M$ y un submódulo $N\subset M$, el $R$-módulo $N$  es finitamente generado.
 \End{corollary}


\Begin{proof} 
Por inducción en el rango de $M$, que denotamos $n$. Para $n=0$ es obvio ya que en este caso $M=\\{0\\}$ tendría que ser el módulo trivial, que no tiene más submódulos que él mismo. 

Sea ahora $n>0$ y supongamos el resultado cierto para $R$-módulos libres de rango $n-1$. Como $M\cong R^n$, basta probar el resultado para $R^n$. Observamos que $R^n=R^{n-1}\times R$ y consideramos el homomorfismo de proyección sobre la última coordenada $p=p\_2\colon R^n\rightarrow R$, cuyo núcleo es $R^{n-1}\times \\{0\\}\cong R^{n-1}$, que es libre de rango $n-1$. Sea $N\subset R^n$ un submódulo y $p\_{|\_{N}}\colon N\rightarrow R$ la restricción del homomorfismo anterior. Como 
$$\ker p\_{|\_{N}}=N\cap \ker p= N\cap (R^{n-1}\times \\{0\\})\subset R^{n-1}\times \\{0\\},$$ 
deducimos que $\ker p\_{|\_{N}}$ es finitamente generado por hipótesis de inducción. Es más, por el primer [teorema](#isomodules) de isomorfía aplicado a $p\_{|\_{N}}$, 
$$\frac{N}{\ker p\_{|\_{N}}}\cong \operatorname{im} p\_{|\_{N}}.$$
Más aún, $\operatorname{im} p\_{|\_{N}}\subset R$ es un submódulo, por tanto un ideal, y $R$ es un dominio de ideales principales, así que $\operatorname{im} p\_{|\_{N}}$ es finitamente generado (por un solo elemento). Ahora podemos deducir, haciendo uso de la proposición anterior, que $N$ es finitamente generado.
 \End{proof}




## Generadores y relaciones

Supongamos que deseamos construir un $\mathbb Z$-módulo $M$ generado por tres elementos $\\{a\_1,a\_2,a\_3\\}\subset M$ que satisfagan las siguientes ecuaciones (relaciones):
$$\begin{array}{rcrcrcl}
3a\_1&+&2a\_2&+&a\_3&=&0,\cr
8a\_1&+&4a\_2&+&2a\_3&=&0,\cr
7a\_1&+&6a\_2&+&2a\_3&=&0,\cr
9a\_1&+&6a\_2&+&a\_3&=&0.
\end{array}$$
¿Cómo hacerlo? Las relaciones anteriores pueden ser codificadas en una matriz que tiene por columnas a los coeficientes de cada una de las ecuaciones,
$$A=\left(\begin{array}{cccc}
3&8&7&9\cr
2&4&6&6\cr
1&2&2&1
\end{array}\right).$$
Esta matriz define un homomorfismo
$$\mathbb{Z}^4\stackrel{A}\longrightarrow \mathbb{Z}^3$$
Veamos que el cociente $$M=\frac{\mathbb{Z}^3}{\operatorname{im}A}$$
satisface las condiciones deseadas. En efecto, está generado por las clases de los elementos de la base canónica de $\mathbb{Z}^3$,
$$\begin{array}{rcl}
a\_1&=&\bar{e}\_1,\cr
a\_2&=&\bar{e}\_2,\cr
a\_3&=&\bar{e}\_3.
\end{array}$$
Además $\operatorname{im}A$ está generado por las imágenes de los elementos de la base canónica de $\mathbb{Z}^4$,
$$\begin{array}{rcrcrcr}
Ae\_1&=&3e\_1&+&2e\_2&+&e\_3,\cr
Ae\_2&=&8e\_1&+&4e\_2&+&2e\_3,\cr
Ae\_3&=&7e\_1&+&6e\_2&+&2e\_3,\cr
Ae\_4&=&9e\_1&+&6e\_2&+&e\_3,
\end{array}$$
cuyas clases en el cociente se anulan, lo cual equivale a las ecuaciones del principio. Más aún, esta construcción es universal ya que, por la [proposición](#factorquotientmodules) de factorización de homomofismos a través de cocientes, dado un $\mathbb Z$-módulo $N$ y tres elementos $\\{b\_1,b\_2,b\_3\\}\subset N$ que satisfacen las ecuaciones 
$$\begin{array}{rcrcrcl}
3b\_1&+&2b\_2&+&b\_3&=&0,\cr
8b\_1&+&4b\_2&+&2b\_3&=&0,\cr
7b\_1&+&6b\_2&+&2b\_3&=&0,\cr
9b\_1&+&6b\_2&+&b\_3&=&0,
\end{array}$$
existe un único homomorfismo
$$g\colon M\longrightarrow N$$
que satisface 
$$\begin{array}{rcl}
g(a\_1)&=&b\_1,\cr
g(a\_2)&=&b\_2,\cr
g(a\_3)&=&b\_3.
\end{array}$$
Este homomorfismo es la factorización de $\phi\_{\\{b\_1,b\_2,b\_3\\}}\colon\mathbb{Z}^3\rightarrow N$ a través de la proyección natural al cociente $M=\mathbb{Z}^3/\operatorname{im}A$. Tendríamos que comprobar que las hipótesis de la [proposición](#factorquotientmodules) mencionada se cumplen, es decir que $\operatorname{im} A\subset \ker \phi\_{\\{b\_1,b\_2,b\_3\\}}$. Como $\operatorname{im} A$ está generado por $\\{Ae\_1,Ae\_2,Ae\_3,Ae\_4\\}$, basta ver que $Ae\_i\in \ker \phi\_{\\{b\_1,b\_2,b\_3\\}}$ para todo $i$, es decir que $\phi\_{\\{b\_1,b\_2,b\_3\\}}(Ae\_i)=0$, $i=1,2,3,4$. Esto equivale a las cuatro ecuaciones anteriores para los $b_i$.

Esta construcción se puede generalizar de manera obvia del siguiente modo. Dado un anillo cualquiera $R$, queremos construir un $R$-módulo $M$ con *generadores* $\\{a\_1,\dots,a\_m\\}\subset M$ donde se satisfagan las ecuaciones (*relaciones*)
$$r\_{1j}a\_1+\cdots+r\_{mj}a\_m=0,\quad 1\leq j\leq n,$$
donde $r\_{ij}\in R$, $1\leq i\leq m$, $1\leq j\leq n$. Estas relaciones están determinadas por la matriz $A=(r\_{ij})$, que define un homomorfismo
$$R^n\stackrel{A}\longrightarrow R^m.$$
Podemos tomar $$M=\frac{R^m}{\operatorname{im}A}$$
ya que las clases de los elementos de la base canónica de $R^m$ generan $M$,
$$a\_i=\bar{e}\_i,\quad 1\leq i\leq m,$$
y las imágenes de los elementos de la base canónica de $R^n$ generan $\operatorname{im}A$,
$$Ae\_j=r\_{1j}e\_1+\cdots+r\_{mj}e\_m,\quad 1\leq j\leq n.$$
Estas imágenes se anulan en el cociente, lo cual equivale a las ecuaciones (relaciones) del principio. Esta construcción es universal en virtud de la [proposición](#factorquotientmodules) de factorización de homomorfismos a través de cocientes, ya que dado un $R$-módulo $N$ y elementos $\\{b\_1,\dots,b\_m\\}\subset N$ que satisfacen 
$$r\_{1j}b\_1+\cdots+r\_{mj}b\_m=0,\quad 1\leq j\leq n,$$
existe un único homomorfismo
$$g\colon M\longrightarrow N$$
que satisface 
$$g(a\_i)=b\_i,\quad 1\leq i\leq m,$$
que es la factorización de $\phi\_{\\{b\_1,\dots,b\_m\\}}\colon R^m\rightarrow N$ a través de la proyección natural al cociente $M=R^m/\operatorname{im}A$. Las hipótesis de la [proposición](#factorquotientmodules) mencionada se cumplen porque $\operatorname{im}A\subset \ker \phi\_{\\{b\_1,\dots,b\_m\\}}$ ya que $\operatorname{im}A$ está generado por los $Ae_i$ y $\phi\_{\\{b\_1,\dots,b\_m\\}}(Ae_i)=0$ debido a que los $b_i$ satisfacen las mismas ecuaciones (relaciones) que los $a_i$.

\Begin{definition} 
Una **presentación** de un $R$-módulo $M$ consiste en dos homomorfismos $$R^n\stackrel{A}\longrightarrow R^m\stackrel{f}\twoheadrightarrow M$$ tales que $f$ es sobreyectivo e $\operatorname{im} A=\ker f$. Esto, en virtud del primer [teorema](#isomodules) de isomorfía, equivale a dar una matriz $A$ y un isomorfismo $$\bar{f}\colon \frac{R^m}{\operatorname{im} A}\stackrel{\cong}\longrightarrow M.$$ Decimos que un módulo es **finitamente presentado** si admite una presentación. 
 \End{definition}


\Begin{remark} 
En las condiciones de la definición, el $R$-módulo $M$ está generado por $\\{f(e\_1),\dots,f(e\_m)\\}\subset M$, y estos generadores satisfacen las relaciones determinadas por la matriz $A$. 
 \End{remark}



\Begin{proposition}\label{fgfp} 
Dado un dominio de ideales principales $R$, todo $R$-módulo finitamente generado $M$ admite una presentación. 
 \End{proposition}


\Begin{proof} 
Sea $S=\\{a\_1,\dots,a\_m\\}\subset M$ un conjunto de generadores. Por serlo, el homomorfismo $\phi\_S\colon R^m\rightarrow M$ es sobreyectivo, así que $$\frac{R^m}{\ker\phi\_{S}}\cong M.$$ Según hemos visto anteriormente, el submódulo $\ker \phi\_S\subset R^n$ es finitamente generado. Escogemos un conjunto de generadores $S'=\\{b\_1,\dots,b\_n\\}\subset \ker \phi\_{S}$, que por tanto inducen otro homomorfismo sobreyectivo $\phi\_{S'}\colon R^n\rightarrow \ker \phi\_{S}$. Consideramos su composición con la inclusión, $$A\colon R^n\stackrel{\phi\_{S'}}\twoheadrightarrow \ker \phi\_S\hookrightarrow R^m,$$ que estará definida por una matriz $A$. Al ser $\phi\_{S'}$ sobreyectiva, $\operatorname{im}A=\ker \phi\_{S}$, con lo que $A$ es una presentación de $M$.
 \End{proof}


Una presentación de un módulo se puede modificar y simplificar de los siguientes modos.

\Begin{proposition}\label{simplify} 
Si el $R$-módulo $M$ está presentado por la matriz $A$ de tamaño $m\times n$ entonces también está presentado por la matriz $A'$ en los siguientes casos: 

* Si $A'=QAP^{-1}$ siendo $P$ y $Q$ matrices invertibles.

* Si $A'$ se obtienen a partir de $A$ eliminando una columna de ceros,
$$
A=\left(
\begin{array}{cccc}
&&0&\cr
&&\vdots&\cr
&&0&
\end{array}
\right).
$$

* Si la $j$-ésima columna de $A$ es $ue_i$, donde $u\in R^\times$ es una unidad, y $A'$ se obtiene borrando la $i$-ésima fila y la $j$-ésima columna de $A$,
$$
A=\left(
\begin{array}{cccc}
&&0&\cr
&&\vdots&\cr
\cdots&\cdots&u&\cdots\cr
&&\vdots&\cr
&&0&\cr
\end{array}
\right).
$$

 \End{proposition}

\Begin{proof} 
 
* Las matrices invertibles $P$ y $Q$ se corresponden con meros cambios de base en $R^m$ y $R^n$, respectivamente, con lo cual tenemos un isomorfismo $$\begin{array}{rcl}
R^m/\operatorname{im}A&\stackrel{\cong}\longrightarrow& R^m/\operatorname{im}A'\cr [x]&\mapsto& [Qx].\end{array}$$
Usando el primer [teorema](#isomodules) de isomorfía, podemos comprobar que esta aplicación está en efecto bien definida y es un isomorfismo.

* Una columna de ceros se corresponde con la relación $0=0$, que no aporta nada, con lo cual puede eliminarse.

* En este caso la $j$-ésima columna se corresponde con la relación $ua_i=0$, que equivale a $a\_i=0$, pues $u$ es una unidad, así que podemos simplemente eliminar $a\_i$ de la lista de generadores y $a\_i=0$ de la de relaciones. Esto se corresponde con la eliminación de la $i$-ésima fila y la $j$-ésima columna de $A$.

 \End{proof}


Cuando una matriz es especialmente sencilla resulta fácil identificar el módulo que presenta.

\Begin{proposition}\label{easy} 
El $R$-módulo $R^m/\operatorname{im}D$ presentado por la matriz $$D=\left( \begin{array}{ccc} d\_1&&\cr &\ddots&\cr &&d\_n\cr \hline &0& \end{array} \right)$$ de tamaño $m\times n$ con una caja superior diagonal de tamaño $n\times n$ y una caja inferior trivial de tamaño $(m-n)\times n$, es isomorfo a $$\frac{R}{(d\_1)}\times \cdots \times\frac{R}{(d\_n)}\times R^{m-n}.$$ 
 \End{proposition}


\Begin{proof} 
Es obvio, ya que este módulo está generado por $\\{a\_1,\dots,a\_m\\}$, donde $a\_i=\bar e\_i$, y las relaciones correspondientes a la matriz $D$ son $$d\_ia\_i=0,\quad 1\leq i\leq n.$$ Por tanto las únicas relaciones existentes nos dicen que hemos de considerar la $i$-ésima coordenada módulo $(d\_i)$, $1\leq i\leq n$. El isomorfismo está simplemente definido por
$$
\begin{array}{rcl}
\frac{R^m}{\operatorname{im} D}
&\stackrel{\cong}\longrightarrow&
\frac{R}{(d\_1)}\times \cdots \times\frac{R}{(d\_n)}\times R^{m-n},\cr
{[(a\_1,\dots,a\_m)]}&\mapsto&(\bar{a}\_1,\dots, \bar{a}\_n,a\_{n+1},\dots,a\_m).
\end{array}
$$
 \End{proof}



## Forma normal de Smith

En esta sección veremos cómo la matriz de una presentación de un módulo se puede simplificar mediante operaciones elementales.

\Begin{definition} 
Las **operaciones elementales por filas** para matrices con entradas en un anillo $R$ son las siguientes:

1. Añadirle a una fila un múltiplo de otra, $F\_i+rF\_j$, $i\neq j$, $r\in R$.

2. Intercambiar dos filas $F\_i\leftrightarrow F\_j$, $i\neq j$.

3. Multiplicar una fila por una unidad $u\in R^\times$, $uF\_i$ .

Las **operaciones elementales por columnas** se definen análogamente.

 \End{definition}


Las operaciones elementales anteriores se corresponden con el producto por los siguientes tipos de matrices.

\Begin{definition} 
Las **matrices elementales** son las que se obtienen a partir de la identidad realizando una de las operaciones elementales por filas anteriores. Concretamente:

1. $E_{ij}( r )=\left(\begin{array}{ccccccc}1&&&&&&\cr &\ddots&&&&&\cr &&1&\cdots&r&&\cr &&&\ddots&\vdots&&\cr &&&&1&&\cr &&&&&\ddots&\cr &&&&&&1\end{array}\right)$.

2. $E_{ij}=\left(\begin{array}{ccccccc}1&&&&&&\cr &\ddots&&&&&\cr &&0&\cdots&1&&\cr &&\vdots&\ddots&\vdots&&\cr &&1&\cdots&0&&\cr &&&&&\ddots&\cr &&&&&&1\end{array}\right)$.

3. $E_{ii}(u)=\left(\begin{array}{ccccccc}1&&&&&&\cr &\ddots&&&&&\cr &&1&&&&\cr &&&u&&&\cr &&&&1&&\cr &&&&&\ddots&\cr &&&&&&1\end{array}\right)$.

 \End{definition}


\Begin{remark} 
 Las matrices elementales son invertibles, concretamente:

1. $E\_{ij}( r )^{-1}=E\_{ij}(-r)$.

2. $E\_{ij}^{-1}=E\_{ij}$.

3. $E\_{ii}(u)^{-1}=E\_{ii}(u^{-1})$.

Sus determinantes son
$$\begin{array}{rcl}
|E\_{ij}( r )|&=&1,\cr
|E\_{ij}|&=&-1,\cr
|E\_{ii}(u)|&=&u.
\end{array}$$

Las operaciones elementales por filas y columnas se corresponden con los productos por matrices elementales a izquierda y derecha, respectivamente: 
$$\begin{array}{rclrcl}
A&\stackrel{F\_i+rF\_j}\longrightarrow& E\_{ij}( r )A,& A&\stackrel{C\_i+rC\_j}\longrightarrow& AE\_{ji}( r ),\cr
A&\stackrel{F\_i\leftrightarrow F\_j}\longrightarrow &E\_{ij}A=A,&  A&\stackrel{C\_i\leftrightarrow C\_j}\longrightarrow& AE\_{ij},\cr
A&\stackrel{uF\_i}\longrightarrow& E\_{ii}(u)A,& A&\stackrel{uC\_i}\longrightarrow& AE\_{ii}(u).
\end{array}$$

Por tanto, si $A'$ se obtiene a partir de $A$ a través de operaciones elementales por filas y columnas, entonces existen matrices invertibles $P$ y $Q$ tales que $$A'=QAP^{-1}.$$
En particular $A$ y $A'$ presentan el mismo módulo.

También deducimos que el determinante de una matriz no varía cuando se realiza una operación elemental de tipo 1, cambia de signo al hacer una operación elemental de tipo 2, y pasa a ser un asociado al realizar una operación elemental de tipo 3.
 \End{remark}



\Begin{theorem}\textrm{\normalfont (Forma normal de Smith)}\label{smith} 
Dada una matriz $A$ de tamaño $m\times n$ sobre un dominio euclídeo $R$, existen matrices invertibles $P$ y $Q$, que son de hecho productos de matrices elementales, tales que $$QAP^{-1}=D=\left( \begin{array}{ccc|c} d\_1&&&\cr &\ddots&&0\cr &&d\_k&\cr \hline &0&&0 \end{array} \right)$$ es una matriz con una descomposición de tamaño $2\times 2$ por cajas cuya única caja no trivial es la superior izquierda, que es diagonal con entradas diagonales no nulas y satisface $d\_i|d\_{i+1}$ para todo $1\leq i {<} k$. Esta matriz $D$ se denomina **forma normal de Smith** de $A$. <!--- el número $k$ de entradas no nulas es único y los $d_i$ son únicos salvo asociados. --> 
 \End{theorem}


\Begin{proof} 
La estrategia para probar la existencia consiste en aplicarle a $A$ una serie de operaciones elementales para llegar a una matriz de la forma 
$$\left(\begin{array}{c|c}
d_1&0\cr \hline 0&B
\end{array}\right)$$
donde $d_1$ divide a todas las entradas de $B$. Una vez hecho esto, pasamos a trabajar del mismo modo con la matriz $B$. De este modo obtenemos el resultado por inducción ya que si un elemento de $R$ divide a todas las entradas de una matriz $B$ entonces también divide a las entradas de una matriz obtenida a partir de $B$ mediante una operación elemental.

Sea $A$ una matriz no nula (si fuera nula no habría nada que hacer). Para llegar a una matriz como la anterior a partir de $A$ aplicamos el siguiente procedimiento:

1. Permutando filas y columnas, mueve la entrada no nula de menor tamaño a la esquina superior izquierda.

2. Dada una entrada no nula de la primera columna $a\_{i1}$, $i>1$, realiza la división euclídea $a\_{i1}=c\cdot a\_{11}+r$ y la operación $F\_{i}-c\cdot F\_1$. La entrada $(i,1)$ de la nueva matriz es el resto $r$. Si este resto es no nulo entonces tiene tamaño menor que $a\_{11}$, así que volvermos al paso 1. Si no, continuamos con otra entrada no nula de la primera columna. Si el resto de entradas de la primera columna son $0$, pasamos a hacer lo análogo con la primera fila, es decir, buscamos una entrada $a\_{1j}$ no nula, $j>1$, realizamos la división euclídea $a\_{1j}=c\cdot a\_{11}+r$ y la operación $C\_{j}-c\cdot C\_1$. La entrada $(1,j)$ de la nueva matriz es el resto $r$. Si este resto no es nulo entonces tiene tamaño menor que el de $a\_{11}$ y pasamos al paso 1. Si no, realizamos el mismo procedimiento con otra entrada no nula de la primera fila.

3. Cuando lleguemos aquí es porque el único elemento no nulo de la primera fila y de la primera columna es el $a\_{11}$. Si hay algún elemento no nulo $a\_{ij}$ que no es divisible por $a\_{11}$ realizamos la operación $F\_{1}+F\_{i}$. La matriz resultante tiene el mismo $a\_{11}$, pero en la entrada $(1,j)$ nos encontramos con $a\_{ij}$, que no es múltiplo de $a\_{11}$, así que volvemos al paso 1. (También podríamos hacer la operación $C\_{1}+C\_{j}$ y pasar al paso 1.) Si no lo hay, es porque nuestra matriz ya es de la forma $$\left(\begin{array}{c|c}
d_1&0\cr \hline 0&B
\end{array}\right)$$
y $d_1$ divide a todas las entradas de $B$.

Este procedimiento termina porque cada vez que realizamos una división euclídea con resto no nulo, el mínimo de los tamaños de los elementos no nulos disminuye. Como este número es un entero no negativo, no puede disminuir indefinidamente. Esto asegura que el procedimiento acaba tras un número finito de pasos.

Este método para llegar a la forma normal de Smith se conoce como  **algoritmo de diagonalización** de matrices con entradas en $R$.

En virtud de la correspondencia entre operaciones y matrices elementales, la matriz $Q$ del enunciado se obtiene al realizar sobre la matriz identidad $I_m$ de tamaño $m\times m$ todas las operaciones elementales por filas que hemos usado para hallar $D$, en el mismo orden. Análogamente, $P^{-1}$ se obtiene al aplicarle a $I_n$ todas las operaciones elementales por columnas realizadas para calcular $D$.

<!--- La unicidad de la forma normal de Smith se observa del siguiente modo. Si $d$ divide a todas las entradas de una matriz $A$ entonces también dividirá a todas las entradas de cualquier otra matriz obtenida a partir de $A$ mediante una operación elemental. Las operaciones elementales son reversibles, por tanto el divisor máximo común de las entradas de una matriz no varía al realizar operaciones elementales. La forma normal de Smith se obtiene a partir de $A$ mediante operaciones elementales y el divisor máximo común de sus entradas es $d\_1$, por tanto $d\_1$ también es el divisor máximo común de las entradas de $A$, que es único salvo asociados.

Un **menor** de orden $r$ de una matriz $m\times n$ es el determinante de una submatriz de tamaño $r\times r$, 
$$\left|\begin{array}{ccc}
a\_{i\_1j\_1}&\cdots & a\_{i\_1j\_r}\cr
\vdots&\ddots&\vdots\cr
a\_{i\_rj\_1}&\cdots & a\_{i\_rj\_r}
\end{array}\right|,\qquad 1\leq i\_1{<}\cdots{<}i\_r\leq m,\quad 1\leq j\_1{<}\cdots{<}j	\_r\leq n.$$
Los menores de orden $1$ son simplemente las entradas de la matriz. El razonamiento anterior es igualmente cierto si reemplazamos entradas por menores, es decir, el divisor máximo común de los menores de orden $r$ no varía al hacer operaciones elementales. Para la forma normal de Smith, dicho divisor máximo común es $d\_1\cdots d\_r$ si $1\leq r\leq k$ y $0$ si $r>k$. De aquí se deduce la unicidad de $k$ y de los $d\_i$ salvo asociados. -->
 \End{proof}

La siguiente aplicación es una calculadora de la forma normal de Smith paso a paso. El dato de entrada es una matriz con entradas en $\mathbb{Z}$ expresada como lista de filas.

<div class="sage">
  <script type="text/x-sage">
@interact
def _(A = input_box('[[0,4,6],[5,8,10]]', width = 40, type = matrix, label='Matriz $A=$'), showQ=checkbox(False, label='Calcula $Q$'), showPm=checkbox(False, label='Calcula $P^{-1}$'), auto_update=False):
    def qr(a,b): # euclidean division of a by b with smallest abs(remainder)
        quotient, remainder = a.quo_rem(b)
        if abs(remainder) > abs(b/2): # if the remainder is too big, take the other Euclidean division
            quotient = quotient+sign(b)*sign(remainder)
            remainder = remainder-abs(b)*sign(remainder)
        return [quotient,remainder]
    def smallest(M,l): # find the smallest non-zero element in the bottom right corner starting at (l,l)
        answer = [0] # initialize with trivial answer
        for i in [l .. (M.nrows() - 1)]: # Parse entries
            for j in [l .. (M.ncols() - 1)]:
                if M[i,j] != 0: # check whether entry is non-zero
                    if answer == [0]: # if no non-zero entry had been stored, store this entry
                        answer = [M[i,j],i,j]
                    else: # if some non-zero entry had been stored
                        if abs(M[i,j]) < abs(answer[0]): # check whether the new entry is smaller than the stored value
                            answer = [M[i,j],i,j] # take new entry as new answer
        return answer # it yields the smallest value and its coordinates, or the trivial answer if the submatrix was trivial
    def row_modular(M,l): # find the first element M[l,j] not divisible by M[l,l]
        j = l+1
        while j < M.ncols():
            if M[l,j].mod(M[l,l]) != 0:
                return [M[l,j],j] # return the first one and its column coordinate
            else:
                j = j+1
        return [0] # return this trivial answer if M[l,l] divides all elements to its right
    def nondivisible(M,l): # find in the submatrix below right (l,l) an element which is not divisible by  M[l,l]
        answer = [0] # initialize with trivial answer
        rows = M.nrows() # number of rows
        cols = M.ncols() # number of columns
        i = l # we start checking M[l,l+1]
        j = l+1
        while answer == [0] and i < rows: # we will stop as soon as we find one or we exhaust all entries
            if j < cols: # j is a valid column number
                if M[i,j].mod(M[l,l]) != 0: # check whether entry is not divisible by M[l,l]
                    answer = [M[i,j],i,j] # store entry and coordinates
                else:
                    j = j+1 # next column
            else:
                i = i+1 # next row
                j = l # column l
        return answer # it yields the smallest value and its coordinates, or the trivial answer if the submatrix was trivial
    def format_scalar(r): # display nice multiplying integer
        if r == 1:
            return ' + '
        if r == - 1:
            return ' - '
        if r > 0 and r != 1:
            return ' + '+str(r)
        if r < 0 and r != -1:
            return ' - '+str(-r)
    def type1rows(M,i,j,r): # type 1 row operation with statement (without arrow)
        M.add_multiple_of_row(i,j,r)
        return 'F_{'+str(i+1)+'}'+format_scalar(r)+'F_{'+str(j+1)+'}'
    def type1cols(M,i,j,r): # type 1 column operation with statement (without arrow)
        M.add_multiple_of_column(i,j,r)
        return 'C_{'+str(i+1)+'}'+format_scalar(r)+'C_{'+str(j+1)+'}'
    def type2rows(M,i,j): # type 2 row operation with statement over an arrow
        M.swap_rows(i,j)
        return ' \\stackrel{F_{'+str(i+1)+'} \\leftrightarrow F_{'+str(j+1)+'}}{\\longrightarrow} '
    def type2cols(M,i,j): # type 2 column operation with statement over an arrow
        M.swap_columns(i,j)
        return ' \\stackrel{C_{'+str(i+1)+'} \\leftrightarrow C_{'+str(j+1)+'}}{\\longrightarrow} '
    def smith(M): # compute Smith normal form D and invertible matrices Q and Pm such that Q*M*Pm = D
        Keep = matrix(M) # keep the original argument
        M = matrix(M) # turn M into a matrix in case it where just a list of rows
        d = infinity # initialize smallest non-zero element size with infinity
        i = 0 # start with the whole matrix
        rows = M.nrows() # number of rows
        cols = M.ncols() # number of columns
        Q = identity_matrix(rows) # invertible matrix on the left
        Pm = identity_matrix(cols) # invertible matrix on the right
        L = latex(M) # initialize LaTeX output for algorithm computing D
        LQ = latex(Q) # initialize LaTeX output for algorithm computing Q
        LPm = latex(Pm) # initialize LaTeX output for algorithm computing Pm
        while i < min(rows,cols) and abs(d) > 0: # Row/column where we start operating (the submatrix) 
            small = smallest(M,i) # smallest non-zero element of the submatrix
            d = small[0]
            if d != 0: # check whether the submatrix is non-trivial, and then place the smallest element at (i,i) if non-zero
                if small[1] > i: # the row operation, if necessary
                    L = L + type2rows(M,i,small[1]) + latex(M)
                    LQ = LQ + type2rows(Q,i,small[1]) + latex(Q)
                if small[2] > i: # the column operation, if necessary
                    L = L + type2cols(M,i,small[2]) + latex(M)
                    LPm = LPm + type2cols(Pm,i,small[2]) + latex(Pm)
                nondivrow = row_modular(M,i) # find non-divisible element to the right
                if nondivrow[0] != 0: # column operation for division with remainder, if necessary
                    scalar,d = qr(nondivrow[0],M[i,i]) # the quotient and the remainder, new smallest non-zero element
                    L = L + ' \\stackrel{' + type1cols(M,nondivrow[1],i,-scalar) + '}{\\longrightarrow} ' + latex(M)
                    LPm = LPm + ' \\stackrel{' + type1cols(Pm,nondivrow[1],i,-scalar) + '}{\\longrightarrow} ' + latex(Pm)
                else:
                    nondivcol = row_modular(M.transpose(),i) # find non-divisible element below
                    if nondivcol[0] != 0: # Row operation for division with remainder, if necessary
                        scalar,d = qr(nondivcol[0],M[i,i]) # the quotient and the remainder, new smallest non-zero element
                        L = L + ' \\stackrel{' + type1rows(M,nondivcol[1],i,-scalar) + '}{\\longrightarrow} ' + latex(M)
                        LQ = LQ + ' \\stackrel{' + type1rows(Q,nondivcol[1],i,-scalar) + '}{\\longrightarrow} ' + latex(Q)
                    else: # kill elements to the right and bottom of M[i,i]
                        test = False # >test to check if something (non-zero) will be killed to the right
                        L1 = '' # initialize set of stacked column operations
                        LPm1 = '' # idem
                        for col in [(i+1) .. (cols-1)]: # kill all elements to the right of M[i,i]
                            if M[i,col] != 0:
                                scalar = M[i,col]/M[i,i] # the quotient
                                L1 = L1 + type1cols(M,col,i,-scalar) + ' \\cr '
                                LPm1 = LPm1 + type1cols(Pm,col,i,-scalar) + ' \\cr '
                                test = True # if something has been killed
                        if test: # add new steps if the matrix has been modified
                            L = L + ' \\stackrel{\\substack{' + L1 + '}}{\\longrightarrow} ' + latex(M)
                            LPm = LPm + ' \\stackrel{\\substack{' + LPm1 + '}}{\\longrightarrow} ' + latex(Pm)
                        test = False # test to check if something (non-zero) will be killed at the bottom
                        L2 = '' # initialize set of stacked row operations
                        LQ2 = '' # idem
                        for row in [(i+1) .. (rows-1)]: # kill all elements below M[i,i]
                            if M[row,i] != 0:
                                scalar = M[row,i]/M[i,i] # the quotient
                                L2 = L2 + type1rows(M,row,i,-scalar) + ' \\cr '
                                LQ2 = LQ2 + type1rows(Q,row,i,-scalar) + ' \\cr '
                                test = True # if something has been killed
                        if test: # add new steps if the matrix has been modified
                            L = L + ' \\stackrel{\\substack{' + L2 + '}}{\\longrightarrow} ' + latex(M)
                            LQ = LQ + ' \\stackrel{\\substack{' + LQ2 + '}}{\\longrightarrow} ' + latex(Q)
                        nondiv = nondivisible(M,i) # find in the submatrix below right (i,i) an element which is not divisible by  M[i,i]
                        if nondiv[0] != 0: # if it exists...
                            L = L + ' \\stackrel{' + type1rows(M,i,nondiv[1],1) + '}{\\longrightarrow} ' + latex(M) # perform a row operation to fuck up row i
                            LQ = LQ + ' \\stackrel{' + type1rows(Q,i,nondiv[1],1) + '}{\\longrightarrow} ' + latex(Q)  
                        else:
                            i = i+1
        show(html('Este programa, apartir de una matriz de enteros $A$ introducida como lista de filas, calcula paso a paso su forma normal de Smith $D$ y matrices invertibles $Q$ y $P^{-1}$ tales que $QAP^{-1}=D$.'))
        show(html('C&aacute;lculo de $D$:'))
        show('A='+latex(L)+'=D')
        if showQ:
            show(html('C&aacute;lculo de $Q$:'))
            show('I='+latex(LQ)+'=Q')
        if showPm:
            show(html('C&aacute;lculo de $P^{-1}$:'))
            show('I='+latex(LPm)+'=P^{-1}')
        if Q*Keep*Pm != M: # perform a test
            show('LOS RESULTADOS SON ERRÓNEOS')
        return (M, Q, Pm) # it gives the Smith normal form and two invertible matrices Q and Pm such that Q*M*Pm is the Smith normal form
    smith(A)
 </script>
</div>

El teorema de la forma normal de Smith es cierto más generalmente para dominios de ideales principales. La demostración es análoga pero hace uso de la identidad de Bézout en lugar de la división euclídea y de un tipo más general de operación elemental. La forma normal de Smith es única salvo asociados, aunque no lo hemos probado. <!--- Si $R=\mathbb Z$ hay una única forma normal de Smith que donde todos los $d\_i$ son positivos, ya que todo entero no nulo es asociado de un único entero positivo. A esta forma normal de Smith se que llega usando también operaciones elementales de tipo $3$. Análogamente, si $R=k[x]$, con $k$ un cuerpo, hay una única forma normal de Smith que donde todos los polinomios $d\_i$ son mónicos. -->



\Begin{corollary} 
Toda matriz invertible con entradas en un dominio euclídeo es producto de matrices elementales. 
 \End{corollary}


\Begin{proof} 
El determinante de una matriz $A$ de tamaño $n\times n$ es asociado del determinante de cualquier otra matriz que se obtenga a partir de $A$ tras realizar una operación elemental. En particular, $|A|$ es asociado del determinante de su forma normal de Smith $D$. El determinante $|D|$ es $0$ si $k{<}n$ y $d\_1\cdots d\_n$ si $k=n$. Si $A$ es invertible entonces $|A|$ es una unidad, luego necesariamente $k=n$ y $d\_1\cdots d\_n$ también es una unidad. En particular todos los $d_i$ son unidades, es decir, la forma normal de Smith es un producto de matrices elementales tipo 3, $D=E\_{11}(d\_1)\cdots E\_{nn}(d\_n)$. Despejando $A=Q^{-1}DP$ vemos que $A$ es producto de matrices elementales.
 \End{proof}


\Begin{corollary} 
 Dado un dominio de ideales principales $R$, todo submódulo de $R^m$ es libre y de rango $\leq m$. 
 \End{corollary}


\Begin{proof} 
Sea $M\subset R^m$ un submódulo. Al [demostrar](#fgfp) que todo $R$-módulo finitamente generado es finitamente presentado vimos que se puede suponer sin pérdida de generalidad que $M=\operatorname{im}A$ para cierto homomorfismo $A\colon R^n\rightarrow R^m$ definido por una matriz $A$ de tamaño $m\times n$. El $R$-módulo $M$ está pues generado por las columnas de $A$. Tomamos la forma normal de Smith $D=QAP^{-1}$. Esta ecuación equivale a $DP=QA$, que es lo mismo que decir que el siguiente diagrama de $R$-módulos libres conmuta,

![Cuadrado conmutativo](../images/libres.png)

Como $P$ y $Q$ son invertibles, los homomorfismos que definen son isomorfismos, por tanto $Q$ induce in isomorfismo $M=\operatorname{im}A\cong \operatorname{im}D$. 
La imagen del homomorfismo definido por  
$$
D=\left( \begin{array}{ccc|c} d\_1&&&\cr &\ddots&&0\cr &&d\_k&\cr \hline &0&&0 \end{array} \right)
$$ 
está también generada por sus columnas. Claramente, para generar $\operatorname{im} D$ bastan las primeras $k$ columnas de $D$, que además son linealmente independientes, por tanto forman una base $$\\{d_1e_1,\dots, d_ke_k\\}\subset \operatorname{im} D$$ y este módulo es libre re rango $k\leq m$. Esto implica que $M=\operatorname{im}A\cong \operatorname{im} D$ es libre del mismo rango con base $$\\{d_1Q^{-1}e_1,\dots, d_kQ^{-1}e_k\\}.$$
 \End{proof}


## Teoremas de estructura

Veamos que sobre un dominio de ideales principales todo módulo finitamente generado se descompone salvo isomorfismo como producto de módulos cíclicos.

\Begin{theorem}\textrm{\normalfont (Estructura de módulos finitamente generados sobre un DIP, 1ª forma)} 
Dado un dominio de ideales principales $R$, todo $R$-módulo finitamente generado $M$ es isomorfo a uno de la forma $$\frac{R}{(d\_1)}\times \cdots \times\frac{R}{(d\_n)}\times R^{r}$$ donde $d\_1,\dots,d\_n\in R$ no son cero ni unidades y satisfacen $d\_i|d\_{i+1}$, $1\leq i{<}n$. <!--- Además los enteros $k,r\geq 0$ son únicos y los $d_i$ son únicos salvo asociados. -->
 \End{theorem}


\Begin{proof} 
Hemos visto en una [proposición](#fgfp) anterior que $M$ es finitamente presentado. Sea la matriz $A$ una presentación de $M\cong R^m/\operatorname{im}A$. En virtud de [otra](#simplify), su forma normal de [Smith](#smith)
$D=QAP^{-1}$
también presenta $M\cong R^m/\operatorname{im}D$. Es más, podemos eliminar las columnas de ceros. Más aún, algún $d\_i$ podría ser una unidad (los anteriores también tendrían que serlo, pues lo dividen). En este caso, podríamos eliminar la $i$-ésima fila y la $i$-ésima columna. De este modo acabamos con una matriz $$\left( \begin{array}{ccc} d\_1&&\cr &\ddots&\cr &&d\_n\cr \hline &0& \end{array} \right)$$ donde los $d\_i$ no son nulos ni unidades, y además satisfacen $d\_i|d\_{i+1}$, $1\leq i{<}n$. El módulo presentado por esta matriz es el del enunciado, en virtud de una [proposición](#easy) anterior más.
 \End{proof}

La descomposición anterior de un $R$-módulo $M$ como producto de $R$-módulos cíclicos se puede agrupar en dos factores, la **parte libre** y la **parte de torsión**,
$$\underbrace{\frac{R}{(d\_1)}\times \cdots \times\frac{R}{(d\_n)}}\_{\text{parte de torsión}}\times \underbrace{R^{r}}\_{\text{parte libre}}.$$

\Begin{remark} 
Este primer teorema de estructura demuestra que todo $R$-módulo finitamente generado sobre un DIP $R$ es isomorfo a un producto de módulos cíclicos de un tipo muy particular. Este producto es de hecho único en el siguiente sentido. Si
$$
\frac{R}{(d\_1)}\times \cdots \times\frac{R}{(d\_n)}\times R^{r}
\cong  
\frac{R}{(e\_1)}\times \cdots \times\frac{R}{(e\_m)}\times R^{s},
$$
donde los $d\_i$ y los $e\_j$ no son nulos ni unidades y satisfacen $d\_i\mid d\_{i+1}$ y $e\_j\mid e\_{j+1}$, entonces $r=s$, $n=m$ y cada $d\_i$ es asociado de $e\_i$. 

La demostración de que $r=s$ la veremos en general, pero el resto solo lo probaremos para $R=\mathbb{Z}$ y lo esbozaremos par $R=k[x]$ con $k$ un cuerpo. 
 \End{remark}

\Begin{watch} 
A pesar de la unicidad de la forma del primer teorema de estructura, el isomorfismo no es único. Por ejemplo, de $\frac{\mathbb{Z}}{(2)}\times \frac{\mathbb{Z}}{(2)}$ en sí mismo tenemos dos isomorfismos, la identidad y el intercambio de coordenadas $(a,b)\mapsto (b,a)$.
 \End{watch}

\Begin{remark} 
Todo módulo cíclico $R/(d)$ sobre un DIP $R$ está en la forma del primer teorema de estructura, por tanto la unicidad antes mencionada demuestra que un $R$-módulo es cíclico si y solo si la descomposición dada por el teorema de estructura posee un único factor.
 \End{remark}

Dado un módulo $M$ finitamente generado sobre un DIP, vamos a ver que $T(M)$ es isomorfo a la parte de torsión de la descomposición del teorema de estructura y que $M/T(M)$ es isomorfo a la parte libre.

\Begin{proposition}\label{partsoffg} 
Si $M$ es un $R$-módulo sobre un dominio $R$ tal que
$$M\cong \frac{R}{(d\_1)}\times \cdots \times\frac{R}{(d\_n)}\times R^{r}$$
con $d_i\neq 0$ para todo $i$, entonces 
$$
\begin{array}{rcl}
T(M)&\cong&\frac{R}{(d\_1)}\times \cdots \times\frac{R}{(d\_n)},\cr
M/T(M)&\cong& R^r.
\end{array}
$$
En particular, el $R$-módulo $M/T(M)$ es libre de rango $r$.
 \End{proposition}


\Begin{proof} 
Hemos visto antes que la torsión se preserva por [isomorfismos](#torsionquotient) y además preserva [productos](#torsionproduct), así que, por un lado,
$$
\begin{array}{rcl}
T(M)&\cong&T\left(\frac{R}{(d\_1)}\times \cdots \times\frac{R}{(d\_n)}\times R^{r}\right)\cr
&=&\frac{R}{(d\_1)}\times \cdots \times\frac{R}{(d\_n)}\times \\{0\\}\cr
&\cong&\frac{R}{(d\_1)}\times \cdots \times\frac{R}{(d\_n)}.
\end{array}
$$ 
Por otro lado,
$$
\begin{array}{rcl}
\frac{M}{T(M)}&\cong&
\frac{\frac{R}{(d\_1)}\times \cdots \times\frac{R}{(d\_n)}\times R^{r}}{T\left(\frac{R}{(d\_1)}\times \cdots \times\frac{R}{(d\_n)}\times R^{r}\right)}\cr
&=& \frac{\frac{R}{(d\_1)}\times \cdots \times\frac{R}{(d\_n)}\times R^{r}}{\frac{R}{(d\_1)}\times \cdots \times\frac{R}{(d\_n)}\times\\{0\\}}\cr
&\cong&R^r.
\end{array}$$    
 \End{proof}

Veamos que el rango de la parte libre de la descomposición del teorema de structura solo depende del módulo $M$.

\Begin{corollary}\label{equalrank} 
Dado un dominio $R$ y dos $R$-módulos isomorfos $M\cong N$ tales que 
$$
\begin{array}{rcl}
M&\cong&\frac{R}{(d\_1)}\times \cdots \times\frac{R}{(d\_n)}\times R^{r},
\cr
N&\cong &\frac{R}{(e\_1)}\times \cdots \times\frac{R}{(e\_m)}\times R^{s},
\end{array}
$$
y los $d_i$ y los $e_j$ son no nulos para todos los $i$ y $j$. Entonces $r=s$.
 \End{corollary}

\Begin{proof} 
Como acabamos de ver, $M/T(M)$  es libre de rango $r$ y $N/T(N)$ es libre de rango $s$. También hemos [visto](#torsionquotient) que $M/T(M)\cong N/T(N)$. Deducimos que $r=s$, ya que el rango de un módulo libre es invariante por isomorfismos, pues los isomorfismos preservan bases.
 \End{proof}


\Begin{theorem}\textrm{\normalfont (Teorema chino del resto)} 
 Si $R$ es un DIP y $\operatorname{mcd}(a,b)=1$ entonces tenemos un isomorfismo $$\begin{array}{rcl}g\colon \frac{R}{(ab)}&\stackrel{\cong}\longrightarrow&\frac{R}{(a)}\times \frac{R}{(b)},\cr\bar r&\mapsto &(\bar r,\bar r).\end{array}$$
 \End{theorem}


\Begin{proof} 
Consideramos el homomorfismo de $R$-módulos $$f=\phi\_{\\{(\bar 1,\bar 1)\\}}\colon R\longrightarrow\frac{R}{(a)}\times \frac{R}{(b)}$$ definido por $f(1)=(\bar 1,\bar 1)$. 
Para un $r\in R$ cualquiera, como $f$ preserva el producto por escalares $$f( r )=rf(1)=r(\bar 1,\bar 1)=(\bar r,\bar r).$$ Por el primer [teorema](#isomodules) de isomorfía,
$$
\frac{R}{\ker f}\cong\\operatorname{im} f
$$
y este isomorfismo está definido como $\bar r\mapsto f( r )=(\bar r,\bar r)$. Por tanto bastará probar que $\ker f=(ab)$ y que $f$ es sobreyectivo.


Veamos primero que $\ker f=(ab)$.  En efecto $ab\in\ker f$ ya que $ab\equiv 0$ módulo $(a)$ y módulo $(b)$. Por lo tanto, $(ab)\subset \ker f$. Por otro lado, si $f( r )=(\bar r,\bar r)=(\bar 0,\bar 0)$, es decir si $r\equiv 0$  módulo $(a)$ y módulo $(b)$, entonces $a|r$ y $b|r$ luego $ab=\operatorname{mcm}(a,b)|r$, esto es $r\in (ab)$. 

Veamos ahora que $f$ es sobreyectivo, es decir, que dado cualquier $(\bar c,\bar d)\in \frac{R}{(a)}\times \frac{R}{(b)}$ existe $x\in R$ tal que $f(x)=(\bar{c},\bar{d})$. Esto equivale a resolver el sistema de ecuaciones $$\left\\{\begin{array}{rcl}x&\equiv& c\mod (a),\cr x&\equiv& d\mod (b),\end{array}\right.$$ para $c,d\in R$ cualesquiera. Tomamos una identidad de Bézout $sa+tb=1$ y observamos que $x=sad+tbc$ resuelve la ecuación.
 \End{proof}


\Begin{theorem}\textrm{\normalfont (2ª forma del teorema de estructura)} 
Dado un dominio de ideales principales $R$, todo $R$-módulo finitamente generado $M$ es isomorfo a uno de la forma $$\frac{R}{(p\_1^{m\_1})}\times \cdots \times\frac{R}{(p\_n^{m\_n})}\times R^{r}$$ donde $p\_1,\dots,p\_n\in R$ son primos y $m\_i\geq 1$.
 \End{theorem}


\Begin{proof} 
En virtud de la primera forma del teorema de estructura, basta ver que si $d\in R$ no es nulo ni una unidad, entonces $R/(d)$ es isomorfo a un producto de módulos cíclicos de la forma $R(p^m)$ con $p$ primo.

Todo DIP es un DFU, así que $d$ se puede descomponer, salvo asociados, como producto de potencias de primos no asociados, $p\_{1}^{m\_1}\cdots p\_{n}^{m\_n}$. Entonces, aplicando reiteradamente el teorema chino del resto, obtenemos que $$\frac{R}{(d)}=\frac{R}{(p\_{1}^{m\_1}\cdots p\_{n}^{m\_n})}\cong \frac{R}{(p\_{1}^{m\_1})}\times\cdots\times \frac{R}{(p\_{n}^{m\_n})}.$$
El isomorfismo está definido simplemente como $\bar r\mapsto (\bar r,\dots,\bar r)$.  
 \End{proof}


Las dos formas del teorema de estructura de módulos finitamente generados sobre un DIP son de hecho equivalentes, se puede pasar de una a otra mediante el isomorfismo dado por el teorema chino del resto. La segunda forma del teorema de estructura es por tanto también única, esta vez salvo reordenamiento de los factores de la parte de torsión.

\Begin{example}\textrm{\normalfont (Las dos formas del teorema de estructura)} 
El $\mathbb{Z}$-módulo
$$\frac{\mathbb{Z}}{(2)}\times \frac{\mathbb{Z}}{(2)}\times \frac{\mathbb{Z}}{(2^2)}\times \frac{\mathbb{Z}}{(3)}\times \frac{\mathbb{Z}}{(5)}\times\frac{\mathbb{Z}}{(5^2)}$$
está descompuesto según la segunda forma del teorema de estructura. Para descomponerlo según la primera, comenzamos agrupando los factores que en su denominador tiene las potencias de mayor grado de todos los primos que aparecen, usando el teorema chino del resto, 
$$ \frac{\mathbb{Z}}{(2^2)}\times \frac{\mathbb{Z}}{(3)}\times\frac{\mathbb{Z}}{(5^2)}\cong 
\frac{\mathbb{Z}}{(2^2\cdot 3\cdot 5^2)}=\frac{\mathbb{Z}}{(300)}.$$
Seguidamente, agrupamos las potencias del segundo (si lo hubiere) mayor grado al que aparecen elevados los primos,
$$\frac{\mathbb{Z}}{(2)}\times \frac{\mathbb{Z}}{(5)}\cong \frac{\mathbb{Z}}{(2\cdot 5)}=\frac{\mathbb{Z}}{(10)}.$$
Observamos que aquí ya no aparece ninguna potencia de 3, ya que la única que había ha sido incluida en el grupo anterior. 
Así seguiríamos hasta agotar todos los factores. En este ejemplo solo quedaría uno más, 
$$\frac{\mathbb{Z}}{(2)}.$$
El resultado es 
$$\frac{\mathbb{Z}}{(2)}\times \frac{\mathbb{Z}}{(10)}\times \frac{\mathbb{Z}}{(300)}.$$
Un isomorfismo concreto entre este grupo abeliano y el del comienzo viene dado como composición de dos, primero
$$
\begin{array}{rcl}
\frac{\mathbb{Z}}{(2)}\times \frac{\mathbb{Z}}{(10)}\times \frac{\mathbb{Z}}{(300)}&\stackrel{\cong}\longrightarrow&
\frac{\mathbb{Z}}{(2)}\times \frac{\mathbb{Z}}{(2)}\times \frac{\mathbb{Z}}{(5)}\times \frac{\mathbb{Z}}{(2^2)}\times \frac{\mathbb{Z}}{(3)}\times \frac{\mathbb{Z}}{(5^2)},\cr
(\bar a,\bar b, \bar c)&\mapsto&
(\bar a,\bar b,\bar b, \bar c, \bar c, \bar c),
\end{array}
$$
que es un isomorfismo por el teorema chino del resto, y luego
$$
\begin{array}{rcl}
\frac{\mathbb{Z}}{(2)}\times \frac{\mathbb{Z}}{(2)}\times \frac{\mathbb{Z}}{(5)}\times \frac{\mathbb{Z}}{(2^2)}\times \frac{\mathbb{Z}}{(3)}\times \frac{\mathbb{Z}}{(5^2)}
&\\!\\!\\!\\!\stackrel{\cong}\rightarrow\\!\\!\\!\\!&
\frac{\mathbb{Z}}{(2)}\times \frac{\mathbb{Z}}{(2)}\times \frac{\mathbb{Z}}{(2^2)}\times \frac{\mathbb{Z}}{(3)}\times \frac{\mathbb{Z}}{(5)}\times\frac{\mathbb{Z}}{(5^2)},\cr
(\bar{a}\_1,\bar{a}\_2,\bar{a}\_3,\bar{a}\_4,\bar{a}\_5,\bar{a}\_6)&\\!\\!\\!\\!\mapsto\\!\\!\\!\\!&
(\bar{a}\_1,\bar{a}\_2,\bar{a}\_4,\bar{a}\_5,\bar{a}\_3,\bar{a}\_6),
\end{array}
$$
que es un isomorfismo por la conmutatividad del producto salvo isomorfismo.
 \End{example}



\Begin{example}\textrm{\normalfont (Grupos abelianos con el mismo número de elementos)} 
Los grupos abelianos $$\frac{\mathbb{Z}}{(4)}\times \frac{\mathbb{Z}}{(4)},\qquad\frac{\mathbb{Z}}{(2)}\times \frac{\mathbb{Z}}{(2)}\times \frac{\mathbb{Z}}{(4)},$$ tienen $16$ elementos, pues $4\cdot 4=16=2\cdot 2\cdot 4$, luego existe una biyección entre ambos. Veamos que, a pesar de ello, no son isomorfos. Para verlo jugaremos con la noción de **orden** de un elemento de torsión $a\in A$ de un grupo abeliano $A$, que es el menor entero positivo $n\in\mathbb Z$ tal que $na=0$. El orden de $a$ divide a $n$ si y solo si $na=0$. En particular, para cada entero $n$, el subconjunto $T\_n(A)\subset A$ formado por los elementos cuyo orden divide a $n$ es un subgrupo, que se puede describir como 
$$T_n(A)=\\{a\in A\mid n\cdot a=0\\}.$$
Denotaremos $t\_n(A)$ al orden de $T_n(A)$. Además $T\_n(A\times B)=T\_n(A)\times T\_n(B)$, luego $t\_n(A\times B)=t\_n(A)t\_n(B)$. Es más, todo isomorfismo $A\cong B$ se restringe a $T\_n(A)\cong T\_n(B)$, por tanto en este caso $t\_n(A)=t\_n(B)$. Dado $m\neq 0$, el orden de $\bar a\in\mathbb Z/(m)$ divide a $n$ si y solo si $m\mid na$. Si denotamos $d=\operatorname{mcd}(n,m)$, esto equivale a decir que $\frac{m}{d}\mid a$, por tanto $$T\_n\left(\frac{\mathbb{Z}}{(m)}\right)=\left(\overline{\frac{m}{d}}\right)=\left\\{1\cdot\overline{\frac{m}{d}},\dots,(d-1)\cdot \overline{\frac{m}{d}}\right\\},$$
pues $\overline{\frac{m}{d}}$ tiene orden $d$. Luego $$t\_n\left(\frac{\mathbb{Z}}{(m)}\right)=\operatorname{mcd}(n,m).$$ Aplicando esto a los dos grupos del principio, vemos que el primero cumple $$t\_2\left(\frac{\mathbb{Z}}{(4)}\times \frac{\mathbb{Z}}{(4)}\right)=2\cdot 2=4,$$ mientras que el segundo satisface $$t\_2\left(\frac{\mathbb{Z}}{(2)}\times \frac{\mathbb{Z}}{(2)}\times \frac{\mathbb{Z}}{(4)}\right)=2\cdot 2\cdot 2=8,$$ con lo cual no pueden ser isomorfos.
 \End{example}

El siguiente teorema, combinado con la [proposición](#partsoffg) y el [corolario](#equalrank) anterior, demuestra que la descomposición de un $\mathbb Z$-módulo finitamente generado $M$ dada por el primer teorema de estructura es única. La del segundo también lo será, salvo cambio de orden de los factores de la parte de torsión, pues ambos son equivalentes.

\Begin{theorem} 
Dados dos $\mathbb Z$-módulos 
$$
\begin{array}{rlc}
A&=&\frac{\mathbb Z}{(d\_1)}\times \cdots \times\frac{\mathbb Z}{(d\_n)},\cr
B&=&\frac{\mathbb Z}{(e\_1)}\times \cdots \times\frac{\mathbb Z}{(e\_m)},
\end{array}
$$
donde los $d\_i$ y los $e\_j$ no son nulos ni unidades y satisfacen $d\_i|d\_{i+1}$ y $e\_j|e\_{j+1}$, si $A\cong B$ entonces $n=m$ y cada $d\_i$ es asociado de $e\_i$.
 \End{theorem}


\Begin{proof} 
Podemos suponer sin pérdida de generalidad que los $d\_i$ y los $e\_j$ son positivos. Como ambos grupos son finitos e isomorfos, tienen el mismo orden, es decir, $$d\_1\cdots d\_n=e\_1\cdots e\_m.$$

En $A$, el orden de cualquier elemento divide a $d\_n$, y en $B$ a $e\_m$. Ambos grupos son isomorfos, por tanto el orden de cualquier elemento de $A$ o de $B$ divide a $d\_n$ y a $e\_m$. En $A$ hay un elemento de orden $d\_n$, el $(\bar 0,\dots,\bar 0,\bar 1)$, por tanto $d\_n|e\_m$. En $B$ hay otro con orden $e\_m$, por tanto $e\_m|d\_n$, así que $d\_n=e\_m$. De aquí deducimos también que $$d\_1\cdots d\_{n-1}=e\_1\cdots e\_{m-1}.$$

Demostremos ahora que $d\_{n-1}=e\_{m-1}$. Por un lado, 
$$t\_{d\_{n-1}}(A)=d\_1\cdots d\_{n-2}\cdot d\_{n-1}^2$$
y por otro
$$\begin{array}{rcl}
t\_{d\_{n-1}}(B)&=&\operatorname{mcd}(d\_{n-1},e\_1)\cdots\operatorname{mcd}(d\_{n-1},e\_{m-1})\operatorname{mcd}(d\_{n-1},e\_{m})\cr
&=&\frac{d\_{n-1}e\_1}{\operatorname{mcm}(d\_{n-1},e\_1)}\cdots\frac{d\_{n-1}e\_{m-1}}{\operatorname{mcm}(d\_{n-1},e\_{m-1})}d\_{n-1}\cr
&=&\frac{e\_1\cdots e\_{m-1}d\_{n-1}^m}{\operatorname{mcm}(d\_{n-1},e\_1)\cdots\operatorname{mcm}(d\_{n-1},e\_{m-1})}\cr
&=&\frac{d\_1\cdots d\_{n-2}\cdot d\_{n-1}^{m+1}}{\operatorname{mcm}(d\_{n-1},e\_1)\cdots\operatorname{mcm}(d\_{n-1},e\_{m-1})}.
\end{array}$$
Como necesariamente $t\_{d\_{n-1}}(A)=t\_{d\_{n-1}}(B)$ deducimos que 
$$d\_{n-1}^{m-1}=\operatorname{mcm}(d\_{n-1},e\_1)\cdots\operatorname{mcm}(d\_{n-1},e\_{m-1}).$$
Pero $d\_{n-1}|\operatorname{mcm}(d\_{n-1},e\_{j})$ para todo $1\leq j\leq m-1$, así que la única posibilidad de que ambos productos coincidan es que en todos los casos $d\_{n-1}=\operatorname{mcm}(d\_{n-1},e\_{j})$, es decir $e\_j|d\_{n-1}$. Los papeles de $A$ y $B$, y en particular los de los $d\_i$ y los $e\_j$, son intercambiables, así que también concluimos que $d\_i|e\_{m-1}$ para todo $1\leq i\leq n-1$. En particular $e\_{m-1}|d\_{n-1}$ y $d\_{n-1}|e\_{m-1}$, por tanto $d\_{n-1}=e\_{m-1}$ y deducimos también que $$d\_1\cdots d\_{n-2}=e\_1\cdots e\_{m-2}.$$ 

Este argumento se puede iterar, probando así que los últimos $d\_i$ coinciden con los últimos $e\_j$. Veamos por reducción al absurdo que $n=m$, con lo cual $d\_i=e\_i$ para todo $1\leq i\leq n$. Si $n\neq m$ podemos suponer sin pérdida de generalidad que $n{<}m$. En ese caso acabaríamos probando que $1=e\_1\cdots e\_{m-n}$, pero esto implicaría que estos primeros $e\_j$ son unidades, lo cual sería una contradicción.
  \End{proof}


\Begin{example}\textrm{\normalfont ($k[x]$-módulos de torsión con la misma dimensión)} 
Si $p(x)\in k[x]$ tiene grado $n$, el cociente $k[x]/(p(x))$ tiene dimensión $n$ como $k$-espacio vectorial pues $\\{1,\dots,\bar x^{n-1}\\}$ es una base. Por tanto los $k[x]$-módulos $$\frac{k[x]}{(x^2)}\times \frac{k[x]}{(x^2)},\qquad \frac{k[x]}{(x)}\times \frac{k[x]}{(x)}\times \frac{k[x]}{(x^2)}$$ tienen dimensión $2+2=4=1+1+2$, así que son isomorfos como $k$-espacios vectoriales, pero no como $k[x]$-módulos. En efecto, para verlo, podemos razonar con de **orden** de un elemento de torsión $a\in M$ de un $k[x]$-módulo $M$, que es el polinomio mónico no nulo $p(x)\in k[x]$ de menor grado tal que $p(x)\cdot a=0$. Esta noción de orden satisface propiedades formales similares a las de grupos abelianos. Por ejemplo, al orden de $a$ divide a un polinomio $p(x)\in k[x]$ si y solo si $p(x)\cdot a=0$. Los números relevantes aquí son los $t\_{p(x)}(M)$, que es la dimensión como $k$-espacio vectorial del submódulo $T\_{p(x)}(M)\subset M$ formado por los elementos cuyo orden divide a $p(x)\in k[x]$,
$$T\_{p(x)}(M)=\\{a\in M\mid p(x)\cdot a=0\\}.$$
Tenemos que $T\_{p(x)}(M\times N)=T\_{p(x)}(M)+ T\_{p(x)}(N)$, luego  $t\_{p(x)}(M\times N)=t\_{p(x)}(M)+ t\_{p(x)}(N)$ pues la dimensión de un producto de espacios vectoriales es la suma de las dimensiones de los factores. Es más, todo isomorfismo de $k[x]$-módulos $M\cong N$ se restringe a $T\_{p(x)}(M)\cong T\_{p(x)}(N)$, así que en este caso $t\_{p(x)}(M)= t\_{p(x)}(N)$. Además podemos comprobar que $t\_{p(x)}(k[x]/(q(x)))$ es el grado de $\operatorname{mcd}(p(x),q(x))$. 

Los dos $k[x]$-módulos del comienzo no pueden ser isomorfos porque $$\begin{array}{rcl} t\_{x}\left(\frac{k[x]}{(x^2)}\times \frac{k[x]}{(x^2)}\right)&=&1+1=2,\cr t\_{x}\left(\frac{k[x]}{(x)}\times \frac{k[x]}{(x)}\times \frac{k[x]}{(x^2)}\right)&=&1+1+1=3. \end{array}$$ La demostración de la unicidad de las descomposicións de los teoremas de estructura de $R$-módulos finitamente generados para $R=k[x]$ es análoga al caso de $R=\mathbb Z$, usando para $R=k[x]$ los números $t\_{p(x)}(M)$ y el orden de un $k[x]$-módulo $M$ de torsión $M=T(M)$, que es simplemente su dimensión como $k$-espacio vectorial. La dejamos como ejercicio. 
 \End{example}


## Sistemas de ecuaciones lineales diofánticas

Consideramos un sistema de $m$ ecuaciones lineales con $n$ incógnitas y coeficientes y términos independientes enteros,
$$\left\\{
\begin{array}{ccl}
a\_{11}x\_1+\cdots+a\_{1n}x\_n&=&b\_1,\cr \vdots&&\vdots \cr
a\_{m1}x\_1+\cdots+a\_{mn}x\_n&=&b\_m.
\end{array}
\right.$$
Estamos interesados en hallar las soluciones enteras, es decir, lo consideramos como un sistema de ecuaciones diofánticas.

Si llamamos $$\begin{array}{ccc}A=
\left(\begin{array}{ccc}a\_{11}&\cdots&a\_{1n}\cr\vdots&&\vdots\cr a\_{m1}&\cdots&a\_{mn}\end{array}\right)
,&\vec{x}=\left(\begin{array}{c}x\_1\cr\vdots\cr x\_n\end{array}\right),
&\vec{b}=\left(\begin{array}{c}b\_1\cr\vdots\cr b\_m\end{array}\right)\end{array},$$
podemos expresar el sistema simplemente como
$$A\vec{x}=\vec{b}.$$

Si $A$ está en forma normal de Smith,
$$A=D=\left( \begin{array}{ccc|c} d\_1&&&\cr &\ddots&&0\cr &&d\_k&\cr \hline &0&&0 \end{array} \right)$$
el sistema se reduce a 
$$\left\\{
\begin{array}{ccl}
d\_1x\_1&=&b\_1,\cr 
\vdots&&\vdots \cr
d\_kx\_k&=&b\_k,\cr
0&=&b\_{k+1},\cr 
\vdots&&\vdots \cr
0&=&b\_{m}.
\end{array}
\right.$$
Este sistema claramente tiene solución si y solo si $d\_i|b\_i$ para todo $1\leq i\leq k$ y $b_i=0$ para $k{<}i\leq m$. En dicho caso las soluciones son 
$$x\_i=\frac{b\_i}{d\_i},\quad 1\leq i\leq k;\qquad x\_{k+1},\dots,x\_n\in\mathbb Z;$$ siendo estos últimos valores paramétricos cualesquiera. Observa que la solución es única si además $k=n$.

En general, $A$ tiene una forma normal de Smith $D$ que satisface $QAP^{-1}=D$, es decir $A=Q^{-1}DP$. Tenemos que
$$A\vec{x}=\vec{b}\Leftrightarrow DP\vec{x}=Q\vec{b}.$$
Llamando $$\vec{y}=P\vec{x},$$ lo cual es un simple cambio de veriables, podemos resolver esta ecuación en $\vec{y}$ como arriba, 
$$D\vec{y}=Q\vec{b}.$$
Las soluciones de la ecuación original se obtienen deshaciendo el cambio de variables $$\vec{x}=P^{-1}\vec{y}.$$



## Operadores lineales

Dado un cuerpo $k$ y un $k$-espacio vectorial $V$, un **operador lineal** en $V$ es un endomorfismo $f\colon V\rightarrow V$.


\Begin{proposition} 
Un $k[x]$-módulo es lo mismo que un $k$-espacio vectorial equipado con un operador lineal.
 \End{proposition}


\Begin{proof} 
Un $k[x]$-módulo $M$ es también un $k$-módulo, es decir, un $k$-espacio vectorial, restringiendo el producto por escalares a $k\subset k[x]$. La multiplicación por $x$ es un homomorfismo de $k[x]$-módulos 
$$\begin{array}{rcl}M&\stackrel{x\cdot}\longrightarrow& M,\cr a&\mapsto &x\cdot a,\end{array}$$
en particular también es un homomorfismo de $k$-módulos, es decir, es un operador lineal en el $k$-espacio vectorial $M$.

Recíprocamente, dado un $k$-espacio vectorial $V$ y un operador lineal $f\colon V\rightarrow V$, podemos definir una estructura de $k[x]$-módulo en $V$ del siguiente modo. Dado $v\in V$ y $p(x)=a\_nx^n+\cdots+a\_1x+a\_0\in k[x]$, definimos el producto por escalares como
$$p(x)\cdot v=a\_nf^n(v)+\cdots+a\_1f(v)+a\_0v.$$ Dejamos como ejercicio comprobar que este producto por escalares satisface las propiedades requeridas.
 \End{proof}


\Begin{remark} 
Si $V=k^n$ y consideramos el operador lineal $A\colon k^n\rightarrow k^n$ definido por una matriz $A$ de tamaño $n\times n$ con entradas en $k$, entonces la estructura de $k[x]$-módulo en $k^n$ viene dada por $p(x)\cdot v=p(A)v$ para todo $p(x)\in k[x]$ y $v\in k^n$.
 \End{remark}

\Begin{proposition} 
Dado un operador lineal $A\colon k^n\rightarrow k^n$, el $k[x]$-módulo asociado $k^n$ está presentado por la matriz $A-xI$.
 \End{proposition}

\Begin{proof} 
Hemos de construir un isomorfismo entre el $k[x]$-modulo $k^n$ y el $k[x]$-modulo cociente $$\frac{k[x]^n}{\operatorname{im} (A-xI)}.$$ Para ello, comenzamos considerando el homomorfismo de $k[x]$-modulos
$$\phi=\phi_{\\{e_1,\dots,e_n\\}}\colon k[x]^n\longrightarrow k^n,$$
que está definido por $\phi(e_i)=e_i$. Aquí estamos usando la notación $e_i$ tanto para los elementos de la base canónica del $k[x]$-módulo $k[x]^n$ como para los de la base canónica del $k$-espacio vectorial $k^n$. El homomorfismo $\phi$ es sobreyectivo porque su imagen contiene un conjunto de generadores de $k^n$.

Veamos que $\operatorname{im} (A-xI)\subset\ker \phi$. Como $\operatorname{im} (A-xI)$ está generado por las columnas de la matriz $B=A-xI$, basta ver que estas columnas están en el $\ker \phi$. La $j$-ésima columna es $$b\_{*j}=(a\_{ij})\_{i=1}^n-xe\_j=\sum\_{i=1}^na\_{ij}e\_i-xe\_j.$$ Por tanto, 
$$\phi(b\_{*j})=\sum\_{i=1}^na\_{ij}e\_i-Ae\_j=0,$$
puesto que $\sum\_{i=1}^na\_{ij}e\_i=Ae\_j$ es la $j$-ésima columna de $A$. Esto demuestra que $\phi$ factoriza de manera única a través de la proyección natural, $\phi=g\circ p$,
$$k[x]^n\stackrel{p}\twoheadrightarrow \frac{k[x]^n}{\operatorname{im} (A-xI)}\stackrel{g}\longrightarrow k^n.$$
Como $\phi$ y $p$ son sobreyectivos, $g$ también lo será. 

Queremos probar que $g$ es un isomorfismo. Este homomorfismo sobreyectivo de $k[x]$-módulos también lo es de $k$-modulos, es decir, de $k$-espacios vectoriales. Si demostramos que la dimensión del cociente como $k$-espacio vectorial es $\leq n$, entonces $g$ será necesariamente biyectivo. Sabemos que  $S=\\{\bar{e}\_1,\dots, \bar{e}\_n\\}$ es un conjunto de generadores del cociente como $k[x]$-módulo. Es decir, todo elemento del cociente es una combinación lineal de $S$ con coeficientes polinómicos. Veamos que $S$ es también una base del cociente como $k$-espacio vectorial, es decir, que todo elemento es combinación lineal de $S$ con coeficientes constantes. Para ello basta ver que $x \bar{e}\_j$ es siempre una combinación lineal de $S$ con coeficientes constantes, ya que de aquí se deduciría por inducción que $x^m\bar{e}\_i$ también es una combinación lineal de $S$ con coeficientes constantes para todo $m\geq 1$. La $j$-ésima columna de $A-xI$ es $\sum\_{i=1}^na\_{ij}e\_i-xe\_j$, así que en efecto
$$x\bar{e}\_j=\sum\_{i=1}^na\_{ij}\bar{e}\_i.$$
 \End{proof}



\Begin{proposition} 
Un $k[x]$-módulo $M$ finitamente generado es de torsión, $M=T(M)$, si y solo si tiene dimensión finita como $k$-espacio vectorial.
 \End{proposition}


\Begin{proof} 
$\Rightarrow$ Si $M$ es de torsión entonces por el teorema de estructura de $k[x]$-módulos finitamente generados, $M$ es isomorfo a un producto de una cantidad finita de $k[x]$-módulos cíclicos $k[x]/(p(x))$ con $p(x)\in k[x]$ un polinomio no trivial. Como $k[x]/(p(x))$ tiene dimensión finita como $k$-espacio vectorial (su dimensión es el grado de $p(x)$), deducimos que $M$ también tiene dimensión finita como $k$ espacio vectorial (la suma de las dimensiones de los factores cíclicos del producto). 

$\Leftarrow$ Recíprocamente, si $M$ tiene dimensión finita como $k$ espacio vectorial, entonces no puede tener parte libre en su descomposición como producto de $k[x]$-módulos cíclicos ya que $k[x]$ no tiene dimensión finita como $k$-espacio vectorial.
 \End{proof}


Una **caja de Jordan** es una matriz cuadrada con una constante $\alpha \in k$, denominada **autovalor**, en todas las entradas diagonal principal, $1$ en todas las entradas de la diagonal que está justo por encima de la principal y $0$ en el resto, 

![Caja de Jordan](../images/jordanblock.png)

\Begin{theorem}\textrm{\normalfont (Forma normal de Jordan)} 
Sea $k$ un cuerpo algebraicamente cerrado. Dado un $k$-espacio vectorial de dimensión finita $V$ equipado con un operador lineal $f\colon V\rightarrow V$ existe una base de $V$ respecto de la cual la matriz de $f$ es una matriz diagonal por cajas de Jordan. Esta matriz diagonal por cajas es única salvo permutación de las cajas y se denomina **forma normal de Jordan**.
 \End{theorem}


\Begin{proof} 
Como $k$ es algebraicamente cerrado, los primos en $k[x]$ son los polinomios mónicos de grado $1$ y sus asociados. Sabemos que una base de $$\frac{k[x]}{(x^m)}$$ como $k$-espacio vectorial es  $\\{\bar x^{m-1},\dots,\bar x,1\\}$. Haciendo un cambio de variables es fácil ver que una base de $$\frac{k[x]}{((x-\alpha)^m)}$$ como $k$-espacio vectorial es  $\\{(\bar x-\alpha)^{m-1},\dots,\bar x-\alpha,1\\}$. Como 
$$\begin{array}{rcl}
x\cdot(\bar x-\alpha)^j&=&(x-\alpha+\alpha)\cdot(\bar x-\alpha)^j\cr
&=&(x-\alpha)\cdot(\bar x-\alpha)^j+\alpha\cdot(\bar x-\alpha)^j\cr
&=&(\bar x-\alpha)^{j+1}+\alpha\cdot(\bar x-\alpha)^j,
\end{array}$$ 
la matriz de la multiplicación por $x$,
$$\frac{k[x]}{((x-\alpha)^m)}\stackrel{x\cdot}\longrightarrow \frac{k[x]}{((x-\alpha)^m)}$$
respecto de la base anterior es la caja de Jordan de tamaño $m\times m$ y autovalor $\alpha$.

Usando la primera proposición, consideramos $V$ como un $k[x]$-módulo de torsión con $x\cdot a=f(a)$. En virtud del segundo teorema de estructura, $V$ se descompone como un producto finito de $k[x]$-módulos cíclicos, cocientes por potencias de primos,
$$V\cong\frac{k[x]}{((x-\alpha\_1)^{m\_1})}\times\cdots\times \frac{k[x]}{((x-\alpha\_n)^{m\_n})}.$$
Como $k$-espacio vectorial, el $k[x]$-módulo de la derecha tiene base 
$$\bigcup\_{i=1}^n\\{(0,\dots,(\bar x-\alpha_i)^j,\dots,0)\\}\_{j=m\_i-1}^0,$$ 
donde la coordenada no trivial $(\bar x-\alpha_i)^j$ es la $i$-ésima.
Respecto de esta base, la matriz del homomorfismo de multiplicación por $x$ es la matriz
diagonal por cajas de Jordan de tamaños $m\_i\times m\_i$ y autovalores $\alpha\_i$, $1\leq i\leq n$.
 
![Matriz de Jordan](../images/jordanmatrix.png)

Traslandando esta base a $V$ por el isomorfismo dado por el segundo teorema de estructura, obtenemos una base de $V$ respecto de la cual la matriz de $f$ es esta misma.

La unicidad de la forma normal de Jordan se corresponde con la de la segunda forma del teorema de estructura. Observa que, sin embargo, la base respecto de la cual la matriz de $f$ está en forma normal de Jordan no es única en general.
 \End{proof}


