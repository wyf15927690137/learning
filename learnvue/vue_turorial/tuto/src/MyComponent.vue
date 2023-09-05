<template>
  <div>
    <h1 :class="{'red': isRed, 'underline': true, 'bold': isBold }">Hello, Vue 3!</h1>
    <p>{{counter.count}}</p>
    <p>{{message.split('')}}</p>
    <p>{{message.split('').reverse()}}</p>

    <p :class="classObject">{{message.split('').reverse().join('')}}</p>
    <button v-on:click="increase(counter)"> {{ counter.count }}</button>
    <br>
    <button @:click="counter.count++"> {{ counter.count }}</button>

    <input v-model="text" placeholder="Type here">
    <p>{{ text }}</p>

    <h1 v-if="isRed">Is red!</h1>
    <h1 v-else-if="isBlue">Is blue!</h1>
    <h1 v-else>Is not red!</h1>
    <ul>
      <li v-for="item in list" :key="item.id" :value="item.text">
      {{ item.text }}
      </li>
    </ul>

    <input v-model="newlist" placeholder="Type a new list here">
    <button @click="addItem(newlist)">submit
    </button>
    <ul>
      <li v-for="(item,index) in list" :key="item.id" :value="item.text">
          {{ index }}----{{ item.id }}---{{ item.text }}
          <button @click="removeItem(index)">X</button>
      </li>
    </ul>
  </div>
</template>

<script>
// When you wrap an object with “reactive”, Vue will automatically track its properties and update the view whenever any of them change. You can think of it as a way to make an entire object reactive.
// ref commonly used when you want to create a reactive value that is not an object
import { reactive, ref } from "vue";

let id = 0;
export default {
  name: 'MyComponent',
  data() {
    return {
      counter: reactive({count: 0}),
      message: ref("hello vue"),
      text: ref(""),
      isRed: true,
      isBlue: false,
      isBold: false,
      classObject: {
        'blue': true,
        'underline': false,
      },
      list: [
        {id: id++, text: 'html'},
        {id: id++, text: 'Js'},
        {id: id++, text: 'vue'}
      ],
      newlist: ''
    }
  },
  methods: {
   increase(data) {
     data.count++
   },
    removeItem(index){
     this.list.splice(index,1)
    },
    addItem(item){
      let newItem = {id: id++, text: item}
      this.list.push(newItem)
    }
  }
};
</script>

<style>
.red {
  color: red;
}

.blue {
  color: blue;
}

.bold {
  font-weight: bold;
}

.underline {
  text-decoration: underline;
}
</style>