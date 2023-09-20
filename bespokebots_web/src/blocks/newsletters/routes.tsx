import React from 'react';

// Building blocks Newsletter components
import {
  IndexView as NewsletterIndexView,
  NewsletterWithCard as NewsletterWithCardView,
  NewsletterWithImage as NewsletterWithImageView,
  WithDarkBackground as WithDarkBackgroundView,
} from 'blocks/newsletters';

const routes = [
  {
    path: '/blocks/newsletters',
    renderer: (params = {}): JSX.Element => <NewsletterIndexView {...params} />,
  },
  {
    path: '/blocks/newsletters/newsletter-with-card',
    renderer: (params = {}): JSX.Element => (
      <NewsletterWithCardView {...params} />
    ),
  },
  {
    path: '/blocks/newsletters/newsletter-with-image',
    renderer: (params = {}): JSX.Element => (
      <NewsletterWithImageView {...params} />
    ),
  },
  {
    path: '/blocks/newsletters/with-dark-background',
    renderer: (params = {}): JSX.Element => (
      <WithDarkBackgroundView {...params} />
    ),
  },
];

export default routes;
