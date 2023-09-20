import React from 'react';

// Building blocks Pricing components
import {
  IndexView as PricingIndexView,
  WithHighlightingAndPrimaryColor as WithHighlightingAndPrimaryColorView,
  WithTwoColumnAndMixedHeight as WithTwoColumnAndMixedHeightView,
  WithSimpleBorderedCards as WithSimpleBorderedCardsView,
  SingleChoiceOption as SingleChoiceOptionView,
  WithHighlightingAndSecondaryColor as WithHighlightingAndSecondaryColorView,
  WithOptionTogglerButton as WithOptionTogglerButtonView,
  CompareTable as CompareTableView,
} from 'blocks/pricing';

const routes = [
  {
    path: '/blocks/pricing',
    renderer: (params = {}): JSX.Element => <PricingIndexView {...params} />,
  },
  {
    path: '/blocks/pricing/with-highlighting-and-primary-color',
    renderer: (params = {}): JSX.Element => (
      <WithHighlightingAndPrimaryColorView {...params} />
    ),
  },
  {
    path: '/blocks/pricing/with-two-column-and-mixed-height',
    renderer: (params = {}): JSX.Element => (
      <WithTwoColumnAndMixedHeightView {...params} />
    ),
  },
  {
    path: '/blocks/pricing/with-simple-bordered-cards',
    renderer: (params = {}): JSX.Element => (
      <WithSimpleBorderedCardsView {...params} />
    ),
  },
  {
    path: '/blocks/pricing/single-choice-option',
    renderer: (params = {}): JSX.Element => (
      <SingleChoiceOptionView {...params} />
    ),
  },
  {
    path: '/blocks/pricing/with-highlighting-and-secondary-color',
    renderer: (params = {}): JSX.Element => (
      <WithHighlightingAndSecondaryColorView {...params} />
    ),
  },
  {
    path: '/blocks/pricing/with-option-toggler-button',
    renderer: (params = {}): JSX.Element => (
      <WithOptionTogglerButtonView {...params} />
    ),
  },
  {
    path: '/blocks/pricing/compare-table',
    renderer: (params = {}): JSX.Element => <CompareTableView {...params} />,
  },
];

export default routes;
