import React from 'react';

// Building blocks Testimonials components
import {
  IndexView as TestimonialsIndexView,
  WithLargeImage as WithLargeImageView,
  WithHighlightedCard as WithHighlightedCardView,
  ReviewsWithBorderedGridLayout as ReviewsWithBorderedGridLayoutView,
  WithCompanyLogo as WithCompanyLogoView,
  WithOutlinedCards as WithOutlinedCardsView,
  ReviewsWithSimpleBoxes as ReviewsWithSimpleBoxesView,
  WithBrandBgColor as WithBrandBgColorView,
} from 'blocks/testimonials';

const routes = [
  {
    path: '/blocks/testimonials',
    renderer: (params = {}): JSX.Element => (
      <TestimonialsIndexView {...params} />
    ),
  },
  {
    path: '/blocks/testimonials/with-large-image',
    renderer: (params = {}): JSX.Element => <WithLargeImageView {...params} />,
  },
  {
    path: '/blocks/testimonials/with-highlighted-card',
    renderer: (params = {}): JSX.Element => (
      <WithHighlightedCardView {...params} />
    ),
  },
  {
    path: '/blocks/testimonials/reviews-with-bordered-grid-layout',
    renderer: (params = {}): JSX.Element => (
      <ReviewsWithBorderedGridLayoutView {...params} />
    ),
  },
  {
    path: '/blocks/testimonials/with-company-logo',
    renderer: (params = {}): JSX.Element => <WithCompanyLogoView {...params} />,
  },
  {
    path: '/blocks/testimonials/with-outlined-cards',
    renderer: (params = {}): JSX.Element => (
      <WithOutlinedCardsView {...params} />
    ),
  },
  {
    path: '/blocks/testimonials/reviews-with-simple-boxes',
    renderer: (params = {}): JSX.Element => (
      <ReviewsWithSimpleBoxesView {...params} />
    ),
  },
  {
    path: '/blocks/testimonials/with-brand-bg-color',
    renderer: (params = {}): JSX.Element => (
      <WithBrandBgColorView {...params} />
    ),
  },
];

export default routes;
