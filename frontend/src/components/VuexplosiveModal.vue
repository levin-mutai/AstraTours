<template>
  <form action="" method="post">
    <div
    class="vuexplosive-modal"
    :class="{'vuexplosive-modal-hidden': !active, 'vuexplosive-modal-visible': active}"
    @keydown.esc=" active = false"
    :aria-hidden="modalToggle"
    tabindex="-1"
    role="dialog"
    style="backgroud: antiquewhite;"
  >
    <transition name="scale">
      <div class="vuexplosive-modal-container" v-if="active">
        <div class="vuexplosive-modal-inner">
          <div class="vuexplosive-modal-header">
            <div class="vuexplosive-modal-title pull-centre"><center><b>{{title}}</b></center></div>
            <button
              class="vuexplosive-modal-close"
              @click="modalToggle"
              v-html="closeIcon"
              arial-label="close"
            ></button>
          </div>
          <div class="tab-para">

											<div class="row">
												<div class="col-lg-4 col-md-4 col-sm-12">
													<div class="single-tab-select-box">

														<h2>destination</h2>

														<div class="travel-select-icon">
															<select class="form-control ">

															<option value="default">enter your destination</option><!-- /.option-->

															<option value="kenya">Kenya</option><!-- /.option-->

															<option value="uganda">Uganda</option><!-- /.option-->
															<option value="Tanzania">Tanzania</option><!-- /.option-->

															</select><!-- /.select-->
														</div><!-- /.travel-select-icon -->

														<div class="travel-select-icon">
															<select class="form-control ">

                                <option value="default">Choose your Tourguide: </option><!-- /.option-->

                                <option v-for="data in info" :key="data.photo" :value="data.name">{{data.name}}</option><!-- /.option-->

															</select><!-- /.select-->
														</div><!-- /.travel-select-icon -->

													</div><!--/.single-tab-select-box-->
												</div><!--/.col-->

												<div class="col-lg-2 col-md-3 col-sm-4">
													<div class="single-tab-select-box">
														<h2>check in</h2>
														<div class="travel-check-icon">
															<form action="#">
																<input type="text" name="check_in" class="form-control" data-toggle="datepicker" placeholder="12 -01 - 2017 ">
															</form>
														</div><!-- /.travel-check-icon -->
													</div><!--/.single-tab-select-box-->
												</div><!--/.col-->

											

												<div class="col-lg-2 col-md-1 col-sm-4">
													<div class="single-tab-select-box">
														<h2>duration</h2>
														<div class="travel-select-icon">
															<select class="form-control ">

                                <option value="default">5</option><!-- /.option-->

                                <option value="10">10</option><!-- /.option-->

                                <option value="15">15</option><!-- /.option-->
                                <option value="20">20</option><!-- /.option-->

															</select><!-- /.select-->
														</div><!-- /.travel-select-icon -->
													</div><!--/.single-tab-select-box-->
												</div><!--/.col-->

												<div class="col-lg-2 col-md-1 col-sm-4">
													<div class="single-tab-select-box">
														<h2>members</h2>
														<div class="travel-select-icon">
															<select class="form-control ">

                                <option value="default">1</option><!-- /.option-->

                                <option value="2">2</option><!-- /.option-->

                                <option value="4">4</option><!-- /.option-->
                                <option value="8">8</option><!-- /.option-->

															</select><!-- /.select-->
														</div><!-- /.travel-select-icon -->
													</div><!--/.single-tab-select-box-->
												</div><!--/.col-->

											</div><!--/.row-->

											<center>
                         <div class="about-btn travel-mrt-0 pull-centre" >
													<button class="about-view travel-btn">
														send to cart	
													</button><!--/.travel-btn-->
												</div><!--/.about-btn--></center>
										</div>
          
            
        </div>
      </div>
    </transition>

    <div class="vuexplosive-modal-bg" @click="modalToggle">
      <img class="vuexplosive-modal-explosion-gif" :src="active ? explosionGifUrlBlob : '' " />
    </div>
  </div>
  </form>
</template>


<script>
/* eslint-disable */
export default {
  name: "VuexplosiveModal",
  props: {
    visible: {
      default: false
    },
    title: {
      default: "Book"
    },
    closeIcon: {
      default: `<span>&#x274C;</span>`
    },
    content: {
      default: `<p> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet a tenetur delectus reprehenderit, omnis doloremque at earum officia unde sequi accusantium corporis praesentium deserunt laboriosam dignissimos voluptatum culpa molestiae ullam. 👻</p>`
    },
   
  },
  data: function() {
    return {
      active: false,
      info : null,

      //data to post
      firstname: null,
      lastname: null,
      email: null,
      contact: null,
      tourguide:null,
      date: null,
      Duration: null,
      destination: null,
      bill: null,
    };
  },
  created() {
    fetch(this.explosionGifUrl)
      .then(response => response.blob())
      .then(images => {
        this.explosionGifUrlBlob = URL.createObjectURL(images);
      });
  },

  methods: {
    modalToggle() {
      this.active = !this.active;
    },
    close() {
        this.$emit('close');
      },
      refreshData(){
            this.$axios.get('http://localhost:8000/Destinations')
            .then((response)=>{
                this.info=response.data
            });
        }
    
  },
  watch: {
    visible(oldVal, newVal) {
      this.active = !this.active;
    }
  }
};
</script>


<style scoped>
.vuexplosive-modal {
  font-family: -apple-system, BlinkMacSystemFont, "avenir next", avenir,
    "helvetica neue", helvetica, ubuntu, roboto, noto, "segoe ui", arial,
    sans-serif;
  line-height: 1.5;
  color: rgba(0, 0, 0, 0.8);
  text-align: left;
  background: aliceblue;
  margin-top: 74px;
}

.vuexplosive-modal-container {
  background: rgba(239, 242, 253, 0.664);
  max-width: 95%;
  width: 70%;
  height: auto;
  position: fixed;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  z-index: 9999999;
  padding: 15px;
  border-radius: 5px;
}

.vuexplosive-modal-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.vuexplosive-modal-title {
  font-size: 30px;
  font-weight: bolder;
}
.form-control{
  margin-bottom: 20px;
}

.vuexplosive-modal-close {
  align-self: flex-start;
  font-size: 18px;
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
}

.vuexplosive-modal-content {
  font-size: 18px;
  color: #333;
}

.vuexplosive-modal-bg {
  position: fixed;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  z-index: 999;
}

.vuexplosive-modal-explosion-gif {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: auto;
  min-width: 50%;
  min-height: 50%;
  opacity: 1;
  width: 100%;
  max-width: 100%;
  height: auto;
}

.vuexplosive-modal-footer {
  margin-top: 20px;
}

.vuexplosive-modal-hidden {
  display: none;
}
.vuexplosive-modal-visible {
  display: block;
}

.scale-enter-active {
  animation: bounce-in 0.3s;
}
.scale-leave-active {
  animation: bounce-in 0.3s reverse;
}
@keyframes bounce-in {
  0% {
    transform: translate(-50%, -50%) scale(0);
  }
  50% {
    transform: translate(-50%, -50%) scale(1.2);
  }
  100% {
    transform: translate(-50%, -50%) scale(1);
  }
}
</style>