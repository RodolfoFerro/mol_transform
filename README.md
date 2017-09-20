# mol_transform

Molecular transformations.

## How to use it

You can just simply run:
```
mol_transform.py -f input.xyz -o output.xyz
```
The `-f` tag stands for `file` and will open the file named `input.xyz`, center the first position into the origin and translate the rest of positions to maintain the structure. The `-o` tag stands for `output`, meaning that you need to add the output path (in our example is `output.xyz`).

If you want to translate it using a specific vector (a, b, c), you'll need to do:
```
mol_transform.py -f input.xyz -o output.xyz -t a b c
```

For example, we have the position `(0.47050, -0.66520, -1.79270)` in our file `C20.xyz` and if we want to translate it to the origin (and the rest of the positions to maintain the structure), we would have to run:
```
mol_transform.py -f C20.xyz -o C20_translated.xyz -t -0.47050 0.66520 1.79270
```
**PLEASE OBSERVE** that we need to inverse the signs of each value of the position, since we want a translation negative to that position. Also, in this example we will create the file `C20_translated.xyz` with the translated positions.
