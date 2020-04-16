<template>
    
<b-card v-bind:class="{'is-complete': todo.completed}">  
        <div class="row">
            <div class="d-flex justify-content-between align-items-stretch col">
                <div>
                    <!-- <input class="" type="checkbox" v-on:change="markComplete()" ref="check"> -->
                    <h4 class="todo-title">{{todo.title}}</h4>
                </div>
                <div class="d-flex align-items-start">
                    <button type="button" class = "d-inline expand rounded-circle btn btn-outline-primary ml-1" @click.prevent="expand()" ref="expandButton">^</button>
                    <button type="button" class = "d-inline del btn btn-outline-danger ml-1" @click="$emit('del-todo', todo.id)">x</button>
                       
                </div>
            </div>
        </div>
        <div class="more-content mt-3" ref="collapsible" >
            <div class="row">
                <div class="d-flex justify-content-between align-items-stretch " style="width: 100%">
                
                    <b-card class="flex-fill">
                        <p>{{todo.description}}
                        </p>
                    </b-card>
                    
                    <div class="ml-1">
                        <b-card class="">
                             <p>Due</p>
                            <p v-if="todo.hasDue == 1">{{todo.dueDate}}</p>
                            <p v-else>No Due Date</p>
                        </b-card>
                        <button type="button" class = "del btn btn-outline-secondary" @click="markComplete">COMPLETE</button>

                    </div>       
                </div>  
            </div>
        </div>
    
</b-card>
    
</template>

<script>
export default {
    name: "TodoItem",
    props: ["todo"],

    methods: {
        markComplete(){
            console.log(this.todo.completed)
            this.todo.completed = !this.todo.completed;
        },
        expand(){
            let content = this.$refs.collapsible;
            let button = this.$refs.expandButton;
            if(content.style.maxHeight){
                button.style.transform = "rotate(0deg)"
                content.style.maxHeight = null;
                content.style.overflow = "hidden";
            }else{
                content.style.overflow = "visible";
                button.style.transform = "rotate(180deg)"
                content.style.maxHeight = content.scrollHeight + "px";
            }
        }
    },
    mounted(){
        if(this.todo.completed){
            console.log("hello")
            let checkBox = this.$refs.check;
            
            checkBox.checked = true;
        }
    }
}
</script>

<style scoped>
    /* 
    .todo-item{
        background: #f4f4f4;
        padding: 10px;
        border-radius: 15px 15px;
        border-bottom: 1px #ccc dotted;
    }
    */
    div.is-complete {
        background: lightgrey;
    } 
    .more-content{
        
        max-height: 0;
        transition: max-height 0.2s ease-out;
        overflow: hidden;
        
        background-color: none;
    }
    .todo-title{
        /* max-width: 70%; */
        /* display: inline-block; */
        /* margin-left: 6px; */
    }
    .del{
        /* background: white;
        color: grey;
        border: none;
        height: 35px;
        width: 35px;
        margin-left: 5px;
        border-radius: 50%;
        display: inline-block;
        cursor: pointer;
        float: right; */
    }
    .expand{
        /* background: darkgrey;
        color: white;
        
        border: none;
        
        height: 10px;
        width: 10px;
        
        border-radius: 50%;
        cursor: pointer;
        */
        transition: all 0.3s ease-in-out 0s;
    }
</style>