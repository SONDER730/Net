<template>
  <div class="main-container">
    <!-- 左侧菜单 -->
    <el-menu
      class="el-menu-vertical"
      :default-active="activeMenu"
      @select="handleMenuSelect"
      background-color="#001f3f"
      text-color="#fff"
      active-text-color="#409eff"
    >
      <el-menu-item index="personalInfo">
        个人信息
      </el-menu-item>
      <el-menu-item index="myCompetitions">
        我的竞赛
      </el-menu-item>
      <!--<el-menu-item index="certificateDownload">
        证书下载
      </el-menu-item> -->
      <el-menu-item index="paymentOrders">
        缴费订单
      </el-menu-item>
      <el-menu-item index="changePassword">
        修改密码
      </el-menu-item>
    </el-menu>

    <!-- 右侧内容展示 -->
    <div class="content-container">
      <div  class="my-competitions" >
      <!-- 个人信息部分 -->
      <div v-if="activeMenu === 'personalInfo'">
        <h2>个人信息</h2>
        <div v-if="!editMode">
          <el-row :gutter="20" class="info-display">
            <el-col :span="12">
              <el-card>
                <el-descriptions column="1" border>
                  <el-descriptions-item label="姓名">{{ profileForm.name }}</el-descriptions-item>
                  <el-descriptions-item label="学院">{{ profileForm.school }}</el-descriptions-item>
                  <el-descriptions-item label="专业">{{ profileForm.major }}</el-descriptions-item>
                  <el-descriptions-item label="学号">{{ profileForm.studentID }}</el-descriptions-item>
                </el-descriptions>
              </el-card>
            </el-col>
            <el-col :span="12">
              <el-card>
                <el-descriptions column="1" border>
                  <el-descriptions-item label="年级">{{ profileForm.grade }}</el-descriptions-item>
                  <el-descriptions-item label="性别">{{ profileForm.gender === 'male' ? '男' : '女' }}</el-descriptions-item>
                  <el-descriptions-item label="电话">{{ profileForm.phone }}</el-descriptions-item>
                  <el-descriptions-item label="邮箱">{{ profileForm.email }}</el-descriptions-item>
                </el-descriptions>
              </el-card>
            </el-col>
          </el-row>
          <el-button type="primary" @click="editMode = true">修改信息</el-button>
        </div>

        <div v-else>
          <el-form :model="profileForm" label-width="80px">
            <el-row :gutter="20">
              <el-col :span="12">
                <el-form-item label="姓名">
                  <el-input v-model="profileForm.name"></el-input>
                </el-form-item>
                <el-form-item label="学院">
                  <el-input v-model="profileForm.school"></el-input>
                </el-form-item>
                <el-form-item label="专业">
                  <el-input v-model="profileForm.major"></el-input>
                </el-form-item>
                <el-form-item label="学号">
                  <el-input v-model="profileForm.studentID"></el-input>
                </el-form-item>
              </el-col>
              <el-col :span="12">
                <el-form-item label="年级">
                  <el-select v-model="profileForm.grade" placeholder="请选择年级">
                    <el-option label="大一" value="大一"></el-option>
                    <el-option label="大二" value="大二"></el-option>
                    <el-option label="大三" value="大三"></el-option>
                    <el-option label="大四" value="大四"></el-option>
                  </el-select>
                </el-form-item>
                <el-form-item label="性别">
                  <el-radio-group v-model="profileForm.gender">
                    <el-radio label="male">男</el-radio>
                    <el-radio label="female">女</el-radio>
                  </el-radio-group>
                </el-form-item>
                <el-form-item label="电话">
                  <el-input v-model="profileForm.phone"></el-input>
                </el-form-item>
                <el-form-item label="邮箱">
                  <el-input v-model="profileForm.email"></el-input>
                </el-form-item>
              </el-col>
            </el-row>
            <el-button type="primary" @click="submitProfile">提交</el-button>
            <el-button @click="editMode = false">取消</el-button>
          </el-form>
        </div>
      </div>

      <!-- 我的竞赛部分 -->
      <div  v-if="activeMenu === 'myCompetitions'">
        <div class="competition-header">
          <h2 style="color: #58DAFE;">我的竞赛</h2> 
            <Dialog :showDialog="showDialog=isDialogVisible"  @update:showDialog="value => isDialogVisible = value">
            </Dialog>
          <el-button size="small" type="success" @click="toggleCalendar">{{ showCalendar ? '返回' : '竞赛日历' }}</el-button>
        </div>

        <div v-if="!showCalendar">
          <el-table :data="competitionData" stripe style="width: 100%;">
            <el-table-column prop="name" label="竞赛名称"></el-table-column>
            <el-table-column prop="id" label="编号"></el-table-column>
            <el-table-column prop="progress" label="竞赛进度">
              <template slot-scope="scope">
                <el-progress :percentage="scope.row.progress" :text-inside="true" />
              </template>
            </el-table-column>
            <el-table-column label="操作">
              <template slot-scope="scope">
                <el-button size="small" @click="handleUpload(scope.row.id)">上传材料</el-button>
                <el-button size="small" type="info" @click="viewStatus(scope.row.id)">查看状态</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div class="signupbutton-box">
            <button class="signupbutton" @click="show">我要报名</button>
          </div>
       
        </div>

        <div v-if="showCalendar">
          <Calendar />
        </div>
      </div>

      <!-- 证书下载部分 -->
      <!--
      <div v-if="activeMenu === 'certificateDownload'">
        <h2>证书下载</h2>
        <el-table :data="certificateData" stripe style="width: 100%;">
          <el-table-column prop="name" label="证书名称"></el-table-column>
          <el-table-column prop="issueDate" label="颁发日期"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button size="small" type="info" @click="downloadCertificate(scope.row.id)">下载</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
      -->
      <!-- 缴费订单部分 -->
      <div v-if="activeMenu === 'paymentOrders'">
        <h2>缴费订单</h2>
        <el-table :data="paymentOrdersData" stripe style="width: 100%;">
          <el-table-column prop="id" label="编号"></el-table-column>
          <el-table-column prop="invoiceStatus" label="开票状态"></el-table-column>
          <el-table-column prop="name" label="竞赛名称"></el-table-column>
          <el-table-column prop="peopleCount" label="人数"></el-table-column>
          <el-table-column prop="price" label="价格"></el-table-column>
          <el-table-column width="220"  label="操作">
            <template slot-scope="scope">
              <el-button size="small" type="info" @click="handleViewInvoice(scope.row.id)">查看发票</el-button>
              <el-button size="small" type="primary" @click="handleReissueInvoice(scope.row.id)">重新开票</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>

      <!-- 修改密码部分 -->
      <div v-if="activeMenu === 'changePassword'">
        <h2>修改密码</h2>
        <el-form :model="passwordForm" label-width="120px" class="password-form">
          <el-form-item label="旧密码">
            <el-input v-model="passwordForm.oldPassword" type="password" placeholder="请输入旧密码" style="width: 20%"></el-input>
          </el-form-item>
          <el-form-item label="新密码">
            <el-input v-model="passwordForm.newPassword" type="password" placeholder="请输入8位以上新密码" style="width: 20%"></el-input>
          </el-form-item>
          <el-form-item label="确认密码">
            <el-input v-model="passwordForm.confirmPassword" type="password" placeholder="请再次输入新密码" style="width: 20%"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitPasswordChange">确认</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>


    </div>
 
  </div>
