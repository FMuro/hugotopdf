+++
title = "Fundamentos"
weight = 10
+++

Intuitivamente, un **anillo** es un conjunto donde están definidas las siguientes operaciones:

* Suma.

* Resta.

* Multiplicación.

Estas operaciones deben satisfacer las propiedades habituales.

Además un anillo ha de contener elementos:

* Cero $0$.

* Uno $1$.

Estos elementos deben satisfacer las propiedades usuales con respecto de la suma y la multiplicación.

## Ejemplos


\Begin{example}\textrm{\normalfont (Clásicos)} 
 Los números enteros $\mathbb Z$, racionales $\mathbb Q$, reales $\mathbb R$ y complejos $\mathbb C$ son anillos, pero los naturales $\mathbb N$ no. 
 \End{example}


\Begin{example}\textrm{\normalfont (Polinomios)} 
 Dado un anillo $R$, podemos considerar su anillo de **polinomios** $R[x]$ en una variable $x$, cuyos elementos $p(x)\in R[x]$ son de la forma $$p(x)=a_nx^n+\cdots+a_1x+a_0$$ con *coeficientes* $a\_i\in R$, $1\leq i\leq n$. En ocasiones los denotaremos como si fueran series $$p(x)=\sum\_{n\geq 0}a\_nx^n$$ dando por supuesto que *casi todos* los coeficientes son $0$. Esto facilita la definición de la suma y la multiplicación $$\sum\_{n\geq 0}a\_nx^n+\sum\_{n\geq 0}b\_nx^n=\sum\_{n\geq 0}(a\_n+b\_n)x^n,$$ $$\left(\sum\_{i\geq 0}a\_ix^i\right)\left(\sum\_{j\geq 0}b\_jx^j\right)=\sum\_{n\geq 0}\left(\sum\_{i+j=n}a\_ib\_j\right)x^n.$$ Los anillos de polinomios en varias variables se definen inductivamente $$R[x\_1,\dots, x\_{n-1},x\_n]=(R[x\_1,\dots, x\_{n-1}])[x\_n].$$ 
 \End{example}


\Begin{example} 
También podemos considerar el anillo de **series formales** $R[[x]]$ en una variable $x$ con coeficientes en un anillo $R$. Sus elementos son de la forma $$\sum_{i\geq 0}a_ix^i\in R[[x]],$$ sin restricción sobre los coeficientes $a_i\in R$. La suma y el producto se defininen como antes. Los anillos de series formales en varias variables también se definen inductivamente $$R[[x\_1,\dots, x\_{n-1},x\_n]]=(R[[x\_1,\dots, x\_{n-1}]])[[x\_n]].$$
 \End{example}


## Definición

\Begin{definition} 
 Un **anillo** es un conjunto $R$ equipado con dos aplicaciones, llamadas *suma* y *multiplicación* o *producto*,
$$
\begin{array}{ccc}
R\times R\rightarrow R, &\qquad& R\times R\rightarrow R,\cr
(a,b)\mapsto a+b;&&(a,b) \mapsto ab.
\end{array}
$$
que satisfacen las siguientes propiedades:

* Asociativa: 
$$
\begin{array}{rcl}
a+(b+c)&=&(a+b)+c,\cr 
a(bc)&=&(ab)c.
\end{array}
$$

* Conmutativa: 
$$
\begin{array}{rcl}
a+b&=&b+a,\cr 
ab&=&ba.
\end{array}
$$

* Distributiva:
$$a(b+c)=ab+ac.$$

* Existencia de elementos neutros $0,1\in R$ para la suma y el producto:
$$
\begin{array}{rcl}
0+a&=&a,\cr 
1a&=&a.
\end{array}
$$

* Existencia de un elemento opuesto para la suma $-a\in R$ para todo $a\in R$ de modo que $$a+(-a)=0.$$

 \End{definition}


\Begin{remark} 
La suma de un anillo lo dota de estructura de grupo abeliano. Los elementos neutros son únicos, no puede haber dos distintos que satisfagan la misma propiedad. Los opuestos para la suma también. Restar es sumar el elemento opuesto $a-b=a+(-b)$. Multiplicar por cero siempre da cero, $0a=0$, y además $a(-b)=-ab$. La conmutatividad de la multiplicación no suele exigirse en la definición de anillo, pero nosotros la hemos incluido porque todos los anillos que veremos la satisfacen. Otros, como el anillo $M_{2\times 2}(\mathbb R)$ de matrices $2\times 2$ sobre los números reales, no la cumplen.
 \End{remark}


\Begin{example}\textrm{\normalfont (El anillo trivial)} 
El conjunto unitario $R=\\{0\\}$, dotado de las únicas operaciones suma y multiplicación posibles, es un anillo. Aquí obviamente $1=0$.
 \End{example}


\Begin{proposition} 
En un anillo $R$, $1=0$ si y solo si $R=\\{0\\}$. 
 \End{proposition}


\Begin{proof} 

$\Leftarrow$ Obvio.

$\Rightarrow$ Dado $a\in R$, $a=1a=0a=0$.  

 \End{proof}


\Begin{example}\textrm{\normalfont (Anillos de Boole)} 
Dado un conjunto $X$, el conjunto $\mathcal P(X)=\\{A|A \subset X\\}$ formado por los subconjuntos de $X$ es un anillo, denominado **anillo de Boole**, donde la suma es la *diferencia simétrica*, 
$$A+B=(A\cup B)\setminus (A\cap B)$$ 

![Diferencia simétrica](../../images/symmetric_difference.png) 

y el producto es la intersección, $$AB=A\cap B.$$ ¿Cuál es el $0$? ¿Y el $1$? ¿Y $-A$? ¿Y $A^2$? Dibuja $A+B+C$ para tres conjuntos en posición general.
 \End{example}

\Begin{example}\textrm{\normalfont (Anillo producto)} 
Dados dos anillos $R$ y $S$, el producto cartesiano $R\times S$ es un anillo con las operaciones siguientes:
$$
\begin{array}{rcl}
(r,s)+(r',s')&=&(r+r',s+s'),\cr
(r,s)(r',s')&=&(rr',ss').
\end{array}
$$
El cero es $(0,0)$ y el uno es $(1,1)$.
 \End{example}

\Begin{definition} 
Un subconjunto $S\subset R$ de un anillo $R$ es un **subanillo** si:

* $1\in S$.

* $a+b\in S$ para todo $a,b\in S$.

* $-a\in S$ para todo $a\in S$.

* $ab\in S$ para todo $a,b\in S$.

 \End{definition}


\Begin{remark} 
Un subanillo $S\subset R$ es un anillo por derecho propio con la suma y la multiplicación heredadas de $S$. Observa que $0\in S$. También es un subgrupo para la suma. Ejemplos de subanillos son $\mathbb Z\subset \mathbb Q\subset \mathbb R\subset \mathbb C$ y $R\subset R[x]\subset R[[x]]$.
 \End{remark}


\Begin{example}\textrm{\normalfont (Series convergentes)} 
Si $R=\mathbb R$ o $\mathbb C$, podemos considerar el subanillo de **series convergentes** $R\\{x\\}\subset R[[x]]$. De hecho $R[x]\subset R\\{x\\}\subset R[[x]]$.
 \End{example}


