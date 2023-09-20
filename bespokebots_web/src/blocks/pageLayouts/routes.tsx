import React from 'react';

// Building blocks PageLayouts components
import {
  IndexView as PageLayoutsIndexView,
  WithFixedSidebar as WithFixedSidebarView,
  WithThreeColumns as WithThreeColumnsView,
  WithToggledSidebar as WithToggledSidebarView,
  WithFluidLayoutAndNoSidebar as WithFluidLayoutAndNoSidebarView,
  WithNarrowLayoutAndNoSidebar as WithNarrowLayoutAndNoSidebarView,
} from 'blocks/pageLayouts';

const routes = [
  {
    path: '/blocks/page-layouts',
    renderer: (params = {}): JSX.Element => (
      <PageLayoutsIndexView {...params} />
    ),
  },
  {
    path: '/blocks/page-layouts/with-fixed-sidebar',
    renderer: (params = {}): JSX.Element => (
      <WithFixedSidebarView {...params} />
    ),
  },
  {
    path: '/blocks/page-layouts/with-three-columns',
    renderer: (params = {}): JSX.Element => (
      <WithThreeColumnsView {...params} />
    ),
  },
  {
    path: '/blocks/page-layouts/with-toggled-sidebar',
    renderer: (params = {}): JSX.Element => (
      <WithToggledSidebarView {...params} />
    ),
  },
  {
    path: '/blocks/page-layouts/with-fluid-layout-and-no-sidebar',
    renderer: (params = {}): JSX.Element => (
      <WithFluidLayoutAndNoSidebarView {...params} />
    ),
  },
  {
    path: '/blocks/page-layouts/with-narrow-layout-and-no-sidebar',
    renderer: (params = {}): JSX.Element => (
      <WithNarrowLayoutAndNoSidebarView {...params} />
    ),
  },
];

export default routes;
