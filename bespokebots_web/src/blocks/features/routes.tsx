import React from 'react';

// Building blocks feature section components
import {
  IndexView as FeaturesIndexView,
  SimpleCentered as SimpleCenteredView,
  FeaturesWithCardRepresentation as FeaturesWithCardRepresentationView,
  FeaturesWithSimpleIcons as FeaturesWithSimpleIconsView,
  FeaturesWithCheckMarksAndAbstractImages as FeaturesWithCheckMarksAndAbstractImagesView,
  SimpleLeftAligned as SimpleLeftAlignedView,
  SimpleFeaturesWithAlternateCards as SimpleFeaturesWithAlternateCardsView,
  FeaturesWithLearnMoreLink as FeaturesWithLearnMoreLinkView,
  FeatureCardsWithColorfullIconsAndLearnMoreLink as FeatureCardsWithColorfullIconsAndLearnMoreLinkView,
  FeaturesWithMinimalDesign as FeaturesWithMinimalDesignView,
  OneLineFeatureListWithCheckMarks as OneLineFeatureListWithCheckMarksView,
  FeatureListWithForm as FeatureListWithFormView,
  FeaturesWithIllustration as FeaturesWithIllustrationView,
  FeaturesWithMobileScreenshot as FeaturesWithMobileScreenshotView,
  FeatureCardWithCtaButton as FeatureCardWithCtaButtonView,
  FeatureGridWithBackgrounds as FeatureGridWithBackgroundsView,
  FeaturesWithMasonryCardsAndCheckIcons as FeaturesWithMasonryCardsAndCheckIconsView,
  FeatureListWithDesktopAppScreenshot as FeatureListWithDesktopAppScreenshotView,
  FeaturesWithSimpleLeftAlignedIcons as FeaturesWithSimpleLeftAlignedIconsView,
} from 'blocks/features';

const routes = [
  {
    path: '/blocks/features',
    renderer: (params = {}): JSX.Element => <FeaturesIndexView {...params} />,
  },
  {
    path: '/blocks/features/simple-centered',
    renderer: (params = {}): JSX.Element => <SimpleCenteredView {...params} />,
  },
  {
    path: '/blocks/features/features-with-card-representation',
    renderer: (params = {}): JSX.Element => (
      <FeaturesWithCardRepresentationView {...params} />
    ),
  },
  {
    path: '/blocks/features/features-with-simple-icons',
    renderer: (params = {}): JSX.Element => (
      <FeaturesWithSimpleIconsView {...params} />
    ),
  },
  {
    path: '/blocks/features/features-with-check-marks-and-abstract-images',
    renderer: (params = {}): JSX.Element => (
      <FeaturesWithCheckMarksAndAbstractImagesView {...params} />
    ),
  },
  {
    path: '/blocks/features/simple-left-aligned',
    renderer: (params = {}): JSX.Element => (
      <SimpleLeftAlignedView {...params} />
    ),
  },
  {
    path: '/blocks/features/simple-features-with-alternate-cards',
    renderer: (params = {}): JSX.Element => (
      <SimpleFeaturesWithAlternateCardsView {...params} />
    ),
  },
  {
    path: '/blocks/features/features-with-learn-more-link',
    renderer: (params = {}): JSX.Element => (
      <FeaturesWithLearnMoreLinkView {...params} />
    ),
  },
  {
    path:
      '/blocks/features/feature-cards-with-colorfull-icons-and-learn-more-link',
    renderer: (params = {}): JSX.Element => (
      <FeatureCardsWithColorfullIconsAndLearnMoreLinkView {...params} />
    ),
  },
  {
    path: '/blocks/features/features-with-minimal-design',
    renderer: (params = {}): JSX.Element => (
      <FeaturesWithMinimalDesignView {...params} />
    ),
  },
  {
    path: '/blocks/features/one-line-feature-list-with-check-marks',
    renderer: (params = {}): JSX.Element => (
      <OneLineFeatureListWithCheckMarksView {...params} />
    ),
  },
  {
    path: '/blocks/features/feature-list-with-form',
    renderer: (params = {}): JSX.Element => (
      <FeatureListWithFormView {...params} />
    ),
  },
  {
    path: '/blocks/features/features-with-illustration',
    renderer: (params = {}): JSX.Element => (
      <FeaturesWithIllustrationView {...params} />
    ),
  },
  {
    path: '/blocks/features/features-with-mobile-screenshot',
    renderer: (params = {}): JSX.Element => (
      <FeaturesWithMobileScreenshotView {...params} />
    ),
  },
  {
    path: '/blocks/features/feature-card-with-cta-button',
    renderer: (params = {}): JSX.Element => (
      <FeatureCardWithCtaButtonView {...params} />
    ),
  },
  {
    path: '/blocks/features/feature-grid-with-backgrounds',
    renderer: (params = {}): JSX.Element => (
      <FeatureGridWithBackgroundsView {...params} />
    ),
  },
  {
    path: '/blocks/features/features-with-masonry-cards-and-check-icons',
    renderer: (params = {}): JSX.Element => (
      <FeaturesWithMasonryCardsAndCheckIconsView {...params} />
    ),
  },
  {
    path: '/blocks/features/feature-list-with-desktop-app-screenshot',
    renderer: (params = {}): JSX.Element => (
      <FeatureListWithDesktopAppScreenshotView {...params} />
    ),
  },
  {
    path: '/blocks/features/features-with-simple-left-aligned-icons',
    renderer: (params = {}): JSX.Element => (
      <FeaturesWithSimpleLeftAlignedIconsView {...params} />
    ),
  },
];

export default routes;
