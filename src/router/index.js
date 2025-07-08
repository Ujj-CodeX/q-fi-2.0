import { createRouter , createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import Dash from '../components/UserDashboard.vue'
import Dash2 from '../components/AdminSubject.vue'
import Dash3 from '../components/AdminQuiz.vue'
import Dash4 from '../components/AdminUser.vue'

const routes =[
    {
        path:'/',
        name: 'Home',
        component : Home
    },
    {
        path:'/User',
        name: 'Dash',
        component : Dash
    },
    {
        path:'/Admin_dash',
        name: 'Dash2',
        component : Dash2
    },
    {
        path:'/Admin_Quiz',
        name: 'Dash3',
        component : Dash3
    },
    {
        path:'/Admin_User',
        name: 'Dash4',
        component : Dash4
    },

]

const router = createRouter ({
    history : createWebHistory(process.env.BASE_URL),
    routes

})
export default router