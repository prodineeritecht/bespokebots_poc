import React from 'react';
import Drawer from '@mui/material/Drawer';
import Box from '@mui/material/Box';
import Divider from '@mui/material/Divider';
import Button from '@mui/material/Button';

import {
  FilterSize,
  FilterBrand,
  FilterColor,
  FilterPrice,
  FilterGender,
  FilterCategory,
} from './components';

interface Props {
  // eslint-disable-next-line @typescript-eslint/ban-types
  onClose: () => void;
  open: boolean;
  variant: 'permanent' | 'persistent' | 'temporary' | undefined;
}

const Sidebar = ({ open, variant, onClose }: Props): JSX.Element => {
  return (
    <Drawer
      anchor="left"
      onClose={() => onClose()}
      open={open}
      variant={variant}
      sx={{
        '& .MuiPaper-root': {
          position: 'relative',
          width: '100%',
          maxWidth: { xs: 300, md: 260 },
          minWidth: { xs: 300, md: 260 },
          border: 0,
          zIndex: 1100,
        },
      }}
    >
      <Box paddingY={{ xs: 2, md: 1 }} paddingX={{ xs: 2, md: 0 }}>
        <FilterPrice />
        <Divider sx={{ my: 3 }} />
        <FilterCategory />
        <Divider sx={{ my: 3 }} />
        <FilterGender />
        <Divider sx={{ my: 3 }} />
        <FilterBrand />
        <Divider sx={{ my: 3 }} />
        <FilterSize />
        <Divider sx={{ my: 3 }} />
        <FilterColor />
        <Button variant={'outlined'} size={'large'} fullWidth sx={{ mt: 3 }}>
          Reset all
        </Button>
      </Box>
    </Drawer>
  );
};

export default Sidebar;
