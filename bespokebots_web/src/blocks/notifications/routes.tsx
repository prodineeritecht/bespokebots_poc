import React from 'react';

// Building blocks Notifications components
import {
  IndexView as NotificationsIndexView,
  Simple as SimpleView,
  WithActionButtons as WithActionButtonsView,
  WithAvatarAndButtonsBelow as WithAvatarAndButtonsBelowView,
  WithSplitButtons as WithSplitButtonsView,
} from 'blocks/notifications';

const routes = [
  {
    path: '/blocks/notifications',
    renderer: (params = {}): JSX.Element => (
      <NotificationsIndexView {...params} />
    ),
  },
  {
    path: '/blocks/notifications/simple',
    renderer: (params = {}): JSX.Element => <SimpleView {...params} />,
  },
  {
    path: '/blocks/notifications/with-action-buttons',
    renderer: (params = {}): JSX.Element => (
      <WithActionButtonsView {...params} />
    ),
  },
  {
    path: '/blocks/notifications/with-avatar-and-buttons-below',
    renderer: (params = {}): JSX.Element => (
      <WithAvatarAndButtonsBelowView {...params} />
    ),
  },
  {
    path: '/blocks/notifications/with-split-buttons',
    renderer: (params = {}): JSX.Element => (
      <WithSplitButtonsView {...params} />
    ),
  },
];

export default routes;
