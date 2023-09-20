import React from 'react';

// Building blocks Tables components
import {
  IndexView as TablesIndexView,
  WithAvatarsAndMultilineContent as WithAvatarsAndMultilineContentView,
  SimpleStriped as SimpleStripedView,
  Simple as SimpleView,
} from 'blocks/tables';

const routes = [
  {
    path: '/blocks/tables',
    renderer: (params = {}): JSX.Element => <TablesIndexView {...params} />,
  },
  {
    path: '/blocks/tables/with-avatars-and-multiline-content',
    renderer: (params = {}): JSX.Element => (
      <WithAvatarsAndMultilineContentView {...params} />
    ),
  },
  {
    path: '/blocks/tables/simple-striped',
    renderer: (params = {}): JSX.Element => <SimpleStripedView {...params} />,
  },
  {
    path: '/blocks/tables/simple',
    renderer: (params = {}): JSX.Element => <SimpleView {...params} />,
  },
];

export default routes;
