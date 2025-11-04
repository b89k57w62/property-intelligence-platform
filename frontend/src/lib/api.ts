import axios from 'axios'
import type {
  PropertyTransaction,
  PropertyPresale,
  PropertyRental,
  SearchResponse,
  SearchParams
} from '@/types/property'

const API_BASE_URL = 'http://localhost:8000/api/v1'

// Create axios instance
export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Transactions API
export const transactionsApi = {
  getAll: async (params?: SearchParams) => {
    const { data } = await apiClient.get<SearchResponse<PropertyTransaction>>(
      '/transactions',
      { params }
    )
    return data
  },

  getById: async (id: number) => {
    const { data } = await apiClient.get<PropertyTransaction>(
      `/transactions/${id}`
    )
    return data
  },
}

// Presales API
export const presalesApi = {
  getAll: async (params?: SearchParams) => {
    const { data } = await apiClient.get<SearchResponse<PropertyPresale>>(
      '/presales',
      { params }
    )
    return data
  },

  getById: async (id: number) => {
    const { data } = await apiClient.get<PropertyPresale>(
      `/presales/${id}`
    )
    return data
  },
}

// Rentals API
export const rentalsApi = {
  getAll: async (params?: SearchParams) => {
    const { data } = await apiClient.get<SearchResponse<PropertyRental>>(
      '/rentals',
      { params }
    )
    return data
  },

  getById: async (id: number) => {
    const { data } = await apiClient.get<PropertyRental>(
      `/rentals/${id}`
    )
    return data
  },
}

