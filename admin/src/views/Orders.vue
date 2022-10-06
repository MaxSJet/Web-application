<template>
  <div class="row">
    <div class="col-12">
      <div class="ibox float-e-margins">
        <div class="ibox-title">
          <h5>Список заказов</h5>
        </div>
        <div class="ibox-title d-flex flex-row" style="display: flex; align-items: center;">
          <span class="badge" @click="sort('all')">Все</span>
          <span class="badge" @click="sort(0)">Новые</span>
          <span class="badge" @click="sort(1)">В процессе</span>
          <span class="badge" @click="sort(2)">Завершенные</span>
        </div>


        <div class="ibox-content" style="padding: 10px;max-width: 100%;overflow-x: auto;">
          <table class="table">
            <thead>
            <tr>
              <th v-for="field in fields" :key="field.name">{{field.title}}</th>
              <th>Действие</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="item in dishes" :key="item">
              <td v-for="param in fields" :key="param">
                  <span v-if="param.type === 'object'">
                    <div v-for="bill in item[param.name]" :key="bill">
                        {{bill.name}}
                    </div>
                  </span>
                  <span v-else-if="param.type === 'status'">
                    <span v-if="item[param.name] === 0">
                      <span class="badge badge-primary">Новый</span>
                    </span>
                    <span v-if="item[param.name] === 1">
                      <span class="badge badge-primary">В процессе </span>
                    </span>
                    <span v-if="item[param.name] === 2">
                      <span class="badge badge-primary">Завершен </span>
                    </span>
                  </span>
                  <span v-else>
                     {{item[param.name]}}
                  </span>
              </td>
              <td>
                <button v-if="item.status === 0" type="button" @click="setStatus(item.id, '1')" class="btn btn-primary btn-sm">Начать выполнение</button>
                <button v-if="item.status === 1" type="button" @click="setStatus(item.id, '2')" class="btn btn-primary btn-sm">Завершить</button>
              </td>
            </tr>
            </tbody>
          </table>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Order from "@/Models/Order";
import axios from "axios";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Orders",
  data() {
    return {
      fields: Order,
      dishes: [],
      all: []
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    sort(type) {
      if(type === 'all') {
        this.dishes = this.all
      } else {
        this.dishes = this.all.filter(dish => {
          return dish.status === type
        })
      }
    },
    getData() {
      axios.get('http://178.21.8.23:5000/orders').then(({data}) => {
        this.dishes = data
        this.all = data
      })
    },
    setStatus(id, status) {
      axios.patch('http://178.21.8.23:5000/orders/status/'+id, {
        "status": status
      }).then(({data}) => {
        console.log(data)
        this.getData()
      })
    }
  }
}
</script>

<style scoped>
  .badge {
    margin-right:15px;
  }
  .badge:hover {
    cursor: pointer;
  }
</style>