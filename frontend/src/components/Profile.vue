<!-- Profile.vue -->
<template>
  <div class="profile">
    <h2>个人信息</h2>
    <div v-if="userRole === 'student'">
      <h3>学生信息</h3>
      <p>姓名: {{ user.name }}</p>
      <p>学号: {{ user.student-id }}</p>
      <!-- 更多学生信息 -->
    </div>

    <div v-if="userRole === 'teacher'">
      <h3>教师信息</h3>
      <p>姓名: {{ user.name }}</p>
      <p>工号: {{ user.teacherId }}</p>
      <!-- 更多教师信息 -->
    </div>
  </div>
</template>

<script>
export default {
  props: {
    userRole: {
      type: String,
      required: true,
    },
    user: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
/* 个人信息样式 */
.profile {
  padding: 20px;
  background-color: #f5f5f5;
}
</style>