</template>

<script>
import axios from 'axios'; // 导入 Axios
import Dialog from '@/components/SignupDialog.vue';
import Calendar from '@/components/Calendar.vue';

export default {
  components: {
    Dialog,
    Calendar,
  },
  data() {
    return {
      isDialogVisible:false,
      activeMenu: 'personalInfo',
      editMode: false,
      profileForm: {
        name: '',
        student_id: '',
        gender: 'male',
        phone: '',
        email: '',
        school: '',
        major: '',
        grade: ''
      },
      showCalendar: false,
      competitionData: [
        { id: '001', name: '网络安全竞赛', progress: 70 },
        { id: '002', name: '编程马拉松', progress: 50 },
        { id: '003', name: '数据挖掘比赛', progress: 90 },
      ],
      certificateData: [
        { id: '001', name: '编程大赛证书', issueDate: '2024-09-20' },
        { id: '002', name: 'AI挑战赛证书', issueDate: '2024-09-22' },
      ],
      paymentOrdersData: [
        { id: '001', invoiceStatus: '已开票', name: '竞赛1', peopleCount: 3, price: '¥3000' },
        { id: '002', invoiceStatus: '未开票', name: '竞赛2', peopleCount: 5, price: '¥5000' },
        { id: '003', invoiceStatus: '已开票', name: '竞赛3', peopleCount: 2, price: '¥2000' },
      ],
      passwordForm: {
        oldPassword: '',
        newPassword: '',
        confirmPassword: ''
      }
    };
  },
  created() {
    this.fetchStudentInfo(); // 组件创建时获取学生信息

    // 设置 Axios 拦截器
    axios.interceptors.request.use(config => {
      const token = localStorage.getItem('access_token'); // 从 localStorage 获取 JWT
      if (token) {
        config.headers.Authorization = `Bearer ${token}`; // 添加 Authorization 头
      }
      return config;
    }, error => {
      return Promise.reject(error);
    });
  },
  methods: {
    show(){
      this.isDialogVisible = true;
    },
    fetchStudentInfo() {
      axios.get('/api/student-info/')
        .then(response => {
          // 直接将返回的用户信息赋值给 profileForm
          this.profileForm = response.data;
        })
        .catch(error => {
          console.error('获取学生信息失败:', error);
        });
    },
    handleMenuSelect(index) {
      this.activeMenu = index;
    },
    submitProfile() {
      axios.post('/api/student-info/', this.profileForm, {
        withCredentials: true  // 允许发送Cookie
      })
      .then(response => {
        this.$message.success('信息提交成功');
        this.editMode = false;
        this.fetchStudentInfo(); // 重新获取信息以更新视图
      })
      .catch(error => {
        // 检查错误对象并提取信息
        if (error.response) {
          this.$message.error('提交失败: ' + error.response.data.message || error.response.statusText);
        } else if (error.request) {
          this.$message.error('提交失败: 没有收到响应');
        } else {
          this.$message.error('提交失败: ' + error.message);
        }
      });
    },
    toggleCalendar() {
      this.showCalendar = !this.showCalendar;
    },
    handleUpload(competitionId) {
   const input = document.createElement('input');
   input.type = 'file';
   input.onchange = async (event) => {
    const file = event.target.files[0];
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://127.0.0.1:8000/upload/', formData, {
         headers: {
          'Content-Type': 'multipart/form-data',

        },
        withCredentials: true,  // 允许发送Cookie
      });

      if (response.status === 200) {
        this.$message.success('文件上传成功');
      }
    } catch (error) {
      this.$message.error('文件上传失败: ' + (error.response?.data?.error || error.message));
    }
  };
  input.click();
},
    viewStatus(competitionId) {
      console.log('查看状态', competitionId);
    },
    handleViewInvoice(orderId) {
      console.log('查看发票', orderId);
    },
    handleReissueInvoice(orderId) {
      console.log('重新开票', orderId);
    },
    downloadCertificate(certificateId) {
      console.log('下载证书', certificateId);
    },
    submitPasswordChange() {
      if (this.passwordForm.newPassword !== this.passwordForm.confirmPassword) {
        this.$message.error('新密码与确认密码不一致');
        return;
      }
      console.log('修改密码', this.passwordForm);
    }
  }
};
</script>


