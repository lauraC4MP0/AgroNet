import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import LogIn from './components/LogIn.vue'
import SignUp from './components/SignUp.vue'
import MyProducts from './components/MyProducts.vue'
import NewProduct from './components/NewProduct.vue'
import Home from './components/Home.vue'
import EditProfile from './components/EditProfile.vue'
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
  path:'/product',
  name:"product",
  component:MyProducts
},
{
  path:'/product/new',
  name:"new",
  component:NewProduct
},
{
  path:'/home',
  name:"home",
  component:Home
},
{
  path:'/user/edit',
  name:"edit",
  component:EditProfile
},
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router
