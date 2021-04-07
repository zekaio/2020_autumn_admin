import axios from 'axios'
import { Toast } from 'vant'
import router from '../router'

const baseURL = 'http://localhost:5000'

// axios配置
export const instance = axios.create({
  baseURL,
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
})

export const blobInstance = axios.create({
  baseURL,
  withCredentials: true,
  responseType: 'blob',
})

function succFunc(res) {
  return Promise.resolve(res)
}

function failFunc(err) {
  if (!err.response) {
    Toast.fail({
      message: '服务器无法响应',
    })
  } else {
    switch (err.response.status) {
      // 未登录
      case 401:
        if (router.currentRoute.name != 'login') {
          Toast({
            message: '请先登录',
          })
          router.push({
            path: '/login',
          })
        }
        break
      // 服务器错误
      case 500:
        Toast.fail({
          message: '服务器错误',
        })
        break
      default:
        return Promise.reject(err)
    }
  }
  return new Promise(() => {})
}

instance.interceptors.response.use(succFunc, failFunc)
blobInstance.interceptors.response.use(succFunc, failFunc)
