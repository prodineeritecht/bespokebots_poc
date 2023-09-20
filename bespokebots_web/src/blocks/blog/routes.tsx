import React from 'react';

// Building blocks Blog components
import {
  IndexView as BlogIndexView,
  BlogWithLargeImage as BlogWithLargeImageView,
  VerticallyAlignedBlogCardOverlappedWithDescriptionBox as VerticallyAlignedBlogCardOverlappedWithDescriptionBoxView,
  SimpleVerticalBlogCards as SimpleVerticalBlogCardsView,
  HorizontallyAlignedBlogCardWithShapedImage as HorizontallyAlignedBlogCardWithShapedImageView,
  VerticallyAlignedBlogCardsWithShapedImage as VerticallyAlignedBlogCardsWithShapedImageView,
  BlogCardsWithFullBackgroundImage as BlogCardsWithFullBackgroundImageView,
  VerticalMinimalDesignedBlogCards as VerticalMinimalDesignedBlogCardsView,
} from 'blocks/blog';

const routes = [
  {
    path: '/blocks/blog',
    renderer: (params = {}): JSX.Element => <BlogIndexView {...params} />,
  },
  {
    path: '/blocks/blog/blog-with-large-image',
    renderer: (params = {}): JSX.Element => (
      <BlogWithLargeImageView {...params} />
    ),
  },
  {
    path:
      '/blocks/blog/vertically-aligned-blog-card-overlapped-with-description-box',
    renderer: (params = {}): JSX.Element => (
      <VerticallyAlignedBlogCardOverlappedWithDescriptionBoxView {...params} />
    ),
  },
  {
    path: '/blocks/blog/simple-vertical-blog-cards',
    renderer: (params = {}): JSX.Element => (
      <SimpleVerticalBlogCardsView {...params} />
    ),
  },
  {
    path: '/blocks/blog/horizontally-aligned-blog-card-with-shaped-image',
    renderer: (params = {}): JSX.Element => (
      <HorizontallyAlignedBlogCardWithShapedImageView {...params} />
    ),
  },
  {
    path: '/blocks/blog/vertically-aligned-blog-cards-with-shaped-image',
    renderer: (params = {}): JSX.Element => (
      <VerticallyAlignedBlogCardsWithShapedImageView {...params} />
    ),
  },
  {
    path: '/blocks/blog/blog-cards-with-full-background-image',
    renderer: (params = {}): JSX.Element => (
      <BlogCardsWithFullBackgroundImageView {...params} />
    ),
  },
  {
    path: '/blocks/blog/vertical-minimal-designed-blog-cards',
    renderer: (params = {}): JSX.Element => (
      <VerticalMinimalDesignedBlogCardsView {...params} />
    ),
  },
];

export default routes;
