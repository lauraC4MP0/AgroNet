<template>
  <div id="app" class="app">

    <div class="header">

      <h1>AGRONET</h1>
      <nav>
        <button v-if="is_auth" > Inicio </button>
        <button v-if="is_auth" > Cuenta </button>
        <button v-if="is_auth" > Cerrar Sesión </button>
        <button v-if="!is_auth" v-on:click="loadLogIn" > Iniciar Sesión </button>
        <button v-if="!is_auth" v-on:click="loadSignUp" > Registrarse </button>
      </nav>
    </div>

    <div class="main-component">
      <router-view
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
      >
      </router-view>
    </div>


    <div class="footer">
      <h2>Misión TIC 2022</h2>
    </div>
  </div>
</template>