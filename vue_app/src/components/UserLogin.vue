<!--

UserLogin.vue

The user login the web app.
Written by: Luke Melton
Date: 04/10/2023





-->



<template>
  <v-dialog v-model="dialog" max-width="500">
    <v-card>
      <v-card-title class="headline primary--text">LOG IN</v-card-title>
      <v-card-text>
        <v-form @submit.prevent="login">
          <v-text-field
            v-model="email"
            label="Email"
            required
            type="email"
            :error-messages="errors.email"
          ></v-text-field>
          <v-text-field
            v-model="password"
            label="Password"
            required
            type="password"
            :error-messages="errors.password"
          ></v-text-field>
          <v-alert v-if="errors.unknown" type="error" dismissible>
            {{ errors.unknown }}
          </v-alert>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" @click="login">Log in</v-btn>
        <v-btn @click="dialog = false">Cancel</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import axios from "axios";
import { useStore } from "vuex";

export default defineComponent({
  name: "UserLogin",
  data(): {
    email: string;
    password: string;
    errors: { email: string[]; password: string[]; unknown: string | null };
    dialog: boolean;
  } {
    return {
      email: "",
      password: "",
      errors: { email: [], password: [], unknown: null },
      dialog: true,
    };
  },
  setup() {
    const store = useStore();
    return { store };
  },
  methods: {
    getCookie(name: string): string | null {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
          let cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    },
    async login() {
      console.log("Submitting Login Information");
      console.log(this.email)
      console.log(this.password)
      try {
        let formData = new FormData();
        formData.append('email', this.email);
        formData.append('password', this.password);
        let csrfToken = this.getCookie('csrftoken');
        if (csrfToken !== null) {
          formData.append('csrfmiddlewaretoken', csrfToken);
        } else {
          // handle the case when csrfToken is null, this depends on your application logic
          // you can either not append the csrfmiddlewaretoken or use a default value
          // For example:
          console.log('CSRF token is missing. Please ensure cookies are enabled.');
        }

        axios.defaults.xsrfCookieName = 'csrftoken'; // the name of the cookie Django is using for CSRF validation.
        axios.defaults.xsrfHeaderName = "X-CSRFToken"; // the name of the HTTP header Django is expecting for CSRF validation.

        const response = await axios.post(`${process.env.VUE_APP_API_BASE_URL}/api/auth/login/`, formData, {
          headers: { 
            'Content-Type': 'multipart/form-data',
          } 
        });





        if (response.status === 200) {
          this.store.commit("setToken", response.data.token);

          // Set the axios authorization header
          axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.token}`;
          axios.defaults.headers.common['Authorization'] = `Token ${response.data.token}`;
          this.$emit("login-success");
          this.$emit("login-success");
        } else {
          this.errors = {
            email: [],
            password: [],
            unknown: "Invalid credentials.",
          };
        }
      } catch (error) {
        console.log(error)
        this.errors = {
          email: [],
          password: [],
          unknown: "An error occurred. Please try again later.",
        };
      }
    },
      },
    });


</script>

<style scoped>
.v-dialog {
  --dialog-max-width: 500px;
  --dialog-width: 100%;
  --dialog-content-padding: 24px;
}

.v-card {
  border-radius: 16px;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 2px 4px;
}

.v-card-title {
  font-size: 24px;
}

.v-card-text {
  padding: 24px;
}

.v-alert {
  margin-top: 8px;
}

.v-btn {
  margin-left: 8px;
}
</style>


