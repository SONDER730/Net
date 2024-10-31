<template>
  <div class="lab-container">
    <!-- 1. 实验室展厅 -->
    <section class="lab-exhibition" @mouseover="showText = true" @mouseleave="showText = false">
      <div class="exhibition-image-container">
        <div class="exhibition-image">
          <img :src="exhibitionImage" alt="实验室展厅图片" />
        </div>
        <!-- 左侧的竖直显示文字 -->
        <div class="exhibition-text" :class="{ 'show-text': showText }">
          <span>实验室展厅</span>
        </div>
      </div>
    </section>

    <!-- 2. 实验室靶场 -->
    <section class="lab-range split-background">
      <h2>实验室靶场</h2>
      <div class="lab-range-content">
        <!-- 右侧图片展示 -->
        <div class="lab-range-image">
          <img :src="labImages[activeTab]" alt="教室图片" />
        </div>
        <!-- 左侧 Tabs 切换 -->
        <div class="lab-text-container">
        <div class="lab-tabs">
          <ul>
            <li :class="{ active: activeTab === '102-103' }" @click="activeTab = '102-103'">102-103教室</li>
            <li :class="{ active: activeTab === '104-105' }" @click="activeTab = '104-105'">104-105教室</li>
            <li :class="{ active: activeTab === '107-108' }" @click="activeTab = '107-108'">107-108教室</li>
            <li :class="{ active: activeTab === '109-110' }" @click="activeTab = '109-110'">网109-110教室</li>
            <li :class="{ active: activeTab === '112-113' }" @click="activeTab = '112-113'">112-113网络靶场</li>
          </ul>
        </div>
        <!-- tab对应的详细内容展示 -->
      <div class="lab-details" v-if="activeTab === '102-103'">
        <h3>102-103 教室</h3>
        <p>102-103 教室是专门用于网络攻防演练的场所，配备了先进的网络安全设备。</p>
      </div>
      <div class="lab-details" v-else-if="activeTab === '104-105'">
        <h3>104-105 教室</h3>
        <p>104-105 教室主要用于安全测试与漏洞分析实验，包含最新的安全测试工具。</p>
      </div>
      <div class="lab-details" v-else-if="activeTab === '107-108'">
        <h3>107-108 教室</h3>
        <p>107-108 教室为网络攻防比赛训练场地，旨在培养学生的团队合作与实战技能。</p>
      </div>
      <div class="lab-details" v-else-if="activeTab === '109-110'">
        <h3>109-110 网络靶场</h3>
        <p>109-110 教室配备了网络靶场，学生可以在这里进行网络渗透测试与防御实战演练。</p>
      </div>
      <div class="lab-details" v-else-if="activeTab === '112-113'">
        <h3>112-113 网络靶场</h3>
        <p>112-113 教室是面向高级网络攻防的综合实验室，配备了国际领先的网络攻防设备。</p>
      </div>
      </div>
      </div>


    </section>

    <!-- 3. 实验室创新实践平台 -->
    <section class="split-lab-background lab-innovation">
      <h2 style="color: #fff;">实验室创新实践平台</h2>
      <div class="lab-innovation-image">
        <img :src="innovationImage" alt="创新实践平台图片" />
      </div>
      <div class="lab-innovation-text">
        <p style="color: #fff;"> 实验中心以国家网络强国战略和信创国家战略为指导，紧扣新工科建设的要求，重视创新驱动和智力支撑的需求，致力于打造实验支撑能力、关键核心技术自主创新能力和实战化人才培养能力，目标是成为学院创新人才培养的重要基地。
实验中心位于沙河校区的网安大楼一层，占地面积近一千平米。配备有超过600台/套的各类先进实验平台和实验箱及硬件设备，为全院师生提供实验与实践教学服务。实验中心还支持大学生的创新创业活动和开源社区实践，年使用人数超过700人。
中心环境突出人文化和年轻化特征，充满科技感，深受学生喜爱。因其优秀的环境和管理，实验中心被学校评为实验室建设先进集体和实验室安全先进单位。
作为网络空间安全创新实践基地，实验中心支撑着包括大学生创新创业项目、"雏燕"计划项目在内的多项活动。此外，中心还支持各类学科竞赛，如“北邮杯”全国中学生网络安全技术赛、TSCTF比赛等。与17家网络空间安全行业知名企业建立了合作关系，探索协同育人、专业共建等多方面的合作，为学生提供了通向企业的绿色通道，同时也为企业提供了优质的人才源。
通过这种产、学、用一体的实践教学模式，实验中心不仅为学生提供了丰富的学习和实践机会，同时也架设了学院与行业之间的桥梁，促进了教育与行业的紧密合作。 </p>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeTab: '102-103', // 默认显示的 tab
      showText: false, // 控制文字是否显示
      exhibitionImage: require('@/assets/Background.png'), // 展厅图片
      labImages: {
        '102-103': require('@/assets/1.jpg'),
        '104-105': require('@/assets/2.jpg'),
        '107-108': require('@/assets/3.jpg'),
        '109-110': require('@/assets/4.jpg'),
        '112-113': require('@/assets/5.jpg'),
      },
      innovationImage: require('@/assets/banner1.png'), // 创新实践平台图片
    };
  },
};
</script>

