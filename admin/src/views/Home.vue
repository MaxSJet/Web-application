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
      this.userId = localStorage.getItem('userId')
      this.role = localStorage.getItem('roling')
      axios.get('http://127.0.0.1:5000/orders').then(({data}) => {
        if (this.role == 1 || this.role == 2) {
          this.dishes = data
          this.all = data
        }
        else {
          this.dishes = data.filter((obj) => obj.userId == this.userId)
          this.all = data.filter((obj) => obj.userId == this.userId)
        }
      })
    }
  }
}
</script>

<style scoped>

</style>