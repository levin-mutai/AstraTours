import { createStore } from 'vuex'

export default createStore({
  state: {
    clientid : null,
    userid : null,
    name: null,
    email: null,
    refresh: sessionStorage.getItem('refresh'),
    phonenumber : null,
    isAuthenticated: false, 
    
  },
  getters: {
  },
  mutations: {
    initizeStore(state) {
      if (sessionStorage.getItem('token')) {
        state.refresh= localStorage.getItem('token')
        state.isAuthenticated = true
      }else{
        state.refresh = ''
        state.isAuthenticated = false
      }
    },
    setToken(state, token) {
      state.refresh = token
      state.isAuthenticated = true
    },
    setUser(state, user) {
      state.name = user
    },
    setClientid(state, id) {
      state.clientid = id
    },
    setUserid(state, id) {
      state.userid = id
    },
    setEmail(state, email) {
      state.email = email
    },
    setPhone(state, phon) {
      state.phonenumber = phon
    },removeToken
    (state){
      state.refresh= ''
      sessionStorage.removeItem('refresh')
      sessionStorage.removeItem('access')
      sessionStorage.removeItem('clientid')
      sessionStorage.removeItem('userid')
      state.name = ''
      state.email= ''
      state.phonenumber = ''
      state.clientid = ''
      state.userid= ''
      state.isAuthenticated = false
    }
  },
  actions: {
  },
  modules: {
  }
})
