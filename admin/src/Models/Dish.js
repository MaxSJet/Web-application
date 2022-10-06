const dish = [
  {
    name: 'id',
    title: "#",
    fillable:false,
    type: 'int'
  },
  {
    name: 'name',
    title: "Название",
    fillable:true,
    type: 'string'
  },
  {
    name: 'image_url',
    fillable:true,
    title: "Изображение",
    type: 'image'
  },
  {
    name: 'compound',
    fillable:true,
    title: "Состав",
    type: 'string'
  },
  {
    name: 'cost',
    title: "Цена",
    fillable:true,
    type: 'int'
  },
  {
    name: 'weight',
    title: "Вес",
    fillable:true,
    type: 'int'
  },
  {
    name: 'actions',
    title: "Действия",
    fillable:true,
    type: 'int'
  },
]

export default dish;