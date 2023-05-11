<template>
  <div class="webdav-viewer">
    <h2>WebDAV Viewer</h2>
    <v-form ref="form" @submit.prevent="connectToShare">
      <v-text-field label="Server" v-model="server" required></v-text-field>
      <v-text-field label="Username" v-model="username" required></v-text-field>
      <v-text-field
        label="Password"
        v-model="password"
        type="password"
        required
      ></v-text-field>
      <v-btn type="submit">Connect</v-btn>
    </v-form>
    <v-list v-if="files.length">
      <v-list-item v-for="file in files" :key="file.filename">
        <v-list-item-icon>
          <v-icon v-if="file.type === 'directory'">mdi-folder</v-icon>
          <v-icon v-else>mdi-file-document</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>{{ file.filename }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <v-snackbar v-model="errorSnackbar" color="error" top>
      {{ errorSnackbarMessage }}
      <v-btn text @click="errorSnackbar = false">Close</v-btn>
    </v-snackbar>
    <v-snackbar v-model="successSnackbar" color="success" top>
      {{ successSnackbarMessage }}
      <v-btn text @click="successSnackbar = false">Close</v-btn>
    </v-snackbar>
  </div>
</template>

<script>
import { createClient } from "webdav";

export default {
  data() {
    return {
      server: "",
      username: "",
      password: "",
      files: [],
      errorSnackbar: false,
      errorSnackbarMessage: "",
      successSnackbar: false,
      successSnackbarMessage: "",
    };
  },
  methods: {
    async connectToShare() {
      if (this.$refs.form.validate()) {
        try {
          const client = createClient(this.server, {
            username: this.username,
            password: this.password,
          });

          const directoryItems = await client.getDirectoryContents("/");
          this.files = directoryItems;
          this.showSuccessSnackbar("Connected to the server successfully.");
        } catch (error) {
          console.error(error);
          this.$refs.form.resetValidation();
          this.showErrorSnackbar(
            `Unable to connect to the server. Reason: ${
              error.message || "Unknown error"
            }`
          );
        }
      }
    },
    showErrorSnackbar(message) {
      this.errorSnackbarMessage = message;
      this.errorSnackbar = true;
    },
    showSuccessSnackbar(message) {
      this.successSnackbarMessage = message;
      this.successSnackbar = true;
    },
  },
};
</script>

<style scoped>
.webdav-viewer {
  max-width: 600px;
  margin: 0 auto;
}
</style>
