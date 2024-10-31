import Vue from 'vue';
import Router from 'vue-router';
import InfoView from '@/views/InfoView.vue';
import AnnounceView from '@/views/AnnounceView.vue';
import LoginView from '@/views/LoginView.vue';
import GuideView from '@/views/GuideView.vue';
import StuView from "@/views/StuView.vue";
import TeacherView from "@/views/TeacherView.vue";
// import Profile  from "@/components/Profile.vue";
import Home from "@/views/Home.vue";
import SignupView from "@/views/SignupView.vue";
Vue.use(Router);

export default new Router({
  routes: [
    { path: '/',component: Home},
    { path: '/info', component: InfoView },
    { path: '/student',component:StuView},
    { path: '/teacher',component:TeacherView},
    // { path: '/Profile',component:Profile},
    { path: '/announcement', component: AnnounceView },
    { path: '/login', component: LoginView },
    { path: '/signup', component: SignupView },
    { path: '/guide', component: GuideView },
    { path: '*', redirect: '/info' } // 默认重定向到信息展示页面
  ],
  mode: 'history'
});
