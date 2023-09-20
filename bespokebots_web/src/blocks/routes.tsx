import React from 'react';

// Building blocks components main page
import IndexView from 'blocks/IndexView';
import heroBlocksRoutes from 'blocks/heroes/routes';
import blogBlocksRoutes from 'blocks/blog/routes';
import ctaBlocksRoutes from 'blocks/cta/routes';
import featureBlocksRoutes from 'blocks/features/routes';
import logoGridBlocksRoutes from 'blocks/logoGrid/routes';
import newsletterBlocksRoutes from 'blocks/newsletters/routes';
import pricingBlocksRoutes from 'blocks/pricing/routes';
import statsBlocksRoutes from 'blocks/stats/routes';
import teamBlocksRoutes from 'blocks/team/routes';
import testimonialsBlockSRoutes from 'blocks/testimonials/routes';
import authBlocksRoutes from 'blocks/authentication/routes';
import bannerBlocksRoutes from 'blocks/banners/routes';
import cardsBlocksRoutes from 'blocks/cards/routes';
import formLayoutsBlocksRoutes from 'blocks/formLayouts/routes';
import listsBlocksRoutes from 'blocks/lists/routes';
import notificationsBlocksRoutes from 'blocks/notifications/routes';
import popoverBlocksRoutes from 'blocks/popovers/routes';
import pageLayoutsBlocksRoutes from 'blocks/pageLayouts/routes';
import sidebarsBlocksRoutes from 'blocks/sidebars/routes';
import appStatsBlocksRoutes from 'blocks/appStats/routes';
import tablesBlocksRoutes from 'blocks/tables/routes';
import progressStepsBlocksRoutes from 'blocks/progressSteps/routes';
import userCardsBlocksRoutes from 'blocks/userCards/routes';
import formControlsBlocksRoutes from 'blocks/formControls/routes';
import categoryShowcasesBlocksRoutes from 'blocks/categoryShowcases/routes';
import checkoutPagesBlocksRoutes from 'blocks/checkoutPages/routes';
import productDetailsBlocksRoutes from 'blocks/productDetails/routes';
import productFiltersBlockRoutes from 'blocks/productFilters/routes';
import productGridsBlocksRoutes from 'blocks/productGrids/routes';
import productPickersBlocksRoutes from 'blocks/productPickers/routes';
import productQuickViewsBlocksRoutes from 'blocks/productQuickViews/routes';
import productReviewsBlocksRoutes from 'blocks/productReviews/routes';
import shoppingCartsBlocksRoutes from 'blocks/shoppingCarts/routes';
import storeNavigationBlocksRoutes from 'blocks/storeNavigation/routes';
import storePopupsBlocksRoutes from 'blocks/storePopups/routes';

const routes = [
  {
    path: '/blocks',
    renderer: (params = {}): JSX.Element => <IndexView {...params} />,
  },
  ...heroBlocksRoutes,
  ...blogBlocksRoutes,
  ...ctaBlocksRoutes,
  ...featureBlocksRoutes,
  ...logoGridBlocksRoutes,
  ...newsletterBlocksRoutes,
  ...pricingBlocksRoutes,
  ...statsBlocksRoutes,
  ...teamBlocksRoutes,
  ...testimonialsBlockSRoutes,
  ...authBlocksRoutes,
  ...bannerBlocksRoutes,
  ...cardsBlocksRoutes,
  ...formLayoutsBlocksRoutes,
  ...listsBlocksRoutes,
  ...notificationsBlocksRoutes,
  ...popoverBlocksRoutes,
  ...pageLayoutsBlocksRoutes,
  ...sidebarsBlocksRoutes,
  ...appStatsBlocksRoutes,
  ...tablesBlocksRoutes,
  ...progressStepsBlocksRoutes,
  ...userCardsBlocksRoutes,
  ...formControlsBlocksRoutes,
  ...categoryShowcasesBlocksRoutes,
  ...checkoutPagesBlocksRoutes,
  ...productDetailsBlocksRoutes,
  ...productFiltersBlockRoutes,
  ...productGridsBlocksRoutes,
  ...productPickersBlocksRoutes,
  ...productQuickViewsBlocksRoutes,
  ...productReviewsBlocksRoutes,
  ...shoppingCartsBlocksRoutes,
  ...storeNavigationBlocksRoutes,
  ...storePopupsBlocksRoutes,
];

export default routes;
