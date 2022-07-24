<template>
  <div class="destination">
      <div class="container">
				<div class="gallary-header text-center">
					<h2>
						destinations to visit
					</h2>
					<p>
						These are the lists of Destinations offered by our organisation.  
					</p>
				</div><!--/.gallery-header-->
				<div class="packages-content">
					<div class="row">
                        <!-- <div v-for="data in info" :key="data.photo"> -->
                            <div class="col-md-3 col-sm-4" v-for="data in info" :key="data.photo" >
                            
                               <!-- <a href="#"> -->
                                    <div class="single-package-item" @click="$router.push({ path: '/desc/'+id+'/' })" >
                                    <img :src="data.imageurl" alt="package-place">
                                    <div class="single-package-item-txt">
                                        <h3 class='name'>{{data.name}} </h3>
                                        <div class="packages-para">
                                            <p>
                                                <!-- <span>
                                                    <i class="fa fa-angle-right"></i> 5iption daays 6 nights
                                                </span> -->
                                                <i class="fa fa-angle-right"></i> {{data.description.slice(0, 120)+' ...'}}
                                            </p>
                                            
                                                <hr>
                                                <span>
                                                    <i class="fa fa-angle-right"></i>  {{data.categori}}
                                                </span>
                                                
                                            
                                        </div><!--/.packages-para-->
                                        <div class="packages-review">
                                            
                                                <p v-if="data.rating==5">
                                                    <i class="fa fa-star"></i>
                                                    <i class="fa fa-star"></i>
                                                    <i class="fa fa-star"></i>
                                                    <i class="fa fa-star"></i>
                                                    <i class="fa fa-star"></i>
                                                </p>
                                                <p v-if="data.rating==4">
                                                    <i class="fa fa-star"></i>
                                                    <i class="fa fa-star"></i>
                                                    <i class="fa fa-star"></i>
                                                    <i class="fa fa-star"></i>
                                                </p>
                                                <p v-if="data.rating==3">
                                                    <i class="fa fa-star"></i>
                                                    <i class="fa fa-star"></i>
                                                    <i class="fa fa-star"></i>
                                                </p>
                                                <p v-if="data.rating==2">
                                                    <i class="fa fa-star"></i>
                                                    <i class="fa fa-star"></i>
                                                </p>
                                                <p v-if="data.rating==1">
                                                    <i class="fa fa-star"></i>
                                                    
                                                </p>
                                                <span class="pull-right">{{data.price+' KSH'}}</span>
                                            
                                        </div><!--/.packages-review-->
                                        <div class="about-btn">
                                            <!-- <button class="about-view packages-btn"  @click="showModal = !showModal">
                                                book now
                                            </button> -->
                                            
                                        </div><!--/.about-btn-->
                                    </div><!--/.single-package-item-txt-->
                                </div><!--/.single-package-item-->
                               <!-- </a> -->

                            </div><!--/.col-->
                        <!-- </div> -->

					</div><!--/.row-->
				</div><!--/.packages-content-->
			</div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'destinations',
    data() {
        return {
            info : null,
            showModal: false,
            id : '',
            userid: this.$store.state.userid,
            token: this.$store.state.refresh
        }
    },
    // components: {
  
    // },

    props: {
        visible: {
            default: false
        },
        title: {
            default: "🔥 Boo!"
        },
        closeIcon: {
            default: '<span>&#x274C;</span>'
        },
        content: {
            default: '<p> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet a tenetur delectus reprehenderit'},
        footer: {
        default: '<button>I do nothing!</button>'
        }
    },

    methods: {
        refreshData(){
            axios.get('http://localhost:8000/destinations/')
            .then(res=>{
                this.info=res.data
                this.id = res.data[0].destinationId
            });
        },
        
        
    },
  
      mounted() {

        this.refreshData();
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
.destination{
    padding-top: 75px;
}
.name{
    font:bolder;
    pointer-events: none;
}
</style>