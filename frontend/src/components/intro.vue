<template>
  <div class="intro">
      
        <div class="container">
            <div class="tabs-container">
                 <!-- Some content here -->
            </div>
        </div>
        <div class="amazing">
         <div class="container">
            <div class="row">
               <div class="col-md-12">
                  <div class="amazing-box">
                     <h2>Welcome to AstraTours</h2>
                     <span>Astra tours is a well known organisation that deals with tourism as a whole. We make it easy for you to book a tourism destination from the comfort of your mobile  device</span>
                     <router-link class="nav-link1" :to="{name : 'destinations'}"><i class="fa fa-plane" aria-hidden="true"></i> Book Now</router-link>
                     <!-- <a href="/destinations">Book Now</a> -->
                     <a href="#faq">Get More</a>
                  </div>
               </div>
            </div>
         </div>
      </div>

        <div class="London">
         <div class="container">
            <div class="row">
               <div class="col-md-12">
                  <div class="titlepage">
                     <!-- <h2>Welcome to AstraTours  </h2> -->
                     <br>
                     <span>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters,</span> 
                  </div>
               </div>
            </div>
         </div>
         <div class="container-fluid">
            <div class="London-img">
               <figure><img src="images/London.jpg" alt="img"></figure>
            </div>
         </div>
      </div>
    
  </div>

</template>

<script>
export default {

}
</script>

<style>
.intro{
    height: auto;
   padding-top: 65px;
}
.container::before,
.container::after {
  /* background: url("path/to/curve.svg") center bottom no-repeat; */
  content: '';
  height: 103px;
  position: absolute;
  width: 100%;
}

.container::before {
  bottom: 100%;
}

.container::after {
  top: 100%;
  transform: rotateX(180deg);
}
</style>