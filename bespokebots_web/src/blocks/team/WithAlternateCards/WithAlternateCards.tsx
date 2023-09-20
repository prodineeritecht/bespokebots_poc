import React from 'react';
import { useTheme } from '@mui/material/styles';
import Card from '@mui/material/Card';
import Box from '@mui/material/Box';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import Avatar from '@mui/material/Avatar';
import Grid from '@mui/material/Grid';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import ListItemAvatar from '@mui/material/ListItemAvatar';

import Container from 'components/Container';

const mock = [
  {
    name: 'Clara Bertoletti',
    title: 'MUI lover',
    avatar: 'https://assets.maccarianagency.com/avatars/img4.jpg',
  },
  {
    name: 'Jhon Anderson',
    title: 'Senior Frontend Developer',
    avatar: 'https://assets.maccarianagency.com/avatars/img5.jpg',
  },
  {
    name: 'Chary Smith',
    title: 'SEO at Comoti',
    avatar: 'https://assets.maccarianagency.com/avatars/img6.jpg',
  },
  {
    name: 'Clara Bertoletti',
    title: 'MUI lover',
    avatar: 'https://assets.maccarianagency.com/avatars/img1.jpg',
  },
  {
    name: 'Jhon Anderson',
    title: 'Senior Frontend Developer',
    avatar: 'https://assets.maccarianagency.com/avatars/img2.jpg',
  },
  {
    name: 'Chary Smith',
    title: 'SEO at Comoti',
    avatar: 'https://assets.maccarianagency.com/avatars/img3.jpg',
  },
];

const WithAlternateCards = (): JSX.Element => {
  const theme = useTheme();

  return (
    <Container>
      <Box>
        <Box marginBottom={4}>
          <Typography
            sx={{
              textTransform: 'uppercase',
            }}
            gutterBottom
            color={'text.secondary'}
            align={'center'}
            fontWeight={700}
          >
            Our team
          </Typography>
          <Typography
            variant="h4"
            align={'center'}
            gutterBottom
            sx={{
              fontWeight: 700,
              marginTop: theme.spacing(1),
            }}
          >
            Small team. Big hearts.
          </Typography>
          <Typography variant="h6" align={'center'} color={'text.secondary'}>
            Our focus is always on finding the best people to work with. Our bar
            is high, but you look ready to take on the challenge.
          </Typography>
        </Box>
        <Grid container spacing={2}>
          {mock.map((item, i) => (
            <Grid item xs={12} md={4} key={i}>
              <Box
                width={1}
                height={1}
                component={Card}
                boxShadow={0}
                variant={'outlined'}
                bgcolor={'alternate.main'}
              >
                <CardContent sx={{ padding: 3 }}>
                  <ListItem component="div" disableGutters sx={{ padding: 0 }}>
                    <ListItemAvatar sx={{ marginRight: 3 }}>
                      <Avatar
                        src={item.avatar}
                        variant={'rounded'}
                        sx={{ width: 100, height: 100, borderRadius: 2 }}
                      />
                    </ListItemAvatar>
                    <ListItemText
                      sx={{ margin: 0 }}
                      primary={item.name}
                      secondary={item.title}
                      primaryTypographyProps={{
                        variant: 'h6',
                        fontWeight: 700,
                      }}
                      secondaryTypographyProps={{ variant: 'subtitle1' }}
                    />
                  </ListItem>
                </CardContent>
              </Box>
            </Grid>
          ))}
        </Grid>
      </Box>
    </Container>
  );
};

export default WithAlternateCards;
