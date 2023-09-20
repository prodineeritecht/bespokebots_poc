import React from 'react';

// Building blocks productGrids components
import {
  IndexView as ProductGridsIndexView,
  WithCtaButton as WithCtaButtonView,
  MinimallyDesigned as MinimallyDesignedView,
  WithPromoBadge as WithPromoBadgeView,
} from 'blocks/productGrids';

const routes = [
  {
    path: '/blocks/product-grids',
    renderer: (params = {}): JSX.Element => (
      <ProductGridsIndexView {...params} />
    ),
  },
  {
    path: '/blocks/product-grids/with-cta-button',
    renderer: (params = {}): JSX.Element => <WithCtaButtonView {...params} />,
  },
  {
    path: '/blocks/product-grids/minimally-designed',
    renderer: (params = {}): JSX.Element => (
      <MinimallyDesignedView {...params} />
    ),
  },
  {
    path: '/blocks/product-grids/with-promo-badge',
    renderer: (params = {}): JSX.Element => <WithPromoBadgeView {...params} />,
  },
];

export default routes;
