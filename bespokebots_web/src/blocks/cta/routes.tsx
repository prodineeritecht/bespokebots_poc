import React from 'react';

// Building blocks CTA components
import {
  IndexView as CtaIndexView,
  CtaSimpleCentered as CtaSimpleCenteredView,
  CtaAlignedLeftWithTypedText as CtaAlignedLeftWithTypedTextView,
  CtaWithRightButtons as CtaWithRightButtonsView,
  SupportCenterCta as SupportCenterCtaView,
  CtaWithInputField as CtaWithInputFieldView,
  CtaWithCoverImage as CtaWithCoverImageView,
  CtaWithRightDownloadButton as CtaWithRightDownloadButtonView,
  CtaWithAppStoreButtons as CtaWithAppStoreButtonsView,
  CtaWithIllustration as CtaWithIllustrationView,
  CtaWithRightAppStoreButtons as CtaWithRightAppStoreButtonsView,
} from 'blocks/cta';

const routes = [
  {
    path: '/blocks/cta',
    renderer: (params = {}): JSX.Element => <CtaIndexView {...params} />,
  },
  {
    path: '/blocks/cta/cta-simple-centered',
    renderer: (params = {}): JSX.Element => (
      <CtaSimpleCenteredView {...params} />
    ),
  },
  {
    path: '/blocks/cta/cta-aligned-left-with-typed-text',
    renderer: (params = {}): JSX.Element => (
      <CtaAlignedLeftWithTypedTextView {...params} />
    ),
  },
  {
    path: '/blocks/cta/cta-with-right-buttons',
    renderer: (params = {}): JSX.Element => (
      <CtaWithRightButtonsView {...params} />
    ),
  },
  {
    path: '/blocks/cta/support-center-cta',
    renderer: (params = {}): JSX.Element => (
      <SupportCenterCtaView {...params} />
    ),
  },
  {
    path: '/blocks/cta/cta-with-input-field',
    renderer: (params = {}): JSX.Element => (
      <CtaWithInputFieldView {...params} />
    ),
  },
  {
    path: '/blocks/cta/cta-with-cover-image',
    renderer: (params = {}): JSX.Element => (
      <CtaWithCoverImageView {...params} />
    ),
  },
  {
    path: '/blocks/cta/cta-with-right-download-button',
    renderer: (params = {}): JSX.Element => (
      <CtaWithRightDownloadButtonView {...params} />
    ),
  },
  {
    path: '/blocks/cta/cta-with-app-store-buttons',
    renderer: (params = {}): JSX.Element => (
      <CtaWithAppStoreButtonsView {...params} />
    ),
  },
  {
    path: '/blocks/cta/cta-with-illustration',
    renderer: (params = {}): JSX.Element => (
      <CtaWithIllustrationView {...params} />
    ),
  },
  {
    path: '/blocks/cta/cta-with-right-app-store-buttons',
    renderer: (params = {}): JSX.Element => (
      <CtaWithRightAppStoreButtonsView {...params} />
    ),
  },
];

export default routes;
