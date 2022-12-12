<template>
  <div v-if="role == 1">
    <div class="row">
      <div class="col-12">
        <div class="ibox float-e-margins">
          <div class="ibox-title">
            <h5>Меню на день</h5>
          </div>
          <div class="ibox-content" style="padding: 10px;max-width: 100%;overflow-x: auto;">
            <table class="table">
              <thead>
              <tr>
                <th>Блюдо</th>
                <th>Выбрать</th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="item in dishes" :key="item">
                <td>{{item.name}}</td>
                <td>
                  <input :checked="checkDish(item.id)" @change="select(item.id)" type="checkbox">
                </td>
              </tr>
              </tbody>
            </table>
          </div>
          <a @click="save" type="button" class="btn btn-primary btn-sm">Сохранить</a>
        </div>
      </div>
    </div>
  </div>  
</template>

<script>
import axios from "axios";
import {useRoute} from "vue-router";

export default {
  name: "EditDay",
  data() {
    return {
      dishes: [],
      selectedDishes:[],
      router: useRoute(),
      role: 0,
    }
  },
  mounted() {
    this.role = localStorage.getItem('roling')
    this.getData()
  },
  methods: {
    select(id) {
      if(this.selectedDishes.indexOf(id) >= 0) {
        this.selectedDishes.splice(this.selectedDishes.indexOf(id), 1);
      } else {
        this.selectedDishes.push(id)
      }
    },
    save() {
      let self = this
      let data = {
        dishes: this.selectedDishes
      }
      axios.patch('http://127.0.0.1:5000/menus/'+this.router.params.id, data).then(({data}) => {
        console.log(data)
        self.$router.push('/menu')
      })
    },
    getData() {
      let self = this
      axios.get('http://127.0.0.1:5000/dishes').then(({data}) => {
        this.dishes = data
      })
      axios.get('http://127.0.0.1:5000/menus/'+this.router.params.id).then(({data}) => {
        data.dishes.forEach(function(item) {
          console.log(item)
          self.selectedDishes.push(item.id)
        })
      })
    },
    checkDish(id) {
      if (this.selectedDishes.indexOf(id) >= 0) {
        return true
      }
      return false
    }
  }
}
</script>

<style scoped>

</style>