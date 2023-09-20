import React from 'react';

// Building blocks checkoutPages components
import {
  IndexView as CheckoutPagesIndexView,
  WithTwoColumns as WithTwoColumnsView,
} from 'blocks/checkoutPages';

const routes = [
  {
    path: '/blocks/checkout-pages',
    renderer: (params = {}): JSX.Element => (
      <CheckoutPagesIndexView {...params} />
    ),
  },
  {
    path: '/blocks/checkout-pages/with-two-columns',
    renderer: (params = {}): JSX.Element => <WithTwoColumnsView {...params} />,
  },
];

export default routes;
