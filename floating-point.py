from decimal import Decimal

# Floating point numbers are not exact in Python
print(0.1 + 0.2)
# This is a workaround to get the exact result
print(round(0.1 + 0.2, 2))
# Using Decimal for exact decimal representation
print(Decimal('0.1') + Decimal('0.2'))
