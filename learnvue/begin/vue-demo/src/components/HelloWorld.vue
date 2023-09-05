<template>
  <div class="myclass">
    <h3>learn vue</h3>
    <p>{{ message }}</p>

    <div v-html="rawHtml"></div>

    <!--    <div :id="dynamicid"></div>-->
    <div v-bind:id="dynamicid"></div>

    <div v-if="result">
      <p> {{ result }} is true</p>
    </div>
    <div v-else>
      <p> {{ result }} is false </p>
    </div>

    <p>{{ num + 5 }}</p>
    <p>{{ flag ? "true": "false" }}</p>

    <ul>
      <li v-for="item in newsList">
          {{ item.title }}
      </li>
    </ul>
    <div v-if="type === 'A'">
      <p>A</p>
    </div>
    <div v-else-if="type === 'B'">
      <p>B</p>
    </div>
    <div v-else-if="type === 'C'">
      <p>C</p>
    </div>
    <div v-else>
      <p>not A B C</p>
    </div>

    <div v-show="result"> show result </div>

    <select @change="changeVal($event)" v-model="myoption">
      <template v-for="(list, index) in newsList" :list="list" :index="index" :title="list.title">
          <option v-if= "index === 1" :value="list.title" selected>{{ list.title }}</option>
          <option v-else :value="list.title">{{ list.title }} </option>
      </template>
      <div> {{ myoption }}</div>
    </select>
    <!--<button v-on:click="counter +=1 ">click:counter= {{ counter }}</button>-->
    <button @click="counter +=1 ">click:counter= {{ counter }}</button>

    <button @click="clickHandle">click:handle</button>

    <button @click="say('hi')">say hi</button>
    <button @click="say('what')">say what</button>

    <ul>
      <li @click="clickList(item.id)" v-for="item in newsList"> {{ item.title }}</li>
    </ul>
<!--filter space in the beginning and end of the string-->
    <input type="text" v-model.trim="username">
    <p>{{ username }}</p>
    <input type="text" v-model="username">
    <p>{{ username }}</p>
    <input type="text" v-model.lazy="password">
    <p>{{ password }}</p>
    <button @click="clickGetUserName">Get User Name</button>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      message: "test message",
      rawHtml: "<a href='http://www.baidu.com'>baidu</a>",
      dynamicid: 1007,
      num: 5,
      flag: false,
      username: "yanfeiw",
      result: true,
      type: "D",
      password: "",

      myoption: "title1",
      newsList:[
        {
          id: 1001,
          title: "title1"
        },
        {
          id: 1002,
          title: "title2"
        },
        {
          id: 1003,
          title: "title3"
        }
      ],

      counter: 1
    }
  },
  methods: {
    clickHandle() {
      console.log("click handle"),
          this.message = "a new message"
    },
    say(data){
      console.log(data)
    },
    clickList(data) {
      console.log(data)
    },
    clickGetUserName(){
      console.log(this.username)
    },
    // changeVal:function (event){
    changeVal(event){
     this.myoption = event.target.value;
     alert("you choose" + this.myoption)
    }

  }

}
</script>

