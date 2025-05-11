import axios from 'axios'

// Axios instance for easier applying in redux 
export default axios.create({
 baseURL: 'http://localhost:8000/api',
});