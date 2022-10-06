<template>
  <div class="row">
    <div class="col-12">
      <div class="ibox float-e-margins">
        <div class="ibox-title">
          <h5>Меню на неделю</h5>
        </div>
        <div class="ibox-title">
          <div class="input-daterange input-group" id="datepicker" style="width: 30%;">
            <input type="date" class="input-sm form-control" v-model="from" @change="getData">
            <span class="input-group-addon">to</span>
            <input type="date" class="input-sm form-control" v-model="to" @change="getData">
          </div>
        </div>
        <div class="ibox-content">
          <table class="table">
            <thead>
            <tr>
              <th>Дата</th>
              <th>Блюда</th>
              <th>Действия</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="item in days" :key="item">
              <td>{{item.date}}</td>
              <td>
                <template v-if="item.dishes">
                  <div v-for="dish in item.dishes" :key="dish">
                    {{dish.name}}
                  </div>
                </template>
                <template v-else>
                  <span>Нет блюд</span>
                </template>
              </td>
              <td>
                <router-link :to="{name: 'MenuEdit', params: {id:item.id}}" type="button" class="btn btn-primary btn-sm">Добавить блюдо</router-link>
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
import axios from "axios";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Menu",
  data() {
    return {
      days: [],
      date: new Date,
      from: this.formatDate(new Date()),
      to: this.formatDate(new Date(), 7)
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    formatDate(date, days=0) {
      return `${date.getFullYear()}-${('0' + (date.getMonth() + 1)).slice(-2)}-${('0' + (date.getDate() + days)).slice(-2)}`
    },
    getData() {
      let app = this;
      axios.get('http://178.21.8.23:5000/menus', {
        params: {
          from: app.from,
          to: app.to
        }
      }).then(({data}) => {
        this.days = data
      })
    }
  }
}
</script>

<style scoped>

</style>