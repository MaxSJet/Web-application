<template>
  <div class="middle-box text-center loginscreen animated fadeInDown">
    <div>
      <div>
        <h1 class="logo-name">IN+</h1>
      </div>
      <h3>Админ панель</h3>
      <p>Войдите использую данные для входа чтобы получить доступ к панели администратора</p>
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

export default {
  name: "AuthPage",
  data() {
    return {
      login: '',
      pass: ''
    }
  },
  setup() {
    const toast = useToast();
    return { toast }
  },

  methods: {
    auth() {
      if(this.login === 'admin@admin.com' && this.pass === 'admin') {
        localStorage.setItem('auth', 'true')
        window.location.href='/'
      } else {
        this.toast.error("Вы ввели неверный логин или пароль!");
      }
    }
  }
}
</script>

<style scoped>

</style>