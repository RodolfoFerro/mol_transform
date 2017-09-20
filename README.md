# mol_transform

Molecular transformations.

## How to use it

You can just simply run:
```
mol_transform.py -f C20.xyz -o test.xyz
```
This will open the `file` named `C20.xyz`, center the first coordinate into the origin and translate the rest of coordinates to mantain the structure.

If you want to translate it using a specific vector (a, b, c), you'll need to do:
```
mol_transform.py -f C20.xyz -o test2.xyz -t a b c
```

For example, if we have a position (2.063, -3.112, 4.005) and we want to translate it to the origin (and the rest of the positions), we would have to run:
```
mol_transform.py -f C20.xyz -o test2.xyz -t -2.063 3-112 -4.005
```
Observe that we need to inverse the signs of each value of the position, since we want a translation negative to that position.
