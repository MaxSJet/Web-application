<template>
  <div>
    <div class="row">
      <div class="col-lg-12">
        <div class="ibox float-e-margins">
          <div class="ibox-title">
            <h5>Создание блюда</h5>
          </div>
          <div class="ibox-content">
            <form method="get" class="form-horizontal">

                <div class="form-group">
                  <label class="col-sm-2 control-label">
                    Название
                  </label>
                  <div class="col-sm-10">
                      <input v-model="name" type="text" class="form-control">
                      <small v-if="errors['name']" style="color:red">
                        {{errors['name']}}
                      </small>
                  </div>
                </div>
                <div class="hr-line-dashed"></div>
                <div class="form-group">
                  <label class="col-sm-2 control-label">
                    Состав
                  </label>
                  <div class="col-sm-10">
                      <input v-model="compound" type="text" class="form-control">
                    <small v-if="errors['compound']" style="color:red">
                      {{errors['compound']}}
                    </small>
                  </div>
                </div>
                <div class="hr-line-dashed"></div>
                <div class="form-group">
                  <label class="col-sm-2 control-label">
                    Вес ( В граммах )
                  </label>
                  <div class="col-sm-10">
                      <input v-model="weight" type="text" class="form-control">
                      <small v-if="errors['weight']" style="color:red">
                        {{errors['weight']}}
                      </small>
                  </div>
                </div>
                <div class="hr-line-dashed"></div>
                <div class="form-group">
                  <label class="col-sm-2 control-label">
                    Цена
                  </label>
                  <div class="col-sm-10">
                      <input v-model="cost" type="text" class="form-control">
                      <small v-if="errors['cost']" style="color:red">
                        {{errors['cost']}}
                      </small>
                  </div>
                </div>
                <div class="hr-line-dashed"></div>
                <div class="form-group">
                  <label class="col-sm-2 control-label">
                    Изображение
                  </label>
                  <div class="col-sm-10">
                    <input type="file" ref="file" @change="selectFile">
                    <small v-if="errors['photo']" style="color:red">
                      {{errors['photo']}}
                    </small>
                  </div>
                </div>
                <div class="hr-line-dashed"></div>

              <div class="form-group">
                <div class="col-sm-4 col-sm-offset-2">
                  <router-link :to="{name:'Orders'}" class="btn btn-white" type="submit">Отмена</router-link>
                  <div class="btn btn-primary" @click="create">Создать</div>
                </div>
              </div>
            </form>
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
  name: "CreateDish",
  data() {
    return {
      fields: dish,
      cost: null,
      name: null,
      weight: null,
      compound: null,
      image_url: null,
      photo: null,
      errors: []
    }
  },
  methods: {
    create() {
      let self = this
      this.errors = []
      if(this.checkInputs() === 'ok') {

        let data = new FormData()
        console.log( this.photo)
        data.append('cost', this.cost)
        data.append('name', this.name)
        data.append('weight', this.weight)
        data.append('compound', this.compound)
        data.append('image_url', this.photo)

        axios.post('http://178.21.8.23:5000/dishes/', data, {
          headers: {
            "Content-Type": 'multipart/form-data',
          },
        }).then(({data}) => {
          console.log(data)
          self.$router.push('/dishes')
        })
      }
    },
    selectFile(event) {
      this.photo = event.target.files[0];
    },
    checkInputs() {
      if(this.cost === null) {
        this.errors['cost'] = "Введите корректное значение поля"
      } else {
        let costCheck = this.cost.match(/^[0-9]+$/) != null
        if(costCheck === false) {
          this.errors['cost'] = "Введите корректное значение цены (только цифры)"
        }
      }

      if(this.weight === null) {
        this.errors['weight'] = "Введите корректное значение поля"
      } else {
        let weightCheck = this.weight.match(/^[0-9]+$/) != null
        if(weightCheck === false) {
          this.errors['weight'] = "Введите корректное значение веса (только цифры)"
        }
      }

      if(this.name === null) {
        this.errors['name'] = "Введите корректное значение поля"
      }

      if(this.photo === null) {
        this.errors['photo'] = "Выберите файл"
      }

      if(this.compound === null) {
        this.errors['compound'] = "Введите корректное значение поля"
      }

      if(Object.keys(this.errors).length === 0) {
        return 'ok'
      }
      return 'no'

    }
  }
}
</script>

<style scoped>

</style>