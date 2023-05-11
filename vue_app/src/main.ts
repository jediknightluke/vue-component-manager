import { createApp } from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import axios from "axios";

axios.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("token");
    if (token) {
      config.headers["Authorization"] = `Token ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

import VueAxios from "vue-axios";
import "@mdi/font/css/materialdesignicons.css";

// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
const vuetify = createVuetify({
  components,
  directives,
  theme: {
    defaultTheme: "myTheme",
    themes: {
      myTheme: {
        dark: false, // Set the initial value of the dark theme
      },
    },
  },
});

// vuedraggable
import Draggable from "vuedraggable";

const app = createApp(App);
app
  .use(store)
  .use(vuetify)
  .use(router)
  .use(VueAxios, axios)
  .directive("v-draggable", Draggable);

app.mount("#app");