\Begin{example}\textrm{\normalfont (Anillos de funciones)} 
Si $R$ es un anillo y $X$ es un conjunto, podemos considerar el anillo $R^X$ cuyos elementos son las aplicaciones $X\rightarrow R$. La suma y el producto de aplicaciones $f,g\colon X\rightarrow R$ se define punto a punto, $x\in X$, $$\begin{array}{rcl}(f+g)(x)&=&f(x)+g(x),\cr (f\cdot g)(x)&=&f(x)g(x).\end{array}$$ Si $R=\mathbb R$ o $\mathbb C$ y $X$ es un espacio topológico, tenemos el subanillo $\mathcal C(X)\subset R^X$ de funciones continuas.
 \End{example}

\Begin{exercise} 
Dados dos anillos $R$ y $S$, ¿es $R\times\\{0\\}\subset R\times S$ un subanillo? ¿Y $\\{0\\}\times S\subset R\times S$?
 \End{exercise}

\Begin{definition} 
Una **unidad** $u\in R$ es un elemento de un anillo tal que existe $u^{-1}\in R$, denominado **inverso** de $u$, de modo que $uu^{-1}=1$. Un **cuerpo** es un anillo no trivial donde todos los elementos no nulos son unidades.
 \End{definition}


\Begin{remark} 
El elemento inverso $u^{-1}$ de una unidad $u$ es único. Si $u$ es una unidad entonces $u^{-1}$ también y $(u^{-1})^{-1}=u$. Dividir por una unidad es multiplicar por el elemento inverso $\frac{a}{u}=au^{-1}$. Los elementos $1$ y $-1$ son siempre unidades (no necesariamente distintas) cuyos inversos son ellos mismos. El subconjunto $R^{\times}\subset R$ formado por las unidades de un anillo $R$ es un grupo con la multiplicación. 
 \End{remark}

\Begin{exercise} 
Intenta calcular las unidades de los ejemplos de anillos vistos hasta ahora. ¿Puede el cero ser una unidad? 
 \End{exercise}




## Homomorfismos

Los homomorfismos de anillos son aplicaciones entre anillos que preservan la estructura, es decir, la suma, la multiplicación, el $0$ y el $1$.

\Begin{definition} 
Dados dos anillos $R$ y $S$, un **homomorfismo** $f\colon R\rightarrow S$ es una aplicación tal que, para todo $a,b\in R$, $$\begin{array}{rcl} f(a+b)&=&f(a)+f(b),\cr f(ab)&=&f(a)f(b),\cr f(0)&=&0,\cr f(1)&=&1.\end{array}$$ Un **isomorfismo** es un homomorfismo biyectivo. Un **automorfismo** es un isomorfismo de un anillo en sí mismo.
 \End{definition}


\Begin{remark} 
Los homomorfismos satisfacen $f(-a)=-f(a)$. Es más, si $u$ es una unidad entonces $f(u)$ también y $f(u^{-1})=f(u)^{-1}$. La identidad $\operatorname{id}_R\colon R\rightarrow R$ es un isomorfismo. Comprueba que si $$R\stackrel{f}\longrightarrow S\stackrel{g}\longrightarrow T$$ son homomorfismos entonces la composición $g\circ f\colon R\rightarrow T$ también. Lo mismo es cierto para isomorfismos. Es más, demuestra que si $f\colon R\rightarrow S$ es un isomorfismo entonces su aplicación inversa $f^{-1}\colon S\rightarrow R$ también. El símbolo $\cong$ se usará para denotar la relación de ser isomorfos $R\cong S$. Prueba que esta relación es de equivalencia. 
 \End{remark}


\Begin{example}\textrm{\normalfont (La inclusión)} 
Si $R$ es un anillo y $S\subset R$ es un subanillo, la **inclusión** $i\colon S\hookrightarrow R$, $i(a)=a$, es un homomorfismo. ¿Qué diferencia a la inclusión de la identidad?
 \End{example}

\Begin{example}\textrm{\normalfont (Las proyecciones)} 
Dados dos anillos $R$ y $S$, la proyección sobre la primera coordenada $p_1\colon R\times S\rightarrow R$, $p_1(r,s)=r$, es un homomorfismo. También lo es la proyección sobre la segunda coordenada $p_2\colon R\times S\rightarrow S$, $p_2(r,s)=s$.
 \End{example}


\Begin{proposition} 
Dado un homomorfismo $f\colon R\rightarrow S$, su imagen $\operatorname{im} f\subset S$ es un subanillo. 
 \End{proposition}


\Begin{proof} 

* $1=f(1)\in \operatorname{im} f$.

* $f(a)+f(b)=f(a+b)\in \operatorname{im} f$ para $a,b\in R$.

* $-f(a)=f(-a)\in \operatorname{im} f$ para todo $a\in R$.

* $f(a)f(b)=f(ab)\in \operatorname{im} f$ para todo $a,b\in R$.

 \End{proof}


\Begin{proposition}\label{factorimage} 
Dado un homomorfismo $f\colon R\rightarrow S$ y un subanillo $U\subset S$, si $\operatorname{im} f\subset U$ entonces $f$ factoriza de manera única a través de la inclusión, es decir, existe un único homomorfismo $g\colon R\rightarrow U$ tal que $f=i\circ g$, $$f\colon R\stackrel{g}\rightarrow U\stackrel{i}\hookrightarrow S.$$ 
 \End{proposition}


\Begin{proof} 
Si $f=i\circ g$ entonces tendríamos $$f(a)=(i\circ g)(a)=i(g(a))=g(a).$$ La unicidad de $g$ sería consecuencia de esta fórmula ya que fuerza su definición. Definimos pues la aplicación $g\colon R\rightarrow U$ como $g(a)=f(a)$. Tiene sentido porque $\operatorname{im}f\subset U$. La aplicación $g$ es un homomorfismo pues está definida por la misma fórmula que el homomorfismo $f$.  
 \End{proof}


\Begin{remark} 
 En la proposición anterior podemos siempre tomar $U=\operatorname{im} f$. 
 \End{remark}


\Begin{example}\textrm{\normalfont (La evaluación)} 
Dado un anillo $R$ y $a\in R$ está definido el homomorfismo de **evaluación** $ev_a\colon R[x]\rightarrow R$ como $ev_a(p(x))=p(a)$. Define análogamente homomorfismos de evaluación en los anillos de polinomios en varias variables $R[x_1,\dots, x_n]$, de series convergentes $R\\{x\\}$ y de funciones $R^X$ y $\mathcal C(X)$ definidos arriba.
 \End{example}


Los anillos de polinomios satisfacen una propiedad universal relacionada con los homomorfismos de evaluación.

\Begin{theorem}\textrm{\normalfont (Principio de sustitución)} 
Dado un homomorfismo de anillos $f\colon R\rightarrow S$ y un elemento $c\in S$ existe un único homomorfismo $g\colon R[x]\rightarrow S$ tal que la restricción de $g$ a $R$ es $f$ y $g(x)=c$.
 \End{theorem}


\Begin{proof} 

Dado $p(x)=a_nx^n+\cdots+ a_1x+ a_0\in R[x]$, si tal $g\colon R[x]\rightarrow S$ existiera, $$
\begin{array}{rl}
g(p(x))&=g(a_nx^n+\cdots+a_1x+ a_0)\cr
&=g(a_n)g(x)^n+\cdots+ g(a_1)g(x)+g(a_0)\cr 
&=f(a_n)c^n+\cdots+ f(a_1)c+f(a_0).
\end{array}
$$
Definimos pues
$$
g(p(x))=f(a_n)c^n+\cdots+ f(a_0).
$$
Es tedioso pero trivial comprobar $g$ así definido es un homomorfismo. El cálculo anterior demuestra la unicidad.
 \End{proof}


