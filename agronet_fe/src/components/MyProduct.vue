<template>
    <div v-if="loaded" class="information">
        <h1>Mis Productos</h1>
        <h2>Nombre: <span> {{ name }} </span></h2>
        <h2>Descripcion: <span> {{ description }} </span></h2>
        <h2>Precio: <span> {{ price }} </span></h2>
        <h2>Medida: <span> {{ sales }} </span></h2>
        <h2>Monto: <span> {{ amount }} </span></h2>
    </div>
</template>


<script>
    export default {
        name: "MyProduct",

        data: function(){
            return {
                loaded : false,
                name : "",
                description : "",
                price : 0,
                sales : 0,
                amount : 0,
            }
        },

        methods: {
            getData: async function(){
                if(localStorage.getItem("token_access") === null || localStorage.getItem("token_refresh") === null ){
                    this.$emit("logOut");
                    return;
                }
                await this.veryfyToken();
                let token = localStorage.getItem("token_access");
                let userId = jwt_decode(token).userId.ToString();

                axios.get(
                    `http://http://127.0.0.1:8000/user/${userId}/`,
                    {headers: {'Autorization': `Bearer ${token}`}}
                )
                .then((result) => {
                    this.loaded = true;
                    this.name = result.data.user.name;
                    this.description = result.data.balance;
                    this.price = result.data.price;
                    this.sales = result.data.sales;
                    this.amount = result.data.amount;
                })
                .catch((error) => {
                    this.$emit('logOut');
                })
            },

            verifyToken: function(){
                return axios.post(
                    `http://http://127.0.0.1:8000/refresh/`,
                    {refresh:localStorage.getItem("token_refresh")},
                    {headers={}}
                )
                .then((result) => {
                    localStorage.setItem("token_access", result.data.access)
                })
                .catch((error) => {
                    this.$emit('logOut');
                });
            }
        },

        created: async function(){
            this.getData();
        }
    }
</script>


<style>

.information{
    margin: 0;
    padding: 0%;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.information h1{
    font-size: 60px;
    color: #000000;
}

.information h2{
    font-size: 40px;
    color: #812424;
}

.information span{
    color: #c6c919;
    font-weight: bold;
}

</style>