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
  methods: {
    async login() {
      const store = useStore();
      try {
        const response = await axios.post(process.env.VUE_APP_API_URL,
          {
            email: this.email,
            password: this.password,
          }
        );

        if (response.status === 200) {
          store.commit("setToken", response.data.token);
          this.$emit("login-success");
        } else {
          this.errors = {
            email: [],
            password: [],
            unknown: "Invalid credentials.",
          };
        }
      } catch (error) {
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
