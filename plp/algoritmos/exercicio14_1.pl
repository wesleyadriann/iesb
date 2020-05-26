dobro([],[]).
dobro([CAR|CDR], [Novo_numero|Lista]) :-
    Novo_numero is CAR*2,
    dobro(CDR, Lista).

?- dobro([1, 2, 3, 4, 5], Lista), write(Lista), nl.
