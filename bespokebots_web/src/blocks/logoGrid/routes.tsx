import React from 'react';

// Building blocks Logo Grid components
import {
  IndexView as LogoGridIndexView,
  LogoGridSimpleCentered as LogoGridSimpleCenteredView,
  WithBoxedLogos as WithBoxedLogosView,
  WithLeftAlignedDescriptionBox as WithLeftAlignedDescriptionBoxView,
  WithSwiperAndBrandBackgroundColor as WithSwiperAndBrandBackgroundColorView,
  WithLeftAlignedDescriptionBoxAndBoxedLogos as WithLeftAlignedDescriptionBoxAndBoxedLogosView,
  WithDarkBackgroundAndSimpleDescriptionBox as WithDarkBackgroundAndSimpleDescriptionBoxView,
} from 'blocks/logoGrid';

const routes = [
  {
    path: '/blocks/logo-grid',
    renderer: (params = {}): JSX.Element => <LogoGridIndexView {...params} />,
  },
  {
    path: '/blocks/logo-grid/logo-grid-simple-centered',
    renderer: (params = {}): JSX.Element => (
      <LogoGridSimpleCenteredView {...params} />
    ),
  },
  {
    path: '/blocks/logo-grid/logo-grid-with-boxed-logos',
    renderer: (params = {}): JSX.Element => <WithBoxedLogosView {...params} />,
  },
  {
    path: '/blocks/logo-grid/logo-grid-with-left-aligned-description-box',
    renderer: (params = {}): JSX.Element => (
      <WithLeftAlignedDescriptionBoxView {...params} />
    ),
  },
  {
    path: '/blocks/logo-grid/logo-grid-with-swiper-and-brand-background-color',
    renderer: (params = {}): JSX.Element => (
      <WithSwiperAndBrandBackgroundColorView {...params} />
    ),
  },
  {
    path:
      '/blocks/logo-grid/logo-grid-with-left-aligned-description-box-and-boxed-logos',
    renderer: (params = {}): JSX.Element => (
      <WithLeftAlignedDescriptionBoxAndBoxedLogosView {...params} />
    ),
  },
  {
    path:
      '/blocks/logo-grid/logo-grid-with-dark-background-and-simple-description-box',
    renderer: (params = {}): JSX.Element => (
      <WithDarkBackgroundAndSimpleDescriptionBoxView {...params} />
    ),
  },
];

export default routes;
