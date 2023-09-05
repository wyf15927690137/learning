<script>
export default {
  name: "MyComponent",
  // props pass data from father component to son component
  props:{
    title:{
      type:String,
      default: ""
    },
    age:{
      type:Number,
      default: 0
    },
    person:{
      type:Array,
      default:function (){
        return []
      }
    }
  },
  data() {
    return {
      message: "A message from son component"
    }
  },
  methods:{
    sendClickHandle(){
      this.$emit("OnEvent",this.message)
    }
  }
}

</script>

<template>
  <h3> prop pass data </h3>
  <p>{{ title }} {{age}}</p>
  <ul>
    <li v-for="(item,index) in person" :key="index" >{{item}}</li>
  </ul>
  <button @click="sendClickHandle"> click to pass data from son to father </button>
</template>

<style scoped>
h3{
    color: red;
}
</style>