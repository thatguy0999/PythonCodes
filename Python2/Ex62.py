prices = [4.95, 9.95, 14.95, 19.95, 24.95]

for products in prices:
    print(f'original price: ${products} // discount: ${0.6*products:.2f} // new price: ${0.4*products:.2f}')