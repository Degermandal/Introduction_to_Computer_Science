% Prolog is a declarative programming language, because declarative
% programming refers to programming with recipe so you tell machine what
% you want, machine make the environment itself.


mother(X,Y):-
	female(X),
	parent(X,Y).
father(X,Y):-
	male(X),
	parent(X,Y).
brother(X,Y):-
	male(X),
	parent(Z,X),
	parent(Z,Y),
	X \= Y.
sister(X,Y):-
	female(X),
	parent(Z,X),
	parent(Z,Y),
	X \= Y.
daughter(X,Y):-
	female(X),
	parent(Y,X).
son(X,Y):-
	male(X),
	parent(Y,X).
grandmother(X,Y):-
	female(X),
	parent(X,Z),
	parent(Z,Y).
granfather(X,Y):-
	male(X),
	parent(X,Z),
	parent(Z,Y).
aunt(X,Y):-
	female(X),
	sibling(Z,X),
	parent(Z,Y).
uncle(X,Y):-
	male(X),
	sibling(Z,X),
	parent(Z,Y).

female(miyase).
female(ayse).
female(aydilek).
female(kezban).
female(bahriye).
female(gulden).
female(dilek).
female(deger).
female(ebru).
female(ferdane).
female(aysenur).

male(asim).
male(mustafa).
male(omer).
male(bulent).
male(halil).
male(ozal).
male(aydin).
male(arif).
male(arda).
male(muhammet).
male(hakan).

parent(miyase,aydilek).
parent(miyase,dilek).
parent(miyase,bulent).
parent(asim,aydilek).
parent(asim,dilek).
parent(asim,bulent).
parent(aydilek,ebru).
parent(aydilek,ferdane).
parent(omer,ebru).
parent(omer,ferdane).
parent(bulent,hakan).
parent(kezban,hakan).
parent(dilek,deger).
parent(dilek,arif).
parent(aydin,deger).
parent(aydin,arif).
parent(ayse,aydin).
parent(ayse,ozal).
parent(ayse,bahriye).
parent(mustafa,aydin).
parent(mustafa,ozal).
parent(mustafa,bahriye).
parent(ozal,muhammet).
parent(gulden,muhammet).
parent(bahriye,arda).
parent(bahriye,aysenur).
parent(halil,arda).
parent(halil,aysenur).

child(aydilek,miyase).
child(dilek,miyase).
child(bulent,miyase).
child(aydilek,asim).
child(dilek,asim).
child(bulent,asim).
child(ebru,aydilek).
child(ferdane,aydilek).
child(ebru,omer).
child(ferdane,omer).
child(hakan,bulent).
child(hakan,kezban).
child(deger,dilek).
child(arif,dilek).
child(deger,aydin).
child(arif,aydin).
child(aydin,ayse).
child(ozal,ayse).
child(bahriye,ayse).
child(aydin,mustafa).
child(ozal,mustafa).
child(bahriye,mustafa).
child(muhammet,ozal).
child(muhammet,gulden).
child(arda,bahriye).
child(aysenur,bahriye).
child(arda,halil).
child(aysenur,halil).

sibling(aydin,ozal).
sibling(ozal,bahriye).
sibling(bahriye,aydin).
sibling(arif,deger).
sibling(aydilek,dilek).
sibling(aydilek,bulent).
sibling(dilek,bulent).
sibling(ebru,ferdane).
sibling(aysenur,arda).







