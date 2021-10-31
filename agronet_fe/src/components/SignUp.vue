<template>
  <br />
  <center>
    <div id="error" class="alert alert-danger ocultar" role="alert">
      Las contraseñas no coinciden, vuelve a intentar.
    </div>
  </center>
  <div class="main-signup">
    <form v-on:submit.prevent="processSignUp">
      <h3>Crear cuenta</h3>
      <br />
      <input
        type="text"
        v-model="user.id"
        placeholder="Número de documento de identidad"
        required
      />
      <br />
      <input
        type="text"
        v-model="user.usersname"
        placeholder="Username"
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
        type="tel"
        v-model="user.num_phone"
        placeholder="Teléfono"
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
      <input
        type="password"
        id="pass1"
        v-model="user.password"
        placeholder="Contraseña (8 carácteres)"
        minlength="8"
        required
      />
      <br />
      <input
        type="password"
        id="pass2"
        placeholder="Confirma tu contraseña"
        minlength="8"
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
      <select id="departments" v-on:change="getCities">
        <option disabled selected>Selecciona tu departamento</option>
        <option
          v-for="department in departments"
          :key="department"
          :value="department.id_departament"
        >
          {{ department.name_departament }}
        </option>
      </select>
      <select v-model="user.id_city">
        <option disabled selected>Selecciona tu ciudad</option>
        <option
          v-for="city in filteredCities"
          :key="city"
          :value="city.id_city"
        >
          {{ city.name_city }}
        </option>
      </select>
      <select v-model="user.sex_user">
        <option disabled selected>Seleccione su sexo</option>
        <option value="Masculino">Masculino</option>
        <option value="Femenino">Femenino</option>
        <option>No binario</option>
        <option>Otro</option>
      </select>
      <br />
      <p>¿Eres agricultor?</p>
      <input
        type="radio"
        name="rol"
        value="Agricultor"
        v-model="user.rol_user"
        checked
      />
      <label>Sí, quiero mostrar mis productos</label>
      <br />
      <input type="radio" name="rol" value="Vendedor" v-model="user.rol_user" />
      <label>No, soy comerciante</label>
      <br />
      <button type="submit" id="login">Registrarse</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SignUp",
  data: function () {
    return {
      user: {
        id: null,
        usersname: "",
        name_user: "",
        lastname_user: "",
        email: "",
        address_user: "",
        id_city: null,
        num_phone: null,
        password: "",
        sex_user: "",
        rol_user: "",
      },
      pass1: document.getElementById("pass1"),
      pass2: document.getElementById("pass2"),
      e: document.getElementById("error"),
      b: document.getElementById("login"),
      departments: [],
      department: document.getElementById("departments"),
      cities: [],
      filteredCities: [],
    };
  },
  created: async function () {
    this.getDepartments();
  },
  methods: {
    processSignUp: function () {
      var validacion = true;
      if (pass1.value != pass2.value) {
        document.getElementById("error").classList.add("mostrar");
        alert("Las contraseñas no coinciden, vuelve a intentar");
        validacion = false;
      } else {
        document.getElementById("error").classList.remove("mostrar");
        setTimeout(function () {
          location.reload();
        }, 3000);
        validacion = true;
      }
      if (validacion) {
        axios
          .post(
            "https://ciclo3grupo2agroclicbd.herokuapp.com/user/",
            this.user,
            {
              headers: {},
            }
          )
          .then((result) => {
            let dataSignUp = {
              id: this.user.id,
              token_access: result.data.access,
              token_refresh: result.data.refresh,
            };
            this.$emit("CompletedSignUp", dataSignUp);
          })
          .catch((error) => {
            console.log(error);
            alert("Ha ocurrido un error en el registro");
          });
      }
    },
    getDepartments: function () {
      axios
        .get("https://ciclo3grupo2agroclicbd.herokuapp.com/departament/")
        .then((result) => {
          this.departments = result.data;
        })
        .catch((error) => {
          console.log(error);
          alert("No hay departamentos registrados");
        });
    },
    getCities: function () {
      axios
        .get("https://ciclo3grupo2agroclicbd.herokuapp.com/city/")
        .then((result) => {
          this.cities = result.data;
          this.getFilteredCities();
        })
        .catch((error) => {
          console.log(error);
          alert("No hay ciudades registradas");
        });
    },
    getFilteredCities: function () {
      this.filteredCities = [];
      var dep = document.getElementById("departments").value;
      for (var i = 0; i < this.cities.length; i++) {
        if (this.cities[i].Departament == dep) {
          this.filteredCities.push(this.cities[i]);
        }
      } /*
      for (var city in this.cities) {;
        if (city.Departament == dep) {
          this.filteredCities.push(city);
        }
      }*/
    },
  },
};
</script>

<style>


.main-signup form {
  width: 400px;
  padding: 16px;
  border-radius: 10px;
  margin: auto;
  background-color: mediumaquamarine;
  margin-top: 20px;
  font-size: 20px;
}

.main-signup form h3 {
  height: 0;
  padding: 0%;
}

.main-signup form input[type="text"],
.main-signup form input[type="email"],
.main-signup form input[type="tel"],
.main-signup form input[type="password"],
select {
  width: 350px;
  padding: 3px 10px;
  border: 1px solid white;
  border-radius: 3px;
  background-color: white;
  margin: 8px 0;
  display: inline-block;
  font-size: 18px;
}

.main-signup form input[type="radio"] {
  font-style: italic;
}

.main-signup form button {
  width: 100%;
  padding: 8px 16px;
  margin-top: 28px;
  border-radius: 5px;
  border: 1px solid #000;
  display: block;
  color: white;
  background-color: #000;
}

.main-signup form button:hover {
  cursor: pointer;
}

.main-signup textarea {
  width: 100%;
  height: 100px;
  border: 1px solid white;
  margin: 8px 0;
  resize: none;
  display: block;
}

.main-signup .header nav {
  width: 20%;
}

.main-signup .ocultar {
  display: none;
}

.main-signup .mostrar {
  display: block;
}

#error {
  background-color: #f8d7da;
  height: 40px;
  color: #b53840;
  width: 400px;
  align-items: center;
  align-self: center;
  font-size: 18px;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  border-radius: 5px;
  top: 50%;
}
</style>
