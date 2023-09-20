import React from 'react';

// Documentation pages
import {
  Introduction as IntroductionView,
  QuickStartReactScripts as QuickStartReactScriptsView,
  QuickStartNextJS as QuickStartNextJSView,
  QuickStartGatsbyJS as QuickStartGatsbyJSView,
  Colors as ColorsView,
  TypographyComponent as TypographyComponentView,
  Shadows as ShadowsView,
  PageComponent as PageComponentView,
  ContainerComponent as ContainerComponentView,
  Layouts as LayoutsView,
  Support as SupportView,
  Icons as IconsView,
  Illustrations as IllustrationsView,
  ChangeLog as ChangeLogView,
  Setup as SetupView,
} from 'docs';

const routes = [
  {
    path: '/docs',
    renderer: (params = {}): JSX.Element => <IntroductionView {...params} />,
  },
  {
    path: '/docs/introduction',
    renderer: (params = {}): JSX.Element => <IntroductionView {...params} />,
  },
  {
    path: '/docs/quick-start-react-scripts',
    renderer: (params = {}): JSX.Element => (
      <QuickStartReactScriptsView {...params} />
    ),
  },
  {
    path: '/docs/quick-start-nextjs',
    renderer: (params = {}): JSX.Element => (
      <QuickStartNextJSView {...params} />
    ),
  },
  {
    path: '/docs/quick-start-gatsbyjs',
    renderer: (params = {}): JSX.Element => (
      <QuickStartGatsbyJSView {...params} />
    ),
  },
  {
    path: '/docs/colors',
    renderer: (params = {}): JSX.Element => <ColorsView {...params} />,
  },
  {
    path: '/docs/typography',
    renderer: (params = {}): JSX.Element => (
      <TypographyComponentView {...params} />
    ),
  },
  {
    path: '/docs/shadows',
    renderer: (params = {}): JSX.Element => <ShadowsView {...params} />,
  },
  {
    path: '/docs/page',
    renderer: (params = {}): JSX.Element => <PageComponentView {...params} />,
  },
  {
    path: '/docs/container',
    renderer: (params = {}): JSX.Element => (
      <ContainerComponentView {...params} />
    ),
  },
  {
    path: '/docs/layouts',
    renderer: (params = {}): JSX.Element => <LayoutsView {...params} />,
  },
  {
    path: '/docs/icons',
    renderer: (params = {}): JSX.Element => <IconsView {...params} />,
  },
  {
    path: '/docs/illustrations',
    renderer: (params = {}): JSX.Element => <IllustrationsView {...params} />,
  },
  {
    path: '/docs/support',
    renderer: (params = {}): JSX.Element => <SupportView {...params} />,
  },
  {
    path: '/docs/change-log',
    renderer: (params = {}): JSX.Element => <ChangeLogView {...params} />,
  },
  {
    path: '/docs/setup',
    renderer: (params = {}): JSX.Element => <SetupView {...params} />,
  },
];

export default routes;
