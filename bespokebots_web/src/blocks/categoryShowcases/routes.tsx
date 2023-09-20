import React from 'react';

// Building blocks Category Showcase components
import {
  IndexView as CategoryShowcasesIndexView,
  WithImageGrid as WithImageGridView,
  SpanningColumns as SpanningColumnsView,
  ShowcaseGrid as ShowcaseGridView,
  ShowcaseBgImage as ShowcaseBgImageView,
} from 'blocks/categoryShowcases';

const routes = [
  {
    path: '/blocks/category-showcases',
    renderer: (params = {}): JSX.Element => (
      <CategoryShowcasesIndexView {...params} />
    ),
  },
  {
    path: '/blocks/category-showcases/with-image-grid',
    renderer: (params = {}): JSX.Element => <WithImageGridView {...params} />,
  },
  {
    path: '/blocks/category-showcases/on-spanning-columns',
    renderer: (params = {}): JSX.Element => <SpanningColumnsView {...params} />,
  },
  {
    path: '/blocks/category-showcases/showcase-grid',
    renderer: (params = {}): JSX.Element => <ShowcaseGridView {...params} />,
  },
  {
    path: '/blocks/category-showcases/showcase-bg-image',
    renderer: (params = {}): JSX.Element => <ShowcaseBgImageView {...params} />,
  },
];

export default routes;
