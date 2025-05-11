import { configureStore } from '@reduxjs/toolkit'
import jobReducer from './jobsSlice'

export const store = configureStore({
 reducer: {
  jobs: jobReducer
 },
});