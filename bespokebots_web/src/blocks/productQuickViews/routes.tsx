import React from 'react';

// Building blocks productQuickViews components
import {
  IndexView as ProductQuickViewsIndexView,
  PopupBoxWithProductDetails as PopupBoxWithProductDetailsView,
} from 'blocks/productQuickViews';

const routes = [
  {
    path: '/blocks/product-quick-views',
    renderer: (params = {}): JSX.Element => (
      <ProductQuickViewsIndexView {...params} />
    ),
  },
  {
    path: '/blocks/product-quick-views/popup-box-with-product-details',
    renderer: (params = {}): JSX.Element => (
      <PopupBoxWithProductDetailsView {...params} />
    ),
  },
];

export default routes;
