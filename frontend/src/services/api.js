import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000',
  withCredentials: false, // CORS 문제를 해결하기 위한 옵션
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  }
});

export default {
  getTransactions() {
    return apiClient.get('/transactions/');
  },
  createTransaction(transaction) {
    return apiClient.post('/transactions/', transaction);
  }
}
