/* eslint-disable react/no-unescaped-entities */
import React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Breadcrumbs from '@mui/material/Breadcrumbs';
import Link from '@mui/material/Link';

import Fluid from 'layouts/Fluid';
import Container from 'components/Container';
import ResizableFrame from 'components/ResizableFrame';

const IndexView = (): JSX.Element => {
  return (
    <Fluid>
      <Box bgcolor={'alternate.main'}>
        <Container maxWidth={1500} paddingBottom={'16px !important'}>
          <Breadcrumbs aria-label="breadcrumb">
            <Link underline="hover" color="inherit" href="/blocks">
              Components
            </Link>
            <Link
              underline="hover"
              color="inherit"
              href="/blocks#js--blocks__index-section--application-ui"
            >
              Application UI
            </Link>
            <Typography color="text.primary">Tables</Typography>
          </Breadcrumbs>
        </Container>
        <Container maxWidth={1500} paddingY={'0 !important'}>
          <Box>
            <Typography variant={'h4'} fontWeight={700}>
              Tables
            </Typography>
            <Typography>
              Used to display data lists to your users in a clean, tabular
              format.
            </Typography>
          </Box>
        </Container>
        <ResizableFrame
          src={'/blocks/tables/with-avatars-and-multiline-content'}
          title={'With avatars and multiline content'}
          path={
            './src/blocks/tables/WithAvatarsAndMultilineContent/WithAvatarsAndMultilineContent.js|ts'
          }
        />
        <ResizableFrame
          src={'/blocks/tables/simple-striped'}
          title={'Simple striped'}
          path={'./src/blocks/tables/SimpleStriped/SimpleStriped.js|ts'}
        />
        <ResizableFrame
          src={'/blocks/tables/simple'}
          title={'Simple'}
          path={'./src/blocks/tables/Simple/Simple.js|ts'}
        />
      </Box>
    </Fluid>
  );
};

export default IndexView;
