const dish = [
  {
    name: 'id',
    title: "#",
    fillable:false,
    type: 'int'
  },
  {
    name: 'date',
    title: "Дата",
    fillable:true,
    type: 'string'
  },
  {
    name: 'dishes',
    fillable:true,
    title: "Заказ",
    type: 'object'
  },
  {
    name: 'status',
    fillable:true,
    title: "Статус заказа",
    type: 'status'
  },
  {
    name: 'total',
    title: "Общая стоимость",
    fillable:true,
    type: 'int'
  },
]

export default dish;