<style scoped>
.lab-container {
  height: 100%;
  background-color: #001f3f; /* 背景颜色填充 */
}

/* 实验室展厅样式 */
.lab-exhibition {
  position: relative;
  width: 100%;
  display: flex;
  justify-content: center; /* 保证内容居中 */
  padding: 50px 0; /* 上下留白 */
  background-color: #001f3f; /* 背景颜色 */
}

.exhibition-image-container {
  position: relative;
  width: 70%; /* 图片占据中间80%的宽度 */
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #001f3f; /* 背景颜色填充外部部分 */
}

.exhibition-image img {
  width: 100%;
  height: auto;
  object-fit: cover; /* 图片填充整个 section */
  background-color: #001f3f;
}

.exhibition-text {
  position: absolute;
  top: 0;
  left: -100px;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 4rem;
  font-weight: bold;
  color: white;
  writing-mode: vertical-rl; /* 竖直显示文字 */
  text-orientation: mixed;
  transition: transform 0.5s ease; /* 动画 */
  opacity: 0;
}

.exhibition-text.show-text {
  transform: translateX(100px); /* 鼠标经过时移动文字 */
  opacity: 1;
}

/* 实验室靶场样式 */
.lab-range {
  width: 80%;
  padding: 40px 20px;
  background-color: #e9eef3;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center; /* 使内容居中显示 */
}

.lab-range h2 {
  font-size: 2rem;
  margin-bottom: 20px;
}

.lab-range-content {
  display: flex;
  justify-content: center; /* 居中显示 */
  width: 100%;
  margin-top: 20px;
}

.lab-text-container {
  width: 50%;
}

.lab-tabs {
  width: 40%; /* 增加宽度，使其与图片部分保持一致 */
}

.lab-tabs ul {
  display: flex; /* 将 Tabs 按一行排列 */
  justify-content: space-around; /* 增加tab间的间距 */
  list-style: none;
  padding: 0;
  margin: 0; /* 去除默认的margin */
}

.lab-tabs li {
  padding: 10px 20px; /* 增加左右padding，使tab按钮更宽 */
  cursor: pointer;
  background-color: #1d2430;
  color: white;
  border-radius: 5px;
  text-align: center;
  flex: 1;
  margin-right: 10px;
  transition: background-color 0.3s ease;
}

.lab-tabs li.active {
  background-color: #475669;
}

.lab-range-image {
  width: 55%; /* 调整图片部分的宽度，使其与tab部分保持一致 */
  display: flex;
  justify-content: center;
  align-items: center;
}

.lab-range-image img {
  max-width: 100%;
  height: 300px;
  object-fit: cover;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
}

/* 背景样式 */
.split-background {
  background: linear-gradient(135deg, white 50%, #001f3f 50%);
  border: white;
  margin: 0 auto;
}

/* 靶场详细内容展示 */
.lab-details {
  margin-top: 20px;
  color: white;
  //background-color: #f5f5f5;
  padding: 20px;
  border-radius: 8px;
  text-align: left; /* 使详细内容左对齐显示 */
  line-height: 1.6;
  width: 100%; /* 使其宽度与内容区保持一致 */
  max-width: 800px; /* 限制最大宽度 */
  margin: 0 auto; /* 居中显示 */
}

/* 实验室创新实践平台样式 */
.split-lab-background {
 /*  background: linear-gradient(225deg, white 50%, #001f3f 50%); */
 background:  #021E41; 
  border:white;
  margin: 0;
}

.lab-innovation {
  padding: 40px 20px;
  /* background-color: #1d2430; */
  color: #2C303B;
  text-align: center;
}

.lab-innovation h2 {
  font-size: 2rem;
  margin-bottom: 20px;
}

.lab-innovation-image img {
  max-width: 100%;
  height: 300px;
  object-fit: cover;
  border-radius: 8px;
}

.lab-innovation-text {
  margin-top: 20px;
  font-size: 1rem;
  line-height: 1.6;
}


</style>
