from shopping import shopping_order
from shopping.shopping_cart import ShoppingCart
from shopping.deal.history import History

shopping_order.get_order()
print(dir(shopping_order))

cart = ShoppingCart()
cart.pay()

history = History()
history.log()
