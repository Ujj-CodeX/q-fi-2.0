import { createRouter , createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import Dash from '../components/UserDashboard.vue'
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
    }

]

const router = createRouter ({
    history : createWebHistory(process.env.BASE_URL),
    routes

})
export default router