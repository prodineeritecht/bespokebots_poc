import React from 'react';

// Building blocks Hero components
import {
  IndexView as HeroIndexView,
  FullScreenHeroWithImageSlider as FullScreenHeroWithImageSliderView,
  FullScreenHeroWithPromoImagesAndTypedText as FullScreenHeroWithPromoImagesAndTypedTextView,
  HeroWithFormAndBackgroundGradient as HeroWithFormAndBackgroundGradientView,
  HeroForEcommerceApp as HeroForEcommerceAppView,
  FullScreenHeroWithSubscriptionForm as FullScreenHeroWithSubscriptionFormView,
  HeroWithIllustrationAndSearchBar as HeroWithIllustrationAndSearchBarView,
  HeroWithMobileAppScreenshot as HeroWithMobileAppScreenshotView,
  HeroWithDashboardScreenshotAndCta as HeroWithDashboardScreenshotAndCtaView,
  SimpleHeroWithSearchBox as SimpleHeroWithSearchBoxView,
  SimpleHeroWithCta as SimpleHeroWithCtaView,
  HeroWithIllustrationAndCta as HeroWithIllustrationAndCtaView,
  HeroWithLogoGridAndDesktopScreenshot as HeroWithLogoGridAndDesktopScreenshotView,
  HeroWithBackgroundVideo as HeroWithBackgroundVideoView,
  SimpleHeroWithBottomVideo as SimpleHeroWithBottomVideoView,
  HeroWithPrimaryBackgroundAndDesktopScreenshot as HeroWithPrimaryBackgroundAndDesktopScreenshotView,
  FullScreenHeroWithLogoGrid as FullScreenHeroWithLogoGridView,
  SimpleHeroWithImageAndCtaButtons as SimpleHeroWithImageAndCtaButtonsView,
} from 'blocks/heroes';

const routes = [
  {
    path: '/blocks/heroes',
    renderer: (params = {}): JSX.Element => <HeroIndexView {...params} />,
  },
  {
    path: '/blocks/heroes/full-screen-hero-with-promo-images-and-typed-text',
    renderer: (params = {}): JSX.Element => (
      <FullScreenHeroWithPromoImagesAndTypedTextView {...params} />
    ),
  },
  {
    path: '/blocks/heroes/full-screen-hero-with-image-slider',
    renderer: (params = {}): JSX.Element => (
      <FullScreenHeroWithImageSliderView {...params} />
    ),
  },
  {
    path: '/blocks/heroes/hero-with-form-and-background-gradient',
    renderer: (params = {}): JSX.Element => (
      <HeroWithFormAndBackgroundGradientView {...params} />
    ),
  },
  {
    path: '/blocks/heroes/hero-for-ecommerce-app',
    renderer: (params = {}): JSX.Element => (
      <HeroForEcommerceAppView {...params} />
    ),
  },
  {
    path: '/blocks/heroes/full-screen-hero-with-subscription-form',
    renderer: (params = {}): JSX.Element => (
      <FullScreenHeroWithSubscriptionFormView {...params} />
    ),
  },
  {
    path: '/blocks/heroes/hero-with-illustration-and-search-bar',
    renderer: (params = {}): JSX.Element => (
      <HeroWithIllustrationAndSearchBarView {...params} />
    ),
  },
  {
    path: '/blocks/heroes/hero-with-mobile-app-screenshot',
    renderer: (params = {}): JSX.Element => (
      <HeroWithMobileAppScreenshotView {...params} />
    ),
  },
  {
    path: '/blocks/heroes/hero-with-dashboard-screenshot-and-cta',
    renderer: (params = {}): JSX.Element => (
      <HeroWithDashboardScreenshotAndCtaView {...params} />
    ),
  },
  {
    path: '/blocks/heroes/simple-hero-with-search-box',
    renderer: (params = {}): JSX.Element => (
      <SimpleHeroWithSearchBoxView {...params} />
    ),
  },
  {
    path: '/blocks/heroes/simple-hero-with-cta',
    renderer: (params = {}): JSX.Element => (
      <SimpleHeroWithCtaView {...params} />
    ),
  },
  {
    path: '/blocks/heroes/hero-with-illustration-and-cta',
    renderer: (params = {}): JSX.Element => (
      <HeroWithIllustrationAndCtaView {...params} />
    ),
  },
  {
    path: '/blocks/heroes/hero-with-logo-grid-and-desktop-screenshot',
    renderer: (params = {}): JSX.Element => (
      <HeroWithLogoGridAndDesktopScreenshotView {...params} />
    ),
  },
  {
    path: '/blocks/heroes/hero-with-background-video',
    renderer: (params = {}): JSX.Element => (
      <HeroWithBackgroundVideoView {...params} />
    ),
  },
  {
    path: '/blocks/heroes/simple-hero-with-bottom-video',
    renderer: (params = {}): JSX.Element => (
      <SimpleHeroWithBottomVideoView {...params} />
    ),
  },
  {
    path: '/blocks/heroes/hero-with-primary-background-and-desktop-screenshot',
    renderer: (params = {}): JSX.Element => (
      <HeroWithPrimaryBackgroundAndDesktopScreenshotView {...params} />
    ),
  },
  {
    path: '/blocks/heroes/full-screen-hero-with-logo-grid',
    renderer: (params = {}): JSX.Element => (
      <FullScreenHeroWithLogoGridView {...params} />
    ),
  },
  {
    path: '/blocks/heroes/simple-hero-with-image-and-cta-buttons',
    renderer: (params = {}): JSX.Element => (
      <SimpleHeroWithImageAndCtaButtonsView {...params} />
    ),
  },
];

export default routes;
