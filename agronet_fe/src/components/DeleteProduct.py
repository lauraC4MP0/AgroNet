<template>
  <div class="container">
    <center>
      <h2>Eliminar producto</h2>
      <h3>Selecciona el producto que deseas eliminar:</h3>
      <select v-on:change="setProduct" id="product">
        <option disabled selected>Selecciona el producto a eliminar</option>
        <option
          v-for="product in products"
          :key="product"
          :value="product.name_product"
        >
          {{ product.name_product }}
        </option>
      </select>
    </center>
    <br />
    <div class="info">
      <label
        >Nombre: <strong>{{ product.name_product }}</strong></label
      >
      <br />
      <label
        >Descripción: <strong>{{ product.description_product }}</strong></label
      >
      <br />
      <label
        >Precio: $<strong>{{ product.price_product }}</strong> COP</label
      >
      <br />
      <label
        >Unidad de venta:
        <strong>{{ product.sales_unit_product }}</strong></label
      ><br />
      <label
        >Cantidad: <strong>{{ product.amount_product }}</strong></label
      >
    </div>
    <br />
    <button v-on:click="processDeleteProduct">Eliminar producto</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "DeleteProduct",
  data: function () {
    return {
      product: {
        name_product: "",
        description_product: "",
        price_product: null,
        sales_unit_product: "",
        username_fk: null,
        amount_product: null,
      },
      products: [],
    };
  },
  created: async function () {
    this.getProducts();
  },
  methods: {
    getProducts: function () {
      axios
        .get("https://ciclo3grupo2agroclicbd.herokuapp.com/product/")
        .then((result) => {
          this.products = result.data;
        })
        .catch((error) => {
          console.log(error);
          alert("Ha ocurrido un error, no es posible obtener los productos");
        });
    },
    setProduct: function () {
      var name = document.getElementById("product").value;
      for (var i = 0; i < this.products.length; i++) {
        if (this.products[i].name_product == name) {
          this.product = this.products[i];
        }
      }
    },
    processDeleteProduct: function () {
      alert("Producto eliminado exitosamente");
    },
  },
};
</script>

<style>
body {
  margin: 0 0 0 0;
  box-sizing: border-box;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}

.container {
  width: 400px;
  padding: 16px;
  border-radius: 10px;
  margin: auto;
  background-color: mediumaquamarine;
  margin-top: 20px;
  font-size: 18px;
}

.info {
  background-color: #fff;
  padding: 16px;
  border-radius: 10px;
}
.info label {
  font-style: italic;
}
select {
  width: 350px;
  padding: 3px 10px;
  border: 1px solid #000;
  border-radius: 3px;
  background-color: white;
  margin: 8px 0;
  display: inline-block;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}

button {
  width: 100%;
  padding: 8px 16px;
  margin-top: 28px;
  border-radius: 5px;
  border: 1px solid #000;
  display: block;
  color: white;
  background-color: #000;
}

button:hover {
  cursor: pointer;
}
</style>
