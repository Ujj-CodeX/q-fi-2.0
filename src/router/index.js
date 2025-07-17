import { createRouter , createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import Dash from '../components/UserDashboard.vue'
import Dash2 from '../components/AdminSubject.vue'
import Dash3 from '../components/AdminQuiz.vue'
import Dash4 from '../components/AdminUser.vue'
import test from '../components/UserTest.vue'
import SignUp from '@/components/SignUp.vue'
import Admin_Login from '@/components/Admin_Login.vue'


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
    {
        path:'/Test',
        name: 'test',
        component : test,
        props: route => ({
    quizName: route.query.quizNameName,
    duration: route.query.duration,
    questions: route.query.questions
  })
    },
    {
        path:'/Signup',
        name: 'register',
        component : SignUp
    },
    {
        path:'/admin',
        name: 'admin',
        component : Admin_Login
    },
    


]

const router = createRouter ({
    history : createWebHistory(process.env.BASE_URL),
    routes

})
export default router