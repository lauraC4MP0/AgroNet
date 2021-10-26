import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import LogIn from './components/LogIn.vue'
import SignUp from './components/SignUp.vue'
import NewProduct from './components/NewProduct.vue'
const routes = [{
  path: '/',
  name: 'root',
  component: App
},
{
  path: '/user/signUp',
  name: "signUp",
  component: SignUp
},
{
 path: '/user/logIn',
 name: "logIn",
 component: LogIn
 },
{
  path:'/product/newProduct',
  name:"newProduct",
  component:NewProduct
},
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router
