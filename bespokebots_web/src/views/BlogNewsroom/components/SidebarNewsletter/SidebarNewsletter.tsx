/* eslint-disable react/no-unescaped-entities */
import React from 'react';
import { useFormik } from 'formik';
import * as yup from 'yup';
import { useTheme } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Link from '@mui/material/Link';
import useMediaQuery from '@mui/material/useMediaQuery';

const validationSchema = yup.object({
  email: yup
    .string()
    .trim()
    .email('Please enter a valid email address')
    .required('Email is required.'),
  password: yup
    .string()
    .required('Please specify your password')
    .min(8, 'The password should have at minimum length of 8'),
});

const SidebarNewsletter = (): JSX.Element => {
  const theme = useTheme();
  const isMd = useMediaQuery(theme.breakpoints.up('md'), {
    defaultMatches: true,
  });

  const initialValues = {
    email: '',
    password: '',
  };

  const onSubmit = (values) => {
    return values;
  };

  const formik = useFormik({
    initialValues,
    validationSchema: validationSchema,
    onSubmit,
  });

  return (
    <Box
      component={Card}
      variant={'outlined'}
      padding={2}
      bgcolor={'transparent'}
    >
      <Grid container spacing={4}>
        {isMd ? (
          <Grid item container justifyContent={'center'} xs={12}>
            <Box height={1} width={1} maxWidth={'80%'}>
              <Box
                component={'img'}
                src={
                  'https://assets.maccarianagency.com/svg/illustrations/drawkit-illustration2.svg'
                }
                width={1}
                height={1}
                sx={{
                  filter:
                    theme.palette.mode === 'dark' ? 'brightness(0.8)' : 'none',
                }}
              />
            </Box>
          </Grid>
        ) : null}
        <Grid item xs={12}>
          <Typography
            variant="h6"
            sx={{
              fontWeight: 700,
              marginBottom: 2,
            }}
          >
            Please login to comment
          </Typography>
          <form onSubmit={formik.handleSubmit}>
            <Grid container spacing={2}>
              <Grid item xs={12}>
                <Typography variant={'subtitle2'} sx={{ marginBottom: 2 }}>
                  Enter your email
                </Typography>
                <TextField
                  label="Email *"
                  variant="outlined"
                  name={'email'}
                  fullWidth
                  value={formik.values.email}
                  onChange={formik.handleChange}
                  error={formik.touched.email && Boolean(formik.errors.email)}
                  // @ts-ignore
                  helperText={formik.touched.email && formik.errors.email}
                />
              </Grid>
              <Grid item xs={12}>
                <Box
                  display="flex"
                  flexDirection={{ xs: 'column', sm: 'row' }}
                  alignItems={{ xs: 'stretched', sm: 'center' }}
                  justifyContent={'space-between'}
                  width={1}
                  marginBottom={2}
                >
                  <Box marginBottom={{ xs: 1, sm: 0 }}>
                    <Typography variant={'subtitle2'}>
                      Enter your password
                    </Typography>
                  </Box>
                  <Typography variant={'subtitle2'}>
                    <Link
                      component={'a'}
                      color={'primary'}
                      href={'/password-reset-simple'}
                      underline={'none'}
                    >
                      Forgot your password?
                    </Link>
                  </Typography>
                </Box>
                <TextField
                  label="Password *"
                  variant="outlined"
                  name={'password'}
                  type={'password'}
                  fullWidth
                  value={formik.values.password}
                  onChange={formik.handleChange}
                  error={
                    formik.touched.password && Boolean(formik.errors.password)
                  }
                  // @ts-ignore
                  helperText={formik.touched.password && formik.errors.password}
                />
              </Grid>
              <Grid item container xs={12}>
                <Box
                  display="flex"
                  flexDirection={{ xs: 'column', sm: 'row' }}
                  alignItems={{ xs: 'stretched', sm: 'center' }}
                  justifyContent={'space-between'}
                  width={1}
                  maxWidth={600}
                  margin={'0 auto'}
                >
                  <Box marginBottom={{ xs: 1, sm: 0 }}>
                    <Typography variant={'subtitle2'}>
                      Don't have an account yet?{' '}
                      <Link
                        component={'a'}
                        color={'primary'}
                        href={'/signup-simple'}
                        underline={'none'}
                      >
                        Sign up here.
                      </Link>
                    </Typography>
                  </Box>
                  <Button size={'large'} variant={'contained'} type={'submit'}>
                    Login
                  </Button>
                </Box>
              </Grid>
            </Grid>
          </form>
        </Grid>
      </Grid>
    </Box>
  );
};

export default SidebarNewsletter;
