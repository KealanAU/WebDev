<template>
    <div>
        <table id="tier-table">
            <tbody>
                <tr v-for="tier in tierListData" v-bind:key="tier[0]" >
                    <td class="labelHolder"  v-bind:style=tier[1]>
                        <span class="label">{{tier[0]}}</span>
                    </td>
                    <td>
                        <div class="tier sort"   @drop="dropHandler" @dragover.prevent @dragend="dragendHandler" ></div>
                    </td>
                </tr>    
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
  name: 'TierList',
  data() {
      return {
        tierListData :[
            ["S","background: rgb(255, 127, 127);"],
            ["A","background: rgb(255, 191, 127);"],
            ["B","background: rgb(255, 223, 127);"],
            ["C","background: rgb(191, 255, 127);"],
            ["D","background: rgb(127, 255, 127);"],
            ["F","background: rgb(127, 255, 255);"]
        ]
      }
    },
    methods: {
        dropHandler(ev){
            // works by grabbing image source 

            var node = document.createElement("div");

            node.addEventListener("dragstart", function(ev){

                ev.dataTransfer.setData("text/plain", ev.target.outerHTML);
                window.getSelection().removeAllRanges();

            });

            node.innerHTML = ev.dataTransfer.getData("text/plain");

            
            if(ev.toElement.tagName === "IMG"){
                    console.log(ev);
                    ev.target.parentElement.parentElement.appendChild(node);
                    ev.target.parentElement.parentElement.addEventListener("drop", function(ev){
                        ev.preventDefault();
                        ev.stopPropagation();
                    }
                );
            }
            else{
                ev.target.appendChild(node);
                ev.target.addEventListener("drop", function(ev){
                    ev.preventDefault();
                    ev.stopPropagation();
                });
            }
            // Clear the drag data cache (for all formats/types)

            ev.dataTransfer.clearData();
        },
        dragendHandler(ev){
            if(ev.dataTransfer.dropEffect == "move"){
                ev.target.remove()
            }
        }
    }
}

</script>

<style scoped> 
div{
    display: flex;
    justify-content: space-around;
    user-select: none;
}
td {
    height:80px;
    border: solid 1px #1A1A1A;
    display: table-cell;
    vertical-align: inherit;
}
table {
    border: solid 1px #1A1A1A;
}
.tier{
    background: white;
    min-width: 800px;
    min-height: 80px;
    text-align: left;
    justify-content: left;
}
.label{
    padding: 4px;
}

</style> 