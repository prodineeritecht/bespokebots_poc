import React from 'react';

// Building blocks productDetails components
import {
  IndexView as ProductDetailsIndexView,
  WithLargeImage as WithLargeImageView,
  WithImageGrid as WithImageGridView,
} from 'blocks/productDetails';

const routes = [
  {
    path: '/blocks/product-details',
    renderer: (params = {}): JSX.Element => (
      <ProductDetailsIndexView {...params} />
    ),
  },
  {
    path: '/blocks/product-details/with-large-image',
    renderer: (params = {}): JSX.Element => <WithLargeImageView {...params} />,
  },
  {
    path: '/blocks/product-details/with-image-grid',
    renderer: (params = {}): JSX.Element => <WithImageGridView {...params} />,
  },
];

export default routes;
