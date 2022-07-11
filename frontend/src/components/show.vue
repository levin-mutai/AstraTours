<template>
  <div class="description">

      <div class="title">
   
      </div>
      <div class="row">
          <!-- first row  -->
          <div class="row" v-for="data in info " :key="data.destinationId">
              <div class="col-md-6 col-lg-6">
                  <!-- Image to be used here -->
                  <img :src="data.imageurl" alt="" size="34*34">
              </div>
                <div class="col-md-6 col-lg-6" id="desc" >
                   <!-- a small description of the hotel/destination and the service offered -->
                   <h2>{{data.name}}</h2>
                   <p>
                       {{data.description}}
                   </p>
                   <div class="col" style="padding-bottom:60px;">
                       <h4>{{data.categori}}</h4>
                       <h4>Price : {{data.price}}</h4>
                       <h4>Rating : {{data.rating}}/5</h4>
                   </div>
                
                   <button class="about-view packages-btn pull-right"  @click="message" style="position:relative; vertical-align: bottom;">
                                                Add to cart 
                                            </button>
              </div>
          </div>
          <div class="row" id="experiences">
              <!-- Should loop over this div outputing atleast four experiences -->
              <div class="col-md-3 col-lg-3 lev">
                <div class="card" >
                    <img src="../components/assets/wallp.jpg" alt="" size="34*34">
                    <div class="card-body">
                        <h5 class="card-title">Celebrations at the hotel</h5>
                    </div>
                </div>
              </div>
              <div class="col-md-3 col-lg-3 lev">
                 <div class="card" >
                    <img src="../components/assets/wallp.jpg" alt="" size="34*34">
                    <div class="card-body">
                        <h5 class="card-title">Celebrations at the hotel</h5>
                    </div>
                </div>
              </div>
              <div class="col-md-3 col-lg-3 lev">
                  <div class="card" >
                    <img src="../components/assets/wallp.jpg" alt="" size="34*34">
                    <div class="card-body">
                        <h5 class="card-title">Celebrations at the hotel</h5>
                    </div>
                </div>
              </div>
              <div class="col-md-3 col-lg-3 lev">
                  <div class="card" >
                    <img src="../components/assets/wallp.jpg" alt="" size="34*34">
                    <div class="card-body">
                        <h5 class="card-title">Celebrations at the hotel</h5>
                    </div>
                </div>
              </div>
          </div>

      </div>
  </div>
</template>

<script>
import axios from 'axios';
import FlashMessage from '@smartweb/vue-flash-message';
export default {
    name: 'show',
    data(){
        return{
            info : '',
            id : ''
        }
    },
    methods:{
        message(){
            FlashMessage({
                            title: 'Don\'t Warry',
                            message: 'Be Happy!',
                            time: 5000,
                            flashMessageStyle: {
                                backgroundColor: 'linear-gradient(#e66465, #9198e5)'
                            }
                        });
        },
        getData(id){
            let url = 'hotels/'
            axios.get(url+id+'/').then(res=>{
                    this.info =  res.data
                    this.id = res.data[0].hotelId
            }).catch(err=>{

            }
                
            )
        },
        addToCart(){
            axios.post('user/cart/', {
    "user": this.$store.state.user,
    "hotel": this.id
})
        },
    },
     mounted(){
        this.getData(this.$route.params.id)
    }
}
</script>

<style scoped>
p{
    vertical-align: middle;
    float: left;
}
#experiences{
    padding-top: 70px;
}
.lev img{
    border-radius: 10px 10px 0 0 ;
    /* box-shadow: rgba(60, 64, 67, 0.3) 0px 1px 2px 0px, rgba(60, 64, 67, 0.15) 0px 2px 6px 2px; */
    box-shadow: rgba(0, 0, 0, 0.15) 0px 15px 25px, rgba(0, 0, 0, 0.05) 0px 5px 10px;
}
.lev:hover{
    opacity: 90%;
    transition: opacity .5s;
    cursor: pointer;
    /* box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px; */

}
.card{
    border: none;
    box-shadow: rgba(0, 0, 0, 0.15) 0px 3px 3px 0px;
}
@media screen and (min-width:762px){
    .description{
        padding: 120px 100px 70px 100px;
    }
}
.pull-right{
    
    padding: 6px 18px;
    border-radius: 3px;
    font:bolder;
    /* pointer-events: none; */
}
</style>