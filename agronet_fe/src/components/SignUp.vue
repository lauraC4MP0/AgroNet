<template>
  <div class="main-component">
    <form v-on:submit.prevent="processSignUp">
      <h3>Crear cuenta</h3>
      <br/>
      <input type="text" v-model="user.usersname" placeholder="Número de documento de identidad" required />
      <br />
      <input type="text" v-model="user.name_user" placeholder="Nombres" required />
      <br />
      <input type="text" v-model="user.lastname_user" placeholder="Apellidos" required />
      <br />
      <input type="tel" v-model="user.num_phone" placeholder="Teléfono" required />
      <br />
      <input type="email" v-model="user.email" placeholder="Correo electrónico" required />
      <br />
      <input type="password" v-model="user.password" placeholder="Contraseña (8 carácteres)" minlength="8" required />
      <br />
      <input type="password" placeholder="Confirma tu contraseña" minlength="8" required />
      <br />
      <input type="text" v-model="user.address_user" placeholder="Dirección" required />
      <br />
      <select class="sex">
        <option>Sexo</option>
        <option value="Masculino">Masculino</option>
        <option value="Femenino">Femenino</option>
        <option>No binario</option>
        <option>Otro</option>
      </select>
      <br />
      <select class="department">
        <option>Departamento</option>
      </select>
      <br />
      <select>
        <option>Ciudad</option>
      </select>
      <br />
      <p>¿Eres agricultor?</p>
      <input type="radio" name="rol" checked />
      <label>Sí, quiero mostrar mis productos</label>
      <br />
      <input type="radio" name="rol" />
      <label>No, soy comerciante</label>
      <br />
      <button type="submit">Registrarse</button>
    </form>
  </div>

</template>

<script>
import axios from 'axios';
export default {
  name: "SignUp",
  data: function () {
    return {
      user: {
        usersname: "",
        name_user: "",
        lastname_user: "",
        email: "",
        address_user: "",
        id_city: "",
        id_department: "",
        num_phone: "",
        password: "",
        sex_user: "",
        rol_user: "",
      },
    };
  },
  methods: {
    processSignUp: function () {
      axios
        .post("https://ciclo3grupo2agroclicbd.herokuapp.com/user/", this.user, {
          headers: {},
        })
        .then((result) => {
          let dataSignUp = {
            usersname: this.user.usersname,
            token_access: result.data.access,
            token_refresh: result.data.refresh,
          };
          this.$emit("CompletedSignUp", dataSignUp);
        })
        .catch((error) => {
          console.log(error);
          alert("Ha ocurrido un error en el registro");
        });
    },
  },
};
</script>

<style>
body{
    margin: 0 0 0 0;
    box-sizing: border-box;
  }
form{
  width:400px;
  padding: 16px;
  border-radius: 10px;
  margin:auto;
  background-color:mediumaquamarine;
  margin-top: 20px;
}
form h3{
  height: 0;
  padding: 0%;
}
form input[type="text"],form input[type="email"],form input[type="tel"], form input[type="password"],select{
  width: 300px;
  padding:3px 10px;
  border:1px solid white;
  border-radius: 3px;
  background-color: #f6f6f6;
  margin:8px 0;
  display: inline-block;
}
form input[type="radio"]{
    width: 200px;
  font-style:italic;
}
form button{
  width:100%;
  padding: 8px 16px;
  margin-top: 28px;
  border-radius: 5px;
  border:1px solid #000;
  display: block;
  color:white;
  background-color: #000;
}
form button:hover{
  cursor:pointer;
}
textarea{
  width:100%;
  height: 100px;
  border:1px solid #f6f6f6;
  margin:8px 0;
  resize: none;
  display: block;
}
</style>
