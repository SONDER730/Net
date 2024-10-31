<template>
  <div class="main-container">
    <el-menu
      class="el-menu-vertical"
      :default-active="activeMenu"
      @select="handleMenuSelect"
      background-color="#001f3f"
      text-color="#fff"
      active-text-color="#409eff"
    >
      <el-menu-item index="awards">奖项竞赛</el-menu-item>
      <el-menu-item index="experts">人才专家</el-menu-item>
      <el-menu-item index="tools">科研工具</el-menu-item>
    </el-menu>

    <div class="content-container">
      <div v-if="activeMenu === 'awards'">
        <el-row :gutter="20" class="search-section">
          <el-col :span="5">
            <el-select v-model="searchMethod" placeholder="请选择检索方式">
              <el-option label="标题检索" value="name"></el-option>
              <el-option label="举办单位检索" value="type"></el-option>
            </el-select>
          </el-col>
          <el-col :span="8">
            <el-input v-model="searchQuery" placeholder="请输入检索内容"></el-input>
          </el-col>
          <el-col :span="4">
            <el-date-picker v-model="startDate" type="date" placeholder="起始时间"></el-date-picker>
          </el-col>
          <el-col :span="4">
            <el-date-picker v-model="endDate" type="date" placeholder="结束时间"></el-date-picker>
          </el-col>
          <el-col :span="2">
            <el-button type="primary" @click="search">检索</el-button>
          </el-col>
        </el-row>

        <el-table :data="filteredAwardsData" stripe style="background-color: white;">
          <el-table-column label="状态" width="150">
            <template slot-scope="scope">
              {{ getStatusLabel(scope.row.status) }}
            </template>
          </el-table-column>
          <el-table-column prop="name" label="标题"></el-table-column>
          <el-table-column prop="type" label="发布机构" width="200"></el-table-column>
          <el-table-column prop="reg_time_start" label="报名开始时间" width="180"></el-table-column>
          <el-table-column prop="reg_time_end" label="报名结束时间" width="180"></el-table-column>
          <el-table-column prop="comp_time_start" label="比赛开始时间" width="180"></el-table-column>
          <el-table-column prop="comp_time_end" label="比赛结束时间" width="180"></el-table-column>
        </el-table>
      </div>

      <div v-if="activeMenu === 'experts'">
        <el-row :gutter="20" class="search-section">
          <el-col :span="6">
            <el-select v-model="searchMethod" placeholder="请选择检索方式">
              <el-option label="姓名检索" value="name"></el-option>
              <el-option label="学院检索" value="school"></el-option>
            </el-select>
          </el-col>
          <el-col :span="8">
            <el-input v-model="searchQuery" placeholder="请输入检索内容"></el-input>
          </el-col>
          <el-col :span="2">
            <el-button type="primary" @click="search">检索</el-button>
          </el-col>
        </el-row>

        <el-table :data="expertsData" stripe style="background-color: white;">
          <el-table-column prop="name" label="姓名" width="150"></el-table-column>
          <el-table-column prop="school" label="学院"></el-table-column>
          <el-table-column prop="intro" label="简介"></el-table-column>
        </el-table>
      </div>

      <div v-if="activeMenu === 'tools'">
        <h2>科研工具</h2>
        <p>这里是科研工具部分的内容。</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      activeMenu: 'awards',
      searchMethod: 'name',
      searchQuery: '',
      startDate: null,
      endDate: null,
      awardsData: [],
      filteredAwardsData: [],
      expertsData: [
        { name: '张三', school: '计算机学院', intro: '网络安全专家，专注于安全加密与渗透测试。' },
      ],
    };
  },
  methods: {
    handleMenuSelect(index) {
      this.activeMenu = index;
    },
    fetchAwardsData() {
      axios.get('http://localhost:8000/api/competition-announcement/list/')
        .then(response => {
          this.awardsData = response.data;
          this.filteredAwardsData = response.data;
        })
        .catch(error => {
          console.error("Error fetching awards data:", error);
        });
    },
    search() {
      this.filteredAwardsData = this.awardsData.filter(award => {
        const matchesMethod = this.searchMethod === 'name'
            ? award.name.includes(this.searchQuery)
            : award.type && award.type.includes(this.searchQuery);
        const matchesDateRange = (!this.startDate || new Date(award.reg_time_start) >= new Date(this.startDate)) &&
            (!this.endDate || new Date(award.comp_time_end) <= new Date(this.endDate));
        return matchesMethod && matchesDateRange;
      });
    },
    getStatusLabel(status) {
      const statusLabels = {
        0: "报名未开始",
        1: "报名进行中",
        2: "报名已结束",
        3: "比赛进行中",
        4: "比赛已结束",
      };
      return statusLabels[status] || "未知状态";
    },
  },
  mounted() {
    this.fetchAwardsData(); // 组件挂载时调用 API 获取奖项数据
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
}

.search-section {
  margin-bottom: 20px;
}

.el-table {
  background-color: #fff;
  width: 100%;
}

.el-menu-item {
  color: #fff !important;
  border-bottom: white;
}

.el-menu-item:hover {
  background-color: #409eff !important;
}
</style>
