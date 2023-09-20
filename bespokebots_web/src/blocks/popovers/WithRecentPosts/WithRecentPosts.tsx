import React, { useState } from 'react';
import { useTheme } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Popover from '@mui/material/Popover';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import ListItemIcon from '@mui/material/ListItemIcon';
import Avatar from '@mui/material/Avatar';
import Link from '@mui/material/Link';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';

import Container from 'components/Container';

const mock = [
  {
    title: 'Themeable',
    subtitle:
      'Customize any part of our components to match your design needs.',
    icon: (
      <svg
        height={24}
        width={24}
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth={2}
          d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"
        />
      </svg>
    ),
  },
  {
    title: 'Light and dark UI',
    subtitle:
      'Optimized for multiple color modes. Use light or dark, your choice.',
    icon: (
      <svg
        height={24}
        width={24}
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth={2}
          d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"
        />
      </svg>
    ),
  },
  {
    title: 'Composable',
    subtitle:
      'Designed with composition in mind. Compose new components with ease.',
    icon: (
      <svg
        height={24}
        width={24}
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth={2}
          d="M11 4a2 2 0 114 0v1a1 1 0 001 1h3a1 1 0 011 1v3a1 1 0 01-1 1h-1a2 2 0 100 4h1a1 1 0 011 1v3a1 1 0 01-1 1h-3a1 1 0 01-1-1v-1a2 2 0 10-4 0v1a1 1 0 01-1 1H7a1 1 0 01-1-1v-3a1 1 0 00-1-1H4a2 2 0 110-4h1a1 1 0 001-1V7a1 1 0 011-1h3a1 1 0 001-1V4z"
        />
      </svg>
    ),
  },
  {
    title: 'Developer experience',
    subtitle:
      'Guaranteed to boost your productivity when building your app or website.',
    icon: (
      <svg
        height={24}
        width={24}
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth={2}
          d="M13 10V3L4 14h7v7l9-11h-7z"
        />
      </svg>
    ),
  },
  {
    title: 'Continuous updates',
    subtitle: 'We continually deploy improvements and new updates to theFront.',
    icon: (
      <svg
        height={24}
        width={24}
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth={2}
          d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
        />
      </svg>
    ),
  },
  {
    title: 'Free support',
    subtitle:
      '6 months of free technical support to help you build your website faster.',
    icon: (
      <svg
        height={24}
        width={24}
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth={2}
          d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
        />
      </svg>
    ),
  },
];

const WithRecentPosts = (): JSX.Element => {
  const theme = useTheme();
  const [open, setOpen] = useState(false);
  const [anchorEl, setAnchorEl] = useState(null);
  const handleClick = (event): void => {
    setAnchorEl(event.target);
    setOpen(true);
  };

  const handleClose = (): void => {
    setAnchorEl(null);
    setOpen(false);
  };

  return (
    <Container>
      <Box display={'flex'} justifyContent={'center'}>
        <Box
          display={'flex'}
          alignItems={'center'}
          sx={{ cursor: 'pointer' }}
          onClick={(e) => handleClick(e)}
        >
          <Typography>Solutions</Typography>
          <ExpandMoreIcon
            sx={{
              marginLeft: 0.5,
              width: 16,
              height: 16,
              transform: open ? 'rotate(180deg)' : 'none',
            }}
          />
        </Box>
        <Popover
          elevation={1}
          open={open}
          anchorEl={anchorEl}
          onClose={handleClose}
          anchorOrigin={{
            vertical: 'bottom',
            horizontal: 'center',
          }}
          transformOrigin={{
            vertical: 'top',
            horizontal: 'center',
          }}
          sx={{
            '.MuiPaper-root': {
              marginTop: 2,
            },
          }}
        >
          <Stack spacing={2} maxWidth={460}>
            <List
              sx={{
                width: '100%',
                padding: 2,
              }}
            >
              {mock.map((item, i) => (
                <ListItem
                  key={i}
                  component={Link}
                  href={'#'}
                  alignItems={'flex-start'}
                >
                  <ListItemIcon sx={{ minWidth: 'auto', marginRight: 2 }}>
                    <Box
                      component={Avatar}
                      width={40}
                      height={40}
                      bgcolor={theme.palette.primary.main}
                      color={theme.palette.background.paper}
                      variant={'rounded'}
                    >
                      {item.icon}
                    </Box>
                  </ListItemIcon>
                  <ListItemText
                    primary={item.title}
                    secondary={item.subtitle}
                    primaryTypographyProps={{
                      fontWeight: 700,
                      color: 'text.primary',
                    }}
                  />
                </ListItem>
              ))}
            </List>
            <Stack
              direction={'column'}
              spacing={1}
              padding={2}
              bgcolor={'alternate.main'}
            >
              <Typography
                color={'text.secondary'}
                marginBottom={1}
                sx={{ textTransform: 'uppercase' }}
              >
                Recent posts
              </Typography>
              <Link color={'text.primary'} href={'#'} underline={'none'}>
                Boost your conversion rate
              </Link>
              <Link color={'text.primary'} href={'#'} underline={'none'}>
                How to use search engine optimization
              </Link>
              <Link color={'text.primary'} href={'#'} underline={'none'}>
                Improve your customer experience
              </Link>
              <Box display={'flex'} justifyContent={'flex-end'}>
                <Button
                  size={'large'}
                  endIcon={
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width={20}
                      height={20}
                      viewBox="0 0 20 20"
                      fill="currentColor"
                    >
                      <path
                        fillRule="evenodd"
                        d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z"
                        clipRule="evenodd"
                      />
                    </svg>
                  }
                >
                  Show all
                </Button>
              </Box>
            </Stack>
          </Stack>
        </Popover>
      </Box>
    </Container>
  );
};

export default WithRecentPosts;
