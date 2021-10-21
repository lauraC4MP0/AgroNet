import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import NewProduct from './components/NewProduct.vue'
import SignUp from './components/SignUp.vue'

const routes = [{
  path: '/',
  name: 'root',
  component: App
},
{
  path: '/user/NewProduct',
  name: "NewProduct",
  component: SignUpNewProduct

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
