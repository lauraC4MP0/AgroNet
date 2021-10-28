<template>
  <div id="app" class="app">
    
<div class="menu">
    
        <nav>
        
        <button v-if="!is_auth" v-on:click="loadLogIn" > Iniciar Sesión </button>
        <button v-if="!is_auth" v-on:click="loadSignUp" > Registrarse </button>
        </nav>
      </div>

      
    <div class="header">
    
    <nav>
    <md-button v-if="is_auth" ><router-link to="/product/newProduct"> Inicio</router-link> </md-button>
        <md-button v-if="is_auth" ><router-link to="/product/newProduct"> Perfil</router-link> </md-button>
        <md-button v-if="is_auth" ><router-link to="/product/newProduct"> Producto</router-link> </md-button>
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
  const userId = '123'
 localStorage.setItem("isAuth", true);
 localStorage.setItem("username", data.id);
 localStorage.setItem("token_access", data.token_access);
 localStorage.setItem("token_refresh", data.token_refresh);
 alert("Autenticación Exitosa");
 /*para mantener la sesion*/
 this.is_auth=true;
 //this.verifyAuth();
 //this.$session.start();
  //this.$router.push({name: "newProduct", params:{ username: username }})
 //this.$router.push({ path: '/user', params: {username} })
 this.$router.push({name:'newProduct'});
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
margin: 0 0 0 0;
}
.header{
margin: 3%;
padding: 9%;

/*background-color: rgba(122, 197, 112, 0.932); */
background-position: center center;
background-image: url("headerf.jpg");
background-size:cover;
color:#f6f8f8;
display: flex;
justify-content: space-between;
align-items: unset;
}
.header h1{
height: 5%; 
width: 20%;
text-align: center;
align-content: center;
}
.header nav
{
height: 0%;
width: 25%;
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
border-radius: 50px;
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