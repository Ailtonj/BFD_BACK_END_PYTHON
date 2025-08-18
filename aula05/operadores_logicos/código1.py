a = 10
b = 3

resultado_and = (a > 5) and (b < 5)
resultado_or = (a > 15) or (b > 5)
resultado_nor = not (a > 5)

print(f"(a > 5) and (b < 5): {resultado_and}\n",
      f"(a > 15) or (b > 5): {resultado_or}\n",
      f"not (a > 5): {resultado_nor}")