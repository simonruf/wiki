# Lineare Gleichungssysteme

## Was sind Gleichungssysteme?

Gleichungssysteme sind mehrere Gleichungen, die gleichzeitig gelten sollen.
Nur so kann man Gleichungen mit mehrere unbekannten Variablen lösen.
Man muss so viele Gleichungen haben, wie es Unbekannte gibt.

## Was sind lineare Gleichungssysteme?

Lineare Gleichungssysteme sind Gleichungssysteme, die
aus [linearen Gleichungen](/mathematik/algebra/lineare-gleichungen/) bestehen.

> Beispiel:
> $$ \Big| \begin{matrix} 2x + 3y = 5 \\ 4x + 6y = 10 \end{matrix} \Big| $$

?> Die Striche links und rechts von der Gleichungen bedeuten, dass es sich um ein Gleichungssystem handelt und somit
die Variablen in beiden Gleichungen denselben Wert haben.

### Wie löst man lineare Gleichungen mit zwei Unbekannten?

Um lineare Gleichungssysteme mit zwei Unbekannten zu lösen, muss man mindestens zwei verschiedene Gleichungen haben.
Um diese nun zu lösen, gibt es verschiedene Methoden. Alle Verfahren funktionieren bei jedem Gleichungssystem, jedoch
kann es sein, dass manche Verfahren schneller sind als andere.

#### Das Gleichsetzungsverfahren

Als Erstes löst man beide Gleichungen nach derselben Variable auf.
Dann kann man die beiden Teile der Gleichungen gleichsetzen.
Um dann die andere Variable zu berechnen, muss man die Zahl in eine der beiden Gleichungen einsetzen.

> Beispiel:  
> Wir wollen dieses Gleichungssystem lösen:
> $$ \Big| \begin{matrix} x + y = 31 \\ \frac{x}{4} + \frac{y}{5} = 20 \end{matrix} \Big| $$
> Als Erstes lösen wir beide Gleichungen nach der Variable $x$ auf:
> $$ \Big| \begin{matrix} x = 31 - y \\ x = \frac{400 - 4y}{5} \end{matrix} \Big| $$
> Nun können wir die beiden Gleichungen gleichsetzen:
> $$ 31 - y = \frac{400 - 4y}{5} \tag*{| * 5} $$
> $$ 155 - 5y = 400 - 4y \tag*{| + 5y - 400} $$
> $$ - 245 = y $$
> Nun können wir die Variable $y$ in die erste Gleichung einsetzen:
> $$ x + y = 31 $$
> $$ x + (- 245) = 31 \tag*{| + 245} $$
> $$ x = 276 $$
> So haben wir nun die Lösung für $x$ und $y$:
> $$ \Big| \begin{matrix} x = 276 \\ y = - 245 \end{matrix} \Big| $$

#### Das Einsetzungsverfahren (Substitutionsverfahren)

Beim Einsetzungsverfahren wird eine der beiden Gleichungen in die andere eingesetzt.
Man löst eine der Gleichung nach einer Variable auf und setzt diese dann in die andere Gleichung ein, sodass dann in der
anderen Gleichung nur noch eine Variable übrig bleibt und man diese dann lösen kann.
Um dann die andere Variable auch noch herauszufinden, setzt man die berechnete Zahl in eine der Gleichungen ein.

?> Ob man die erste oder die zweite Gleichung in die andere einsetzt, ist egal.

> Beispiel:  
> Wir wollen dieses Gleichungssystem lösen:
> $$ \Big| \begin{matrix} x + y = 20 \\ \frac{x}{5} + \frac{y}{6} = 30 \end{matrix} \Big| $$
> Als Erstes lösen wir die erste Gleichung nach der Variable $x$ auf:
> $$ x = 20 - y $$
> Nun können wir Gleichung in die zweite Gleichung einsetzen, dass heisst das das $x$ in der zweiten Gleichung
> durch $20 - y$ ersetzt wird:
> $$ \frac{20 - y}{5} + \frac{y}{6} = 30 $$
> Da wir nun nur noch eine Variable haben, können wir die Gleichung nun normal lösen:
> $$ \frac{20 - y}{5} + \frac{y}{6} = 30 \tag*{| * 30} $$
> $$ 120 - 6y + 5y = 900 $$
> $$ 120 - y = 900 \tag*{| + y - 900} $$
> $$ - 780 = y $$
> Nun können wir die Variable $y$ in die erste Gleichung einsetzen:
> $$ x + y = 20 $$
> $$ x + (- 780) = 20 \tag*{| + 780} $$
> $$ x = 800 $$
> So haben wir nun die Lösung für $x$ und $y$:
> $$ \Big| \begin{matrix} x = 800 \\ y = - 780 \end{matrix} \Big| $$

#### Das Additionsverfahren

Beim Additionsverfahren werden die Gleichungen so multipliziert, dass eine der beiden Variablen in beiden Gleichungen
bei der Addition
beider Gleichungen verschwindet.

> Beispiel:  
> Wir wollen dieses Gleichungssystem lösen:
> $$ \Big| \begin{matrix} x + y = 5 \\ 4x + 6y = 10 \end{matrix} \Big| $$
> Wir wollen die Variable $x$ in beiden Gleichungen verschwinden lassen.  
> Dazu multiplizieren wir die erste Gleichung mit $-4$ und die zweite Gleichung mit $1$. Das ergibt:
> $$ \Big| \begin{matrix} - 4x - 4y = - 20 \\ 4x + 6y = 10 \end{matrix} \Big| $$
> Wenn wir nun beide Gleichungen addieren, verschwindet die Variable $x$:
> $$ -4x - 4y + 4x + 6y = -20 + 10 $$
> $$ 2y = -10 $$
> $$ y = -5 $$
> Nun können wir die Variable $y$ in die erste Gleichung einsetzen:
> $$ x + y = 5 $$
> $$ x + (- 5) = 5 \tag*{| + 5} $$
> $$ x = 10 $$
> So haben wir nun die Lösung für $x$ und $y$:
> $$ \Big| \begin{matrix} x = 10 \\ y = - 5 \end{matrix} \Big| $$