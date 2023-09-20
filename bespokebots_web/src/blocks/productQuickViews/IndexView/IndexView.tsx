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
              href="/blocks#js--blocks__index-section--e-commerce"
            >
              E-commerce
            </Link>
            <Typography color="text.primary">Product Quick Views</Typography>
          </Breadcrumbs>
        </Container>
        <Container maxWidth={1500} paddingY={'0 !important'}>
          <Box>
            <Typography variant={'h4'} fontWeight={700}>
              Product Quick Views
            </Typography>
            <Typography>
              Used to quickly explore a product's detail within a modal dialog.
            </Typography>
          </Box>
        </Container>
        <ResizableFrame
          src={'/blocks/product-quick-views/popup-box-with-product-details'}
          title={'Popup box with product details'}
          path={
            './src/blocks/productQuickViews/PopupBoxWithProductDetails/PopupBoxWithProductDetails.js|ts'
          }
          iframeStyles={{ minHeight: 800 }}
        />
      </Box>
    </Fluid>
  );
};

export default IndexView;
