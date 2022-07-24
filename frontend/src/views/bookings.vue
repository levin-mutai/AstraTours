<template>
  <div class="bookings">
     <div class="emp" v-if="bookings == ''">
        <!-- <h1>This is the booking page of the website</h1> -->
      <img src="../components/assets/undraw_empty_street_re_atjq.svg" alt="">
      <br>
      <br>
      <h1 class="oops">oops! you've not booked any services with us. Please login to book</h1>
     </div>

     <div class="nempty" v-for="data in bookings " :key="data.name">
                    <div class="card" style="padding-bottom:30px; margin-bottom:30px;">
                        <!-- <h5 class="card-header">Featured</h5> -->
                        <div class="card-body">
                            <!-- <br>
                            <img src="../components/assets/cart.668e6453.svg" alt="">
                            <br> -->
                            <br>
                            <h3 class="card-title">{{data.id}}</h3>

                            <p class="card-text">{{data.contact}}</p>
                            <p class="card-text">{{data.bill}}</p>
                            <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
                            <br>
                            
                            <!-- <button class="about-view packages-btn pull-right" id="show-modal" style="position:relative; vertical-align: bottom;width: 130px; background-color:#16161d ; border: none;" @click="checkOut(data);showModal = true;">
                                                <small><b>checkout</b>(KSH {{data.price }})</small>
                                            </button> -->
                        </div>
  
                    </div>
                    
                </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'booking',
  data(){
    return{
      userid: this.$store.state.userid,
      token: this.$store.state.refresh,
      bookings : '',
    }
  },
  methods:{
    getBookings(user){
      axios.get('user/park-bookings/'+user+'/').then(res=>{
        this.bookings = res.data
        console.log(this.bookings)
      })
    },
  },
  mounted(){
    this.getBookings(this.$store.state.userid)
        if (this.$store.state.userid==null) {
            
            axios.get('/auth/users/me/').then(res=>{
                   this.$store.commit('setUser', res.data.firstname+' '+res.data.lastname)
                  //  sessionStorage.setItem('clientid', res.data.clientid)
                   sessionStorage.setItem('userid', res.data.id)
                   this.$store.commit('setUserid', res.data.id)
                   
                   this.$store.commit('setEmail', res.data.email)
                   this.$store.commit('setClientid', res.data.clientid)
                   this.$store.commit('setPhone', res.data.contact)
                   alert('runn')
                }).catch(err=>{
                    this.$router.push('/login')
                })
        }

  }

}

</script>

<style scoped>
.emp{
  vertical-align: middle;
  margin-top: 10%;
}
.emp .oops{
  padding-top: 100px;
}
.bookings{
  height: auto;
  padding-top: 80px;
  margin: 0 7%;
  padding-top: 100px;
  padding-bottom: 100px;
}
.row{
    /* height: 200px; */
}
/* #show-modal{
    width: 250px;
    height: 70px;
} */
.card{
    border: none;
    box-shadow: rgba(0, 0, 0, 0.15) 0px 5px 15px 0px;
}
</style>