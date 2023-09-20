import React, { useState, useEffect } from 'react';
import { useTheme } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';

import Container from 'components/Container';

const pages = [
  {
    id: 'general',
    href: '/account-general',
    title: 'General',
  },
  {
    id: 'security',
    href: '/account-security',
    title: 'Security',
  },
  {
    id: 'notifications',
    href: '/account-notifications',
    title: 'Notifications',
  },
  {
    id: 'billing',
    href: '/account-billing',
    title: 'Billing Information',
  },
];

interface Props {
  children: React.ReactNode;
}

const Page = ({ children }: Props): JSX.Element => {
  const [activeLink, setActiveLink] = useState('');
  useEffect(() => {
    setActiveLink(window && window.location ? window.location.pathname : '');
  }, []);

  const theme = useTheme();

  return (
    <Box>
      <Box bgcolor={'primary.main'} paddingY={4}>
        <Container>
          <Typography
            variant="h4"
            fontWeight={700}
            gutterBottom
            sx={{ color: 'common.white' }}
          >
            Account settings
          </Typography>
          <Typography variant="h6" sx={{ color: 'common.white' }}>
            Change account information and settings
          </Typography>
        </Container>
      </Box>
      <Container paddingTop={'0 !important'} marginTop={-8}>
        <Grid container spacing={4}>
          <Grid item xs={12} md={3}>
            <Card sx={{ boxShadow: 3 }}>
              <List
                disablePadding
                sx={{
                  display: { xs: 'inline-flex', md: 'flex' },
                  flexDirection: { xs: 'row', md: 'column' },
                  overflow: 'auto',
                  flexWrap: 'nowrap',
                  width: '100%',
                  paddingY: { xs: 3, md: 4 },
                  paddingX: { xs: 4, md: 0 },
                }}
              >
                {pages.map((item) => (
                  <ListItem
                    key={item.id}
                    component={'a'}
                    href={item.href}
                    disableGutters
                    sx={{
                      marginRight: { xs: 2, md: 0 },
                      flex: 0,
                      paddingX: { xs: 0, md: 3 },
                      borderLeft: {
                        xs: 'none',
                        md: '2px solid transparent',
                      },
                      borderLeftColor: {
                        md:
                          activeLink === item.href
                            ? theme.palette.primary.main
                            : 'transparent',
                      },
                    }}
                  >
                    <Typography
                      variant="subtitle1"
                      noWrap
                      color={
                        activeLink === item.href
                          ? 'text.primary'
                          : 'text.secondary'
                      }
                    >
                      {item.title}
                    </Typography>
                  </ListItem>
                ))}
              </List>
            </Card>
          </Grid>
          <Grid item xs={12} md={9}>
            <Card sx={{ boxShadow: 3, padding: 4 }}>{children}</Card>
          </Grid>
        </Grid>
      </Container>
    </Box>
  );
};

export default Page;
