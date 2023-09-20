import React from 'react';
import { alpha, useTheme } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import Link from '@mui/material/Link';
import { colors } from '@mui/material';

const mock = [
  {
    title: 'Main Demo',
    description:
      'Main demo comes with 18 landing pages, including over 35 commonly used pages that can be combined with demos.',
    illustration:
      'https://assets.maccarianagency.com/screenshots/the-front-main-demo.png',
    illustrationDark:
      'https://assets.maccarianagency.com/screenshots/the-front-main-demo--dark.png',
    href: '/home',
    pages: 53,
    btnText: 'Preview Main Demo',
    bgcolor: 'blue',
  },
  {
    title: 'E-Commerce Demo',
    description:
      'Everything you need to build beautiful, responsive, fully coded e-commerce websites and shop applications.',
    illustration:
      'https://assets.maccarianagency.com/screenshots/the-front-ecommerce-demo.png',
    illustrationDark:
      'https://assets.maccarianagency.com/screenshots/the-front-ecommerce-demo--dark.png',
    href: '/demos/ecommerce',
    pages: 9,
    btnText: 'Preview E-commerce Demo',
    bgcolor: 'pink',
  },
];

const Demos = (): JSX.Element => {
  const theme = useTheme();

  return (
    <Box>
      <Box>
        <Typography
          variant={'h3'}
          fontWeight={700}
          align={'center'}
          gutterBottom
        >
          Ready to use, complete demo pages
          <br />
          for your MUI project
        </Typography>
        <Typography variant={'h6'} color={'text.secondary'} align={'center'}>
          Professionally designed, fully responsive, expertly crafted
          <br />
          demo pages you can use in your MUI projects and customize to your
          heart’s content.
        </Typography>
      </Box>
      <Box>
        {mock.map((item, i) => (
          <Grid
            key={i}
            container
            spacing={{ xs: 4, sm: 6, md: 8 }}
            sx={{ my: { xs: 4, sm: 6, md: 8 } }}
          >
            <Grid item alignItems={'center'} xs={12} md={6}>
              <Stack
                sx={{
                  alignItems: 'flex-start',
                  justifyContent: 'center',
                  width: 1,
                  height: 1,
                }}
                spacing={{ xs: 2, sm: 4 }}
              >
                <Box
                  sx={{
                    p: '4px 8px',
                    borderRadius: 2,
                    border: `1px solid ${theme.palette.text.primary}`,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                  }}
                >
                  <Typography variant={'caption'} fontWeight={700}>
                    {item.pages} pages
                  </Typography>
                </Box>
                <Box>
                  <Typography
                    variant={'h4'}
                    gutterBottom
                    sx={{ fontWeight: 700 }}
                  >
                    {item.title}
                  </Typography>
                  <Typography color="text.secondary" variant={'h6'}>
                    {item.description}
                  </Typography>
                </Box>
                <Button
                  component={Link}
                  href={item.href}
                  target={'_blank'}
                  size={'large'}
                  variant={'contained'}
                  endIcon={
                    <Box
                      component={'svg'}
                      xmlns="http://www.w3.org/2000/svg"
                      fill="currentColor"
                      viewBox="0 0 20 20"
                      width={24}
                      height={24}
                    >
                      <path d="M11 3a1 1 0 100 2h2.586l-6.293 6.293a1 1 0 101.414 1.414L15 6.414V9a1 1 0 102 0V4a1 1 0 00-1-1h-5z" />
                      <path d="M5 5a2 2 0 00-2 2v8a2 2 0 002 2h8a2 2 0 002-2v-3a1 1 0 10-2 0v3H5V7h3a1 1 0 000-2H5z" />
                    </Box>
                  }
                >
                  {item.btnText}
                </Button>
              </Stack>
            </Grid>
            <Grid item xs={12} md={6}>
              <Box position={'relative'} width={1} height={1}>
                <Box
                  component={'img'}
                  src={`${
                    theme.palette.mode === 'light'
                      ? item.illustration
                      : item.illustrationDark
                  }`}
                  alt={item.title}
                  loading={'lazy'}
                  sx={{
                    boxShadow: 3,
                    borderRadius: 2,
                    position: 'relative',
                    width: 1,
                    height: 1,
                    zIndex: 2,
                  }}
                />
                <Box
                  sx={{
                    position: 'absolute',
                    width: 1,
                    height: 1,
                    bgcolor:
                      theme.palette.mode === 'dark'
                        ? alpha(colors[item.bgcolor][50], 0.5)
                        : colors[item.bgcolor][50],
                    borderRadius: 2,
                    zIndex: 1,
                    top: {
                      xs: theme.spacing(2),
                      sm: theme.spacing(3),
                      md: theme.spacing(4),
                    },
                    left: {
                      xs: theme.spacing(-2),
                      sm: theme.spacing(-3),
                      md: theme.spacing(-4),
                    },
                  }}
                />
              </Box>
            </Grid>
          </Grid>
        ))}
      </Box>
    </Box>
  );
};

export default Demos;
