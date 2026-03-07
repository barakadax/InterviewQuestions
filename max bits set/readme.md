# Max bits set

Given an array of numbers you need to find the bit column with the most 1s,
for example `[13,8,2,7,3]`
You could use `AND` bitwise logic:

```shell
1, 1, 0, 1
1, 0, 0, 0
0, 0, 1, 0
0, 1, 1, 1
0, 0, 1, 1
----------
         3
```

Both the LSB and column to the left has three times 1 bits in them so your function should return 3
