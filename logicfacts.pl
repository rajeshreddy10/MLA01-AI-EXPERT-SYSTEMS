
```prolog
boy(jack).
child(X):boy(X);girl(X).
gets(X,train);gets(X,doll);gets(X,coal).
```

Queries:

```prolog
? child(jack).
? gets(jack, What).
