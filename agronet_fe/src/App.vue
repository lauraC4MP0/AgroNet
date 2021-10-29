<template>
  <div id="app" class="app">
    <div class="header">
      <h1>AGRONET APP</h1>
        <nav>
        <button v-if="!is_auth" v-on:click="loadLogIn" > Iniciar Sesión </button>
        <button v-if="!is_auth" v-on:click="loadSignUp" > Registrarse </button>

        <md-button v-if="is_auth" ><router-link to="/user/home"> Inicio</router-link> </md-button>
        <md-button v-if="is_auth" ><router-link to="/user/perfil"> Perfil</router-link> </md-button>
        <md-button v-if="is_auth" ><router-link to="/product/newProduct"> Producto</router-link> </md-button>
        <md-button v-if="is_auth" v-on:click="loadMyProduct" ><router-link to="/product/myproduct"> Mis Productos</router-link> </md-button>
        <md-button v-if="is_auth" v-on:click="logout" ><router-link to="/user/signUp"> Cerrar Sesión</router-link> </md-button>
        </nav>
    </div>
    
    <div class="main-component">
      <router-view
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
      >
      </router-view>
    </div>


    
  </div>
</template>

<script>
  export default {
    name: 'App',
    data: function(){
      return{
        is_auth: false
      }
    },
components: {
},
methods:{
verifyAuth: function() {
  if(this.is_auth == false){
    this.$router.push({name: "logIn"})
  }
  else {
    this.$router.push({name: "home"})
  }
},
loadLogIn: function(){
  this.$router.push({name: "logIn"})
},

loadSignUp: function(){
  console.log("test singup")
  this.$router.push({name: "signUp"})
},

logout: function(data){
  localStorage.removeItem(data.token_access);
  this.is_auth=false;
  this.$router.push({name:'logIn'});
},
completedLogIn: function(data) {
 localStorage.setItem("isAuth", true);
 localStorage.setItem("username", data.id);
 localStorage.setItem("token_access", data.token_access);
 localStorage.setItem("token_refresh", data.token_refresh);
 console.log(localStorage.getItem("username"));
 alert("Autenticación Exitosa");
 /*para mantener la sesion*/
 this.is_auth=true;
 //this.verifyAuth();
 //this.$session.start();
  //this.$router.push({name: "newProduct", params:{ username: username }})
 //this.$router.push({ path: '/user', params: {username} })
 this.verifyAuth();
 },
completedSignUp: function(data) {
 alert("Registro Exitoso");
 this.$router.push("/user/logIn")
 },
},
created: function(){
  this.verifyAuth()
}
}
</script>

<style>
body{
max-width: 0 0 0 0;
}

.header{
margin: 0%;
padding: 0%;
width: 100%;
height: 10vh;
min-height: 100px;
background-color: #0b5240;
color: white;
display: flex;
justify-content: space-between;
align-items: center;
}

.header h1{
width: 20%;
text-align: center;
}

.header nav
{
height: 0%;
width: 20%;
display: flex;
justify-content: space-around;
align-items: center;
font-size: 20px;


}

.menu nav button{
color: #E5E7E9;
background: #0b5240;
border: 1px solid #E5E7E9;
align-items: right;
border-radius: 5px;
padding: 10px 20px;
}

.header nav button:hover
{
color: #283747;
background: #E5E7E9;
border: 1px solid #E5E7E9;
}

.main-component{
height: 75vh;
margin: 0%;
padding: 0%;
background: #FDFEFE;
}


</style>