\Begin{corollary} 
Dado un homomorfismo de anillos $f\colon R\rightarrow S$ y elementos $c_1,\dots, c_n\in S$ existe un único homomorfismo $g\colon R[x_1,\dots,x_n]\rightarrow S$ tal que la restricción de $g$ a $R$ es $f$ y $g(x_i)=c_i$, $1\leq i\leq n$.
 \End{corollary}


\Begin{proof} 

Por inducción en $n$.

Para $n=1$, la existencia y unicidad de $g\colon R[x_1]\rightarrow S$ es consecuencia del teorema anterior.

Veamos que $n-1\Rightarrow n$. Suponiendo que hay un único homomorfismo $h\colon R[x\_1,\dots,x\_{n-1}]\rightarrow S$ que se restringe a $f\colon R\rightarrow S$ sobre las constantes y satisface $g(x_i)=c_i$, $1\leq i\leq n-1$, aplicamos el teorema anterior a $$R[x\_1,\dots,x\_n]=(R[x\_1,\dots,x\_{n-1}])[x\_n]$$ y obtenemos el homomorfismo buscado.  
 \End{proof}


El anillo de los enteros cumple la siguiente curiosa propiedad, que en términos categóricos se denomina ser *inicial* en la categoría de los anillos.

\Begin{proposition} 
Para todo anillo $R$ existe un único homorfismo $f\colon \mathbb Z\rightarrow R$. 
 \End{proposition}


\Begin{proof} 
Cualquier homomorfismo $f\colon \mathbb Z\rightarrow R$ satisface $f(0)=0$ y $f(1)=1$. Por tanto, si $n>0$ en $\mathbb Z$,
$$\begin{array}{rcl}
f(n)&=&f(1+\stackrel{n}{\cdots}+1)\cr&=&f(1)+\stackrel{n}{\cdots}+f(1)\cr&=&1+\stackrel{n}{\cdots}+1,\cr
f(-n)&=&-f(n).
\end{array}$$
Es fácil comprobar que estas fórmulas definien un homomorfismo, que ha de ser único.  
 \End{proof}



## Ideales

Existe otro tipo destacado de subconjunto de un anillo que juega un papel más importante que los subanillos.

\Begin{definition} 
Dado un anillo $R$, un **ideal** $I\subset R$ es un subconjunto tal que:

* $0\in I$.

* $a+b\in I$ para todo $a,b\in I$.

* $-a\in I$ para todo $a\in I$.

* $ra\in I$ para todo $r\in R$ y $a\in I$.

 \End{definition}

En $\mathbb Z$ los números pares forman un ideal.


\Begin{remark} 
Un ideal $I\subset R$ es un subgrupo para la suma. Si $a_1,\dots,a_n\in I$ y $r_1,\dots, r_n\in R$ entonces la **combinación lineal** $r_1a_1+\cdots+r_na_n\in I$. Todo anillo posee al menos el ideal **total** $R\subset R$ y el **trivial** $\\{0\\}\subset R$. Además, si $R$ no es el anillo trivial, el ideal total es distinto del trivial.
 \End{remark}

\Begin{proposition} 
El **núcleo** de un homomorfismo $f\colon R\rightarrow S$, $$\ker f=\\{a\in R\;|\;f(a)=0\\},$$ es un ideal $\ker f\subset R$.
 \End{proposition}


\Begin{proof} 


* $0\in\ker f$ pues $f(0)=0$.

* Si $a,b\in\ker f$ entonces $a+b\in \ker f$ puesto que $f(a+b)=f(a)+f(b)=0+0=0$.

* Si $a\in\ker f$ entonces $-a\in \ker f$ puesto que $f(-a)=-f(a)=0$.

* Si $a\in\ker f$ y $r\in R$ entonces $ra\in \ker f$ pues $f(ra)=f( r )f(a)=f( r )0=0$.
 
 \End{proof}

Por tanto, en $R[x]$, los polinomios $f(x)$ tales que $f(1)=0$ forman un ideal pues constituyen el núcleo del homomorfismo de evaluación en $1\in R$. De hecho podríamos evaluar en cualquier otro elemento de $R$. También podríamos reemplazar $R[x]$ por otro de los anillos de funciones antes vistos.


\Begin{remark} 
 Como ocurre con los grupos, un homomorfismo de anillos $f\colon R\rightarrow S$ es inyectivo si y solo si $\ker f=\\{0\\}$. De otro modo, la inyectividad de $f$ equivale a que si $a\in R$ es tal que $f(a)=0$ entonces $a=0$.
 \End{remark}

\Begin{exercise} 
Dados dos anillos $R$ y $S$, ¿es $R\times\\{0\\}\subset R\times S$ un ideal? ¿Y $\\{0\\}\times S\subset R\times S$?
 \End{exercise}

Definimos ahora el ideal generado por un conjunto de elementos de un anillo, que es el menor ideal que los contiene.

\Begin{definition}\label{generators} 
El **ideal generado por** un conjunto finto de elementos $a_1,\dots,a_n\in R$ está formado por todas las combinaciones lineales de los generadores con coeficientes en el anillo:  $$(a_1,\dots,a_n)=\\{r_1a_1+\dots+r_na_n\;|\; r_1,\dots,r_n\in R\\}\subset R.$$ Un **ideal principal** es uno que está generado por un único elemento $(a)=\\{ra\,|\, r\in R\\}$ y que por tanto está formado por sus múltiplos. 
 \End{definition}

En $\mathbb Z$, el ideal de los números pares es $(2)$.


\Begin{exercise} 
Comprueba que $(a_1,\dots,a_n)$ es en efecto un ideal. Observa que $a_1,\dots,a_n\in (a_1,\dots, a_n)$. Es más, demuestra que si $I\subset R$ es un ideal y $a_1,\dots,a_n\in I$ entonces $(a_1,\dots,a_n)\subset I$. Intenta dar una definición razonable de ideal generado por un conjunto infinito de elementos que satisfaga las propiedades análogas al caso finito. 
 \End{exercise}


\Begin{proposition} 
Todos los ideales de $\mathbb Z$ son principales. Es más, todo ideal no nulo de $\mathbb Z$ está generado por cualquiera de sus elementos de valor absoluto mínimo.
 \End{proposition}


\Begin{proof} 

Sea $I\subset \mathbb Z$ un ideal. Si $I=\\{0\\}=(0)$ ya es principal. Si no, tomamos $a\in I$, $a\neq 0$, de valor absoluto mínimo. Veamos que $I=(a)$.

Por un lado $(a)\subset I$ pues $a\in I$.

Por otro, dado $b\in I$ realizamos la división euclídea de $b$ por $a$, $$b=ca+r.$$ El resto satisface $|r|<|a|$. Además $r=b-ca\in I$, por tanto $r=0$ y $b=ca\in (a)$.  
 \End{proof}

La demostración de la proposición anterior solo usa la noción de división euclídea, por tanto es válida no solo para $\mathbb Z$ sino para cualquier *dominio euclídeo* (noción conocida que repasaremos más adelante). La siguiente proposición destaca otro caso particular de interés.


\Begin{proposition} 
Dado un cuerpo $k$, todos los ideales de $k[x]$ son principales. Es más, todo ideal no nulo de $k[x]$ está generado por cualquiera de sus elementos de grado mínimo.
 \End{proposition}


