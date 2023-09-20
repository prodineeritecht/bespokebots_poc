import React from 'react';

// Building blocks storePopups components
import {
  IndexView as StorePopupsIndexView,
  PopupWithDiscount as PopupWithDiscountView,
  PopupWithImage as PopupWithImageView,
} from 'blocks/storePopups';

const routes = [
  {
    path: '/blocks/store-popups',
    renderer: (params = {}): JSX.Element => (
      <StorePopupsIndexView {...params} />
    ),
  },
  {
    path: '/blocks/store-popups/popup-with-discount',
    renderer: (params = {}): JSX.Element => (
      <PopupWithDiscountView {...params} />
    ),
  },
  {
    path: '/blocks/store-popups/popup-with-image',
    renderer: (params = {}): JSX.Element => <PopupWithImageView {...params} />,
  },
];

export default routes;
