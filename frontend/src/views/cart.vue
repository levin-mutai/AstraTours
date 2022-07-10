<template>
<div class="cart">
    <div class="row">
        <div class="col" v-if="items==''">
           


        <div class="empt" v-if="items == ''">
            <div class="card">
  <!-- <h5 class="card-header">Featured</h5> -->
  <div class="card-body">
      <br>
      <img src="../components/assets/cart.668e6453.svg" alt="">
      <br>
      <br>
    <h3 class="card-title">Your Cart is empty</h3>

    <p class="card-text">Browse our destinations/hotels and discover our best deals!</p>
    <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
  </div>
  
</div>
        </div>
        </div>
        <!-- <div class="col-md-3 col-lg-3">
            <button type="button" class="btn btn-primary btn-lg">CHECKOUT({{bill}})</button>
        </div> -->
    </div>
</div>
  
</template>

<script>
import axios from 'axios'
export default {
    name: 'cart',

    data(){
        return{
            items : ''
        }
    },
    methods:{
        fetchall(){
            let userid = this.userid
            axios.get('http://localhost:8000/user/cart/'+userid+'/').then(res=>{
                this.items = res.data
                console.log(res.data)
            })
        }
    },
    mounted(){
        this.fetchall()
    }
}
</script>

<style scoped>
.cart{
    margin: 0 7%;
    padding-top: 100px;
    padding-bottom: 100px;
}
.row{
    /* height: 200px; */
}
.card{
    border: none;
    box-shadow: rgba(0, 0, 0, 0.15) 0px 5px 15px 0px;
}
.empt{
    padding-bottom: 90px ;
}
</style>