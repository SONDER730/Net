<template>
  <div>
    <!-- 这是根元素，包裹所有内容 -->
    <div class="home-container">
      <!-- 第一个div：欢迎界面 -->
      <div class="carousel">
        <section class="welcome-section">
          <div class="welcome-text">
            <h1>欢迎来到北京邮电大学网络空间安全实验平台</h1>
            <p>我们致力于为网络空间安全的研究和实践提供坚实的技术支持，培养卓越的网络安全人才。</p>
          </div>
        </section>
        <el-carousel height="100vh">
          <el-carousel-item v-for="item in carouselImages" :key="item">
            <!-- <h3 class="small">{{ item }}</h3> -->
            <video autoplay="autoplay" muted="muted" loop="loop" v-if="item.type === 'video'" style="width: 100%;"
              :src="item.url"></video>
            <img v-else style="width: 100%;height: 100%;" :src="item.url" alt="">
          </el-carousel-item>
        </el-carousel>
        <!-- 搜索框 -->
        <!-- <div class="kuaisu">
          <div class="kuaisu-a">
            <input style="outline: none;border: 0;" type="text" placeholder="快速探索 Telecommunications University"/>
   
          </div>
          <div class="kuaisu-b">
            <div class="zixian"></div>
            <ul>
              <li>高频搜索内容 ></li>
              <li><a href="#">本科生招生</a></li>
              <li><a href="#">研究生招生</a></li>
              <li><a href="#">110周年校庆</a></li>
              <li><a href="#">建党100周年</a></li>
              <li><a href="#">抗击新冠肺炎疫情</a></li>
            </ul>
          </div>
		</div> -->
      </div>
<!-- 
		<div class="zhouniantu">
				<img src="https://nic.bupt.edu.cn/images/banner01.jpg" alt="" />
		</div> -->

      <!-- 第二个div：实验室滚动图片 --> <!-- 轮播图展示图片 -->
      <!-- <section class="lab-carousel-section">
        <h2>实验室展示</h2>
    
        <el-carousel :interval="4000" type="card" height="300px">
          <el-carousel-item v-for="(image, index) in carousel@/assets/images" :key="index">
            <img :src="image" alt="实验室展示图片" class="carousel-image" />
          </el-carousel-item>
        </el-carousel>
      </section> -->

      <!-- 第三个div：特征介绍 -->
      <section class="features-section">
        <!-- <div>
          <h2 class="feature-black">我们的特色</h2>
          <div class="features-container">
            <div class="feature">
              <h3>高质量实验设备</h3>
              <p>我们拥有最先进的实验设施，确保学生能够在真实的环境中进行实验操作。</p>
              <div class="line1 line"></div>
              <div class="line2 line"></div>
              <div class="line3 line"></div>
              <div class="line4 line"></div>
            </div>
            <div class="feature">
              <h3>行业合作</h3>
              <p>与多个知名企业合作，提供丰富的实习机会和实际项目训练。</p>
              <div class="line1 line"></div>
              <div class="line2 line"></div>
              <div class="line3 line"></div>
              <div class="line4 line"></div>
            </div>
            <div class="feature">
              <h3>顶级师资力量</h3>
              <p>由国内外知名教授和专家组成的师资团队，提供专业的指导与支持。</p>
              <div class="line1 line"></div>
              <div class="line2 line"></div>
              <div class="line3 line"></div>
              <div class="line4 line"></div>
            </div>
          </div>
          <div class="features-container">
            <div class="feature">
              <h3>高质量实验设备</h3>
              <p>我们拥有最先进的实验设施，确保学生能够在真实的环境中进行实验操作。</p>
              <div class="line1 line"></div>
              <div class="line2 line"></div>
              <div class="line3 line"></div>
              <div class="line4 line"></div>
            </div>
            <div class="feature">
              <h3>行业合作</h3>
              <p>与多个知名企业合作，提供丰富的实习机会和实际项目训练。</p>
              <div class="line1 line"></div>
              <div class="line2 line"></div>
              <div class="line3 line"></div>
              <div class="line4 line"></div>
            </div>
            <div class="feature">
              <h3>顶级师资力量</h3>
              <p>由国内外知名教授和专家组成的师资团队，提供专业的指导与支持。</p>
              <div class="line1 line"></div>
              <div class="line2 line"></div>
              <div class="line3 line"></div>
              <div class="line4 line"></div>
            </div>
          </div>
        </div> -->
        <br>   <br>   <br>   <br>
        <div class="stastistical-part2">
          <!-- section-seperator -->
          <div class="section-seperator in-point">
            <div class="container-template">
              <h2 style="font-weight: normal;margin-right: 50px;">
                <i class="english" style="color: rgb(165, 242, 211);">Education &amp; Academic</i>
                <p class="name">校园文化</p>
                <span class="line" style="background: rgb(165, 242, 211);"></span>
              </h2>
            </div>
            <div class="tuji clearfix">
              <div class="tujiitem1 fl">
                <img class="pic" src="@/assets/images/tujiimg1.png" alt="" width="100%" height="483">
                <div class="txtCover">那年，我们挥汗如雨的地方</div>
              </div>
              <ul class="tujiitem2 fl">
                <li>
                  <img class="pic" src="@/assets/images/4ec4c897-feaf-4305-80e5-83099bf41b80.png" alt="" width="100%" height="245">
                  <div class="txtCover">图书馆</div>
                </li>
                <li>
                  <img class="pic" src="@/assets/images/tujiimg2.png" alt="" width="100%" height="245">
                  <div class="txtCover">北邮校训石</div>
                </li>
                <li>
                  <img class="pic" src="@/assets/images/tujiimg4.png" alt="" width="100%" height="245">
                  <div class="txtCover">校园一角</div>
                </li>
                <li>
                  <img class="pic" src="@/assets/images/tujiimg5.png" alt="" width="100%" height="245">
                  <div class="txtCover"></div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      <!-- 第四个div：竞赛公示 -->
      <section class="competition-section">
        <div class="competition-text">
          <!-- 第一部分：竞赛介绍 -->
          <div class="competition-intro">
            <h2>网安竞赛</h2>
            <p>网络安全竞赛是提升学生技能与知识的绝佳平台。通过参与竞赛，学生能够接触到最前沿的技术，并挑战自我。</p>
          </div>

          <!-- 第二部分：平台介绍 -->
          <div class="competition-platform">
            <h3>竞赛公示平台</h3>
            <p>在我们的竞赛公示平台上，您可以了解到最新的竞赛信息，查看比赛规则、报名方式、奖项设置等。</p>
          </div>

          <!-- 第三部分：跳转链接 -->
          <div class="competition-links">
            <h4>相关链接</h4>
            <el-button type="primary" class="competition-btn" @click="navigateToPlatform">
              前往竞赛公示平台
            </el-button>
            <el-button type="success" class="competition-btn" @click="navigateToApply">
              申报竞赛
            </el-button>
          </div>
        </div>

        <!-- 右侧图片部分 -->
        <div class="competition-image">
          <img style="width: 60%;" src="https://nic.bupt.edu.cn/__local/1/5D/B1/2A9079DC9FB25A68B71B1940BB8_117EBE37_4FF14.png" alt="Competition" />
        </div>
      </section>
    </div>

    <!-- 页脚 -->
    <section class="home-footer">
      <!-- <div class="home-footer-item">
        <p>联系我们</p>
      </div> -->
      <div>
        <p>© 2024 北京邮电大学网络空间安全实验平台. 版权所有.</p>
      </div>
    </section>
  </div>
