q4(S) :-
    permutation([1,2,3,4], S),
    S = [A,B,C,D],
    abs(A-B) =\= 1,
    abs(A-C) =\= 2,
    abs(A-D) =\= 3,
    abs(B-C) =\= 1,
    abs(B-D) =\= 2,
    abs(C-D) =\= 1.


?- q4(S).

