ocorrencia(Letra,[],0).
ocorrencia(Letra, [CAR|CDR],N) :-
	ocorrencia(Letra, CDR, N1),
	(
    	Letra == CAR
    	-> N is N1 + 1
    	;   N = N1
    ).

?- ocorrencia(b, [a, b, c, d, e], N), write(N), nl.
