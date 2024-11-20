% KB1
woman(mia).
woman(jody).
woman(yolanda).
playsAirGuitar(jody).
party.

% Queries for KB1
% ?- woman(mia).
% ?- playsAirGuitar(mia).
% ?- party.
% ?- concert.

% KB2
happy(yolanda).
listens2music(mia).
listens2music(yolanda) :- happy(yolanda).
playsAirGuitar(mia) :- listens2music(mia).
playsAirGuitar(yolanda) :- listens2music(yolanda).

% KB3
likes(dan, sally).
likes(sally, dan).
likes(john, brittney).
married(X, Y) :- likes(X, Y), likes(Y, X).
friends(X, Y) :- likes(X, Y); likes(Y, X).

% KB4
food(burger).
food(sandwich).
food(pizza).
lunch(sandwich).
dinner(pizza).
meal(X) :- food(X).

% KB5
owns(jack, car(bmw)).
owns(john, car(chevy)).
owns(olivia, car(civic)).
owns(jane, car(chevy)).
sedan(car(bmw)).
sedan(car(civic)).
truck(car(chevy)).
