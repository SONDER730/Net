
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
      <el-menu-item index="teacherInfo">
        教师信息
      </el-menu-item>
      <el-menu-item index="studentManagement">
        学生管理
      </el-menu-item>
      <el-menu-item index="competitionManagement">
        竞赛管理
      </el-menu-item>
      <!--
      <el-menu-item index="reportCertificates">
        报告与证书
      </el-menu-item>
      -->
      <el-menu-item index="generatePDF">
        生成PDF证明
      </el-menu-item>
    </el-menu>

    <!-- 右侧内容展示 -->
    <div class="content-container">
      <!-- 教师信息模块 -->
      <div v-if="activeMenu === 'teacherInfo'">
        <div class="info-notification">
          <el-card>
            <p>待审核学生竞赛申请: {{ pendingStudents }}</p>
            <p>未完成竞赛流程: {{ pendingCompetitions }}</p>
            <p>系统通知: {{ systemNotifications }}</p>
          </el-card>
        </div>
        <div class="teacher-info">
          <h2>教师个人信息</h2>
          <el-card>
            <el-descriptions column="1" border>
              <el-descriptions-item label="姓名">{{ teacherInfo.name }}</el-descriptions-item>
              <el-descriptions-item label="学院">{{ teacherInfo.department }}</el-descriptions-item>
            
              <el-descriptions-item label="工号">{{ teacherInfo.id }}</el-descriptions-item>
              <el-descriptions-item label="联系方式">{{ teacherInfo.phone }}</el-descriptions-item>
              <el-descriptions-item label="邮箱">{{ teacherInfo.email }}</el-descriptions-item>
            </el-descriptions>
          </el-card>
        </div>
      </div>

      <!-- 学生管理模块 -->
      <div v-if="activeMenu === 'studentManagement'">
        <h2>学生管理</h2>
        <el-input v-model="searchQuery" placeholder="按学生姓名、学号、竞赛项目进行搜索"></el-input>
        <el-table :data="studentData" stripe>
          <el-table-column prop="name" label="姓名"></el-table-column>
          <el-table-column prop="studentID" label="学号"></el-table-column>
          <el-table-column prop="competition" label="竞赛项目"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button size="small" @click="approveStudent(scope.row)">批准</el-button>
              <el-button size="small" type="danger" @click="rejectStudent(scope.row)">拒绝</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>

<!-- 竞赛管理模块 -->
      <div v-if="activeMenu === 'competitionManagement'">
        <h2>竞赛管理</h2>
        <el-table :data="competitionData" stripe>
          <el-table-column prop="title" label="竞赛名称"></el-table-column> <!-- 使用 title 字段 -->
          <el-table-column prop="description" label="描述"></el-table-column> <!-- 使用 description 字段 -->
          <el-table-column prop="start_date" label="开始日期"></el-table-column> <!-- 使用 start_date 字段 -->
          <el-table-column prop="end_date" label="结束日期"></el-table-column> <!-- 使用 end_date 字段 -->
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button size="small" @click="reviewMaterials(scope.row)">查看材料</el-button>
              <el-button size="small" @click="confirmProcess(scope.row)">确认流程</el-button>
            </template>
          </el-table-column>
        </el-table>
        <el-button type="primary" @click="openUploadDialog">上传竞赛</el-button>
      </div>

      <!-- 上传竞赛弹窗 -->
      <el-dialog title="上传竞赛" :visible.sync="uploadDialogVisible" width="40%">
        <el-form :model="newCompetition" label-width="100px">
          <el-form-item label="竞赛名称">
            <el-input v-model="newCompetition.title" placeholder="输入竞赛名称"></el-input>
          </el-form-item>
          <el-form-item label="描述">
            <el-input v-model="newCompetition.description" type="textarea" placeholder="输入竞赛描述"></el-input>
          </el-form-item>
          <el-form-item label="开始日期">
            <el-date-picker v-model="newCompetition.start_date" type="date" placeholder="选择开始日期"></el-date-picker>
          </el-form-item>
          <el-form-item label="结束日期">
            <el-date-picker v-model="newCompetition.end_date" type="date" placeholder="选择结束日期"></el-date-picker>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="uploadDialogVisible = false">取消</el-button>
          <el-button type="primary" @click="submitCompetition">提交</el-button>
        </span>
      </el-dialog>



      <!-- 报告与证书模块 -->
      <!--
      <div v-if="activeMenu === 'reportCertificates'">
        <h2>报告与证书</h2>
        <el-input v-model="searchQuery" placeholder="按学生、竞赛项目、时间进行搜索"></el-input>
        <el-table :data="reportData" stripe>
          <el-table-column prop="studentName" label="学生姓名"></el-table-column>
          <el-table-column prop="competition" label="竞赛项目"></el-table-column>
          <el-table-column prop="uploadDate" label="上传日期"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button size="small" @click="viewReport(scope.row)">查看总结</el-button>
              <el-button size="small" @click="viewCertificate(scope.row)">查看证书</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
      -->

      <!-- 生成PDF证明模块 -->
      <div v-if="activeMenu === 'generatePDF'">
        <h2>生成PDF证明</h2>
        <el-table :data="pdfData" stripe>
          <el-table-column prop="studentName" label="学生姓名"></el-table-column>
          <el-table-column prop="competition" label="竞赛项目"></el-table-column>
          <el-table-column prop="status" label="状态"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button size="small" type="success" @click="generatePDF(scope.row)">生成PDF</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </div>
    <!-- 弹窗 -->
<el-dialog title="查看材料" :visible.sync="dialogVisible" width="50%">
<p>姓名：{{selectedStudent.name}}</p>
  <p>学号：{{selectedStudent.studentID}}</p>
  <p>竞赛项目：{{selectedStudent.competition}}</p>
  <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="downloadMaterial">下载材料</el-button>
        <el-button @click="dialogVisible = false">关闭</el-button>
      </span>
