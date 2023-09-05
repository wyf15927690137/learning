<!-- 展示模板 -->
<template>
  <div >
    <img decoding="async" src="./assets/logo.png">
    <MyComponent></MyComponent>
  </div>
</template>

<script>
// 导入组件
import MyComponent from "@/components/MyComponent.vue";
export default {
  name: 'app',
  components: {
    MyComponent
  }
}
</script>
<!-- 样式代码 -->
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>