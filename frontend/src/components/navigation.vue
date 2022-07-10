<template>
  <div class="hello">

    <!-- nav menu -->
    <div class="sticky" style="width:100%;">
      <nav class="navbar1">
        
         <div class="lo">
            <img :src="require('./assets/logo.png')" alt="Sav4ner" class="logo"> <h1 class="he">Astra<span>Tours</span></h1>
         </div>
        
        <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
        
          <ul class="">
            <li class="nav-item">
                
                <router-link class="nav-link1" :to="{name : 'home'}"><i class="fa fa-home" aria-hidden="true"></i>
Home</router-link>
            </li>
            <li class="nav-item">
                
                <router-link class="nav-link1" :to="{name : 'destinations'}"><i class="fa fa-plane" aria-hidden="true"></i> Destinations</router-link>
            </li>
            <li class="nav-item">
                
                <router-link class="nav-link1" :to="{name : 'hotels'}"><i class="fa fa-bed" aria-hidden="true"></i> Hotels</router-link>
            </li>
            <li class="nav-item">
               
                <router-link class="nav-link1" :to="{name : 'bookings'}"><i class="fa fa-bookmark-o" aria-hidden="true"></i> Bookings</router-link>
            </li>
            <li class="nav-item">
                
                <router-link class="nav-link1" :to="{name : 'cart'}"><i class="fa fa-shopping-cart" aria-hidden="true"></i> Cart</router-link>
            </li>
            
        </ul>
        <div class="about-btn">
             
          <router-link class="login" :to="{name : 'login'}"><i class="fa fa-sign-in" aria-hidden="true"> login</i> </router-link>
          

          <img :src="require('./assets/prof.png')"   class="rounded-circle">
              
          
        </div>
        <div class="bars">
          <i class="fa fa-bars" aria-hidden="true" style="font-size:24px; margin-right:40px; color:white; margin-top:20px;"></i>
        </div>
        <!-- <div class="cross" >
          <div class="cros1" style="width:20x; height:2px; background:white; "></div>
          <div class="cros2" style="width:20x; height:2px; background:white; "></div>
        </div> -->
       
      </nav>
       <div class="drop">
          <ul class="">
            <li class="nav-item">
                
                <router-link class="nav-link1" :to="{name : 'home'}"><i class="fa fa-home" aria-hidden="true"></i>
Home</router-link>
            </li>
            <li class="nav-item">
                
                <router-link class="nav-link1" :to="{name : 'destinations'}"><i class="fa fa-plane" aria-hidden="true"></i> Destinations</router-link>
            </li>
            <li class="nav-item">
                
                <router-link class="nav-link1" :to="{name : 'hotels'}"><i class="fa fa-bed" aria-hidden="true"></i> Hotels</router-link>
            </li>
            <li class="nav-item">
               
                <router-link class="nav-link1" :to="{name : 'bookings'}"><i class="fa fa-bookmark-o" aria-hidden="true"></i> Bookings</router-link>
            </li>
            <li class="nav-item">
                
                <router-link class="nav-link1" :to="{name : 'cart'}"><i class="fa fa-shopping-cart" aria-hidden="true"></i> Cart</router-link>
            </li>
            
        </ul>
        </div>
    </div>
   
    
  </div>
</template>

<script>
export default {
  name: 'navigation',
  props: {
    msg: String
  }
}

  
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.bars{
  display: none;

}
.drop{
  display: none;
}
.cross{
  margin-left: 40px;
}
.rounded-circle{
  /* background-color:rgb(209, 195, 195); */
  border: indigo;
  border-width: 4px;
  vertical-align:middle;
  margin-top: -40px;
  margin-right: 10px;
  z-index:1 ;
  width: 40px;
  height: 40px;
}
.lo{
  display: flex;
  flex-direction: row;
  justify-content:start;
  float: left;
  
}

.login{

  vertical-align:middle;
  margin-top: -40px;
  margin-right: 10px;
  color: antiquewhite;
  font-weight: bolder;
  font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
.login:hover{
   background: #454647;
    /* transition: .01s; */
    color: orange;
    /* padding:17px 10px; */
    border-radius: 4px;
    margin-top: -36px;
    padding: 5px;
}
body{
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

}
.he{
  color: aliceblue;
  float: left;

  margin-top: 15px;
  font: bolder;
  font-family: 'Comforter', cursive;
  font-family: 'Dancing Script', cursive;
  font-family: 'Tillana', cursive;
}
.he span{
  color: orange;
}
/* nav decorators */
 .router-link-exact-active router-link-active {
    background: #454647;
    transition: .5s;
    color: antiquewhite;
    padding:14px 10px;
    border-radius: 4px;
  }
  .nav-link1:hover{
    background: #454647;
    /* transition: .01s; */
    color: aliceblue;
    /* padding:17px 10px; */
    border-radius: 4px;
    margin-top: 4px;
  }
a{
  text-decoration: none;
}
.navbar1{
  margin-top: 0;
  margin-left: 0;
  width:100%;
  height: 65px;
  background: #16161d;
  position: absolute;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-content:stretch;
  
}
.navbar1 ul {
  list-style: none;
  display: flex;
  flex-direction: row;
  float: right;
  /* margin-right: 10%; */
  margin-top:-1px;
  
  
}
.nav-item {
    margin-top: 2px;
   padding: 0 1.6vh;
}
.nav-link1{
  /* margin-top: 10px; */
  color:orange;
  font:bolder;
  font-size: 20px;
   padding: 12px 8px;
}
.sticky{
    position: fixed;
    z-index:2;
}
.logo{
  margin: 2px 5px;
  height: 60px;
  width: auto;
  float: left;
  margin-top: 22px;
  margin-left: 3%;
}
#image{
  float: right;
  color: orange;
  font: bolder;
  margin-right: -3%;

}

@media screen and (max-width: 1070px) {
  .bars{
  display: inline;

}
  .navbar1 ul{
    display: none;
  }
  .rounded-circle{
    display: none;
  }
  .login{
    margin-right: 10px;
  }
  .drop{
    height: 100vh;
    width: 80%;
    background: #16161d;
    display: block;
    margin-left: -10800px;
    
  }
  .drop ul{
    justify-content: space-between  ;
     display: block;
  }
  .nav-link1{
    padding-top: 70px;
  }
  .nav-link1:hover{
    background: transparent;
    /* transition: .01s; */
    color: aliceblue;
    /* padding:17px 10px; */
    border-radius: 4px;
    margin-top: 4px;
  }
  .nav-link1:active{
    background: transparent;
    /* transition: .01s; */
    color: aliceblue;
    /* padding:17px 10px; */
    border-radius: 4px;
    margin-top: 4px;
  }
  .show{
    display: block;
     height: 100vh;
    width: 80%;
    background: #16161d;
    margin-left: 0;
    transition: all .3s;
    
  }
  
}


</style>
