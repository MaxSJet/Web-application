<template>
  <div v-if="role == 1">
    <div class="row">
      <div class="col-12">
        <div class="ibox float-e-margins">
          <div class="ibox-title d-flex flex-row" style="display: flex; align-items: center;">
            <div style="display: flex; align-items: center;">
              <h5 style="margin-right: 15px">Список блюд</h5>
              <router-link :to="{name: 'CreateDish'}" type="button" class="btn btn-primary btn-sm">Добавить блюдо</router-link>
            </div>
          </div>
          <div class="ibox-title">
            <div class="d-flex flex-row" style="display: flex; align-items: center; width: 100%;">
              <input style="height: 30px;width: 130px;border: 1px solid #1ab394;outline:none;border-radius: 3px 0 0 3px;" type="text" placeholder="Поиск" v-model="search">
              <a style="margin: 0;height:30px; width: 55px;border: 0;outline:none;border-radius: 0 3px 3px 0;" type="button" class="btn btn-primary btn-sm" @click="searching">Поиск</a>
            </div>
          </div>
          <div class="ibox-content" style="padding: 10px;max-width: 100%;overflow-x: auto;">
            <table class="table">
              <thead>
                <tr>
                  <th v-bind:key="item.name" v-for="item in fields">{{ item.title }}</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in dishes" :key="item">
                  <td>{{item.id}}</td>
                  <td>{{item.name}}</td>
                  <td><img style="width:100px" :src="item.image_url" alt="..."></td>
                  <td>{{item.compound}}</td>
                  <td>{{item.cost}}</td>
                  <td>{{item.weight}}</td>
                  <td><a @click="deleteDish(item.id)" class="btn btn-danger btn-sm">Удалить</a></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>  
</template>

<script>
import dish from "@/Models/Dish";
import axios from 'axios'

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Dishes",
  data() {
    return {
      fields: dish,
      dishes: [],
      dishesAll:[],
      search:'',
      isBusy: true,
      role: null
    }
  },
  mounted() {
    this.role = localStorage.getItem('roling')
    this.getData()
  },
  methods: {
    searching() {
      if(this.search !== '') {
        this.dishes = this.dishesAll.filter(dish => {
          return dish.name.toLowerCase().includes(this.search.toLowerCase())
        })
      } else {
        this.dishes = this.dishesAll
      }

    },
    deleteDish(id) {
      let self = this
      axios.delete('http://178.21.8.23:5000/dishes/'+id).then(({data}) => {
        console.log(data)
        self.getData()
      })
    },
    async getData() {
      await axios.get('http://178.21.8.23:5000/dishes').then(({data}) => {
        this.dishes = data
        this.dishesAll = data
      })

      this.isBusy = false
    }
  }
}
</script>

<style scoped>
  .btn-default {
    margin-right: 15px;
  }

</style>
