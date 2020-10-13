import Vue from 'vue';
import VueRouter from 'vue-router';
import index from './views/index.vue';
import login from './views/login.vue';

Vue.use(VueRouter);

const routerPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
  return routerPush.call(this, location).catch(error => error);
};

const routes = [
  {
    path: '/login',
    component: login,
  },
  {
    path: '/index',
    component: index,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
