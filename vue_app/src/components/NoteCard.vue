<template>
  <v-card :color="cardColor">
    <v-dialog v-model="colorPickerDialog" max-width="500px">
      <v-color-picker v-model="noteColor"></v-color-picker>
    </v-dialog>
    <v-card-title>
      <v-text-field
        v-model="noteTitle"
        clearable
        @keydown.enter.prevent
        background-color="transparent"
      >
      </v-text-field>
      <v-spacer></v-spacer>
    </v-card-title>
    <v-card-text>
      <v-textarea
        v-model="noteContent"
        auto-grow
        clearable
        background-color="transparent"
      />
    </v-card-text>
    <v-card-actions>
      <!-- Move the color picker button to the card actions section -->
      <v-btn icon @click="colorPickerDialog = true">
        <v-icon>mdi-palette</v-icon>
      </v-btn>
      <v-btn icon @click="$emit('delete-note')">
        <v-icon>mdi-close</v-icon>
      </v-btn>

      <v-btn icon @click="saveNoteCard">
        <v-icon>mdi-content-save</v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
  <v-alert v-model="successAlert" type="success" dismissible>
    Note saved successfully!
  </v-alert>
  <v-alert v-model="errorAlert" type="error" dismissible>
    Failed to save note!
  </v-alert>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { AxiosError } from "axios";
import { Store, useStore } from "vuex";

export default defineComponent({
  name: "NoteCard",
  props: ["darkState"],
  inject: ["$http"],
  data() {
    return {
      noteTitle: "",
      noteContent: "",
      noteColor: "white",
      colorPickerDialog: false,
      successAlert: false,
      errorAlert: false,
    };
  },
  watch: {
    noteColor(newColor) {
      this.$forceUpdate();
    },
  },
  computed: {
    cardColor() {
      return this.darkState ? "grey darken-3" : this.noteColor;
    },
  },
  methods: {
    async saveNoteCard() {
      const store = useStore();
      try {
        const response = await this.$http.post(process.env.VUE_APP_NOTECARD_URL,
          {
            title: this.noteTitle,
            body: this.noteContent,
            user: store.state.userId,
          }
        );
        console.log(response.data);
        // Display the success alert
        this.successAlert = true;
      } catch (error) {
        console.error("An error occurred:", error);
        this.errorAlert = true;
        if (error && typeof error === "object" && "response" in error) {
          const axiosError = error as AxiosError;
          if (axiosError.response) {
            console.log(axiosError.response.data);
          }
        } else {
          console.error("An unexpected error occurred:", error);
        }
      }
    },
  },
});
</script>

<style scoped>
.note-card {
  width: 320px;
  min-height: 150px;
  padding: 20px;
  box-sizing: border-box;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  position: relative;
  overflow-wrap: break-word;
}

input[type="text"],
textarea {
  background-color: transparent;
  border: none;
  outline: none;
  resize: none;
  width: 100%;
}

input[type="text"]::placeholder,
textarea::placeholder {
  color: rgba(0, 0, 0, 0.5);
}
</style>
