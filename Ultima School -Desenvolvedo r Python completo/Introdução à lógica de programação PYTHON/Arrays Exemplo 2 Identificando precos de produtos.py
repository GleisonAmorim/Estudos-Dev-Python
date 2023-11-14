#indices      0     1   2      3
"""produtos = [25.59, 10, 5.50, 60.89, 1, 6]
total = 0
for i in range(len(produtos)):
    total = total + produtos[i]
    #print(i, produtos[i], total)
print("O total do seu carrinho de compras é: ", + total)"""

produtos = [25.59, 10, 5.50, 60.89, 1, 6]
for i in range(len(produtos)):
    if produtos[i] < 8:
        print(i,produtos[i])
