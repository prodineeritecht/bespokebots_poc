import React from 'react';
import { useTheme } from '@mui/material/styles';
import useMediaQuery from '@mui/material/useMediaQuery';
import Box from '@mui/material/Box';
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';

const Gallery = (): JSX.Element => {
  const theme = useTheme();

  const isMd = useMediaQuery(theme.breakpoints.up('md'), {
    defaultMatches: true,
  });

  const photos = [
    {
      src: 'https://assets.maccarianagency.com/backgrounds/img25.jpg',
      source: 'https://assets.maccarianagency.com/backgrounds/img25.jpg',
      rows: 1,
      cols: 2,
    },
    {
      src: 'https://assets.maccarianagency.com/backgrounds/img22.jpg',
      source: 'https://assets.maccarianagency.com/backgrounds/img22.jpg',
      rows: 1,
      cols: 1,
    },
    {
      src: 'https://assets.maccarianagency.com/backgrounds/img24.jpg',
      source: 'https://assets.maccarianagency.com/backgrounds/img24.jpg',
      rows: 1,
      cols: 1,
    },
    {
      src: 'https://assets.maccarianagency.com/backgrounds/img21.jpg',
      source: 'https://assets.maccarianagency.com/backgrounds/img21.jpg',
      rows: 1,
      cols: 2,
    },
  ];

  return (
    <Box>
      <ImageList
        variant="quilted"
        cols={3}
        rowHeight={isMd ? 300 : 200}
        gap={isMd ? 16 : 4}
      >
        {photos.map((item, i) => (
          <ImageListItem key={i} cols={item.cols} rows={item.rows}>
            <img
              height={'100%'}
              width={'100%'}
              src={item.src}
              alt="..."
              loading="lazy"
              style={{
                objectFit: 'cover',
                filter:
                  theme.palette.mode === 'dark' ? 'brightness(0.7)' : 'none',
                cursor: 'poiner',
                borderRadius: 8,
              }}
            />
          </ImageListItem>
        ))}
      </ImageList>
    </Box>
  );
};

export default Gallery;