</el-dialog>
  </div>

</template>

<script>
import axios from 'axios'; // 引入 axios

export default {
  data() {
    return {
      activeMenu: 'teacherInfo', // 当前活动的 tab，默认是教师信息
      editMode: false,

      // 通知数量
      pendingStudents: 5,
      pendingCompetitions: 3,
      systemNotifications: 2,

      // 教师信息
     teacherInfo: {
        name: '',
        department: '',
        teacher_id: '',
        contact: '',
        email: ''
      },

      // 学生管理数据
      studentData: [
        { name: '张三', studentID: 'S123456', competition: '编程大赛' },
        { name: '李四', studentID: 'S234567', competition: 'AI挑战赛' }
      ],

      // 竞赛管理数据
      competitionData: [], // 竞赛数据数组
      uploadDialogVisible: false,
      newCompetition: {
        title: '',
        description: '',
        start_date: '',
        end_date: ''
      },

      // 报告与证书数据
      reportData: [
        { studentName: '张三', competition: '编程大赛', uploadDate: '2024-09-15' },
        { studentName: '李四', competition: 'AI挑战赛', uploadDate: '2024-09-16' }
      ],

      // 生成PDF证明数据
      pdfData: [
        { studentName: '张三', competition: '编程大赛', status: '未生成' },
        { studentName: '李四', competition: 'AI挑战赛', status: '已生成' }
      ],

      // 搜索查询
      searchQuery: '',
      //弹窗可见性
      dialogVisible: false,
      //选中的竞赛材料（用于在弹窗中展示）
      //selectedCompetition: {},
      selectedStudent: {},
    };
  },
    created() {
    this.fetchTeacherInfo(); // 组件创建时获取教师信息

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
    handleMenuSelect(index) {
      this.activeMenu = index;
    },
    fetchTeacherInfo() {
      axios.get('/api/teacher-info/', { withCredentials: true })
        .then(response => {
          // 直接将返回的用户信息赋值给 profileForm
          this.teacherInfo = response.data;
        })
        .catch(error => {
          console.error('获取学生信息失败:', error);
        });
    },
    submitTeacherInfo() {
      console.log('Submitting teacher info:', this.teacherInfo);
      axios.post('/api/teacher-info/', this.teacherInfo, { withCredentials: true })  // 使用 POST 方法
        .then(response => {
          this.$message.success('信息提交成功');
          this.editMode = false;
          this.fetchTeacherInfo(); // 提交后重新获取数据以更新视图
        })
        .catch(error => {
          this.$message.error('提交失败: ' + (error.response?.data?.message || error.message));
        });
    },
    approveStudent(student) {
      console.log('批准学生:', student.name);
    },
    rejectStudent(student) {
      console.log('拒绝学生:', student.name);
    },
    reviewMaterials(student) {
      //console.log('查看材料:', student.studentID);
      //this.selectedCompetition = competition;//更新选中的竞赛材料
      //this.dialogVisible = true;//打开弹窗
      this.selectedStudent = student;//更新选中的竞赛材料
      this.dialogVisible = true;//打开弹窗
    },
    confirmProcess(competition) {
      console.log('确认流程:', competition.name);
    },
    viewReport(student) {
      console.log('查看总结:', student.studentName);
    },
    viewCertificate(student) {
      console.log('查看证书:', student.studentName);
    },
    generatePDF(student) {
      console.log('生成PDF:', student.studentName);
    },
    downloadMaterial() {
      const content = `姓名：${this.selectedStudent.name}
                       学号：${this.selectedStudent.studentID}
                       竞赛项目：${this.selectedStudent.competition}`;
      const blob = new Blob([content], {type: 'text/plain;charset=utf-8'});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'material.txt'; // 文件名可以根据需要更改
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url); // 释放内存
    },


    handleMenuSelect(index) {
      this.activeMenu = index;
      if (index === 'competitionManagement') {
        this.fetchCompetitions(); // 切换到竞赛管理时加载数据
      }
    },
    openUploadDialog() {
      this.uploadDialogVisible = true;
    },
    fetchCompetitions() {
      // 获取竞赛数据
      axios.get('http://localhost:8000/api/competition/list/')
        .then(response => {
          this.competitionData = response.data; // 加载数据到表格
        })
        .catch(error => {
          console.error("获取竞赛数据失败:", error);
        });
    },
    submitCompetition() {
      const competitionData = {
        title: this.newCompetition.title,
        description: this.newCompetition.description,
        start_date: this.formatDate(this.newCompetition.start_date),
        end_date: this.formatDate(this.newCompetition.end_date),
      };

      axios.post('http://localhost:8000/api/competition/upload/', competitionData)
        .then(response => {
          console.log("上传成功:", response.data);
          this.uploadDialogVisible = false;
          this.resetCompetitionForm();
          this.fetchCompetitions(); // 重新获取竞赛数据，刷新表格
        })
        .catch(error => {
          console.error("上传失败:", error);
        });
    },
    formatDate(date) {
      const d = new Date(date);
      if (isNaN(d.getTime())) {
        console.error("Invalid date value:", date);
        return '';
      }
      return d.toISOString().split('T')[0];
    },
    resetCompetitionForm() {
      this.newCompetition = {
        title: '',
        description: '',
        start_date: '',
        end_date: ''
      };
    }
  },
  mounted() {
    // 初次加载时获取竞赛数据
    this.fetchCompetitions();
  }
}
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

.info-notification {
  margin-bottom: 20px;
}

.teacher-info {
  margin-top: 20px;
}

.el-button {
  margin-left: 10px;
}
</style>
