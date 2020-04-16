

<template>
  <div id="app">
    <!-- Create a todo list which is the main component viewed -->
    <todo-list v-bind:todoList="todos" v-on:del-todo="deleteTodo" v-on:add-todo="addTodo" class="mt-3 main"/>  
  </div>
</template>

<script>

import TodoList from '../components/TodoList.vue'
import axios from 'axios';

export default {
  name: 'Home',
  components: {
    TodoList,
  },
  data(){
    return{
      //todos data for application only data needed, could add server ip here and endpoint informmation
      todos: []
    }
  },
  methods:{
    
    deleteTodo(id){
      axios.delete('http://127.0.0.1:5000/todos/'+id)
      .then(res => this.todos = this.todos.filter(todo => todo.id !== id,res.data))
      .catch(err => console.log(err));
    },

    addTodo(newTodo){
      const {title, completed, description, hasDue, dueDate} = newTodo;
      fetch('http://127.0.0.1:5000/todos', {
          method: 'POST',
          body: JSON.stringify({
            title: title,
            completed: completed,
            description: description,
            hasDue: hasDue,
            dueDate: dueDate
          }),
          headers: {
            "Content-type": "application/json; charset=UTF-8"
          }
        })
        .then(dataWrappedByPromise => dataWrappedByPromise.json())
        .then(data => this.todos.push(data))  
        .catch(err => console.log(err));         
    }
  },

  created(){
    fetch('http://127.0.0.1:5000/todos')
      .then(response => response.json())
      .then(json => this.todos = json)
      .catch(err => console.log(err));      
  }
}
</script>

<style>

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  .main{
    transition: all 1s;
  }
  body{
    font-family: Arial, Helvetica, sans-serif;
    line-height: 1.4;
    text-align: center;

  }
  .btn{
    display: inline-block;
    border: none;
    background: #555;
    color: #fff;
    padding: 7px 20px;
    cursor: pointer;
  }

  .btn:hover{
    background: #666;
  }
</style>
