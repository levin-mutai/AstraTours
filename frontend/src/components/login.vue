<template >
  <div class="logi">
      <div class="form">
          <form @submit.prevent="login" method="post">
  <div class="imgcontainer">
    <img :src="require('./assets/prof.png')"  alt="Avater" class="rounded-circle">
  </div>

  <div class="container2">
    <label for="uname"><b><i class="fa fa-user-secret" aria-hidden="true">Username</i></b></label>
    <input type="text" placeholder="Enter Username" name="uname" required v-model="username"> 

    <label for="psw"><b> <i class="fa fa-key" aria-hidden="true"> Password</i> </b></label>
    <input type="password" placeholder="Enter Password" name="psw" required v-model="password">

    <button type="submit" @click="login">Login</button>
    <label>
      <input type="checkbox" checked="checked" name="remember"> Remember me
    </label>
  </div>

  <div class="contain" style="background-color:#f1f1f1">
    <button type="button" class="cancelbtn1"> <router-link  :to="{name : 'signup'}"><i class="fa fa-address-book" aria-hidden="true"> Sign Up</i> </router-link> </button>
    
    <span class="psw"><a href="#">Forgot password?</a></span>

  </div>
  
 
  </form>
  
      </div>
    
  </div>
</template>

<script>
import miniToastr from 'mini-toastr'
miniToastr.init()
import axios from 'axios'
export default {
    name: 'login',
    data() {
        return {
            password:"",
            username:"",
        }
    },
    methods: {
        login(){
            axios.post('http://127.0.0.1:8000/api/token/',{
                "username" : this.username,
                "password" : this.password
            })
            .then(Response=>{
                const token = Response.data.access
                const refresh_token = Response.data.refresh
                axios.defaults.headers.common['Authorization'] = 'Bearer ' + token

                this.$store.commit('setToken', Response.data.refresh)
                // localStorage.setItem('token', token)
                sessionStorage.setItem('access', token)
                sessionStorage.setItem('refresh', refresh_token)
                  //  this.$router.push("/");
                
                axios.get('/auth/users/me/').then(res=>{
                   this.$store.commit('setUser', res.data.firstname+' '+res.data.lastname)
                  //  sessionStorage.setItem('clientid', res.data.clientid)
                   sessionStorage.setItem('userid', res.data.id)
                   this.$store.commit('setUserid', res.data.id)
                   
                   this.$store.commit('setEmail', res.data.email)
                   this.$store.commit('setClientid', res.data.clientid)
                   this.$store.commit('setPhone', res.data.contact)
                   this.$router.go(-1)
                }).catch(err=>{
                    console.log('Fetching user data : ',err)
                })
            }).catch(err=>{
                miniToastr.error("Wrong creds Please check and try agin", "Incorrect creds/Poor Connection", 2000)
            })
        }
    },
}
</script>

<style>
    .rounded-circle{
        height: 80px;
        width: 80px;
    }
    /* Bordered form */
    .logi{
        
        padding-top: 75px;
        /* width: 100vh; */

    }
    .contain{
         background: rgb(236, 234, 234);
         width: 60%;
  margin: 20px 20%;
  background: rgb(236, 234, 234);
  
    }
.form {
  border: 3px solid #f1f1f1;
  width: 60%;
  margin: 20px 20%;
  background: rgb(236, 234, 234);
  border-radius: 20px;
  padding-bottom: 30px;
}

/* Full-width inputs */
input[type=text], input[type=password] {
  width: 100%;
  border-radius:5px ;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}
input[type=text]:focus, input[type=password]:focus   {
    outline: none;
  border: 1px solid #16161d;
}
/* Set a style for all buttons */
button {
  background-color: #04AA6D;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 30%;
  border-radius: 10px;
  align-self: center;
}

/* Add a hover effect for buttons */
button:hover {
  opacity: 0.8;
}

/* Extra style for the cancel button (red) */
.cancelbtn1 {
  width: auto;
  padding: 10px 18px;
  background-color: transparent;
}

/* Center the avatar image inside this container */
.imgcontainer {
  text-align: center;
  margin: 24px 0 12px 0;
}

/* Avatar image */
img.avatar {
  width: 40%;
  border-radius: 50%;
}

/* Add padding to containers */
.container2 {
  padding: 16px;
}

/* The "Forgot password" text */
span.psw {
  float: right;
  padding-top: 16px;
}

/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 500px) {
  span.psw {
    display: block;
    float: none;
    
  }
  .form{
      margin: 20px 5%;
      width: 80%;
  }
  .cancelbtn1 {
    width: 90%;
  }
}
</style>