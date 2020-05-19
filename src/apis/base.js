import axios from 'axios';

const timeout = 3000;

const request = axios.create({
  baseURL: `${process.env.VUE_APP_APIPATH}`,
  headers: {
    'Content-Type': 'application/json',
    'x-api-key': `${process.env.VUE_APP_API_KEY}`,
  },
  timeout,
});

export { request as default }
