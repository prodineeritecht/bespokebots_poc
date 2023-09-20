import React, { useState } from 'react';
import { useTheme } from '@mui/material/styles';
import useMediaQuery from '@mui/material/useMediaQuery';
import Box from '@mui/material/Box';
import Pagination from '@mui/material/Pagination';

import { Topbar, Sidebar } from './components';

interface Props {
  children: React.ReactNode;
}

const SidebarFilters = ({ children }: Props): JSX.Element => {
  const theme = useTheme();
  const isMd = useMediaQuery(theme.breakpoints.up('md'), {
    defaultMatches: true,
  });

  const [openSidebar, setOpenSidebar] = useState(false);

  const handleSidebarOpen = (): void => {
    setOpenSidebar(true);
  };

  const handleSidebarClose = (): void => {
    setOpenSidebar(false);
  };

  const open = isMd ? false : openSidebar;

  return (
    <Box display={'flex'}>
      <Sidebar
        onClose={handleSidebarClose}
        open={open}
        variant={isMd ? 'permanent' : 'temporary'}
      />
      <Box marginLeft={{ xs: 0, md: 4 }} width={1}>
        <Topbar onSidebarOpen={handleSidebarOpen} />
        <Box paddingY={4}>{children}</Box>
        <Box display={'flex'} justifyContent={'center'} width={1}>
          <Pagination count={10} size={'large'} color="primary" />
        </Box>
      </Box>
    </Box>
  );
};

export default SidebarFilters;
