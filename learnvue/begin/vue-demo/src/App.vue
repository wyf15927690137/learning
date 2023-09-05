<!-- 展示模板 -->
<template>
  <div >
    <img decoding="async" src="./assets/logo.png">
    <p> {{message}}</p>
    <MyComponent @OnEvent="getDataHandle" :title="title" :age="age" :person="person"></MyComponent>
  </div>
</template>

<script>
// 导入组件
import MyComponent from "@/components/MyComponent.vue"

export default {
  name: 'app',
  data(){
    return{
      title: "The first title",
      age: 20,
      person: ['A','B','C'],
      message: ""
    }
  },
  components: {
    MyComponent
  },
  methods:{
    getDataHandle(data){
      this.message= data;
    }
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