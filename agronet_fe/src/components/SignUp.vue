<template>
  <div class="signup">
    <div class="container">
      <h2>Crear cuenta</h2>
      <br />
      <h3>Ingrese su información, por favor:</h3>
      <br />
      <form v-on:submit.prevent="processSignUp">
        <input
          type="text"
          v-model="user.usersname"
          placeholder="Número de documento de identidad"
          required
        />
        <br />
        <input
          type="text"
          v-model="user.name_user"
          placeholder="Nombres"
          required
        />
        <br />
        <input
          type="text"
          v-model="user.lastname_user"
          placeholder="Apellidos"
          required
        />
        <br />
        <input
          type="text"
          v-model="user.address_user"
          placeholder="Dirección"
          required
        />
        <br />
        <input
          type="tel"
          v-model="user.num_phone"
          placeholder="Teléfono"
          required
        />
        <br />
        <input
          type="password"
          v-model="user.password"
          placeholder="Contraseña (8 carácteres)"
          minlength="8"
          required
        />
        <br />
        <input
          type="email"
          v-model="user.email"
          placeholder="Correo electrónico"
          required
        />
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
        <input
          type="password"
          placeholder="Confirma tu contraseña"
          minlength="8"
          required
        />
        <br />
        <button type="submit">Registrarse</button>
      </form>
    </div>
  </div>
</template>

<script>

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
            token_refres: result.data.refresh,
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
.signup {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.container {
  border: 3px solid seagreen;
  border-radius: 10px;
  width: 25%;
  height: 60%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.signup h2,
h3 {
  color: seagreen;
}

.signup form {
  width: 70%;
}

.signup input {
  height: 40px;
  width: 100%;
  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;
  border: 1px solid seagreen;
}

.signup button {
  width: 100%;
  height: 40px;
  color: white;
  background: seagreen;
  border: 1px solid white;
  border-radius: 5px;
  padding: 10px 25px;
  margin: 5px 0 25px 0;
}

.signup button:hover{
    background: seagreen;
    color:white;
    border: 1px solid seagreen;
}
</style>
