import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'

const routes = [{
  path: '/',
  name: 'root',
  component: App
},
               {
  path: '/user/signUp',
  name: "signUp",
  component: SignUp
}]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