Veamos ahora la relación entre ideales y unidades.

\Begin{proposition} 
Un ideal $I\subset R$ contiene una unidad $\Leftrightarrow$ $I=R$.
 \End{proposition}


\Begin{proof} 

$\Leftarrow$ Obvio porque $1\in R=I$ es una unidad.

$\Rightarrow$ Si $u\in I\subset R$ es una unidad, $u^{-1}\in R$ y por ser $I$ un ideal $1=uu^{-1}\in I.$

Si $1\in I$ y $a\in R$ entonces $1a=a\in I$, por tanto $R\subset I$, así que $I=R$.  
 \End{proof}


\Begin{corollary} 
Un anillo es un cuerpo $\Leftrightarrow$ tiene solo dos ideales (necesariamente el total y el trivial).
 \End{corollary}


\Begin{proof} 

$\Rightarrow$ Sea $k$ un cuerpo. Los cuerpos, en tanto que anillos no triviales, tienen al menos dos ideales: el trivial y el total. Si $I\subset k$ es un ideal no trivial entonces existe un elemento $a\in I\subset k$ no nulo. Como $k$ es un cuerpo este elemento ha de ser una unidad, así que $I=k$.

$\Leftarrow$ Sea $R$ un anillo cuyos dos únicos ideales son $\\{0\\}$ y $R$. En particular $R$ no es trivial. Sea $a\in R$ un elemento no trivial. Como $a\in (a)$, este ideal no puede ser el trivial, así que ha de ser el total $(a)=R$. Al ser $1\in R=(a)$ ha de existir un elemento $r\in R$ tal que $ra=1$, así que $a$ es una unidad.  
 \End{proof}


\Begin{corollary} 
Si $f\colon k\rightarrow R$ es un homomorfismo de anillos donde $k$ es un cuerpo y $R$ no es trivial entonces $f$ es inyectivo.
 \End{corollary}


\Begin{proof} 

El ser $f\colon k\rightarrow R$ un homomorfismo, $f(1)=1$. Como $R$ no es trivial, $1\neq 0$ luego $1\notin\ker f\subset k$ no puede ser el total. Por ser $k$ es un cuerpo la única opción posible es $\ker f=\\{0\\}$, luego $f$ es inyectivo.  
 \End{proof}



## Cocientes

\Begin{definition} 
Dado un anillo $R$ y un ideal $I\subset R$, el **anillo cociente** $R/I$ es el cociente de los grupos abelianos subyacentes dotado de la multiplicación $$(a+I)(b+I)=(ab)+I.$$
 \End{definition}


\Begin{remark} 
 Recordemos que $R/I=\\{a+I\,|\, a\in R\\}$ de modo que $a+I=b+I$ si y solo si $a-b\in I$. En particular $a+I=0+I$ si y solo si $a\in I$. El elemento $a+I$ del cociente se denomina **clase** de $a$ **módulo** $I$. Cuando el ideal $I$ se sobreentiende se escribe simplemente $$a+I=\bar a=[a].$$ La suma en el cociente se define como $(a+I)+(b+I)=(a+b)+I$. El cero y el uno en el cociente son $0+I$ y $1+I$. Comprueba que $R/R$ es el anillo trivial y $R/(0)\cong R$. Los cocientes $\mathbb Z/(n)$ son bien conocidos, $\bar a\in\mathbb Z/(n)$ es una unidad si y solo si $\operatorname{mcd}(a,n)=1$, luego $\mathbb Z/(n)$ es un cuerpo si y solo si $n$ es primo.
 \End{remark}


\Begin{theorem} 
El anillo cociente $R/I$ está bien definido. Su estructura es la única que hace que la **proyección natural** $p\colon R\twoheadrightarrow R/I$, $p(a)=a+I$, sea un homomorfismo. El núcleo de esta proyección es $\ker p=I$. 
 \End{theorem}


\Begin{proof} 

