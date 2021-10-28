<template>
    <div id="newProduct" class="header">
            <nav>
                <button v-if="is_auth" v-on:click="loadHome">Inicio</button>
                <button v-if="is_auth" v-on:click="loadNewProduct">Nuevo Producto</button>
                <button v-if="is_auth" v-on_click="loadEditarProducto">Editar Producto</button>
                <button v-if="is_auth" v-on:click="loadEliminarProducto">Eliminar Producto</button>
                <button v-if="is_auth" v-on:click="loadMisProductos">Mis Productos</button>
            </nav>
    </div>
        <div class="main-component">
            <form v-on:submit.prevent="processNewProduct">
                <h2>Agregar nuevo producto</h2>
                <input type="text" v-model="product.name_product" placeholder="Nombre del producto" required>
                <br>
                <textarea name="description" placeholder="Descripción del producto (máximo 300 carácteres)" maxlength="300"></textarea>
                <br>
                <label>Precio unitario (pesos colombianos):</label>
                <br>
                <input type="number" name="price" min="1000" step="1000" required value=1000>
                <br>
                <label>Unidad de venta:</label>
                <br>
                <select class="unit" v-model="product.unit_Sales_product">
                    <option value="kilogramo">Kilogramo</option>
                    <option value="libra">Libra</option>
                    <option value="gramo">Gramo</option>
                    <option value="litro">Litro</option>
                    <option value="mililitro">Mililitro</option>
                </select>
                <select class="id" v-model="product.username_fk_id">
                  <option disabled selected>Seleccione su id</option>
                </select>
                <div class="amount">
                    <h2>Cantidad</h2>
                    <label>Cantidad (en unidades de venta) que tienes disponibles para venta.<br></label>
                    <center>
                    <input type="number" name="amount" min="1" step="1" required value=1>
                    </center>
                    <br>
                    <label>Si vendes por libras, debes poner cuántas libras tienes diponibles.</label>
                </div>
                <br>
                <label>Adjuntar imagen (opcional):</label>
                <br>
                <br>
                <input type="file" name="image" accept="image/png, image/jpg">
                <br>
                <button type="submit">Crear producto</button>
            </form>
        </div>
</template>

<script>
import axios from 'axios';
export default {
  name:"NewProduct",
  data:function(){
    return{
      product:{
        name_product:"",
        description_product:"",
        price_product:"",
        sales_unit_product:"",
        amount_product:"",
        username_fk_id:"",
        image_product:null,
      }
    }
  },
  methods:{
    processNewProduct:function(){
      axios.post("https://ciclo3grupo2agroclicbd.herokuapp.com/product/",this.product,{headers:{}})
      .then((result)=>{
        let dataNewProduct={
          name_product:this.user.name_product,
          token_access:result.data.access,
          token_refresh:result.data.refresh,
        }
        this.$emit('completedNewProduct',dataNewProduct)
      })
      .catch((error)=>{
        console.log(error)
        alert("Ha ocurrido un error en el registro");
      });
    }
  }
}
</script>

<style>
body{
    margin: 0 0 0 0;
    
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  }
form{
  width: 500px;
  padding: 16px;
  border-radius: 10px;
  margin:auto;
  background-color:#0b5240;
  margin-top: 20px;
}
textarea{
    width:400px;
    border-radius: 10px;
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
form input[type="radio"]{
  font-style:italic;
  font-size: 18px;
  padding:0;
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

</style>
