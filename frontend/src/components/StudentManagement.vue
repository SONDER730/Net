<template>
  <div>
    <el-button @click="goBack" type="primary">Back</el-button>
    <h2>学生管理</h2>
    <el-table :data="studentData" stripe style="width: 100%; background-color: white;">
      <!-- 序号列 -->
      <el-table-column type="index" label="序号" width="50"></el-table-column>

      <!-- 学生姓名列 -->
      <el-table-column prop="name" label="姓名"></el-table-column>

      <!-- 报名状态列 -->
      <el-table-column prop="registrationStatus" label="报名状态"></el-table-column>

      <!-- 性别列 -->
      <el-table-column prop="gender" label="性别"></el-table-column>

      <!-- 年级列 -->
      <el-table-column prop="grade" label="年级"></el-table-column>

      <!-- 学校列 -->
      <el-table-column prop="school" label="学校"></el-table-column>

      <!-- 指导老师列 -->
      <el-table-column prop="teacher" label="指导老师"></el-table-column>

      <!-- 资质证书列 -->
      <el-table-column prop="certificate" label="资质证书"></el-table-column>

      <!-- 操作列 -->
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button size="small" type="primary" @click="editStudent(scope.row.id)">修改</el-button>
          <el-button size="small" type="danger" @click="deleteStudent(scope.row.id)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  props: {
    studentData: Array // 从父组件传递学生数据
  },
  methods: {
    goBack() {
      this.$emit('back'); // 触发父组件的返回事件
    },
    editStudent(id) {
      console.log('修改学生信息', id);
      // 实现修改学生信息的逻辑
    },
    deleteStudent(id) {
      console.log('删除学生', id);
      // 实现删除学生的逻辑
    }
  }
};
</script>

<style scoped>
.el-button {
  margin-bottom: 20px;
}
.el-table {
  background-color: white;
  box-shadow: 0 2px 12px 0 rgba(0,0,0,0.1);
}
</style>
