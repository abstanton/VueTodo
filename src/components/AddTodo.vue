<template>
    <div class="add-todo">
        <b-card class="col">
        
        <b-form @submit="addTodo">
            <div class="container">
            <div class="row">
                <div class="col">
                    <b-form-group
                        id="input-group-1"         
                        label-for="input-1"
                    >
                        <b-form-input
                        id="input-1"
                        type="text"
                        v-model="title"
                        required
                        placeholder="Todo Title"
                        ></b-form-input>
                    </b-form-group>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <b-form-textarea
                        id="textarea"
                        v-model="details"
                        placeholder="Todo Description"
                        rows="3"
                        max-rows="6"
                    ></b-form-textarea>
                </div>
            </div>
            
            <div class="row align-items-center mt-1">
             
                <div class="col">
                    <b-input-group>
                        <b-input-group-prepend is-text>
                            <b-form-checkbox
                            id="checkbox-1"
                            name="checkbox-1"
                            v-model="hasDue"
                            value="yes"
                            unchecked-value="no"
                            class="mr-n2"
                            ></b-form-checkbox>
                        </b-input-group-prepend>
                        <b-form-datepicker v-bind:disabled="isDisabled()" v-model="dueDate" placeholder="Due Date"></b-form-datepicker>
                    </b-input-group>
                </div>
            </div>
            <div class="row mt-2">
                <b-button class="btn btn-outline-primary" type="submit" variant="outline">Create Todo</b-button>            
            </div>
            </div>
        </b-form>
        
        </b-card>

        
        
    </div>
</template>

<script>


export default {
    name: "AddTodo",
    data(){
        return{
            title: '',
            hasDue: "yes",
            dueDate: '',
            details: ''
        }
    },
    methods:{
        addTodo(e){
            e.preventDefault();
            const newTodo = {
                title: this.title,
                completed: 0,
                description: this.details,
                hasDue: (this.hasDue=="yes") ? 1 : 0, 
                dueDate: this.dueDate
            }

            this.$emit('add-todo', newTodo);
            this.title = ''
            this.hasDue = "no"
            this.dueDate = ''
            this.details = ''
        },
        isDisabled(){
            if(this.hasDue == "yes"){
                return false;
            }
            else{
                return true;
            }
        }
    }
}
</script>

<style scoped>
    .add-todo{
        padding-top:0px;
        transition: padding-top 0.8s ease-out;
        
        margin: 0 auto;
        border-radius: 15px 15px;
    }
    form{
        display: flex;
    }
    input[type="text"] {
        flex: 10;
        padding: 5px;
    }

    input[type="submit"] {
        flex: 2;
    }
</style>