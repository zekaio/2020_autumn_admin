<template>
  <div class="index">
    <div>
      当前报名人数：{{ count }}
      <van-button
        style="margin-left: 20px"
        plain
        type="primary"
        @click="downloadExcel"
        >下载excel</van-button
      >
    </div>
    <van-pull-refresh v-model="refreshing" @refresh="onRefresh">
      <el-table :data="details" height="90vh" style="width: 100vw" border>
        <el-table-column
          fixed
          prop="name"
          label="姓名"
          width="180"
        ></el-table-column>
        <el-table-column
          prop="tel"
          label="手机号"
          width="200"
        ></el-table-column>
        <el-table-column prop="sex" label="性别" width="100"></el-table-column>
        <el-table-column prop="mail" label="邮箱" width="240"></el-table-column>
        <el-table-column
          prop="grade"
          label="年级"
          width="180"
        ></el-table-column>
        <el-table-column
          prop="campus"
          label="校区"
          width="180"
        ></el-table-column>
        <el-table-column
          prop="college"
          label="学院"
          width="240"
        ></el-table-column>
        <el-table-column
          prop="dormitory"
          label="宿舍"
          width="240"
        ></el-table-column>
        <el-table-column
          prop="first"
          label="第一志愿"
          width="240"
        ></el-table-column>
        <el-table-column
          prop="second"
          label="第二志愿"
          width="240"
        ></el-table-column>
        <el-table-column
          prop="adjust"
          label="是否服从调剂"
          width="120"
        ></el-table-column>
        <el-table-column prop="description" label="自我介绍" width="300">
        </el-table-column>
      </el-table>
    </van-pull-refresh>
  </div>
</template>

<script>
import { apis } from '../api/apis'
export default {
  name: 'index',
  data() {
    return {
      count: 0,
      details: [],
      refreshing: false,
    }
  },
  methods: {
    downloadExcel() {
      apis.excel().then((res) => {
        const url = window.URL.createObjectURL(res.data)
        const a = document.createElement('a')
        a.href = url
        a.download = window.localStorage.getItem('department')
          ? `${window.localStorage.getItem('department')}.xlsx`
          : '人员信息.xlsx'
        a.click()
      })
    },
    onRefresh() {
      apis.update(this.details[0] ? this.details[0].id : 0).then((res) => {
        console.log(res.data.data)
        this.details = [...res.data.data, ...this.details]
        this.refreshing = false
      })
      apis.count().then((res) => {
        this.count = res.data.data
      })
    },
  },
  async mounted() {
    apis.count().then((res) => {
      this.count = res.data.data
    })
    apis.get().then((res) => {
      this.details = [...this.details, ...res.data.data]
      console.log(this.details)
    })
  },
}
</script>

<style scoped></style>