Para ver que la multiplicación está bien definida hay que comprobar que $$\left.\begin{array}{r}a+I=a'+I\cr b+I=b'+I\end{array}\right\\}\Rightarrow(ab)+I=(a'b')+I.$$ Esto equivale a $$\left.\begin{array}{r}a-a'\in I\cr b-b'\in I\end{array}\right\\}\Rightarrow ab-a'b'= (a-a')b+a'(b-b')\in I.$$ Las propiedades que el producto y la suma deben satisfacer se cumplen obviamente pues se derivan de las correspondientes propiedades de $R$.

Probemos la unicidad. Si $p\colon R\rightarrow R/I$ es un homomorfismo entonces
$$\begin{array}{rcl}
p(a+b)&=&p(a)+p(b),\cr p(ab)&=&p(a)p(b),
\end{array}$$
lo cual equivale a
$$\begin{array}{rcl}
(a+b)+I&=&(a+I)+(b+I),\cr (ab)+I&=&(a+I)(b+I).
\end{array}$$

El núcleo de la proyección natural es $$\ker p =\\{a\in R\;|\; p(a)=0\\},$$ pero $p(a)=a+I$ y $a+I=0+I$ si y solo si $a\in I$, luego $\ker p=I$.  
 \End{proof}


\Begin{proposition}\label{factorquotient} 
Dado un ideal $I\subset R$ y un homomorfismo $f\colon R\rightarrow S$ tal que $I\subset \ker f$, $f$ factoriza de manera única a través de la proyección natural, es decir existe un único homomorfismo $g\colon R/I\rightarrow S$ tal que $f=g\circ p$, $$f\colon R\stackrel{p}\twoheadrightarrow R/I\stackrel{g}\rightarrow S.$$
 \End{proposition}


\Begin{proof} 

Si $f=g\circ p$ entonces tendríamos $$f(a)=(g\circ p)(a)=g(p(a))=g(a+I).$$ Definimos la aplicación $g\colon R/I\rightarrow S$ como $$g(a+I)=f(a).$$ Veamos que en efecto está bien definida. La unicidad se seguirá de la primera fórmula.

Si $a+I=a'+I$ entonces $a-a'\in I\subset\ker f$ luego $$0=f(a-a')=f(a)-f(a').$$ Por tanto $$g(a+I)=f(a)=f(a')=g(a'+I).$$ Claramente $g$ es un homomorfismo pues se definie como el homomorfismo $f$ en los representantes.  
 \End{proof}


\Begin{remark} 
 En la proposición anterior podemos tomar siempre $I=\ker f$. 
 \End{remark}


\Begin{theorem}\textrm{\normalfont (Primer Teorema de Isomorfía)}\label{primer} 
Dado un homomorfismo $f\colon R\rightarrow S$, existe un único homomorfismo $\bar f\colon R/\ker f\rightarrow \operatorname{im}f$ tal que $f$ factoriza como $f=i\circ\bar f\circ p$, es decir, $f$ encaja en el siguente **diagrama conmutativo**, 

![Primer teorema de isomorfía](../../images/isomorfianillos.png)

 Aquí $p$ es la proyección natural e $i$ es la inclusión. Además $\bar f$ es un isomorfismo.
 \End{theorem}


\Begin{proof} 
[Por un lado](#factorimage) podemos factorizar $f\colon R\rightarrow S$ de manera única como $f=i\circ g$, $$f\colon R\stackrel{g}\rightarrow \operatorname{im} f\stackrel{i}\hookrightarrow S,$$ donde $g(a)=f(a)$. En particular $$\ker g = \ker f.$$

[Por otro lado](#factorquotient) podemos factorizar $g\colon R\rightarrow \operatorname{im} f$ de manera única como $g=\bar f\circ p$, $$g\colon R\stackrel{p}\twoheadrightarrow R/\ker f\stackrel{\overline{f}}\rightarrow \operatorname{im} f,$$ donde $\bar f(\bar{a})=g(a)=f(a)$. 

Por tanto $f=i\circ g= i\circ(\overline{f}\circ i)$, como queríamos. La unicidad de $\bar f$ se deduce de esta fórmula, ya que fuerza su definición:
$$
\begin{array}{rcl}
f(a)&=&(i\circ\bar f\circ p)(a)\cr
&=&i(\bar{f}(p(a)))\cr
&=&i(\bar{f}(\bar{a}))\cr
&=&\bar{f}(\bar{a}).
\end{array}
$$

Veamos que $\bar f\colon R/\ker f\rightarrow \operatorname{im} f$ es un isomorfismo. Comenzamos probando que es inyectivo. Sea $\bar{a}\in R/\ker f$ tal que $\bar f(\bar{a})=0$. Como $\bar f(\bar{a})=f(a)$, deducimos que $a\in \ker f$, por lo que $\bar{a}=\bar{0}$.

Veamos que $\bar f\colon R/\ker f\rightarrow \operatorname{im} f$ es sobreyectiva. Dado $b\in\operatorname{im} f$ existe $a\in R$ tal que $f(a)=b$. Por tanto $\bar f(\bar{a})=f(a)=b$.  
 \End{proof}


\Begin{corollary} 
$\mathbb R[x]/(x^2+1)\cong\mathbb C$.
 \End{corollary}


\Begin{proof} 
Consideremos el homomorfismo $f\colon \mathbb R[x]\rightarrow\mathbb C$ definido por la inclusión $\mathbb R\subset\mathbb C$ y tal que $f(x)=i$. Este homomorfismo es sobreyectivo ya que dado $a+ib\in\mathbb C$, $f(bx+a)=a+ib$ por tanto $\operatorname{im} f =\mathbb C$. Basta ahora ver que $\ker f=(x^2+1)$. Como $\mathbb R$ es un cuerpo, es suficiente comprobar que $x^2+1\in\ker f$ pero $\ker f$ no posee ningún polinomio no trivial de grado $<2$. Claramente $f(x^2+1)=i^2+1=0$. Si $bx+a\in\mathbb{R}[x]$ es un polinomio no trivial entonces $f(bx+a)=a+ib$ es un número complejo no trivial, con lo que queda demostrado.
 \End{proof}


Concluimos con un estudio de los ideales de un anillo cociente.

\Begin{proposition} 
Sea $f\colon R\rightarrow S$ un homomorfismo. 

* Si $J\subset S$ es un ideal entonces $f^{-1}(J)\subset R$ también y además $\ker f\subset f^{-1}(J)$. 

* Si $I\subset R$ es un ideal y $f$ es sobreyectivo entonces $f(I)\subset S$ también es un ideal.

 \End{proposition}


\Begin{proof} 
Comenzamos por el primer apartado:

* $0\in f^{-1}(J)$ porque $f(0)=0\in J$.

* Si $a,b\in f^{-1}(J)$ es porque $f(a),f(b)\in J$, luego $f(a+b)=f(a)+f(b)\in J$ y por tanto $a+b\in f^{-1}(J)$.

* En el caso anterior también $f(-a)=-f(a)\in J$, así que $-a\in f^{-1}(J)$.

* Es más, dado $r\in R$,  $f(ra)=f( r )f(a)\in J$ luego $ra\in f^{-1}(J)$.

Además, como $\\{0\\}\subset J$, $\ker f=f^{-1}(\\{0\\})\subset f^{-1}(J)$.

En el segundo caso:

* $0=f(0)\in f(I)$ pues $0\in I$.

* Si $a,b\in I$ entonces $a+b\in I$ luego $f(a)+f(b)=f(a+b)\in f(I)$.

* En el caso anterior también $-a\in I$ luego $-f(a)=f(-a)\in f(I)$.

* Es más, dado $s\in S$, por ser $f$ sobreyectiva $s=f( r )$ para cierto $r\in R$, y como $ra\in I$ entonces $sf(a)=f( r )f(a)=f(ra)\in f(I)$.  

 \End{proof}


\Begin{theorem}\textrm{\normalfont (de correspondencia)} 
Dado un anillo $R$ y un ideal $I$, si $p\colon R\twoheadrightarrow R/I$ denota la proyección natural tenemos la siguiente biyección $$\begin{array}{rcl}\left\\{\text{ideales de }R\text{ que contienen a }I\right\\}&\longleftrightarrow& \left\\{\text{ideales de }R/I\right\\},\cr I'&\mapsto&p(I'),\cr p^{-1}(J)&\leftarrow&J.\end{array}$$
 \End{theorem}


\Begin{proof} 

La proyección natural es un homomorfismo sobreyectivo con núcleo $I$, por tanto las aplicaciones del enunciado están bien definidas por la proposición anterior. Veamos que una es inversa de la otra. La igualdad $p(p^{-1}(J))=J$ es cierta por ser $p$ sobreyectiva. En general $I'\subset p^{-1}(p(I'))$. Veamos que la otra inclusión es también cierta si $I\subset I'$. Dado $a\in p^{-1}(p(I'))$, $p(a)\in p(I')$ por tanto existe $b\in I'$ tal que $p(b)=p(a)$. Esto implica que $p(a-b)=p(a)-p(b)=0$, es decir, $a-b\in I\subset I'$, por tanto $a=b+(a-b)\in I'$. 
 \End{proof}





## Añadir elementos a un anillo

La siguiente definición nos da una receta para añadir nuevos elementos a un anillo contenido en otro mayor.

\Begin{definition} 
Dado un anillo $S$, un subanillo $R\subset S$ y $s\in S$, el menor subanillo $R[s]\subset S$ que contiene a $R$ y a $s$ es la imagen del homomorfismo $g\colon R[x]\rightarrow S$ definido como la inclusión $i\colon R\hookrightarrow S$ sobre $R$ tal que $g(x)=s$, $R[s]=\operatorname{im} g$.
 \End{definition}


\Begin{remark} 
La propiedad de ser el menor viene dada porque todo elemento de $R[s]$ se puede expresar (aunque no de manera única) como $a_ns^n+\cdots+a_1s+a_0$ para ciertos $a_i\in R$. Por tanto, si $U\subset S$ es un subanillo tal que $R\subset U$ y $s\in U$ entonces $R[s]\subset U$. En particular $\mathbb R[i]=\mathbb C$ y $\mathbb Z[i]\subset\mathbb C$ son los enteros de Gauss. 
 \End{remark}

\Begin{exercise} 
Da una definición directa del menor subanillo $R[s_1,\dots,s_n]\subset S$ que contiene a varios elementos $s_i\in S$. 
 \End{exercise}

También podemos añadir nuevos elementos a un anillo $R$ de manera abstracta, es decir, sin tener previamente otro anillo mayor. El propio anillo de polinomios $R[x]$ consiste en añadirle un nuevo elemento $x$ a $R$ de manera libre. Veamos cómo añadir elementos que satisfagan ecuaciones.

Dado un polinomio $p(x)=a\_nx^n+\cdots + a_1x+ a\_0\in R[x]$, consideramos el anillo $S=R[x]/(p(x))$. Por abuso de notación, la clase de una constante $a\in R$ en $S$ se denotará igual, $a\in S$, no $\bar a$. En este nuevo anillo $\bar x\in S$ es una raíz de $p(x)$ puesto que

$$ p(\bar{x})=a_n\bar x^n+\cdots + a_1 \bar x+ a_0=\overline{p(x)}=\bar 0\in S.$$

Este anillo posee en ciertos casos una descripción similar a la de los números complejos.

Para demostrarlo usaremos el siguiente resultado que asegura que en $R[x]$ siempre podemos dividir por un polinomio mónico del modo habitual.

\Begin{lemma} 
Dado un polinomio **mónico** $p(x)=x^n+\cdots + a_1x+ a\_0\in R[x]$ 
y otro polinomio cualquiera $f(x)\in R[x]$, existen dos únicos polinomios  
$c(x), r(x)\in R[x]$ tales que $r(x)$ tiene grado $<n$ y $f=c\cdot p+r$. 
 \End{lemma}


\Begin{proof} 
Sea $f\_0=f$. Si grado $f_0<n$ entonces podemos tomar $c=0$ y $r=f_0$. Veamos ahora cómo proceder si grado $f_0\geq n$. En este caso existen polinomios $c\_1,f\_1\in R[x]$ tales que grado $f\_1<$ grado $f\_0$ y $f\_0=c\_1\cdot p + f\_1$. En efecto, si $f\_0=b\_mx^m+\cdots$ tiene grado  $m\geq n$ podemos tomar $c_1(x)=b\_mx^{m-n}$, que tiene sentido pues estamos suponiendo que $m\geq n$. Si el grado de $f\_1$ sigue siendo $\geq n$,  podemos aplicar el mismo razonamiento a $f\_1$ obteniendo así polinomios $c\_2,f\_2\in R[x]$ tales que grado $f\_2<$ grado $f\_1$ y $f\_1=c\_2\cdot p + f\_2$. Podemos continuar
$$
\begin{array}{rcl}
f\_0&=&c\_1\cdot p + f\_1,\cr
&\vdots&\cr
f\_{i-1}&=&c\_i\cdot p + f\_i,
\end{array}
$$
hasta que grado $f_i<n$. De este modo
$$f=(c\_1+\cdots+c\_i)\cdot p+f\_i$$
y podemos tomar $c=c\_1+\cdots+c\_i$ y $r=f\_i$. Hemos probado la existencia.

Veamos la unicidad de $r$. Si $f=c\cdot p+r=c'\cdot p+r'$ en las condiciones del enunciado, tenemos entonces que $r-r'=(c'-c)\cdot p$. Por un lado $r-r'$ tiene grado $<n$. Supongamos por reducción al absurdo que $c'\neq c$. Entonces $c'-c=e\_kx^k+\cdots$ para cierto $k\geq 0$ y $e\_k\in R$ no nulo. Esto implica que $(c'-c)\cdot p=e\_kx^{k+n}+\cdots$ y por tanto tendría grado $\geq n$. Hemos llegado a una contradicción, así que $c=c'$, luego también $r=r'$.
 \End{proof}

