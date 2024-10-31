<template>
  <div class="form-container">
    <!-- 左侧表单区域插槽 -->
    <div class="form-left">
      <slot name="form"></slot>
    </div>

    <!-- 右侧背景区域 -->
    <div class="form-right">
      <div class="welcome-message">
        <h2>{{ welcomeTitle }}</h2>
        <hr class="divider" />
        <p>{{ welcomeMessage }}</p>
        <el-button type="text" class="read-more-btn">{{ buttonText }}</el-button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FormContainer',
  props: {
    welcomeTitle: {
      type: String,
      default: 'Welcome to YourPlatform'
    },
    welcomeMessage: {
      type: String,
      default: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam.'
    },
    buttonText: {
      type: String,
      default: 'Learn More'
    }
  }
};
</script>

<style scoped>
/* 移除页面滚动条 */
html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  overflow: hidden;
}

.form-container {
  display: flex;
  height: auto; /* 自动调整高度，根据内容大小 */
  min-height: 80vh; /* 设置一个最小高度，确保页面布局不会太小 */
  width: 90vw;  /* 调整宽度，不需要全屏显示 */
  margin: 10vh auto; /* 居中容器 */
  background: linear-gradient(to right, #f3f8ff 48%, #1d2430 52%);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
  border-radius: 10px; /* 增加圆角，增强美观 */
}


.form-left, .form-right {
  width: 50%;
  padding: 40px;
}

.form-right {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #1d2430;
  color: white;
  text-align: center;
}

.welcome-message {
  max-width: 400px;
  text-align: center;
}

.welcome-message h2 {
  font-size: 1.5rem; /* 增大标题字体 */
  font-weight: 700;
  margin-bottom: 15px;
}

.welcome-message p {
  font-size: .75rem; /* 微调字体大小 */
  line-height: 1.7;
  margin-bottom: 25px;
}

.divider {
  width: 80%; /* 使用相对宽度 */
  max-width: 300px; /* 设定最大宽度，防止太长 */
  height: 0;
  border-top: .5px solid white;
  margin: 20px auto;
}


.read-more-btn {
  color: #ff4d4f;
  border: 2px solid #ff4d4f;
  padding: 8px 25px;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s ease; /* 添加渐变效果 */
}

.read-more-btn:hover {
  background-color: #ff4d4f;
  color: white;
}
</style>
