## 1 dict to list  => ## unzip
dict is 2 array, one is uniq

    { k, ...  => v, ... }

=> 

    [(k,v), ...]


## list 2 index   => ## zip[k=1, 1:]

    [(v1, u1, ... ), (v2, u2, ...), ...]
    
=>
    
    {
        v1: [(u1, ..), (ux, ...)],  # duplication value set
        v2: (uy, ...)
    }
    
## move   => ##   sub.a => a

    {
        sub: {
            a: x
        },
        b: y
    }
    
=> 
    
    {
        a: x,
        b: y
    }
    
