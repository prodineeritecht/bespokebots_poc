import React from 'react';
import { alpha, useTheme } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Divider from '@mui/material/Divider';
import AppBar from '@mui/material/AppBar';

import Container from 'components/Container';
import { Topbar, Footer } from './components';

const ChildMock = (): JSX.Element => {
  const theme = useTheme();
  return (
    <Container>
      <Box
        width={1}
        height={1}
        minHeight={800}
        borderRadius={2}
        border={`2px solid ${theme.palette.divider}`}
        sx={{
          borderStyle: 'dashed',
        }}
      />
    </Container>
  );
};

const WithNarrowLayoutAndNoSidebar = (): JSX.Element => {
  const theme = useTheme();
  return (
    <Box>
      <AppBar
        position={'fixed'}
        sx={{
          backgroundColor: theme.palette.background.paper,
          borderBottom: `1px solid ${alpha(theme.palette.divider, 0.1)}`,
        }}
        elevation={0}
      >
        <Container paddingY={{ xs: 1, sm: 1.5 }}>
          <Topbar />
        </Container>
      </AppBar>
      <main>
        <Box height={{ xs: 58, sm: 66, md: 71 }} />
        <Box display="flex" flex="1 1 auto" overflow="hidden">
          <Box display="flex" flex="1 1 auto" overflow="hidden">
            <Box flex="1 1 auto" height="100%" overflow="auto">
              <ChildMock />
              <Divider />
              <Container paddingY={4}>
                <Footer />
              </Container>
            </Box>
          </Box>
        </Box>
      </main>
    </Box>
  );
};

export default WithNarrowLayoutAndNoSidebar;
