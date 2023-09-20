import React from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';

const mock = [
  {
    title: 'Can I purchase a gift certificate?',
    subtitle:
      'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.',
  },
  {
    title: 'What is your return policy?',
    subtitle:
      'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.',
  },
  {
    title: 'Do you sell gift cards?',
    subtitle:
      'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.',
  },
  {
    title: 'Can I change plans later on?',
    subtitle:
      'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.',
  },
  {
    title: 'Is this a subscription service?',
    subtitle:
      'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.',
  },
  {
    title: 'Can I purchase a gift certificate?',
    subtitle:
      'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.',
  },
];

const Faq = (): JSX.Element => {
  return (
    <Box>
      <Box marginBottom={4}>
        <Typography fontWeight={700} variant={'h4'} align={'center'}>
          Frequently asked questions
        </Typography>
      </Box>
      <Grid container spacing={4}>
        {mock.map((item, i) => (
          <Grid key={i} item xs={12} sm={6} md={4}>
            <Typography variant={'h6'} fontWeight={600} gutterBottom>
              {item.title}
            </Typography>
            <Typography color="text.secondary">{item.subtitle}</Typography>
          </Grid>
        ))}
      </Grid>
    </Box>
  );
};

export default Faq;
