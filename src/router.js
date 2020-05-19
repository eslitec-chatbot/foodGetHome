import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/poke',
      name: 'poke',
      component: () => import(/* webpackChunkName: "about" */ './views/Poke.vue')
    },
    {
      path: '/pokemon',
      name: 'pokemon',
      component: () => import(/* webpackChunkName: "about" */ './components/Pokemons.vue')
    },
    {
      path: '*',
      redirect: '/',
    }
  ]
})