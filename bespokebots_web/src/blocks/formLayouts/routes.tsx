import React from 'react';

// Building blocks FormLayouts components
import {
  IndexView as FormLayoutsIndexView,
  Account as AccountView,
  Contact as ContactView,
} from 'blocks/formLayouts';

const routes = [
  {
    path: '/blocks/form-layouts',
    renderer: (params = {}): JSX.Element => (
      <FormLayoutsIndexView {...params} />
    ),
  },
  {
    path: '/blocks/form-layouts/account',
    renderer: (params = {}): JSX.Element => <AccountView {...params} />,
  },
  {
    path: '/blocks/form-layouts/contact',
    renderer: (params = {}): JSX.Element => <ContactView {...params} />,
  },
];

export default routes;
