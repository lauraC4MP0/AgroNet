<template>
  <div id="app" class="app">
    <div class="menu">
      <nav>
        <button v-if="!is_auth" v-on:click="loadLogIn">Iniciar Sesión</button>
        <button v-if="!is_auth" v-on:click="loadSignUp">Registrarse</button>
      </nav>
    </div>

    <div class="header">

    </div>
    <div class="menu_bar">
    <nav>
  <ul>
    <li>
      <a v-if="is_auth"><router-link to="/home"> Inicio</router-link></a>
    </li>
    <li>
      <a v-if="is_auth"><router-link to="/user/edit"> Perfil</router-link></a>
    </li>
    <li>
      <a v-if="is_auth"><router-link to="/product"> Mis Productos</router-link></a>
    </li>
		<li><a v-if="is_auth"><router-link to="/product/new"> Nuevo Producto</router-link></a></li>
						
						
						
			
    
    <li>
      <a v-if="is_auth" v-on:click="logout"> Cerrar sesión</a>
    </li>
  </ul>
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
  name: "App",
  data: function () {
    return {
      is_auth: false,
    };
  },
  components: {},
  methods: {
    verifyAuth: function () {
      if (this.is_auth == false) {
        this.$router.push({ name: "logIn" });
      }
    },
    loadLogIn: function () {
      this.$router.push({ name: "logIn" });
    },
    loadSignUp: function () {
      console.log("test singup");
      this.$router.push({ name: "signUp" });
    },
    logout: function (data) {
      localStorage.removeItem(data.token_access);
      this.is_auth = false;
      this.$router.push({ name: "logIn" });
    },
    completedLogIn: function (data) {
      const userId = "123";
      localStorage.setItem("isAuth", true);
      localStorage.setItem("username", data.id);
      localStorage.setItem("token_access", data.token_access);
      localStorage.setItem("token_refresh", data.token_refresh);
      alert("Autenticación Exitosa");
      /*para mantener la sesion*/
      this.is_auth = true;
      //this.verifyAuth();
      //this.$session.start();
      //this.$router.push({name: "newProduct", params:{ username: username }})
      //this.$router.push({ path: '/user', params: {username} })
      this.$router.push({ name: "home" });
    },
    completedSignUp: function (data) {
      alert("Registro Exitoso");
      this.$router.push("/user/logIn");
    },
  },
  created: function () {
    this.verifyAuth();
  },
};
</script>

<style>



body{
margin: 0 0 0 0;

}

.header{

padding: 9%;
/*background-color: rgba(122, 197, 112, 0.932); */

background: url("headerf.jpg");
background-size:cover;
color:#f6f8f8;
justify-content: space-between;
align-items: unset;
}


.menu nav button{
color: #E5E7E9;
background: #0b5240;
border: 1px solid #E5E7E9;
align-items: right;
border-radius: 50px;
padding: 10px 20px;
float: right;
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
background: url(https://elsolweb.tv/wp-content/uploads/2020/02/Cultivo-de-Fresa-Subachoque-2-scaled.jpg)
}
@import url(https://fonts.googleapis.com/css?family=Open+Sans);

.menu_bar html {
  height:100%;
  background-image: linear-gradient(to right top, #8e44ad 0%, #3498db 100%);
}

.menu_bar nav {
  max-width: 960px;
  mask-image: linear-gradient(90deg, rgba(255, 255, 255, 0) 0%, #ffffff 25%, #ffffff 75%, rgba(255, 255, 255, 0) 100%);
  margin: 0 auto;
  padding: 10px 0;
}

.menu_bar nav ul {
  text-align: center;
  background: linear-gradient(90deg, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 0.2) 25%, rgba(255, 255, 255, 0.2) 75%, rgba(255, 255, 255, 0) 100%);
  box-shadow: 0 0 25px rgba(0, 0, 0, 0.1), inset 0 0 1px rgba(255, 255, 255, 0.6);
}

.menu_bar nav ul li {
  display: inline-block;
}

.menu_bar nav ul li a {
  padding: 18px;
  font-family: "Open Sans";
  text-transform:uppercase;
  color: #0b5240;
  font-size: 18px;
  text-decoration: none;
  display: block;
}

.menu_bar nav ul li a:hover {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1), inset 0 0 1px rgba(255, 255, 255, 0.6);
  background: rgba(255, 255, 255, 0.1);
  color: rgba(0, 35, 122, 0.7);
}
</style>