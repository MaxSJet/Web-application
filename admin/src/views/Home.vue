<template>
  <div class="row">
    <div class="col-lg-4">
      <div class="ibox float-e-margins">
        <div class="ibox-title">
          <h5>Всего заказов</h5>
        </div>
        <div class="ibox-content">
          <h1 class="no-margins">{{Object.keys(orders).length}}</h1>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Home",
  data() {
    return {
      orders: []
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    getData() {
      axios.get('http://178.21.8.23:5000/orders').then(({data}) => {
        this.orders = data
        console.log(data)
        console.log(Object.keys(data).length)
      })
    },
  }
}
</script>

<style scoped>

</style>