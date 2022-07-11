<template>
<div class="cart">
    <div class="row">
        <div class="col" v-if="items==''">
           


        <div class="empt" >
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

            
                <div class="nempty" v-for="data in info " :key="data.name">
                    <div class="card" style="padding-bottom:30px; margin-bottom:30px;">
                        <!-- <h5 class="card-header">Featured</h5> -->
                        <div class="card-body">
                            <!-- <br>
                            <img src="../components/assets/cart.668e6453.svg" alt="">
                            <br> -->
                            <br>
                            <h3 class="card-title">{{data.name}}</h3>

                            <p class="card-text">{{data.description}}</p>
                            <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
                            <br>
                            <button class="about-view packages-btn pull-right" id="show-modal" style="position:relative; vertical-align: bottom;width: 130px; background-color:#16161d ; border: none;" @click="checkOut(data);showModal = true;">
                                                <small><b>checkout</b> (KSH {{data.price}})</small>
                                            </button>
                        </div>
  
                    </div>
                </div>

        <!-- <div class="col-md-3 col-lg-3">
            <button type="button" class="btn btn-primary btn-lg">CHECKOUT({{bill}})</button>
        </div> -->
        <!-- <button id="show-modal" @click="showModal = true">Show Modal</button> -->
        {{tel}},{{email}}
        <Teleport to="body">
            <!-- use the modal component, pass in the prop -->
            <modal :show="showModal" @close="showModal = false">
            <template #header>
                <h3>Book With Us</h3>
            </template>

            <template #body>
                
                    <div class="input-group">
                    <span class="input-group-text">Email and Phonenumber</span>
                    <input type="email" aria-label="Email" class="form-control" placeholder="email@gmail.com" required v-model="email">
                    <input type="tel" aria-label="Phone number" class="form-control" placeholder="phone number" required v-model="tel">
                </div>
                <!-- <div class="input-group mb-5" style="margin-top: 20px;">
                    <select class="form-select" id="inputGroupSelect02" required>
                        <option selected>Choose...</option>
                        <option value="1">One</option>
                        <option value="2">Two</option>
                        <option value="3">Three</option>
                    </select>
                    <label class="input-group-text" for="inputGroupSelect02">Tourguide</label>
                </div> -->
                <!-- </form> -->
            </template>
            <template #btn-name @click="alert('levin')">
                Book
            </template>

            </modal>
        </Teleport>
    </div>
</div>
  
</template>

<script>
import Modal from './Modal.vue'
import { BModal, VBModal } from 'bootstrap-vue'
import axios from 'axios'
import Swal from 'sweetalert2'
export default {
    name: 'cart',

    data(){
        return{
            items : '',
            info: [],
            userid: '',
            destinationId : '',
            bill: '',
            showModal: false,
            tel : '',
            email: ''

        }
    },
    components:{
        VBModal,
        Modal
    },
    methods:{
        fetchall(){
            let userid = this.$store.state.user
            axios.get('user/cart/'+userid+'/').then(res=>{
                this.items = res.data
                this.check(this.items)
            })
        },
         getData(id){
            let url = 'hotels/'
            axios.get(url+id+'/').then(res=>{
                    
                    let a =  res.data
                    this.info.append(res.data[0])
            }).catch(err=>{

            }
                
            )
        },
        getPark(id){
            let url = 'destinations/'
            axios.get(url+id+'/').then(res=>{
                    
                    let a =  res.data
                    this.info.push(a[0])
            }).catch(err=>{

            }
                
            )
        },
        check(items){
            items.forEach(element => {
                console.log(element.park)
                let hotelid = element.hotel
                let parkid = element.park
                if(parkid){
                    this.getPark(parkid)
                }else{
                    this.getData(hotelid)
                }
            });
            console.log(this.info)
        },
        checkOut(data){

            setTimeout(() => {
                if (data.park == 1) {
                axios.post('user/park-bookings/',{
                    "email": "",
                    "contact": "0768850685",
                    "bill": data.price,
                    "userID": this.$store.state.user,
                    "tourguideId": null,
                    "destinationId": data.destinationId
            },
            console.log(this.bill,this.destinationId)
            ).then(res=>{
                Swal.fire({
                            title: "Booked",
                            // text: 'User Deleted',
                            icon: 'success',
                            confirmButtonText: 'OK'
                        })
            })
            } else {
                 axios.post('user/park-bookings/',{
                    "email": this.email,
                    "contact": this.tel,
                    "bill": data.price,
                    "userID": this.$store.state.user,
                    "destinationId": data.hotelId
            },
            console.log(this.bill,this.destinationId)
            ).then(res=>{
                Swal.fire({
                            title: "Booked",
                            // text: 'User Deleted',
                            icon: 'success',
                            confirmButtonText: 'OK'
                        })
            })
            }
            }, 10000);
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
/* #show-modal{
    width: 250px;
    height: 70px;
} */
.card{
    border: none;
    box-shadow: rgba(0, 0, 0, 0.15) 0px 5px 15px 0px;
}
.empt{
    padding-bottom: 90px ;
}
</style>