</template>
<script>
export default {
  name: "HomePage",
  data () {
    return {
      // 实验室滚动展示图片路径
      carouselImages: [
        {
          type: 'pic',
          url: require('@/assets/lb4.jpg')
        },
        {
          type: 'video',
          url: require('@/assets/video/lb1.mp4'),
        }, {
          type: 'pic',
          url: 'https://nic.bupt.edu.cn/images/ban002ner_shoutu.jpg',
        },
      ],

    };
  },
  methods: {
    // 导航到竞赛公示平台
    navigateToPlatform () {
      this.$route.push("/announcement")
      // window.open("https://example.com/competition-platform", "_blank");
    },
    // 导航到竞赛申报页面
    navigateToApply () {
      this.$route.push("/info")
      // window.open("https://example.com/competition-apply", "_blank");
    },
  },
};
</script>

<style lang="scss" scoped>
.section-seperator {
  position: relative;
  display: flex;
  overflow: hidden;
  .container-template{
    position: absolute;
    top: 0;
    left: -200px;
    z-index: 10000;
    width: 40%;
    height: 100%;
    transform: skewX(-25deg);
    // background: 117,179,191;
    background: rgba($color: #73B3BE, $alpha: .6);
    display: flex;
    align-items: center;
    justify-content: end;
   &::after{
    // content: '333';
    // position: absolute;
    // right:  -100px;
    // width: 200px;
    // height: 100%;
    // top: 0;
    // z-index: 1;
    // background: rgba($color: #73B3BE, $alpha: .6);
   
   }
  }
}
.tuji{
  display: flex;
  height: 483px;
  overflow: hidden;
  .fl{
    overflow: hidden;
  
 
    li{
      overflow: hidden;
    }
  }
}
.tujiitem1{
  flex: 2;
  height: 100%;
  position: relative;
  .txtCover{
    font-size: 20px;
      position: absolute;
      right: 10px;
      bottom: 10px;
  }
}
.pic{
  transition: all 1s;
  cursor: pointer;
  &:hover{
 transform: scale(1.1);  
}
}

.tujiitem2{
  height: 100%;
  flex: 1;
  display: flex;
  flex-wrap: wrap;
  li{
    width: 50%;
    position: relative;
    .txtCover{
      font-size: 20px;
      position: absolute;
      right: 10px;
      bottom: 10px;
  }
    img{
      height: 100%;
    }
  }

}
.carousel {
  width: 100%;
  position: relative;
}

.home-container {
  font-family: 'Arial', sans-serif;
  background-color: #001f3f;
  color: white;
  overflow: hidden;
  padding: 0;
}

/* 第一个div 样式 */
.welcome-section {
  padding: 100px 20px;
  text-align: center;
  /* background-color: #001f3f; */
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 999;
}

.welcome-text h1 {
  font-size: 2.5rem;
  margin-bottom: 20px;
}

.welcome-text p {
  font-size: 1.2rem;
}

/* 第二个div 样式 */
.lab-carousel-section {
  padding: 50px 20px;
  background: linear-gradient(to bottom, #001f3f, #ffffff);
  ;
  text-align: center;
}

.lab-carousel-section h2 {
  font-size: 2rem;
  margin-bottom: 20px;
}

.carousel-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

/* 第三个div 样式 */
.features-section {
  /* margin-top: 100px; */
  padding: 110px 20px;
  background-color: white;
  background: url('../assets/bg-ssss.jpg') no-repeat;
}

.feature-black {
  color: black;
}

.features-section h2 {
  font-size: 2rem;
  text-align: center;
  margin-bottom: 20px;
}

.features-container {
  display: flex;
  justify-content: space-around;
  margin-bottom: 40px;
  margin-top: 40px;
}

.feature {
  width: 20%;
  background-color: #2C303B;
  padding: 20px;
  border-radius: 8px;
  position: relative;
  overflow: hidden;
  transition: all 1s;
  cursor: pointer;
  &:hover{
    transform: scale(1.1);
    .line1{
    left: 0;
  }
  .line2{
    right: 0;
  }
  .line3{
    top: 0;
  }
  .line4{
    bottom: 0;
  }
  }
  .line{
    position: absolute;
    // border: 1px solid #fff;
    background: #fff;
    transition: all 1s;
  }
  .line1{
    width: 100%;
    height: 2px;
    top:  10px;
    left: -100%;
  }
  .line2{
    width: 100%;
    height: 2px;
    bottom:  10px;
    right:  -100%;
  }
  .line3{
    width: 2px;
    height:100%;
    top:100%;
    left:  10px;
  }
  .line4{
    width: 2px;
    height: 100%;
    bottom: 100%;
    right:  10px;
  }
}


.feature h3 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.feature p {
  font-size: 1rem;
}
/* 第四个div 样式 */

.competition-section {
  margin: 0 auto;
  width: 80%;
  display: flex;
  justify-content: space-between;
  padding: 50px 20px;
  background-color: #001f3f;
  // background: #000;
  // background: url(https://nic.bupt.edu.cn/images/footer_box01_bg.jpg);
  border-top: 1px solid white;
  color: white;
}

.competition-text {
  width: 50%;
  padding-right: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

.competition-intro h2 {
  font-size: 1.8rem;
  margin-bottom: 15px;
}

.competition-intro p {
  font-size: 1rem;
  line-height: 1.6;
}

.competition-platform h3 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.competition-platform p {
  font-size: 1rem;
  line-height: 1.6;
}

.competition-links h4 {
  font-size: 1.2rem;
  margin-bottom: 10px;
}

.competition-btn {
  margin-right: 10px;
}

.competition-image {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 50%;

}

.competition-image img {
  max-width: 100%;
  border-radius: 8px;
}
/* 页脚样式 */
.home-footer {
  padding: 20px 0;
  text-align: center;
  background-color: #001f3f;
  border-top: 1px solid white;
  color: #ccc;
}

.footer p {
  margin: 0;
  font-size: 0.9rem;
}

ul{
  list-style: none;
  margin: 0;
  padding: 0;
}
.zhouniantu{
	width: 85%;
	margin: 0 auto;
	margin-bottom: 30px;
}
.zhouniantu img{
	width: 100%;
}
.home-footer-item{
  width: 100%;
  height: 200px;
  background: url(https://nic.bupt.edu.cn/images/footer_box01_bg.jpg) no-repeat;
}
</style>
