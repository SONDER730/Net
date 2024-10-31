<template>
  <FormContainer
    welcomeTitle="欢迎注册"
    welcomeMessage="请填写以下信息完成注册，并选择您的身份"
    buttonText="了解更多"
  >
    <!-- 表单部分通过插槽传递 -->
    <template v-slot:form>
      <h2 class="signup-title">注册</h2>
<!--      <p class="signup-subtitle">请填写您的账号、密码、邮箱和身份</p>-->

      <!-- 注册表单 -->
      <el-form :model="signupForm" ref="signupForm" :rules="rules" class="signup-form" label-position="top">
        <!-- 身份选择 -->
        <el-form-item label="请选择您的身份" prop="role">
          <el-radio-group v-model="signupForm.role" size="large">
            <el-radio label="student">学生</el-radio>
            <el-radio label="teacher">教师</el-radio>
          </el-radio-group>
        </el-form-item>

        <!-- 账号 -->
        <el-form-item v-if="signupForm.role === 'student'" label="学号" prop="student_id">
  <el-input
    v-model="signupForm.student_id"
    placeholder="请输入学号"
    class="input-field"
    size="large"
  />
</el-form-item>

<el-form-item v-if="signupForm.role === 'teacher'" label="教工号" prop="teacher_id">
  <el-input
    v-model="signupForm.teacher_id"
    placeholder="请输入教工号"
    class="input-field"
    size="large"
  />
</el-form-item>

        <!-- 密码 -->
        <el-form-item label="密码" prop="password">
          <el-input
            v-model="signupForm.password"
            placeholder="请输入密码"
            type="password"
            class="input-field"
            prefix-icon="el-icon-lock"
            size="large"
          />
        </el-form-item>

        <!-- 确认密码 -->
        <el-form-item label="确认密码" prop="confirmPassword">
          <el-input
            v-model="signupForm.confirmPassword"
            placeholder="请再次输入密码"
            type="password"
            class="input-field"
            prefix-icon="el-icon-lock"
            size="large"
          />
        </el-form-item>

        <!-- 邮箱 -->
        <el-form-item label="邮箱" prop="email">
          <el-input
            v-model="signupForm.email"
            placeholder="请输入邮箱地址"
            class="input-field"
            prefix-icon="el-icon-message"
            size="large"
          />
        </el-form-item>

        <!-- 注册按钮 -->
        <el-form-item>
          <el-button type="primary" class="signup-btn" @click="onSignup">注册</el-button>
        </el-form-item>
      </el-form>

      <!-- 注册选项 -->
      <div class="signup-options">
        <router-link to="/login" class="login-link">已有账号? 立即登录</router-link>
      </div>
    </template>
  </FormContainer>
</template>

<script>
import FormContainer from '@/components/FormContainer.vue';

import axios from 'axios';

export default {
  name: 'SignupView',
  components: {
    FormContainer,  // 注册 FormContainer 组件
  },
  data() {
    return {
      signupForm: {
        role: 'student',  // 默认是学生身份
        student_id: '',  // 学生注册时使用的字段
        teacher_id: '',  // 教师注册时使用的字段
        password: '',
        confirmPassword: '',  // 确认密码
        email: ''
      },
      rules: {
        student_id: [
          { required: true, message: '请输入学号', trigger: 'blur' },
        ],
        teacher_id: [
          { required: true, message: '请输入教工号', trigger: 'blur' },
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 6, message: '密码长度不能少于6位', trigger: 'blur' },
        ],
        confirmPassword: [
          { required: true, message: '请再次输入密码', trigger: 'blur' },
          { validator: this.validateConfirmPassword, trigger: 'blur' },
        ],
        email: [
          { required: true, message: '请输入邮箱地址', trigger: 'blur' },
          { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] },
        ],
        role: [
          { required: true, message: '请选择身份', trigger: 'change' },
        ],
      }
    };
  },
  methods: {
    validateConfirmPassword(rule, value, callback) {
      if (value !== this.signupForm.password) {
        callback(new Error('两次输入的密码不一致'));
      } else {
        callback();
      }
    },
    async onSignup() {
      this.$refs.signupForm.validate(async (valid) => {
        if (valid) {
          try {
            const payload = {
              role: this.signupForm.role,
              password: this.signupForm.password,
              email: this.signupForm.email,
            };

            // 根据身份选择相应的 ID 字段
            if (this.signupForm.role === 'student') {
              payload.student_id = this.signupForm.student_id;
            } else if (this.signupForm.role === 'teacher') {
              payload.teacher_id = this.signupForm.teacher_id;
            }

            const response = await axios.post('http://127.0.0.1:8000/api/register/', payload);
            if (response.status === 201) {
              this.$message.success('注册成功！');
              this.$router.push('/login');
            }
          } catch (error) {
            if (error.response && error.response.data.error) {
              this.$message.error('注册失败: ' + JSON.stringify(error.response.data.error));
            } else {
              this.$message.error('注册失败，请稍后重试');
            }
          }
        } else {
          console.log('表单验证失败');
          return false;
        }
      });
    }
  }
};
</script>

<style scoped>
/* 标题和副标题样式 */
.signup-title {
  font-size: 2.0rem;
  margin-bottom: 10px;
  text-align: center;
  font-weight: bold;
}

.signup-subtitle {
  font-size: 1.2rem;
  margin-bottom: 20px;
  text-align: center;
  color: #888;
}

/* 表单样式 */
.signup-form {
  width: 100%;
}

/* 输入框样式 */
.input-field {
  width: 100%;
  margin-bottom: 1px;
}

/* 注册按钮样式 */
.signup-btn {
  width: 100%;
  height: 50px;
  font-size: 1.2rem;
  background-color: #1d2430;
  color: white;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.signup-btn:hover {
  background-color: #3a3f51;
}

/* 注册选项链接 */
.signup-options {
  margin-top: 10px;
  text-align: center;
}

.login-link {
  color: #409eff;
  text-decoration: none;
}

.login-link:hover {
  text-decoration: underline;
}
</style>
