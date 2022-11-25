<template>
  <div v-if="auth === true">
    <div id="wrapper">
      <nav class="navbar-default navbar-static-side" role="navigation">
        <div class="sidebar-collapse">
          <ul class="nav metismenu" id="side-menu">
            <li class="nav-header">
              <div class="dropdown profile-element">
                <a data-toggle="dropdown" class="dropdown-toggle" href="#">
                  <span class="clear">
                    <span class="block m-t-xs">
                      <strong class="font-bold">{{role}}</strong>
                   </span>
                  </span>
                </a>
              </div>
              <div class="logo-element">
                IN+
              </div>
            </li>
            <li>
              <router-link :to="{name:'Home'}">
                <i class="fa fa-pie-chart"></i>
                <span class="nav-label">Главная</span>
              </router-link>
            </li>
            <li>
              <router-link :to="{name:'Dishes'}">
                <i class="fa fa-flask"></i>
                <span class="nav-label">Блюда</span>
              </router-link>
            </li>
            <li>
              <router-link :to="{name:'Orders'}">
                <i class="fa fa-database"></i>
                <span class="nav-label">Заказы</span>
              </router-link>
            </li>
            <li>
              <router-link :to="{name:'Menu'}">
                <i class="fa fa-book"></i>
                <span class="nav-label">Меню на неделю</span>
              </router-link>
            </li>
          </ul>
        </div>
      </nav>

      <div id="page-wrapper" class="gray-bg">
        <div class="row border-bottom">
          <nav class="navbar navbar-static-top white-bg" role="navigation" style="margin-bottom: 0">
            <div class="navbar-header">
              <a class="navbar-minimalize minimalize-styl-2 btn btn-primary " href="#"><i class="fa fa-bars"></i> </a>
            </div>
            <ul class="nav navbar-top-links navbar-right">
              <li>
                <a href="login.html">
                  <i class="fa fa-sign-out"></i> {{name}}
                </a>
              </li>
            </ul>
          </nav>
        </div>

        <div class="wrapper wrapper-content">
          <router-view></router-view>
        </div>

      </div>
    </div>
  </div>
  <div v-else style="    background-color: white;">
    <router-view></router-view>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'App',
  data() {
    return {
      auth:false,
      role: 0,
      name: ''
    }
  },
  mounted() {
    //   this.auth = false
    axios.get('http://127.0.0.1:5000/times/current_user')
    .then(({data}) => {
      console.log(data)
      this.auth = true
      this.role = data.role>1?'Админ':''
      this.name = data.full_name
      // let a = localStorage.getItem('auth')
    })
    // if(a !== 'true') {
    //   if(window.location.pathname !== '/auth') {
    //     window.location.href="/auth"
    //   }
    // } else {
    // }
  }
}
</script>

<style>

</style>
