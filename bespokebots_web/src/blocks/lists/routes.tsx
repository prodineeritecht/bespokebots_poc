import React from 'react';

// Building blocks Lists components
import {
  IndexView as ListsIndexView,
  ListWithNestedItem as ListWithNestedItemView,
  WithAvatars as WithAvatarsView,
  ListWithVerticalLine as ListWithVerticalLineView,
} from 'blocks/lists';

const routes = [
  {
    path: '/blocks/lists',
    renderer: (params = {}): JSX.Element => <ListsIndexView {...params} />,
  },
  {
    path: '/blocks/lists/list-with-nested-item',
    renderer: (params = {}): JSX.Element => (
      <ListWithNestedItemView {...params} />
    ),
  },
  {
    path: '/blocks/lists/with-avatars',
    renderer: (params = {}): JSX.Element => <WithAvatarsView {...params} />,
  },
  {
    path: '/blocks/lists/list-with-vertical-line',
    renderer: (params = {}): JSX.Element => (
      <ListWithVerticalLineView {...params} />
    ),
  },
];

export default routes;
