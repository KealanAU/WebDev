<template>
  <div id="unsorted" @dragend="dragendHandler"> 
    <div class="imgSize" v-for="icecreams in iceCreamData" v-bind:key="icecreams[0]" @dragstart="dragstart_handler">
      <img class="imgSize" :src=getAsset(icecreams[1])>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ItemsSortComp',
  data() {
    return {
      iceCreamData: [
        ["Billabong","Billabong.jpg"],
        ["Bubble-o-bill","Bubble-o-bill.jpg"],
        ["Calippo","Calippo.jpg"],
        ["Cornetto","Cornetto.jpg"],
        ["Cyclone","Cyclone.jpg"],
        ["Dixie-Cup","Dixie-Cup.jpg"],
        ["Drumstick","Drumstick.jpg"],
        ["Frosty-Fruits","Frosty-Fruits.jpg"],
        ["Golden-Gaytime","Golden-Gaytime.jpg"],
        ["Hava-Heart","Hava-Heart.jpg"],
        ["Icy-Pole-2","Icy-Pole-2.jpg"],
        ["Lifesavers","Lifesavers.jpg"],
        ["Magnum","Magnum.jpg"],
        ["Maxibon","Maxibon.jpg"],
        ["Milo-Scoop-Shake","Milo-Scoop-Shake.jpg"],
        ["Rainbow-PaddlePop","Rainbow-PaddlePop.jpg"],
        ["Splice","Splice.jpg"],
        ["Sunny-Boy","Sunny-Boy.jpg"],
        ["Weis-Mango","Weis-Mango.jpg"],
        ["Zooper-Dooper","Zooper-Dooper.jpg"]
      ]
    }
  },
  methods:{

    getAsset(img){

      return require("./../assets/img/" + img);
    },

    dragstart_handler(ev)
    {
      ev.dataTransfer.setData("text/plain", ev.target.outerHTML);
      window.getSelection().removeAllRanges();
    },

    dragendHandler(ev)
    {
      if(ev.dataTransfer.dropEffect == "move"){
          ev.target.remove()
          this.submitData();
      }
    },

    submitData()
    { 
      for(let i=0; i < 6; i++){
      console.log(document.getElementById("tier-table").rows[i].cells[1]);
      }
    }

  }
}



</script>

<style scoped>
.imgSize{
  height: 80px;
  width: 80px;
  display: inline-block;
  justify-content: left;
}
#unsorted{
  max-width: 800px;
  min-height: 80px;
  display: inline-table;
}
img::selection{
  background: transparent;
}
</style>
