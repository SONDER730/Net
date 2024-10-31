<template>
  <div class="calendar-container">
    <!-- 竞赛日历 -->
    <full-calendar
      :options="calendarOptions"
      :header="{
        left: 'prev,next today',
        center: 'title',
        right: 'dayGridMonth,timeGridWeek,timeGridDay'
      }"
      height="600px"
    ></full-calendar>
  </div>
</template>

<script>
import FullCalendar from '@fullcalendar/vue'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'

export default {
  components: {
    FullCalendar
  },
  data() {
    return {
      calendarOptions: {
        plugins: [ dayGridPlugin ],
        initialView: 'dayGridMonth',
        events: [
            { title: '网络安全竞赛', start: '2024-09-15', end: '2024-09-18' },
            { title: '编程马拉松', start: '2024-09-20', end: '2024-09-22' }
        ] // 示例事件
      },


      events: [
        { title: '网络安全竞赛', start: '2024-09-15', end: '2024-09-18' },
        { title: '编程马拉松', start: '2024-09-20', end: '2024-09-22' }
      ]
    }
  },
  methods: {
    goBack() {
      this.$emit('backToCompetitions') // 通知父组件返回到“我的竞赛”
    }
  }
}
</script>

<style scoped>
.calendar-container {
  width: 100%;
  padding: 20px;
  background-color: #f5f7fa; /* 浅灰色背景，符合网站风格 */
}

.back-btn {
  margin-bottom: 20px;
  background-color: #409eff; /* 按钮颜色符合网站主色调 */
  border-radius: 4px;
  color: white;
  padding: 10px 20px;
}

.full-calendar {
  background-color: white;
  padding: 15px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}
</style>
