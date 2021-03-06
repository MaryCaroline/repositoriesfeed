import axios from 'axios';
import Cookies from 'js-cookie';
import { fetchRepositories, followRepository, fetchUserRepositories } from './repositories';
import { fetchCommits, fetchCommitsByRepository } from './commits';
import postLogout from './auth';

axios.interceptors.request.use((config) => {
  const token = Cookies.get('rfeedtoken');
  if (token != null) {
    // eslint-disable-next-line no-param-reassign
    config.headers.Authorization = `Token ${token}`;
  }
  return config;
}, (err) => {
  Promise.reject(err);
});

export {
  fetchRepositories,
  followRepository,
  fetchUserRepositories,
  fetchCommitsByRepository,
  fetchCommits,
  postLogout,
};
