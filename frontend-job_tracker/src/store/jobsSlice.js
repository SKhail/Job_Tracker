import axios from 'axios'
import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";


// Fetch all jobs 
export const fetchJobs = createAsyncThunk('jobs/fetchJobs', async () => {
 const response = await axios.get('/jobs/');
 return await response.json();
});

const jobsSlice = createSlice({
 name: 'jobs',
 initialState: {
  items: [],
  status: 'idle',
  error: null,
 },
 reducers: {},
 extraReducers: (builder) => {
  builder
   .addCase(fetchJobs.pending, (state) => {
    state.status = 'loading';

   })
   .addCase(fetchJobs.fulfilled, (state, action) => {
    state.status = 'succeeded';
    state.items = action.payload;
   })
   .addCase(fetchJobs.rejected, (state, action) => {
    state.status = 'failed';
    state.items = action.error.message;
   })
 },
});

export default jobsSlice.reducer