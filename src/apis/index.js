import request from './base';

export const getUserCrops = async ({ lineId }) => {
  try {
    const body = {
      api: "getUserCrop",
      data: {
        lineId
      }
    }
    const response = await request.post('/', body)
    return response.data
  } catch (e) {
    throw new Error(e.message)
  }
}

export const getCrop = async ({ traceCode }) => {
  try {
    const body = {
      api: "getCrop",
      data: {
        traceCode
      }
    }
    const response = await request.post('/', body)
    return response.data
  } catch (e) {
    throw new Error(e.message)
  }
}

export const getAllCrop = async () => {
  try {
    const body = {
      api: "getCrop",
      data: {}
    }
    const response = await request.post('/', body)
    return response.data
  } catch (e) {
    throw new Error(e.message)
  }
}

export const createUser = async ({ lineId, name, profileImage }) => {
  try {
    const body = {
      api: "createUser",
      data: {
        lineId,
        name,
        profileImage
      }
    }
    const response = await request.post('/', body)
    return response.data
  } catch (e) {
    throw new Error(e.message)
  }
}

export const updateUserCrop = async ({ lineId, traceCode }) => {
  try {
    const body = {
      api: "updateUserCrop",
      data: {
        lineId,
        traceCode
      }
    }
    const response = await request.post('/', body)
    return response.data
  } catch (e) {
    throw new Error(e.message)
  }
}