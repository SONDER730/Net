<template>
  <div class="dialog" v-if="showDialog">
    <div class="dialog-content">
      <div class="title">
        <h2>竞赛报名</h2><!--标题 -->
      </div>
       <span class="close" @click="hideDialog">关闭</span>
       <span class="clear" @click="clearData">清空</span>

        <form class="myform" @submit.prevent="submitForm"><!--竞赛报名的表单 -->
          <div class="mytable">
            <el-row>
              <el-col :span="4">
                <span>姓名：</span>
              </el-col>
              <el-col :span="8">
                <el-input v-model="formData.name" required></el-input>
              </el-col>
              <el-col :span="4">
                <span>学号：</span>
              </el-col>
              <el-col :span="8">
                <el-input v-model="formData.student_id" required></el-input>
              </el-col>
            </el-row>
            <el-row>
              <el-col :span="4">
                <span>指导教师：</span>
              </el-col>
              <el-col :span="8">
                <el-select v-model="formData.teacher" placeholder="选择指导教师" required>
                <el-option v-for="teacher in teachers" :key="teacher.id" :label="teacher.name" :value="teacher.id"></el-option>
                </el-select>
              </el-col>
              <el-col :span="4">
                <span>竞赛名称：</span>
              </el-col>
              <el-col :span="8">
                <el-select v-model="formData.selectedCompetition" placeholder="选择竞赛" required>
                <el-option v-for="competition in filteredCompetitions" :key="competition.id" :label="competition.name" :value="competition"></el-option>
                </el-select>
              </el-col>
            </el-row>
          </div>

          <button class="submitbotton" type="submit"> 提交</button>
        </form>

    </div>
  </div>
</template>

<script>
import axios from 'axios';
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
        selectedCompetition: null,
        teacher:null,//匹配教师的id
      },
      searchQuery: '',
      competitions: [],
      teachers:[],
      filteredCompetitions: [],
    };
  },
  computed: {
    filteredCompetitions() {
      return this.competitions.filter(competition =>
          competition.name.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
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
        selectedCompetition: null,
      };
      this.searchQuery='';
      this.filteredCompetitions=[];
    },
    hideDialog() {
      this.$emit("update:showDialog", false)
    },
    submitForm() {
      if (this.formData.selectedCompetition && this.formData.teacher) {
        axios.post('/api/apply-competition/', this.formData)
          .then(response => {
            alert('申请提交成功！');
          })
          .catch(error => {
            console.error("There was an error submitting the application!", error);
          });
      } else {
        alert('请选择一个竞赛和指导教师');
      }
    },
    filterCompetitions() {

    },
    selectCompetition(competition) {
      this.formData.selectedCompetition = competition; // 更新选中的竞赛
    },
  },
  mounted(){
    axios.get('/api/competitions/')
      .then(response => {
        this.competitions = response.data;
      })
      .catch(error => {
        console.error("There was an error fetching the competitions!", error);
      });

    axios.get('/api/teachers/')
      .then(response => {
        this.teachers = response.data;
      })
      .catch(error => {
        console.error("There was an error fetching the teachers!", error);
      });
  },
};
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
  height: 100%;
  margin: auto;
  top: 10px;
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

.dialog-content form {
  position: relative;
  text-align: center;
  margin: auto;
  height: 100%;
}


input{
  border:none;
  text-align: center;
  font-size: 17px;
}
.dialog-content .close {
  color: dimgrey;
  position:absolute;
  right:4%;
  top:5%;
  font-size: 15px;
  font-weight: bold;
}
.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}

.dialog-content .clear {
  color: dimgrey;
  position:absolute;
  right:4%;
  top:5%;
  font-size: 15px;
  font-weight: bold;
}
.clear:hover,
.clear:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}

form button {
  color: dimgrey;
  position:absolute;
  right:45%;
  bottom:25%;
  font-size: 15px;
  font-weight: bold;
}

.dialog-content .clear{
  position: absolute;
  right:13%;
  top: 5%;
}


.search-section {
  display: flex;
  gap: 20px; /* 相当于 el-row 的 gutter */
  margin-bottom: 20px; /* 可选，根据需要调整 */
}

.search-item {
  flex: 1; /* 让每个子项占据可用空间 */
}

.competition-list-container {
  margin:auto;
  max-width:70%;
  height: 8em; /* 每行大约2em，四行就是8em */
  overflow-y: auto; /* 超出部分形成滚动条 */
}


.selected {
  background-color: #e0e0e0; /* 选中项的背景颜色 */
}

.myform .el-row {
  display: flex;
  align-items: center; /* 使内容垂直居中 */
  margin-bottom: 20px; /* 调整这个值来改变行间距 */
}
.myform .el-col:nth-child(odd) {
  text-align: center; /* 使奇数列的文字右对齐 */
}
.myform .el-col:nth-child(even) {
  text-align: center; /* 使偶数列的文字左对齐 */
}
</style>