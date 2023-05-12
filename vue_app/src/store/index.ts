import { createStore } from "vuex";

export default createStore({
  state: {
    userId: null,
    token: null,
  },
  getters: {
    userId: (state) => state.userId,
  },
  mutations: {
    setUserId(state, userId) {
      state.userId = userId;
    },
    setToken(state, token) {
      state.token = token;
    },
    removeToken(state) {
      state.token = null;
    },
  },
  actions: {
    setUserId({ commit }, userId) {
      commit("setUserId", userId);
    },
    setToken({ commit }, token) {
      commit("setToken", token);
    },
    removeToken({ commit }) {
      commit("removeToken");
    },
  },
  modules: {},
});
