<template>
  
  <header :class="{navbar:true,accNavbar:$route.path !=='/'}" >
    <div class="navbar-container" :style="{ height: '40px' }">
      <!-- 左侧 LOGO 区域 -->
      <div class="logo">
        <img src="@/assets/logo.png" alt="Logo" />
        <span class="logo-text"></span>
      </div>

      <!-- 中间导航菜单 -->
      <nav class="nav-links">
        <ul>
          <li><router-link to="/">首页</router-link></li>
          <li><router-link to="/info">信息展示</router-link></li>
          <li><router-link to="/announcement">竞赛指南</router-link></li>
          <!-- <li><router-link to="/guide">使用指南</router-link></li> -->
        </ul>
      </nav>

      <!-- 右侧按钮 -->
      <div class="nav-actions">
        <!-- 如果未登录，显示登录和注册按钮 -->
        <template v-if="!isLoggedIn">
          <el-button type="primary" size="small" class="login-btn" @click="onLoginClick">登录</el-button>
          <el-button type="primary" size="small" class="login-btn" @click="SignupClick">注册</el-button>
        </template>
        <!-- 如果已登录，显示用户下拉菜单 -->
        <template v-else>
          <el-dropdown>
            <el-button type="primary" size="small" class="user-btn">
              {{ userRole === 'student' ? '学生' : '教师' }}主页<i class="el-icon-arrow-down el-icon--right"></i>
            </el-button>
            <el-dropdown-menu slot="dropdown">
              <!-- 使用 router-link 跳转到不同的应用中心 -->
              <el-dropdown-item>
                <router-link :to="userRole === 'student' ? '/student' : '/teacher'">应用中心</router-link>
              </el-dropdown-item>

              <!-- 退出登录按钮 -->
              <el-dropdown-item divided @click="onLogoutClick">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </template>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  props: {
    isLoggedIn: {
      type: Boolean,
      default: false,
    },
    userRole: {
      type: String,
      default: '',
    },
  },
  methods: {
    onLoginClick() {
      this.$router.push('/login'); // 跳转到登录页面
    },
    SignupClick() {
      this.$router.push('/signup'); // 跳转到注册页面
    },
    onLogoutClick() {
      this.$emit('logout'); // 触发父组件的登出逻辑
    },
  }
};
</script>

<style scoped>
  .noneNavbar{
    display: block !important;
    height: 60px;
  }
.accNavbar{
 background-color: #001f3f !important; 
}
/* 样式保持不变 */
.navbar {
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
  /* background-color: #001f3f; */
  /* background-color: rgba(0, 31, 63, .6); 50% 透明度的白色 */
  background: -webkit-linear-gradient(bottom,  rgba(0, 31, 63, 0.2), rgba(0, 31, 63, 0.3), rgba(0, 31, 63, 0.4), rgba(0, 31, 63, 0.5), rgba(0, 31, 63, 0.6), rgba(0, 31, 63, 0.7), rgba(0, 31, 63, 0.8)); 
  z-index: 1000;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease;
  padding: 10px 0;
}
.navbar::before{
  position: absolute;
  top: 0;
  left: 0;
  display: block;
  content: '';
  width: 100%;
  height: 8px;
  background-color: #013f7d;
}

.navbar-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 30px;
}

.logo {
  display: flex;
  align-items: center;
}

.logo img {
  height: 30px;
  margin-right: 10px;
}

.logo-text {
  font-size: 1.4rem;
  font-weight: 500;
  color: #ffffff;
}

.nav-links ul {
  list-style: none;
  display: flex;
  margin: 0;
  padding: 0;
}

.nav-links ul li {
  margin-right: 20px;
}

.nav-links ul li a {
  color: #ffffff;
  text-decoration: none;
  /* font-weight: 400; */
  font-size: 1.0rem;
  transition: color 0.3s ease;
  font-weight: bold;
}

.nav-links ul li a:hover {
  color: #013f7d;
}

.nav-actions {
  display: flex;
  align-items: center;
}

.login-btn {
  background-color: #4A6CF7;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  padding: 8px 15px;
}

.login-btn:hover {
  background-color: #007bff;
}

.user-btn {
  background-color: #4A6CF7;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  padding: 8px 15px;
}

.user-btn:hover {
  background-color: #007bff;
}

@media (max-width: 768px) {
  .nav-links {
    display: none;
  }

  .logo-text {
    font-size: 1.2rem;
  }
}

@media (min-width: 769px) {
  .nav-links {
    display: flex;
  }
}
</style>