\Begin{corollary}\label{uniquerep} 
Dado un polinomio mónico $p(x)=x^n+\cdots + a\_1x+ a\_0\in R[x]$ de grado $n$, todo elemento de $R[x]/(p)$ posee un único representante de grado $<n$. 
 \End{corollary}


\Begin{proof} 
En efecto, dado $[f]\in R[x]/(p)$, $r\in R[x]$ es un representante de $[f]$ si y solo si $f-r\in (p)$, lo que equivale a la existencia de $c\in R[x]$ tal que $f-r=c\cdot p$, es decir, $f=c\cdot p+r$. Este resultado se deduce por tanto del lema anterior.
 \End{proof}

\Begin{remark} 
El corolario anterior nos dice que, bajo sus condiciones, todo elemento de $R[x]/(p)$ se puede escribir de manera única como $$b\_{n-1}\bar{x}^{n-1}+\cdots+ b\_1\bar{x}+b\_0,$$ donde $b\_0,\dots, b\_{n-1}\in R$.

En particular, si $n\geq 1$, el homomorfismo $R\hookrightarrow R[x]/(p)\colon r\mapsto\bar{r}$ que envía cada constante a la clase del correspondiente polinomio constante es inyectivo. Por ello, en adelante eliminaremos la barra de las clases de los polinomios constantes y las denotaremos simplemente $r$. De este modo podemos ver $R$ como un subanillo $R\subset R[x]/(p)$. Esto refuerza la idea de que este cociente *añade* elementos a $R$.
 \End{remark}

En adelante, cuando hablemos de añadirle a un anillo $R$ una raíz $\alpha$ de un polinomio $p(x)\in R[x]$ de manera abstracta nos estaremos refiriendo al cociente $R[x]/(p)$ y a $\alpha=\bar{x}$, que como hemos visto es una raíz de $p(x)$ en este anillo. Si $p$ es mónico de grado $n$, todo elemento de $R[x]/(p)$ se escribe de manera única como $b\_{n-1}\alpha^{n-1}+\cdots+ b\_1\alpha+b\_0$, con $b\_0,\dots, b\_{n-1}\in R$.

Es posible añadir a un anillo de manera abstracta no solo uno sino varios elementos que satisfagan determinadas ecuaciones. Se puede hacer tanto de manera directa como inductiva. Prueba a hacerlo como ejericio.


\Begin{example}\textrm{\normalfont ($\mathbb Z[x]/(x^3+3x+1)$)} 
Todo elemento de este anillo se puede expresar de manera única como $a_2 \bar x^2+ a_1 \bar x+ a_0$ para ciertos coeficientes $a_0,a_1,a_2\in\mathbb Z$. La suma se calcula sumando coeficientes. El producto es más complejo porque suele ser necesario reducir el grado del representante obtenido. Esto se hace usando que $\bar x$ es una raíz del denominador. Concretamente en este caso $\bar x^3+3\bar x+1=0$, luego $$\begin{array}{rcl}\bar x^3&=& -3\bar x-1,\cr \bar x^4&=& -3\bar x^2-\bar x,\cr\bar x^5&=& -3\bar x^3-\bar x^2\cr&=& -3(-3\bar x-1)-\bar x^2\cr&=&-\bar x^2+9\bar x+3,\cr\bar x^6&=&\dots\end{array}$$Usamos esto en el siguiente ejemplo de cálculo,$$\begin{array}{rcl}(- \bar x^2+ \bar x+ 2)(\bar x+ 1)&=& -\bar x^3+3\bar x+2\cr&=& -(-3\bar x-1)+3\bar x+2\cr&=&6\bar x+3.\end{array}$$
 \End{example}


\Begin{example}\textrm{\normalfont ($(\mathbb Z/(4))[x]/(2x^2-1)$)} 
En este anillo la posible generalización del corolario anterior es totalmente falsa. En efecto, aquí $2=0$ ya que $0=2(2\bar x^2-1)=4\bar x^2-2=2$ pues $4=0$ en $\mathbb Z/4$. Además $\bar x^2$ no se puede expresar como la clase de un polinomio de grado ${<}2$ porque, si se pudiera, entonces el ideal $(2x^2-1)\subset (\mathbb Z/(4))[x]$ tendría polinomios mónicos de grado $2$, pero no tiene.
 \End{example}


## Dominios y fracciones 

