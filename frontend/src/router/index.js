import { createRouter, createWebHistory ,createMemoryHistory,createWebHashHistory} from 'vue-router'
import home from '../views/home.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: home
  },
  {
    path: '/destinations',
    name: 'destinations',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/destinations.vue')
  },
 {
  path: '/hotels',
    name: 'hotels',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/hotels.vue')
  },
  {
  path: '/bookings',
    name: 'bookings',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/bookings.vue')
  },
  {
  path: '/cart',
    name: 'cart',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/cart.vue')
  },
  {
  path: '/login',
    name: 'login',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../components/login.vue')
  },
  {
  path: '/signup',
    name: 'signup',
   
    component: () => import(/* webpackChunkName: "signup" */ '../components/signup.vue')
  },
  // {
  //   path: '/desc',
  //     name: 'desc',
     
  //     component: () => import(/* webpackChunkName: "signup" */ '../components/desc.vue')
  // },
  {
    path: '/desc/:id',
      name: 'desc',
      
      component: () => import(/* webpackChunkName: "signup" */ '../components/desc.vue')
  },
]

const router = createRouter({
  // history: createMemoryHistory(),
  history: createWebHashHistory(),
  // history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
