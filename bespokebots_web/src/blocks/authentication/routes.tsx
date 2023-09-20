import React from 'react';

// Building blocks Authentication components
import {
  IndexView as AuthIndexView,
  SimpleSignUpForm as SimpleSignUpFormView,
  SignUpFormWithCoverImage as SignUpFormWithCoverImageView,
  SimpleSignInForm as SimpleSignInFormView,
  SignInFormWithCoverImage as SignInFormWithCoverImageView,
  ResetPasswordSimpleForm as ResetPasswordSimpleFormView,
  AuthFormWithDarkBg as AuthFormWithDarkBgView,
} from 'blocks/authentication';

const routes = [
  {
    path: '/blocks/authentication',
    renderer: (params = {}): JSX.Element => <AuthIndexView {...params} />,
  },
  {
    path: '/blocks/authentication/simple-sign-up-form',
    renderer: (params = {}): JSX.Element => (
      <SimpleSignUpFormView {...params} />
    ),
  },
  {
    path: '/blocks/authentication/sign-up-form-with-cover-image',
    renderer: (params = {}): JSX.Element => (
      <SignUpFormWithCoverImageView {...params} />
    ),
  },
  {
    path: '/blocks/authentication/simple-sign-in-form',
    renderer: (params = {}): JSX.Element => (
      <SimpleSignInFormView {...params} />
    ),
  },
  {
    path: '/blocks/authentication/sign-in-form-with-cover-image',
    renderer: (params = {}): JSX.Element => (
      <SignInFormWithCoverImageView {...params} />
    ),
  },
  {
    path: '/blocks/authentication/reset-password-simple-form',
    renderer: (params = {}): JSX.Element => (
      <ResetPasswordSimpleFormView {...params} />
    ),
  },
  {
    path: '/blocks/authentication/auth-form-with-dark-bg',
    renderer: (params = {}): JSX.Element => (
      <AuthFormWithDarkBgView {...params} />
    ),
  },
];

export default routes;
