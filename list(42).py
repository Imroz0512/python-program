#list slicing
amazon_cart =['nootbook','sunglasses','Radio','vrset','kid toys']
amazon_cart[0] = 'mobile'
new_cart =  amazon_cart[:]
new_cart[0] = 'laptop'
print(new_cart)
print(amazon_cart)