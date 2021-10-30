<template>
    <div class = "header">
        <h1>AgroNet</h1>
            <nav>
                <button v-if = "is_auth" v-on:click = "loadHome">Inicio</button>
                <button v-if = "is_auth" v-on:click = "loadNewProduct">Nuevo Producto</button>
                <button v-if = "is_auth" v-on:click = "EditProduct">Editar Producto</button>
                <button v-if = "is_auth" v-on:click = "DeleteProduct">Eliminar Producto</button>
                <button v-if = "is_auth" v-on:click = "Products">Mis Productos</button>
            </nav>
    </div>

    <div class = deleteProduct>
      <div class = "title">
        <h3>aquí podrás <strong>eliminar</strong></h3>
      </div>
      <div class = "subtitle">
        <h2><strong>TUS PRODUCTOS</strong></h2>
      </div>
      </div>
      <div class = "productTable">
        <div class="container">
          </div>
          <div class="row">
              <div class="col-sm-6">
                  <table id="productTable" class="table table-bordered table-condensed table-striped">
                      <thead>
                          <tr>
                              <th>Producto</th>
                              <th>Descripción</th>
                              <th>Precio</th>
                              <th>Unidad de venta</th>
                              <th>Unidades disponibles</th>
                              <th>Eliminar</th>
                          </tr>
                      </thead>
                  </table><hr></hr>
              </div>
          </div>
      </div>
      
      </div> 
    </template>
    
    <script>
    import axios from 'axios';
        export default {
          name:"DeleteProduct",
          data:function(){
            return{
              product:{
                name_product:"",
                description_product:"",
                price_product:"",
                sales_unit_product:"",
                amount_product:"",
                username_fk_id:""
              }
            }
          },
          methods:{
            processDeleteProduct:function(){
              axios.delete("https://ciclo3grupo2agroclicbd.herokuapp.com/product/",this.product,{headers:{}})
              .then((result)=>{
                let dataNewProduct={
                  name_product:this.user.name_product,
                  token_access:result.data.access,
                  token_refresh:result.data.refresh,
                }
                this.$emit('completedDeleteProduct',dataDeletedProduct)
              })
              .catch((error)=>{
                console.log(error)
                alert("Ha ocurrido un error en el proceso");
              });
            }
          }
        }
    </script>
    
    <style>
      body{
        margin: 0 0 0 0;
        box-sizing: border-box;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
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
    
      .home label{
        font-size: 18px;
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
        width: 70%;
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
    
      .title{
        margin: 0 0 0 0;
        width: 100%;
        padding-top: 40px;
        padding-bottom: 20px;
        height: 5px;
        min-height: 5px;
        background-color: white;
        color:orange;
        display: flex;
        justify-content: space-between;
        align-items: center;
        vertical-align: bottom;
      }
    
      .subtitle{
        margin: 0 0 0 0;
        width: 100%;
        padding-top: 5px;
        padding-bottom: 60px;
        height: 5px;
        min-height: 5px;
        background-color: white;
        color:orange;
        display: flex;
        justify-content: space-between;
        align-items: center;
        vertical-align: top;
      }
    
      .title h3{
        margin: auto;
        text-align: center;
        vertical-align: text-bottom;
      }
    
      .subtitle h2{
        margin: auto;
        width: 30%;
       text-align: center;
       vertical-align: text-top;
    
      }
    
      table{
        width: 90%;
        margin-top: 30px;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: auto;
        align-items: auto;
        color: seagreen;
    
      }
    
      th, td{
        margin-top: 100px;
        text-align: center;
        vertical-align: middle;
      }
    
      hr {
        color: seagreen;
        background-color: seagreen;
        height: 5px;
        align-self: center;
        margin: auto;
        width: 90%;
      }
    
     .footer{
        margin:0 0 0 0;
        padding:0;
        width: 20x;
        height: 10vh;
        min-height: 20px;
        background-color:seagreen;
        color: white;
        width: 100%;
        height: 100px;
        display: flex;
        justify-content:center;
        align-items: center;
      }
    
      .footer h3{
        margin-right: 5%;
        margin-top: 0%;
        width: 100%;
        height: 100%;
        display: flex;
        justify-content:right;
        align-items: center;
      }
      
    </style>
    </body>
    </html>