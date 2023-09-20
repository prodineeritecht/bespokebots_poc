import React from 'react';

// Building blocks Team components
import {
  IndexView as TeamIndexView,
  TeamWithCircledPhotos as TeamWithCircledPhotosView,
  WithOverlappedCards as WithOverlappedCardsView,
  WithLargeImagesAndSocialIcons as WithLargeImagesAndSocialIconsView,
  TeamWithSmallSquarePhotos as TeamWithSmallSquarePhotosView,
  WithSimpleCards as WithSimpleCardsView,
  WithAlternateCards as WithAlternateCardsView,
} from 'blocks/team';

const routes = [
  {
    path: '/blocks/team',
    renderer: (params = {}): JSX.Element => <TeamIndexView {...params} />,
  },
  {
    path: '/blocks/team/team-with-circled-photos',
    renderer: (params = {}): JSX.Element => (
      <TeamWithCircledPhotosView {...params} />
    ),
  },
  {
    path: '/blocks/team/with-overlapped-cards',
    renderer: (params = {}): JSX.Element => (
      <WithOverlappedCardsView {...params} />
    ),
  },
  {
    path: '/blocks/team/with-large-images-and-social-icons',
    renderer: (params = {}): JSX.Element => (
      <WithLargeImagesAndSocialIconsView {...params} />
    ),
  },
  {
    path: '/blocks/team/team-with-small-square-photos',
    renderer: (params = {}): JSX.Element => (
      <TeamWithSmallSquarePhotosView {...params} />
    ),
  },
  {
    path: '/blocks/team/with-simple-card',
    renderer: (params = {}): JSX.Element => <WithSimpleCardsView {...params} />,
  },
  {
    path: '/blocks/team/with-alternate-card',
    renderer: (params = {}): JSX.Element => (
      <WithAlternateCardsView {...params} />
    ),
  },
];

export default routes;
