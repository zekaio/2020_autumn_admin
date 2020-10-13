import Vue from 'vue';
import App from './App.vue';
import router from './router';
import { Button, Form, Field, PullRefresh, List } from 'vant';
import { Table, TableColumn } from 'element-ui';

Vue.config.productionTip = false;

Vue.use(Button)
  .use(Form)
  .use(Field)
  .use(PullRefresh)
  .use(List)
  .use(Table)
  .use(TableColumn);

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
