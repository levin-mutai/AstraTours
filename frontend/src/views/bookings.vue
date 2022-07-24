<template>
  <div class="bookings">
     <div class="emp">
        <!-- <h1>This is the booking page of the website</h1> -->
      <img src="../components/assets/undraw_empty_street_re_atjq.svg" alt="">
      <br>
      <br>
      <h1 class="oops">oops! you've not booked any services with us. Please login to book</h1>
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
    }
  },
  mounted(){
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
}
</style>