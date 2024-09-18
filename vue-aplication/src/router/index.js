import { createRouter, createWebHistory } from 'vue-router'
import MainView from '../views/MainView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: MainView
    },
    {
      path: '/sobre',
      name: 'sobre',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/resultado',
      name: 'resultado',
      component: () => import('../views/ResultView.vue')
    },
    { 
      //Rota pega tudo
      path: '/:catchAll(.*)', 
      redirect: '/'
    }
  ]
})

export default router
