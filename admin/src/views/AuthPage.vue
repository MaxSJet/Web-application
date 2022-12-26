<template>
  <div class="middle-box text-center loginscreen animated fadeInDown">
    <div>
      <div>
        <h1 class="logo-name">IN+</h1>
      </div>
      <h3>Админ панель</h3>
      <p>Войдите используя данные для входа, чтобы получить доступ к панели администратора</p>
      <form class="m-t" role="form" action="index.html">
        <div class="form-group">
          <input v-model="login" type="email" class="form-control" placeholder="Username" required="">
        </div>
        <div class="form-group">
          <input v-model="pass" type="password" class="form-control" placeholder="Password" required="">
        </div>
        <div type="submit" class="btn btn-primary block full-width m-b" @click="auth">Войти</div>
      </form>
    </div>
  </div>
</template>

<script>
import { useToast } from "vue-toastification";
import axios from 'axios';

export default {
  name: "AuthPage",
  data() {
    return {
      login: '',
      pass: ''
    }
  },    
  setup() {
    localStorage.setItem('roling', '0')
    localStorage.setItem('auth', 'false')
    localStorage.setItem('userId', '0')
    const toast = useToast();
    return { toast }
  },

  methods: {
    auth() {
      axios.get('http://127.0.0.1:5000/times/current_user')
    .then(({data}) => {
        data.forEach(user => { // Поместить в функцию, для того, чтобы можно было использовать else
          if (user.login == this.login && user.password == this.pass) {
            
            localStorage.setItem('auth', 'true')
            window.location.href='/'
            localStorage.setItem('userId', user.id)
            localStorage.setItem('roling',user.role)
          }
          })
        })
        }
      }
}
</script>

<style scoped>

</style>