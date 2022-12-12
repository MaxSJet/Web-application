<template>
    <div class="row">
      <div class="col-12">
        <div class="ibox float-e-margins">
          <div class="ibox-title">
            <h5>Меню</h5>
          </div>
          <div class="ibox-content" style="padding: 10px;max-width: 100%;overflow-x: auto;">
            <table class="table">
              <thead>
              <tr>
                <th>#</th>
                <th>Название</th>
                <th>Изображение</th>
                <th>Состав</th>
                <th>Цена</th>
                <th>Вес</th>
                <th>Количество</th>
              </tr>
              </thead>
              <tbody>
                <tr v-for="(item, index) in dishes" :key="item.id">
                  <td>{{item.id}}</td>
                  <td>{{item.name}}</td>
                  <td><img style="width:100px" :src="item.image_url" alt="..."></td>
                  <td>{{item.compound}}</td>
                  <td>{{item.cost}}</td>
                  <td>{{item.weight}}</td>
                  <td>
                    <input v-model="item.number" type="number"  class="form-control pull-left" style="width:35%" placeholder="0" min="0">
                  </td>
                  <td v-if="(item.number > 0 && this.dishes[index].clicked)">
                    <button 
                    class='btn btn-danger btn-sm'
                    @click="this.dishes[index].clicked = false; remove(dishes[index])">
                      Удалить
                    </button>
                  </td>
                  <td v-if="item.number > 0">
                    <button 
                    :class="this.dishes[index].clicked ? 'btn btn-success btn-sm' : 'btn btn-primary btn-sm'"
                    @click="(select(item.id, item.number), buttonClick(index))"
                    :disabled="this.dishes[index].clicked">
                    {{ this.dishes[index].clicked ? 'Добавлено' : 'Добавить' }}
                    </button>
                  </td>
                </tr> 
              </tbody>
            </table>
          </div>
          <a t=10 @click="save" type="button" class="btn btn-primary btn-sm add">Собрать</a>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  
  //import { computed } from "@vue/reactivity";
  import axios from "axios";
  import {useRoute} from "vue-router";
  
  export default {
    name: "UserMenu",
    data() {
      return {
        dishes: [],
        selectedDishes:[],
        router: useRoute(),
        userId : 0,
        number: 0,
        orderdishes:[],
      }
    },
    mounted() {
      this.getData()
    },
    methods: {
      select (id, number) {
        if (this.selectedDishes.indexOf(id) >= 0) {
          this.selectedDishes.splice(this.selectedDishes.indexOf(id), 1);
        } else {
          this.selectedDishes.push(id)
        }
      this.number = number
      this.orderdishes.push({
        "dish_id": id,
        "amount": this.number
        })  
      },
      remove(dish) {
        this.selectedDishes.pop(dish.id);
        const objWithIdIndex = this.orderdishes.findIndex((obj) => obj.dish_id === dish.id);
        this.orderdishes.splice(objWithIdIndex, 1)
      },
      save() {
        let self = this
        self.userId = localStorage.getItem('userId')
        let data = {
          dishes: this.orderdishes,
          userId: self.userId
        }
        axios.post('http://127.0.0.1:5000/orders/', data).then(({data}) => {
          console.log(data)
          self.$router.push('/orders')
        })
      },
      getData() {
        let self = this
        axios.get('http://127.0.0.1:5000/dishes').then(({data}) => {
          this.dishes = data
        })
        axios.get('http://127.0.0.1:5000/menus/'+this.router.params.id).then(({data}) => {
          data.dishes.forEach(function(item) {
            self.selectedDishes.push(item.id)
          })
        })
      },
      checkDish(id) {
        if (this.selectedDishes.indexOf(id) >= 0) {
          return true
        }
        return false
      },
  
      buttonClick(index) {
        this.dishes[index].clicked = !this.dishes[index].clicked
      } 
    }
  }
  </script>
  
  <style scoped>
  .add {
    margin-top: 10px; 
  }
  
  </style>