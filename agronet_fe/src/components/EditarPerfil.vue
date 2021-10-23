<template>
    <h2>Editar perfil</h2>
    <form action="" method="post">
        <br><label for="fname">Documento de identidad:</label>
        <br><input type="text" id="Documento_Identidad" placeholder="Digite su documento">
        <br><label for="fname">Nombre:</label>
        <br><input type="text" id="Nombre" placeholder="Digite su nombre">
        <br><label for="fname">Apellido:</label>
        <br><input type="text" id="Apellido" placeholder="Digite su apellido">
        <br><label for="fname">Direccion:</label>
        <br><input type="text" id="Direccion" placeholder="Digite su direccion">
        <br><label for="fname">Telefono celular:</label>
        <br><input type="text" id="Telefono" placeholder="Digite su numero telefonico">
        <br><label for="fname">Correo electronico:</label>
        <br><input type="text" id="Correo" placeholder="Digite su correo">
        <br><select name="Sexo">
            <option selected value="0"> Sexo </option>
                <option value="1">Femenino</option>
                <option value="2">Masculino</option>
                <option value="3">Indefinido</option>
        </select>
        <br><label for="fname">Ciudad:</label>
        <br><input type="text" id="Ciudad" placeholder="Digite su ciudad">
        <br><label for="fname">Departamento:</label>
        <br><input type="text" id="Departamento" placeholder="Digite su departamento">
        <button id="Boton_Aceptar" v-on:click="Aceptar">Aceptar</button>
    </form>
</template>


<script>
export default {
  name: "Editar_Perfil",

  data: function () {},

  methods: {
    Aceptar: function () {},
  },

  created: function () {},
};
</script>


<style>
body{
    margin: 0 0 0 0;
    box-sizing: border-box;
    padding: 0px 20px 20px 20px;
    border: 5px solid black;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  }

form{
  width: 500px;
  padding: 16px;
  border-radius: 10px;
  margin:auto;
  background-color:mediumaquamarine;
  margin-top: auto;
}

textarea{
    border-radius: 10px;
    width: 450px;
    font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-size: 18px;;
}

.amount{
    width: 450px;
    padding:16px;
    padding-top: 1px;
    background-color: white;
    border-radius: 10px ;
    margin-top: 0;
    align-items: center;
    align-content: center;
    border-top: 0;
}
.main-component label{
    font-size: 18px;
}

.amount h2{
    border-top: 0;
}

.amount select{
    align-items: center;
    align-content: center;
    align-self: center;
}

form h3{
  height: 0;
  padding: 0%;
}

form input[type="text"],form input[type="email"],form input[type="tel"], form input[type="password"],select, form input[type="number"]{
  width: 450px;
  padding:3px 10px;
  border:1px solid white;
  border-radius: 3px;
  background-color:white;
  margin:8px 0;
  display: inline-block;
  font-size: 18px;
}

form .amount input[type="number"]{
    background-color: white;
    width: 40px;
    height: 40px;
    border:1px solid black;
    border-radius: 3px;
    align-content: center;
    align-items: center;
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
  border:1px solid white;
  margin:8px 0;
  resize: none;
  display: block;
}

.header{
  margin: 0%;
  padding: 0;
  width: 100%;
  height:10vh;
  min-height: 100px;
  background-color:seagreen;
  color:white;
  display:flex;
  justify-content: space-between;
  align-items: center;
}

.header h1{
  width: 20%;
  text-align: center;
}

.header nav{
  height: 100%;
  width: 20%;
  display:flex;
  justify-content: space-around;
  align-items: center;
  font-size: 20px;
}

.header nav button{
  color:mediumaquamarine;
  background-color: white;
  border: 1px solid black;
  border-radius: 5px;
  padding:10px 20px;
}

.header nav button:hover{
  color: seagreen;
  background-color: white;
  border: 1px solid white;
  cursor: pointer;
}

.footer{
  margin:0;
  padding:0;
  width:100%;
  height: 10vh;
  min-height: 100px;
  background-color:seagreen;
  color: white;
}

.footer h2{
  width: 90%;
  height: 100%;
  display: flex;
  justify-content:right;
  align-items: center;
}
</style>