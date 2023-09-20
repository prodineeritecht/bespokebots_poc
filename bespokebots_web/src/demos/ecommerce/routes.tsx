import React from 'react';

// Demo E-commerce
import {
  IndexView,
  Cart as CartView,
  Checkout as CheckoutView,
  EmptyCart as EmptyCartView,
  Listing as ListingView,
  Promotions as PromotionsView,
  OrderComplete as OrderCompleteView,
  ProductOverview as ProductOverviewView,
} from 'demos/ecommerce/views';

const routes = [
  {
    path: '/demos/ecommerce',
    renderer: (params = {}): JSX.Element => <IndexView {...params} />,
  },
  {
    path: '/demos/ecommerce/cart',
    renderer: (params = {}): JSX.Element => <CartView {...params} />,
  },
  {
    path: '/demos/ecommerce/checkout',
    renderer: (params = {}): JSX.Element => <CheckoutView {...params} />,
  },
  {
    path: '/demos/ecommerce/empty-cart',
    renderer: (params = {}): JSX.Element => <EmptyCartView {...params} />,
  },
  {
    path: '/demos/ecommerce/listing',
    renderer: (params = {}): JSX.Element => <ListingView {...params} />,
  },
  {
    path: '/demos/ecommerce/promotions',
    renderer: (params = {}): JSX.Element => <PromotionsView {...params} />,
  },
  {
    path: '/demos/ecommerce/order-complete',
    renderer: (params = {}): JSX.Element => <OrderCompleteView {...params} />,
  },
  {
    path: '/demos/ecommerce/product-overview',
    renderer: (params = {}): JSX.Element => <ProductOverviewView {...params} />,
  },
];

export default routes;
