<div id="app">
<runoob></runoob>
</div>

<script>
var Child = {
  template: '<h1>自定义组件!</h1>'
}

// 创建根实例
new Vue({
  el: '#app',
  components: {
    // <runoob> 将只在父模板可用
    'runoob': Child
  }
})
</script>