\Begin{definition} 
Dado un anillo $R$, un **divisor de cero** es un elemento $a\in R$ no nulo, $a\neq 0$, tal que existe otro $b\in R$, $b\neq 0$, de modo que $ab=0$. Un anillo no trivial $R$ es un **dominio (de integridad)** si no posee divisores de cero.
 \End{definition}


\Begin{remark} 
Dicho de otro modo, $R$ es un dominio cuando dados $a,b\in R$ tales que $ab=0$ entonces $a=0$ o $b=0$. Los dominios poseen la **propiedad cancelativa**, es decir, si $ab=ac$ y $a\neq 0$ entonces $b=c$ ya que esto equivale a $a(b-c)=0$. Los cuerpos $k$ y los enteros $\mathbb Z$ son dominios. Los subanillos de un dominio también son dominios. El anillo $\mathbb Z/(6)$ no es un dominio porque aquí $2\cdot 3=6=0$ pero $2\neq 0\neq 3$.
 \End{remark}


\Begin{proposition} 
Si $R$ es un dominio entonces $R[x]$ también.
 \End{proposition}


\Begin{proof} 
Dados dos polinomios no nulos $p(x)=a_nx^n+\cdots$ y $q(x)=b_mx^m+\cdots$ de grados respectivos $n$ y $m$ ($a_n\neq 0\neq b_m$), su producto $p(x)q(x)=a_nb_mx^{n+m}+\cdots$ es no nulo de grado $n+m$ ya que $a_nb_m\neq 0$ por ser $R$ un dominio.
 \End{proof}


\Begin{corollary} 
Si $R$ es un dominio entonces $R[x_1,\dots, x_n]$ también.
 \End{corollary}


Cualquier subanillo de un cuerpo es un dominio. Veamos que, recíprocamente, todo dominio se puede incluir en un cuerpo.

\Begin{definition} 
Dado un dominio $R$, su **cuerpo de fracciones** $Q( R )$ es el cociente del conjunto $$\left\\{\frac{a}{b}\;\bigg|\; a,b\in R,\,b\neq 0\right\\}$$ por la relación de equivalencia $$\frac{a}{b}\sim\frac{a'}{b'}\Leftrightarrow ab'=a'b$$ dotado de las operaciones $$\begin{array}{rcl}\displaystyle \frac{a}{b}+\frac{c}{d}&\displaystyle =&\displaystyle  \frac{ad+bc}{bd},\cr\displaystyle \frac{a}{b}\cdot\frac{c}{d}&\displaystyle =&\displaystyle \frac{a c}{b d}.\end{array}$$
 \End{definition}

El ejemplo principal es $Q(\mathbb Z)=\mathbb Q$.

\Begin{proposition} 
El cuerpo de fracciones $Q( R )$ de un dominio $R$ está bien definido. La aplicación $i\colon R\rightarrow Q( R )$, $i(a)=\frac{a}{1}$, es un homomorfismo inyectivo. Todo homomorfismo inyectivo $f\colon R\rightarrow k$ donde $k$ es un cuerpo factoriza de manera única a través de $i$, es decir, existe un único homomorfismo $g\colon Q( R )\rightarrow k$ tal que $f=g\circ i$, $$f\colon R\stackrel{i}\rightarrow Q( R )\stackrel{g}\rightarrow k.$$
 \End{proposition}


