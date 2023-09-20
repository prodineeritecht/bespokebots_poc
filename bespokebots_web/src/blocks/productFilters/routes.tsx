import React from 'react';

// Building blocks productFilters components
import {
  IndexView as ProductFiltersIndexView,
  FiltersWithDropdown as FiltersWithDropdownView,
  FiltersWithSidebar as FiltersWithSidebarView,
} from 'blocks/productFilters';

const routes = [
  {
    path: '/blocks/product-filters',
    renderer: (params = {}): JSX.Element => (
      <ProductFiltersIndexView {...params} />
    ),
  },
  {
    path: '/blocks/product-filters/filters-with-dropdown',
    renderer: (params = {}): JSX.Element => (
      <FiltersWithDropdownView {...params} />
    ),
  },
  {
    path: '/blocks/product-filters/filters-with-sidebar',
    renderer: (params = {}): JSX.Element => (
      <FiltersWithSidebarView {...params} />
    ),
  },
];

export default routes;
