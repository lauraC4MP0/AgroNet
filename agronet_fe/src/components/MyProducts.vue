<template>
<div class="main-component">
  <center><h2>Mis productos</h2><h3>Aquí puedes ver todos tus productos</h3></center>
  <ul class="list">
    <li v-for="product in products" :key="product">Nombre: {{product.name_product}}<br>Descripción: {{product.description_product}}<br>Precio: ${{product.price_product}}<br>Unidad de venta: {{product.sales_unit_product}}<br>Cantidad: {{product.amount_product}}<br>usuario: {{product.username_fk}}
    </li>
  </ul>
</div>
</template>


<script>
import axios from "axios";

export default {
  name: "MyProducts",
  data: function () {
    return {
      is_auth: true,
      
      products: [],
    };
  },
  created: async function () {
    this.processMyProducts();
  },
  methods: {
    processMyProducts: function () {
      axios
        .get("https://ciclo3grupo2agroclicbd.herokuapp.com/product/")
        .then((result) => {
          console.log(result.data);
          this.products = result.data;
        })
        .catch((error) => {
          console.log(error);
          alert("No fue posible cargar los productos, intente mas tarde.");
        });
    },
  },
};
</script>


<style>

body{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
h2,h3{
font-style: italic;
}
.list{
  counter-reset: li; 
    list-style: none; 
    *list-style: decimal; 
    font: 15px ;
    padding: 20px;
    margin-bottom: 4em;
    text-shadow: 0 1px 0 #000;
}

.list ul{
  margin: 0 0 0 2em;
  padding:16px;
}

.list li{
  position: relative;
    display: block;
    padding: .4em .4em .4em 2em;
    *padding: .4em;
    margin: .5em 0;
    background-color: #fff;
    color: #000;
    text-decoration: none;
    border-radius: .3em;
    transition: all .3s ease-out;  
}

.list li:hover{
  background: rgb(207, 233, 233);
  border: 1px solid #000;
}

.list li:hover:before{
  transform: rotate(360deg); 
}

.list li:before{
  content: counter(li);
    counter-increment: li;
    position: absolute; 
    left: -1.3em;
    top: 50%;
    margin-top: -1.3em;
    background: mediumaquamarine;
    height: 2em;
    width: 2em;
    line-height: 2em;
    border: 1px solid #000;
    text-align: center;
    font-weight: bold;
    border-radius: 2em;
    transition: all .3s ease-out;
}
</style>
