<template>
  <div class="description">

      <div class="title">
   
      </div>
      <div class="row">
          <!-- first row  -->
          <div class="row">
              <div class="col-md-6 col-lg-6">
                  <!-- Image to be used here -->
                  <img src="../components/assets/wallp.jpg" alt="" size="34*34">
              </div>
               <div class="col-md-6 col-lg-6" id="desc">
                   <!-- a small description of the hotel/destination and the service offered -->
                   <p>
                       Lorem ipsum dolor sit amet consectetur adipisicing elit. Harum dolorum aspernatur magni laboriosam autem nisi assumenda. Excepturi asperiores quia odio natus quasi quod ipsum suscipit quisquam, eveniet voluptas eum enim.
                       Magni nam fugiat voluptates dolores, ab ut neque officiis recusandae voluptatem adipisci id vitae ea, soluta debitis molestias veniam vel quae illum? Error eos distinctio recusandae tempore dolore illo doloremque.
                       Quia similique odio quaerat laudantium distinctio in magnam molestiae, neque, qui, numquam ea excepturi a hic minus fugit nobis sed? Dolores aspernatur repellat in ab dolor, voluptatem nemo dignissimos error.
                   </p>
                   {{$route.params.id}}
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
import FlashMessage from '@smartweb/vue-flash-message';
export default {
    name: 'desc',
    data(){
        return{

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
        }
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