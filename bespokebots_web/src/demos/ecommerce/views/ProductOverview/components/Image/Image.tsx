import React from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';

interface Props {
  images: Array<string>;
  title: string;
}

const Image = ({ images, title }: Props): JSX.Element => {
  return (
    <Grid container spacing={2} sx={{ height: 1 }}>
      {images.map((item, i) => (
        <Grid key={i} item xs={i === 0 ? 12 : 6}>
          <Box
            sx={{
              display: 'flex',
              height: 1,
              '& img': {
                width: 1,
                height: 1,
                objectFit: 'cover',
                borderRadius: 2,
              },
            }}
          >
            <img src={item} alt={title} loading={'lazy'} />
          </Box>
        </Grid>
      ))}
    </Grid>
  );
};

export default Image;
