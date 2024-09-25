import axios from 'axios';

const API_URL = 'http://localhost:8000'; // FastAPI 서버 URL

export const fetchTransactions = async () => {
  const response = await axios.get(`${API_URL}/transactions/`);
  return response.data;
};

export const createTransaction = async (transaction) => {
  const response = await axios.post(`${API_URL}/transactions/`, transaction);
  return response.data;
};

export const login = async (username, password) => {
  const response = await axios.post(`${API_URL}/token`, new URLSearchParams({
    username,
    password,
  }));
  return response.data;
};

export const fetchUser = async (token) => {
  const response = await axios.get(`${API_URL}/users/me`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return response.data;
};