\Begin{proof} 
La relación es simétrica y reflexiva porque el producto en $R$ es conmutativo. Veamos la transitividad. Si $$\displaystyle \frac{a}{b}\sim \frac{a'}{b'}\sim \frac{a''}{b''}$$ entonces 
$$\begin{array}{rcl}
ab'&=&a'b,\cr 
a'b''&=&a'' b'.
\end{array}$$ 
En particular, 
$$\begin{array}{rcl}
(a b'') b'&=&(ab')b''\cr
&=&(a'b)b''\cr
&=&(a'b'')b\cr
&=&(a'' b')b\cr
&=&(a'' b)b'.
\end{array}$$
Por la propiedad cancelativa de los dominios, $ab''=a'' b$, es decir $\frac{a}{b}\sim \frac{a''}{b''}$. Por tanto el conjunto cociente $Q( R )$ está bien definido. Demostrar que las definiciones de la suma y la multiplicación en $Q(R)$ no dependen de la elección de fracciones representantes es laborioso pero trivial, no es distinto de la construcción clásica de los números racionales. También es fácil probar que los axiomas que definen los anillos se verifican. Obviamente el cero y el uno de $Q( R )$ son $\frac{0}{1}$ y $\frac{1}{1}$, respectivamente. Por tanto una fracción $\frac{a}{b}$ es nula $\Leftrightarrow$ $a=0$. Si $\frac{a}{b}$ es no nula entonces es claramente una unidad y $(\frac{a}{b})^{-1}=\frac{b}{a}$, por lo que $Q( R )$ es un cuerpo.

Es inmediato ver que $i$ es un homomorfismo. Es inyectivo porque $a\in\ker f$ si y solo si $\frac{a}{1}=\frac{0}{1}$, lo cual equivale a $a=0$.

Dado $f\colon R\rightarrow k$ como en el enunciado, si existiera una descomposición $f=g\circ i$ entonces tendríamos que
$$f(a)=(g\circ i)(a)=g(i(a))=g\left(\frac{a}{1}\right).$$
Toda fracción de $Q( R )$ se puede descomponer como
$$\frac{a}{b}=\frac{a}{1}\cdot\frac{1}{b}=\frac{a}{1}\left(\frac{b}{1}\right)^{-1},$$
por tanto tendríamos que
$$g\left(\frac{a}{b}\right)=g\left(\frac{a}{1}\left(\frac{b}{1}\right)^{-1}\right)=g\left(\frac{a}{1}\right)g\left(\frac{b}{1}\right)^{-1}=f(a)f(b)^{-1}.$$
Esto demuestra que, caso de existir, $g$ sería único.

Ahora basta definir $g\colon Q( R )\rightarrow k$ como $g\left(\frac{a}{b}\right)=f(a)f(b)^{-1}$. Esta definición tiene sentido porque, como $b\neq 0$ y $f$ es inyectivo, $f(b)\neq 0$, y al ser $k$ un cuerpo todo elemento no nulo tiene inverso, luego $f(b)^{-1}$ existe. Con esta definición es un ejercicio comprobar que $g$ es un homomorfismo.  
 \End{proof}

\Begin{corollary} 
Dado un homomorfismo inyectivo entre dominios $f\colon R\rightarrow S$, existe un único homomorfismo entre sus cuerpos de fracciones $g\colon Q( R )\rightarrow Q(S)$ que extiende $f$, en el sentido de que el siguiente cuadrado es conmutativo

![Cuerpos de fracciones](../../images/fractionfield.png)

es decir, $g\circ i_R=i_S\circ f$, donde $i_R$ e $i_S$ son las inclusiones de $R$ y $S$ en sus cuerpos de fracciones.
 \End{corollary}

\Begin{proof} 
Basta aplicar la proposición anterior a $i_S\circ f\colon R\rightarrow Q(S)$, que es inyectivo por ser composición de inyectivos. El homomorfismo $g$ estará por tanto definido como $g\left(\frac{a}{b}\right)=\frac{g(a)}{g(b)}$.
 \End{proof}


\Begin{definition} 
Dado un cuerpo $k$, el **cuerpo de funciones racionales** en una variable se define como $k(x)=Q(k[x])$.
 \End{definition}


\Begin{exercise} 
Da dos definiciones del cuerpo de funciones racionales en varias variables $k(x_1,\dots,x_n)$, una inductiva y otra directa, que sean aparentemente distintas pero isomorfas.
 \End{exercise}


\Begin{definition} 
Los ideales distintos del total se denominan **propios**. Un ideal $I\subsetneq R$ es **primo** si dados $a,b\in R$ tales que $ab\in I$ entonces $a\in I$ o $b\in I$.
 \End{definition}


\Begin{remark} 
Un ideal $I\subset R$ es propio si y solo si $R/I$ no es trivial. Si $p\in\mathbb Z$ es un primo entonces el ideal $(p)\subset \mathbb Z$ es primo ya que si $ab\in (p)$ es porque $p$ divide a $ab$, luego $p$ ha de dividir a $a$ o a $b$, es decir $a\in(p)$ o $b\in(p)$. En general $(0)\subset R$ es primo si y solo si $R$ es un dominio.
 \End{remark}


\Begin{proposition} 
Un ideal $I\subset R$ es primo $\Leftrightarrow$ $R/I$ es un dominio.
 \End{proposition}


\Begin{proof} 

Ser un ideal propio se corresponde con tener un cociente no trivial. Veamos la equivalencia del resto de propiedades.

$\Rightarrow$ Dados $\bar a,\bar b\in R/I$, si $\bar a\bar b =\overline{ab}=\bar 0$ entonces $ab\in I$, luego $a\in I$ o $b\in I$, es decir $\bar a=\bar 0$ o $\bar b=\bar 0$.

$\Leftarrow$ Dados $a,b\in R$, si $ab\in I$ entonces $\bar a\bar b=\overline{ab}=\bar 0$, luego $\bar a=\bar 0$ o $\bar b=\bar 0$, es decir $a\in I$ o $b\in I$.
 
 \End{proof}


\Begin{definition} 
Un ideal $I\subsetneq R$ es **maximal** si los únicos ideales que lo contienen son el total $R$ y el propio $I$.
 \End{definition}


\Begin{remark} 
De otro modo, no puede existir ningún ideal $J$ tal que $I\subsetneq J\subsetneq R$. Todo anillo no trivial posee al menos un ideal maximal. ¿Cuál es en el caso de los cuerpos?
 \End{remark}


\Begin{proposition} 
Un ideal $I\subset R$ es maximal $\Leftrightarrow$ $R/I$ es un cuerpo.
 \End{proposition}


\Begin{proof} 
Recordemos que un cuerpo es un anillo no trivial con dos ideales. El anillo $R/I$ es no trivial si y solo si $I\subsetneq R$, que es la primera condición de maximalidad. Es más $R/I$ tiene solo dos ideales si y solo si solo hay dos ideales de $R$ que contengan a $I$ (necesariamente el total y el propio $I$). Esta es la segunda condición de maximalidad.  
 \End{proof}


\Begin{corollary} 
Todo ideal maximal es primo.
 \End{corollary}


\Begin{definition} 
Un **dominio de ideales principales** (también **DIP** o **PID**) es un dominio donde todos los ideales son principales.
 \End{definition}

Son dominios de ideales principales $\mathbb Z$ y $k[x]$ si $k$ es un cuerpo.



\Begin{proposition} 
En un dominio de ideales principales $R$ todos los ideales primos no nulos son maximales.
 \End{proposition}


\Begin{proof} 

Supongamos que $(a)\subset (b)\subset R$, con $(a)$ primo y $a\neq0$. Entonces $a=cb$ para cierto $c\in R$. En particular $cb\in (a)$, que es primo, luego $c\in (a)$ o $b\in (a)$.

Si $b\in (a)$ entonces $(b)\subset (a)$, luego $(a)=(b)$.

Si $c\in (a)$ entonces $c=da$ para cierto $d\in R$, por tanto $a=dab=dba$. Por la propiedad cancelativa $db=1$, así que $b$ es una unidad, luego $(b)=R$. 
 \End{proof}


\Begin{example}\textrm{\normalfont (Ideales maximales y geometría)} 
Dado un cuerpo $k$, todo punto $\mathbf{a}=(a\_1,\dots,a\_n)\in k^n$ del espacio afín $n$-dimensional define un ideal maximal de $k[x\_1,\dots,x\_n]$, $$I_{\mathbf{a}}=(x\_1-a\_1,\dots,x\_n-a\_n).$$ Es en efecto maximal porque es el núcleo del homomorfismo sobreyectivo de evaluación $$\begin{array}{rcl} k[x\_1,\dots,x\_n]&\longrightarrow& k,\cr p(x\_1,\dots,x\_n)&\mapsto&p(a\_1,\dots,a\_n). \end{array}$$ Por tanto $k[x\_1,\dots,x\_n]/I_{\mathbf{a}}\cong k$ es un cuerpo por el primer teorema de isomorfía. El **Teorema de los Ceros de Hilbert** dice que si $k=\mathbb C$ o cualquier otro cuerpo algebraicamente cerrado, entonces estos son los únicos ideales maximales de $k[x\_1,\dots,x\_n]$, con lo que tendríamos una biyección, $$\\{\text{Ideales maximales de }k[x\_1,\dots,x\_n]\\}\longleftrightarrow k^n.$$ Como consecuencia de esto y de la caracterización de ideales de un cociente deducimos que si $X\subset k^n$ es el conjunto de soluciones de unas ecuaciones polinómicas, $p_i(x\_1,\dots,x\_n)\in k[x\_1,\dots,x\_n]$, $1\leq i\leq m$, $$X\colon\left\\{ \begin{array}{c} p_1(x\_1,\dots,x\_n)=0,\cr \vdots\quad\cr p_m(x\_1,\dots,x\_n)=0, \end{array} \right.$$ entonces tenemos una biyección $$\\{\text{Ideales maximales de }k[x\_1,\dots,x\_n]/(p_1,\dots,p_m)\\}\longleftrightarrow X.$$ El álgebra del anillo cociente $k[x\_1,\dots,x\_n]/(p_1,\dots,p_m)$ no solo captura el conjunto de puntos de $X$ sino toda su geometría. Por desgracia, otros resultados más precisos al respecto se escapan del alcance de la asignatura.
 \End{example}


\Begin{example}\textrm{\normalfont (Ideales maximales, análisis y topología)} 
Dado un espacio topológico compacto de Hausdorff $X$, denotamos $\mathcal C(X)$ al anillo de funciones continuas $X\rightarrow \mathbb C$. Cualquier punto $x\in X$ define un homomorfismo sobreyectivo $$\begin{array}{rcl} ev_x\colon\mathcal C(X)&\longrightarrow& \mathbb C,\cr f&\mapsto&f(x), \end{array}$$ cuyo núcleo $\ker ev_x\subset\mathcal C(X)$ es un ideal maximal por el primer teorema de isomorfía. La **Teoría de Representación de Gelfand** dice que todos los ideales maximales de $\mathcal C(X)$ son de esta forma, con lo que tenemos una biyección $$\\{\text{Ideales maximales de }\mathcal C(X)\\}\longleftrightarrow X.$$ Esta correspondencia da lugar a una equivalencia de categorías entre los espacios compactos de Hausdorff y las $C^{\ast}$-álgebras conmutativas unitarias, que es una clase de anillos a la que $\mathcal C(X)$ pertenece. Esto permite estudiar la topología desde el punto de vista del álgebra y del análisis funcional. 
 \End{example}

