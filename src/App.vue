<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import router from '@/router';
import *  as config from './config'
export default {
  beforeCreate () {
    this.$liff.init({
      liffId: config.config.liffId // use own liffId
    })
    .then(() => {
      // Start to use liff's api
      if (!this.$liff.isLoggedIn()) {
        // set `redirectUri` to redirect the user to a URL other than the front page of your LIFF app.
        // this.$liff.login();
        // console.log(this.$liff.getAccessToken())
      }
      this.initializeApp()
    })
    .catch((err) => {
      // Error happens during initialization
      console.log(err.code, err.message);
    });
  },
  data: () => ({
    profile: {
      userId: '',
      displayName: '',
      pictureUrl: '',
      statusMessage: ''
    }
  }),
  created() {
    const page = this.$route.query.page
    if (page === 'poke') {
      router.push('poke')
    }
  },
  methods: {
    initializeApp () {
      console.log("init app")
    },
    getProfile () {
      let _this = this
      this.$liff.getProfile().then(function (profile) {
        _this.profile = profile
      }).catch(function (error) {
        alert('Error getting profile: ' + error)
      })
    }
  }
}
</script>

<style lang="scss">
  @import './assets/scss/all';
</style>
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
#nav a.router-link-exact-active {
  color: #42b983;
}
</style>