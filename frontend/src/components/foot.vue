<template>
  <div class="">
      <div class="footer">
        
          <contact/>
        <hr>
      copyyright @ sav4ner 2022
        <br>
        <br>
      </div>
    </div>
</template>

<script>
import contact from '../components/contact.vue'
export default {
    name: 'Footer',
    components : {
        contact
    }
}
</script>

<style>
.footer{
  width: 100%;
  height: auto;
  bottom: 0;
  position: relative;
  padding-bottom: 0;
  background: #16161d;
  color:orange;
  font:bolder;
  font-size: 20px;
  text-align: center;
  margin-top: 0;
  
  
}
</style>