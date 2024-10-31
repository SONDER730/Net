<template>
  <FormContainer
    welcomeTitle="欢迎使用平台"
    welcomeMessage="请输入您的账号信息并选择身份进行登录，享受我们的服务"
    buttonText="了解更多"
  >
    <!-- 表单部分通过插槽传递 -->
    <template v-slot:form>
      <h2 class="login-title">登录</h2>

      <!-- 身份选择 -->
      <el-form :model="loginForm" class="login-form">
        <el-form-item>
          <el-radio-group v-model="loginForm.role" size="large">
            <el-radio label="student">学生登录</el-radio>
            <el-radio label="teacher">教师登录</el-radio>
          </el-radio-group>
        </el-form-item>

        <!-- 账号 -->
        <el-form-item>
          <el-input
            v-model="loginForm.username"
            placeholder="请输入账号"
            class="input-field"
            prefix-icon="el-icon-user"
            size="large"
          />
        </el-form-item>

        <!-- 密码 -->
        <el-form-item>
          <el-input
            v-model="loginForm.password"
            placeholder="请输入密码"
            type="password"
            class="input-field"
            prefix-icon="el-icon-lock"
            size="large"
          />
        </el-form-item>

        <!-- 验证码 -->
        <el-form-item>
          <el-input
            v-model="loginForm.captcha"
            placeholder="请输入验证码"
            class="input-field"
            size="large"
          />
          <!-- 验证码图片 -->
          <img :src="captchaImageSrc" alt="验证码" class="captcha-image" @click="refreshCaptcha">
        </el-form-item>

        <!-- 登录按钮 -->
        <el-form-item>
          <el-button type="primary" class="login-btn" @click="onLogin">登录</el-button>
        </el-form-item>
      </el-form>

      <!-- 登录选项 -->
      <div class="login-options">
        <router-link to="/forgot-password" class="forgot-password-link">忘记密码?</router-link>
        <p>没有账号? <router-link to="/signup" class="signup-link">立即注册</router-link></p>
      </div>
    </template>
  </FormContainer>
</template>

<script>
import FormContainer from '@/components/FormContainer.vue';
import axios from 'axios';

export default {
  name: 'LoginView',
  components: {
    FormContainer,  // 注册 FormContainer 组件
  },
  data() {
    return {
      loginForm: {
        role: null,  // 用户身份（student 或 teacher）
        username: '',  // 账号
        password: '',  // 密码
        captcha: '',   // 验证码（可以根据需要）
      },
      captchaImageSrc: 'http://127.0.0.1:8000/captcha/',  // 验证码图片路径
    };
  },
  methods: {
    async onLogin() {
      if (this.loginForm.username && this.loginForm.password && this.loginForm.captcha) {
        try {
          // 发送 POST 请求到后端 Django API
          const response = await axios.post('http://127.0.0.1:8000/login/', {
            user_id: this.loginForm.username,
            password: this.loginForm.password,
            role: this.loginForm.role,  // 'student' 或 'teacher'
            captcha: this.loginForm.captcha,  // 添加验证码字段
          }, {
});
          localStorage.setItem('access_token', response.data.access);
          localStorage.setItem('refresh_token', response.data.refresh);

          // 处理登录成功的响应
          if (response.status === 200) {
            this.$emit('login', this.loginForm.role, true);  // 触发登录事件
            this.$router.push('/');  // 登录成功后跳转到首页
          }
        } catch (error) {
          // 处理后端返回的错误信息
          if (error.response && error.response.data.error) {
            this.$message.error(error.response.data.error);  // 显示后端返回的错误信息
          } else {
            this.$message.error('登录失败，请检查您的登录信息');
          }
        }
      } else {
        this.$message.error('请填写完整的登录信息');
      }
    },
    refreshCaptcha() {
      // 刷新验证码图片，通过改变图片的请求地址来避免缓存问题
    this.captchaImageSrc = `http://127.0.0.1:8000/captcha/?t=${new Date().getTime()}`;
    }
  }
};
</script>

<style scoped>
/* 标题和副标题样式 */
.login-title {
  font-size: 1.8rem;
  margin-bottom: 10px;
  text-align: center;
  font-weight: bold;
}

/* 表单样式 */
.login-form {
  width: 100%;
}

/* 输入框样式 */
.input-field {
  width: 100%;
  margin-bottom: 15px;
}

/* 验证码图片样式 */
.captcha-image {
  display: block;
  margin-top: 10px;
  max-width: 150px;
  cursor: pointer;
}

/* 登录按钮样式 */
.login-btn {
  width: 100%;
  height: 50px;
  font-size: 1rem;
  background-color: #1d2430;
  color: white;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.login-btn:hover {
  background-color: #3a3f51;
}

/* 登录选项链接 */
.login-options {
  margin-top: 10px;
  text-align: center;
}

.forgot-password-link, .signup-link {
  color: #409eff;
  text-decoration: none;
}

.forgot-password-link:hover, .signup-link:hover {
  text-decoration: underline;
}
</style>