<style scoped>
.main-container {
  display: flex;
  height: 100vh;
  background-color: #001f3f;
}

.el-menu-vertical {
  width: 250px;
  background-color: #001f3f;
  color: #fff;
}

.content-container {
  flex: 1;
  padding: 20px;
  background-color: white;
  color: black;
  background: url('@/assets/bg-student.png') no-repeat ;
  background-position: center center;
  background-size: cover; /* 背景图基于容器大小伸缩 */
  position: relative;
}

.el-menu-item {
  color: #fff !important;
}

.el-menu-item:hover {
  background-color: #409eff !important;
}

.el-menu-item.is-active {
  background-color: #409eff !important;
}

.competition-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.el-table {
  background-color: white;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  text-align: center;
}

.signupbutton{
  background-color:royalblue;
  color:white;
  border: none;
  border-radius: 12px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 23px;
  padding: 6px 10px;
  transition: background-color 0.3s;
}

.signupbutton:hover {
  background-color: deepskyblue; /* 鼠标悬停时按钮背景颜色 */
}
.my-competitions{
  width: 80%;
  /* background: #fff; */
  padding: 10px;
  border-radius: 15px;
   position: absolute;
   top: 50%;
   left: 50%;
   transform: translate(-50%,-50%);
}
.my-competitions > div > h2 {
  color: #58DAFE;
}
.signupbutton-box{
  display: flex;
  width: 100%;
  justify-content: end;
}
</style>

