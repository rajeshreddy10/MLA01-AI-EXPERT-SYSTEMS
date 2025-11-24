location(delhi, india).
location(paris, france).
stays(rahul, delhi).
stays(alice, paris).
state_of(P,S):stays(P,C),location(C,S).
```

Queries:

```prolog
? state_of(rahul, S).
? stays(X, C), location(C, S).
