import React from 'react';

// Building blocks shoppingCarts components
import {
  IndexView as ShoppingCartsIndexView,
  CartWithOrderSummery as CartWithOrderSummeryView,
  EmptyCart as EmptyCartView,
} from 'blocks/shoppingCarts';

const routes = [
  {
    path: '/blocks/shopping-carts',
    renderer: (params = {}): JSX.Element => (
      <ShoppingCartsIndexView {...params} />
    ),
  },
  {
    path: '/blocks/shopping-carts/cart-with-order-summery',
    renderer: (params = {}): JSX.Element => (
      <CartWithOrderSummeryView {...params} />
    ),
  },
  {
    path: '/blocks/shopping-carts/empty-cart',
    renderer: (params = {}): JSX.Element => <EmptyCartView {...params} />,
  },
];

export default routes;
