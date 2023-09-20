import React from 'react';

// Building blocks Stats components
import {
  IndexView as StatsIndexView,
  WithCountUpNumbersAndCoverImage as WithCountUpNumbersAndCoverImageView,
  WithCountUpNumbersAndMap as WithCountUpNumbersAndMapView,
  StatsWithCard as StatsWithCardView,
  WithBorderedCardsAndBrandColor as WithBorderedCardsAndBrandColorView,
  WithAbstractVisualRepresentation as WithAbstractVisualRepresentationView,
  ClientSatisfaction as ClientSatisfactionView,
} from 'blocks/stats';

const routes = [
  {
    path: '/blocks/stats',
    renderer: (params = {}): JSX.Element => <StatsIndexView {...params} />,
  },
  {
    path: '/blocks/stats/with-count-up-numbers-and-cover-image',
    renderer: (params = {}): JSX.Element => (
      <WithCountUpNumbersAndCoverImageView {...params} />
    ),
  },
  {
    path: '/blocks/stats/with-count-up-numbers-and-map',
    renderer: (params = {}): JSX.Element => (
      <WithCountUpNumbersAndMapView {...params} />
    ),
  },
  {
    path: '/blocks/stats/stats-with-card',
    renderer: (params = {}): JSX.Element => <StatsWithCardView {...params} />,
  },
  {
    path: '/blocks/stats/with-bordered-cards-and-brand-color',
    renderer: (params = {}): JSX.Element => (
      <WithBorderedCardsAndBrandColorView {...params} />
    ),
  },
  {
    path: '/blocks/stats/with-abstract-visual-representation',
    renderer: (params = {}): JSX.Element => (
      <WithAbstractVisualRepresentationView {...params} />
    ),
  },
  {
    path: '/blocks/stats/client-satisfaction',
    renderer: (params = {}): JSX.Element => (
      <ClientSatisfactionView {...params} />
    ),
  },
];

export default routes;
