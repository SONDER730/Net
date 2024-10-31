<template>
  <div class="dialog" v-if="showDialog">
    <div class="dialog-content">
      <div class="title">
        <h2>竞赛报名</h2><!--标题 -->
      </div>
       <span class="close" @click="hideDialog">关闭</span>

        <form class="myform" @submit.prevent="submitForm"><!--竞赛报名的表单 -->
          <div class="mytable">
            <el-row>
              <el-col :span="3">
                <span>姓名：</span>
              </el-col>
              <el-col :span="6">
                <el-input v-model="formData.name" required></el-input>
              </el-col>
              <el-col :span="3">
                <span>学号：</span>
              </el-col>
              <el-col :span="6">
                <el-input v-model="formData.student_id" required></el-input>
              </el-col>
            </el-row>
        <el-row :gutter="3" class="search-section">
          <el-col :span="3">
            <el-select v-model="searchMethod" placeholder="请选择检索方式">
              <el-option label="标题检索" value="title"></el-option>
              <el-option label="举办单位检索" value="organization"></el-option>
            </el-select>
          </el-col>

          <el-col :span="5">
            <el-input v-model="searchQuery" placeholder="请输入检索内容"></el-input>
          </el-col>
          <el-col :span="6">
            <el-date-picker v-model="startDate" type="date" placeholder="起始时间"></el-date-picker>
          </el-col>

          <el-col :span="5">
            <el-date-picker v-model="endDate" type="date" placeholder="结束时间"></el-date-picker>
          </el-col>
          <el-col :span="2">
            <el-button type="primary" @click="search">检索</el-button>
          </el-col>
        </el-row>


           <!-- 数据表格 -->
        <el-table :data="awardsData" stripe style="background-color: white; text-align: center;">
          <el-table-column prop="status" label="状态" width="100"></el-table-column>
          <el-table-column prop="title" label="标题" width="200"></el-table-column>
          <el-table-column prop="organization" label="发布机构" width="180"></el-table-column>
          <el-table-column prop="scope" label="范围" width="150"></el-table-column>
          <el-table-column prop="officialDate" label="官方日期" width="150"></el-table-column>
          <el-table-column prop="deadline" label="截止日期" width="150"></el-table-column>
        </el-table>
          </div>
          <button class="confirmbutton" type="submit">提交</button>
        </form>

    </div>
  </div>
</template>

<script>
export default {
  props: {
    showDialog: {
      type: Boolean,
      default: false,
    }
  },
  data() {
    return {
      localshowDialog: this.showDialog,
      formData: {
        name: '',
        student_id: '',
        competition: '',
      },
      searchMethod: '',
      searchQuery: '',
      startDate: '',
      endDate: '',
      awardsData: [
        { status: '未截止', title: '2024年网络安全竞赛', organization: '北京邮电大学', scope: '全国', officialDate: '2024-09-25', deadline: '2024-10-15' },
        // 更多数据...
      ],
    };
  },
  watch: {
    showDialog(newVal) {
      this.localshowDialog = newVal;
    }
  },
  methods: {
    clearData() {
      this.formData = {
        name: '',
        competiton: '',
        student_id: '',
      };
    },
    hideDialog() {
      this.$emit("update:showDialog", false)
    },
    submitForm() {
      // 这里可以添加提交表单的逻辑，比如发送请求到后端
      console.log('Form data submitted:', this.formData);
      // axios.post('your-api-endpoint', this.form)
      //   .then(response => {
      //     // 处理响应
      //   })
      //   .catch(error => {
      //     // 处理错误
      //   });
      this.hideDialog();
      alert('提交成功');
      this.clearData();
    },
    search() {
      // 搜索逻辑
    },
  }
}
</script>

<style scoped>
.dialog { /* 显示模态框 */
  position: fixed; /* 或者 absolute */
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  z-index: 1; /* 位于顶层 */
  background-color: rgba(0, 0, 0, 0.25); /* 半透明背景 */
}

.dialog-content {
  position: relative;
  background-color: #fefefe;
  width: 60%;
  height: 80%;
  margin: auto;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 20px;
  border: 1px solid #888;
  z-index: 1000;

}

.title {
  text-align: center;
}

.myform {
  text-align: center;
  margin: auto;
}
.mytable{
  margin:10px auto;
}

input{
  border:none;
  text-align: center;
  font-size: 17px;
}
.dialog-content .close {
  color: #aaa;
  position:absolute;
  right:5%;
  top:3%;
  font-size: 15px;
  font-weight: bold;
}
.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}

.dialog-content .confirmbutton{
  position: absolute;
  right:47%;
  bottom: 10%;
}


.search-section {
  display: flex;
  gap: 20px; /* 相当于 el-row 的 gutter */
  margin-bottom: 20px; /* 可选，根据需要调整 */
}

.search-item {
  flex: 1; /* 让每个子项占据可用空间 */
}
</style>