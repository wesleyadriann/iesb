fatorial(0,1).
fatorial(Numero,F) :-
   Numero > 0,
   Numero1 is Numero-1,
   fatorial(Numero1,F1),
   F is Numero * F1.

?- fatorial(5, N), write(N), nl.
