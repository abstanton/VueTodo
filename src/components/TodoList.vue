<template>
    <div class="row justify-content-center">
      <div class = "TodoList col-10 ">   
         
          <!-- <transition-group name="list" tag="p">   
              <div v-bind:key="todo.id" v-for="(todo, index) in todoList">
                  <AddTodo v-if="index == (todoList.length-1)" v-on:add-todo="$emit('add-todo', $event)" class="mt-2"/>
                  <TodoItem v-else v-bind:todo="todo" v-on:del-todo="$emit('del-todo', todo.id)"/>
                  
              </div>
                    
          </transition-group>   -->
          
          <transition-group name="list" tag="p">   
              <div v-bind:key="(n==todoList.length+1) ? '1000' : todoList[n-1].id" v-for="n in (todoList.length+1)">
                  <AddTodo v-if="n== (todoList.length+1)" v-on:add-todo="$emit('add-todo', $event)" class="mt-2"/>
                  <TodoItem v-else v-bind:todo="todoList[n-1]" v-on:del-todo="$emit('del-todo', todoList[n-1].id)"/>
              </div>
                    
          </transition-group>     
          
             
          

      </div>
    </div>
    
</template>

<script>

import TodoItem from './TodoItem.vue';
import AddTodo from './AddTodo.vue';


export default {
    name: "TodoList",
    components: {
        TodoItem,
        AddTodo
    },
    props: ["todoList"] 
    
}
</script>


<style scoped>
/* .TodoList{
    width: 70%;
    margin: 0 auto;
} */
.list-item {
  display: inline-block;
  margin-right: 10px;
}
.list-enter-active{
  transition: all 0.5s;
  
}
.list-leave-active{
    transition: all 1s;
    position: fixed;
    width: 83%;
} 
.list-enter, .list-leave-to /* .list-leave-active below version 2.1.8 */ {
  opacity: 0;
  transform: translateX(60px);
}
.list-move {
  transition: transform 0.9s;
}
</style>