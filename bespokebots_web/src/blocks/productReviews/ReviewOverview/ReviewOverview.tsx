import React from 'react';
import { useTheme } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';

import Container from 'components/Container';

const mock = [
  {
    score: 4,
    title: 'Love this product!',
    feedback:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    subtitle: 'by Christopher, July 15h 2020',
  },
  {
    score: 5,
    title: 'Great price & quality',
    feedback:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    subtitle: 'by Sarah, July 14h 2020',
  },
  {
    score: 5,
    title: 'Highly recommended',
    feedback:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    subtitle: 'by Toby, July 13h 2020',
  },
  {
    score: 5,
    title: 'Best watch I have ever bought',
    feedback:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    subtitle: 'by Dakota, July 12h 2020',
  },
  {
    score: 5,
    title: 'First class customer service',
    feedback:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    subtitle: 'by Pheobe, July 11th 2020',
  },
  {
    score: 4,
    title: 'Love my new watch',
    feedback:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    subtitle: 'by George, July 10th 2020',
  },
];

const ReviewOverview = (): JSX.Element => {
  const theme = useTheme();

  return (
    <Container display={'flex'} justifyContent={'center'} alignItems={'center'}>
      <Grid container spacing={4}>
        <Grid item xs={12}>
          <Box
            sx={{
              display: 'flex',
              flexDirection: { xs: 'column', md: 'row' },
              alignItems: { xs: 'flex-start', md: 'center' },
              justifyContent: { md: 'space-between' },
            }}
          >
            <Box>
              <Typography variant={'h4'} fontWeight={700} marginBottom={1}>
                Customer reviews
              </Typography>
              <Box display={'flex'} alignItems={'center'}>
                <Box display={'flex'} alignItems={'center'}>
                  {[1, 2, 3, 4, 5].map((r) => (
                    <Box
                      key={r}
                      component={'svg'}
                      color={
                        r <= 4
                          ? theme.palette.primary.main
                          : theme.palette.divider
                      }
                      width={24}
                      height={24}
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 20 20"
                      fill="currentColor"
                    >
                      <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                    </Box>
                  ))}
                </Box>
                <Typography color={'text.secondary'} marginLeft={1}>
                  Based on 12 reviews
                </Typography>
              </Box>
            </Box>
            <Button
              size={'large'}
              variant={'contained'}
              sx={{
                marginTop: { xs: 2, md: 0 },
              }}
            >
              Write a review
            </Button>
          </Box>
        </Grid>
        <Grid item xs={12}>
          <Divider />
        </Grid>
        {mock.map((item, i) => (
          <Grid key={i} xs={12} sm={6} item>
            <Box display={'flex'} alignItems={'center'}>
              {[1, 2, 3, 4, 5].map((r) => (
                <Box
                  key={r}
                  component={'svg'}
                  color={
                    r <= item.score
                      ? theme.palette.primary.main
                      : theme.palette.divider
                  }
                  width={20}
                  height={20}
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                </Box>
              ))}
            </Box>
            <Typography variant={'caption'} color={'text.secondary'}>
              {item.subtitle}
            </Typography>
            <Typography marginY={1}>{item.title}</Typography>
            <Typography>{item.feedback}</Typography>
          </Grid>
        ))}
        <Grid container item xs={12} justifyContent={'center'}>
          <Button
            size={'large'}
            variant={'outlined'}
            endIcon={
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                width={20}
                height={20}
              >
                <path
                  fillRule="evenodd"
                  d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                  clipRule="evenodd"
                />
              </svg>
            }
          >
            Load more
          </Button>
        </Grid>
      </Grid>
    </Container>
  );
};

export default ReviewOverview;
