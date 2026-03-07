# Parity check

You are given an n times n matrix of bits (0s and 1s).
A matrix has "Parity Property" if every row sum and every column sum is even.
Your goal is to categorize the matrix:
- OK: If the matrix already has the parity property.
- Change bit (i, j): If the parity property can be restored by flipping exactly one bit at coordinates $(i, j)$.
- Corrupt: If the matrix cannot reach the parity property by flipping only one bit.
