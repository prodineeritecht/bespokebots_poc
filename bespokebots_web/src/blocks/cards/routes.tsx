import React from 'react';

// Building blocks Cards components
import {
  IndexView as CardsIndexView,
  CardWithColorAccent as CardWithColorAccentView,
  CardWithCheckboxes as CardWithCheckboxesView,
  CardWithAddButton as CardWithAddButtonView,
} from 'blocks/cards';

const routes = [
  {
    path: '/blocks/cards',
    renderer: (params = {}): JSX.Element => <CardsIndexView {...params} />,
  },
  {
    path: '/blocks/cards/card-with-color-accent',
    renderer: (params = {}): JSX.Element => (
      <CardWithColorAccentView {...params} />
    ),
  },
  {
    path: '/blocks/cards/card-with-checkboxes',
    renderer: (params = {}): JSX.Element => (
      <CardWithCheckboxesView {...params} />
    ),
  },
  {
    path: '/blocks/cards/card-with-add-button',
    renderer: (params = {}): JSX.Element => (
      <CardWithAddButtonView {...params} />
    ),
  },
];

export default routes;
