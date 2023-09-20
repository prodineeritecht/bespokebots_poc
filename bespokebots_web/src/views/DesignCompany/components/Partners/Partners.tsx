import React from 'react';
import { useTheme } from '@mui/material/styles';
import Box from '@mui/material/Box';

const Partners = (): JSX.Element => {
  const theme = useTheme();
  return (
    <Box display="flex" flexWrap="wrap" justifyContent={'center'}>
      {[
        'https://assets.maccarianagency.com/svg/logos/airbnb-original.svg',
        'https://assets.maccarianagency.com/svg/logos/amazon-original.svg',
        'https://assets.maccarianagency.com/svg/logos/fitbit-original.svg',
        'https://assets.maccarianagency.com/svg/logos/netflix-original.svg',
        'https://assets.maccarianagency.com/svg/logos/google-original.svg',
        'https://assets.maccarianagency.com/svg/logos/paypal-original.svg',
      ].map((item, i) => (
        <Box maxWidth={90} marginTop={2} marginRight={4} key={i}>
          <Box
            component="img"
            height={1}
            width={1}
            src={item}
            alt="..."
            sx={{
              filter:
                theme.palette.mode === 'dark'
                  ? 'brightness(0) invert(0.7)'
                  : 'brightness(0)',
            }}
          />
        </Box>
      ))}
    </Box>
  );
};

export default Partners;
