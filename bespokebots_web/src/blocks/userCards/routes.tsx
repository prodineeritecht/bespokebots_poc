import React from 'react';

// Building blocks userCards components
import {
  IndexView as UserCardsIndexView,
  UserCardGrid as UserCardGridView,
  UserCardWithBackground as UserCardWithBackgroundView,
  UserCardWithRating as UserCardWithRatingView,
} from 'blocks/userCards';

const routes = [
  {
    path: '/blocks/user-cards',
    renderer: (params = {}): JSX.Element => <UserCardsIndexView {...params} />,
  },
  {
    path: '/blocks/user-cards/user-card-grid',
    renderer: (params = {}): JSX.Element => <UserCardGridView {...params} />,
  },
  {
    path: '/blocks/user-cards/user-card-with-background',
    renderer: (params = {}): JSX.Element => (
      <UserCardWithBackgroundView {...params} />
    ),
  },
  {
    path: '/blocks/user-cards/user-card-with-rating',
    renderer: (params = {}): JSX.Element => (
      <UserCardWithRatingView {...params} />
    ),
  },
];

export default routes;
