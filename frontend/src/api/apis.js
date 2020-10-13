import { instance, blobInstance } from './config';

export let apis = {
  // 登录
  login: (username, password) => {
    return instance({
      url: '/admin/session',
      method: 'post',
      data: JSON.stringify({
        username,
        password,
      }),
    });
  },

  // 获取信息
  get: () => {
    return instance({
      url: `/admin/user/detail`,
      method: 'get',
    });
  },

  // 下拉刷新
  update: first_id => {
    return instance({
      url: `/admin/user/detail/update?first_id=${first_id}`,
      method: 'get',
    });
  },

  // 获取excel
  excel: () => {
    return blobInstance({
      url: '/admin/user/excel',
      method: 'get',
    });
  },

  // 获取报名人数
  count: () => {
    return instance({
      url: '/admin/user/count',
      method: 'get',
    });
  },
};
