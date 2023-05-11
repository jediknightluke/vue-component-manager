<template>
  <div id="app">
    <v-app :style="{ backgroundColor: colors.background }">
      <v-app-bar :color="colors.topBar" app v-if="isLoggedIn && showTopBar">
        <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
        <v-toolbar-title>My App</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon @click="showTopBar = false">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-app-bar>

      <!-- Side navagation drawer start -->

      <v-navigation-drawer
        :color="colors.sideDrawer"
        app
        clipped
        mini-variant-width="80"
        v-model="drawer"
        v-if="isLoggedIn"
      >
        <!-- Profile -->

        <v-list>
          <v-list-item>
            <v-row no-gutters>
              <v-col cols="3">
                <v-icon>mdi-account</v-icon>
              </v-col>
              <v-col cols="9">
                <v-list-item-title>Profile</v-list-item-title>
              </v-col>
            </v-row>
          </v-list-item>

          <!-- Add Components -->

          <v-list-item @click="openAddComponentsModal">
            <v-row no-gutters>
              <v-col cols="3">
                <v-icon>mdi-plus-box</v-icon>
              </v-col>
              <v-col cols="9">
                <v-list-item-title>Add Components</v-list-item-title>
              </v-col>
            </v-row>
          </v-list-item>

          <!-- Handle Logout -->

          <v-list-item v-if="isLoggedIn" @click="logout">
            <v-row no-gutters>
              <v-col cols="3">
                <v-icon>mdi-logout</v-icon>
              </v-col>
              <v-col cols="9">
                <v-list-item-title>Logout</v-list-item-title>
              </v-col>
            </v-row>
          </v-list-item>
        </v-list>

        <!-- Toggle Dark Mode -->

        <v-divider></v-divider>
        <v-list-item @click="toggleDarkMode">
          <v-row no-gutters>
            <v-col cols="3">
              <v-icon>mdi-theme-light-dark</v-icon>
            </v-col>
            <v-col cols="9">
              <v-list-item-title>Toggle Dark Mode</v-list-item-title>
            </v-col>
          </v-row>
        </v-list-item>
        <v-divider></v-divider>

        <v-spacer></v-spacer>
        <v-btn fixed bottom @click="drawer = false" block> Close Drawer </v-btn>
      </v-navigation-drawer>

      <!-- Side navagation drawer end -->

      <v-btn
        v-if="!showTopBar"
        fab
        small
        fixed
        top
        style="z-index: 5"
        :style="{ right: '24px', backgroundColor: colors.topBar }"
        @click="showTopBar = true"
      >
        <v-icon>mdi-chevron-up</v-icon>
      </v-btn>

      <!--
      Begin Component Grid Layout
      -->

      <v-main>
        <v-container v-container fluid>
          <v-row v-if="isLoggedIn">
            <!--
            Begin Component Grid Layout
            -->

            <!--
              Chessboard
            -->

            <v-col
              :cols="getColCols('chessBoard')"
              :md="getColMd('chessBoard')"
              v-if="components.chessBoard"
            >
              <v-card
                :style="getColStyles('chessBoard')"
                class="component-border"
              >
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn icon small @click="toggleFullscreen('chessBoard')">
                    <v-icon>mdi-fullscreen</v-icon>
                  </v-btn>
                  <v-btn icon small @click="deleteComponent('chessBoard')">
                    <v-icon>mdi-close</v-icon>
                  </v-btn>
                </v-card-actions>
                <ChessBoard />
              </v-card>
            </v-col>

            <!--
              PointCounter
            -->

            <v-col
              :cols="getColCols('pointCounter')"
              :md="getColMd('pointCounter')"
              v-if="components.pointCounter"
            >
              <v-card
                :style="getColStyles('pointCounter')"
                class="component-border"
              >
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn icon small @click="toggleFullscreen('pointCounter')">
                    <v-icon>mdi-fullscreen</v-icon>
                  </v-btn>
                  <v-btn icon small @click="deleteComponent('pointCounter')">
                    <v-icon>mdi-close</v-icon>
                  </v-btn>
                </v-card-actions>
                <PointCounter />
              </v-card>
            </v-col>

            <!--
              NoteCard
            -->

            <v-col
              :cols="getColCols('noteCard')"
              :md="getColMd('noteCard')"
              v-if="components.noteCard"
            >
              <v-card
                :style="getColStyles('noteCard')"
                class="component-border"
              >
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn icon small @click="toggleFullscreen('noteCard')">
                    <v-icon>mdi-fullscreen</v-icon>
                  </v-btn>
                  <v-btn icon small @click="deleteComponent('noteCard')">
                    <v-icon>mdi-close</v-icon>
                  </v-btn>
                </v-card-actions>
                <v-btn @click="addNote">Add Note</v-btn>
                <v-row>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                    lg="3"
                    v-for="(note, index) in notes"
                    :key="index"
                  >
                    <NoteCard @delete-note="handleDeleteNote(index)"></NoteCard>
                  </v-col>
                </v-row>
              </v-card>
            </v-col>

            <!--
              SMB Viewer
            -->

            <v-col
              :cols="getColCols('webDavViewer')"
              :md="getColMd('webDavViewer')"
              v-if="components.webDavViewer"
            >
              <v-card
                :style="getColStyles('webDavViewer')"
                class="component-border"
              >
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn icon small @click="toggleFullscreen('webDavViewer')">
                    <v-icon>mdi-fullscreen</v-icon>
                  </v-btn>
                  <v-btn icon small @click="deleteComponent('webDavViewer')">
                    <v-icon>mdi-close</v-icon>
                  </v-btn>
                </v-card-actions>
                <WebDavViewer />
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-main>
    </v-app>

    <!--
      User Login
    -->

    <v-dialog v-model="dialog" persistent max-width="500" v-if="!isLoggedIn">
      <UserLogin
        @login-success="handleLoginSuccess"
        @close-dialog="dialog = false"
      />
    </v-dialog>
  </div>

  <!--
      Add Components
    -->

  <v-dialog v-model="addComponentDialog" max-width="400">
    <v-card>
      <v-card-title>Select a component to add</v-card-title>
      <v-card-text>
        <v-list>
          <v-list-item
            v-for="(component, componentName) in components"
            :key="componentName"
            @click="addComponent(componentName)"
          >
            <v-list-item-title>{{ componentName }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import NoteCard from "./components/NoteCard.vue";
import ChessBoard from "./components/ChessBoard.vue";
import PointCounter from "./components/PointCounter.vue";
import UserLogin from "./components/UserLogin.vue";
import { reactive, computed, provide } from "vue";
import WebDavViewer from "./components/WebDavViewer.vue";
import { useStore } from "vuex";

import { useRouter } from "vue-router";

interface FullscreenComponents {
  [key: string]: boolean;
}

export default defineComponent({
  components: {
    NoteCard,
    UserLogin,
    ChessBoard,
    PointCounter,
    WebDavViewer,
  },
  data(): {
    notes: { title: string; text: string; color: string }[];
    drawer: boolean;
    components: { [key: string]: boolean };
    addComponentDialog: boolean;
    showTopBar: boolean;
  } {
    return {
      addComponentDialog: false,
      notes: [],

      drawer: true,

      components: {
        chessBoard: true,
        pointCounter: true,
        noteCard: true,
        webDavViewer: true,
      },

      showTopBar: true,
    };
  },
  methods: {
    handleLoginSuccess() {
      this.isLoggedIn = true;
      this.dialog = false;
    },
    addNote() {
      const newNote = {
        title: "",
        text: "",
        color: "",
      };
      this.notes = [...this.notes, newNote];
    },
    handleDeleteNote(index: number) {
      this.notes.splice(index, 1);
    },
    deleteComponent(componentName: string) {
      this.components[componentName] = false;
    },
    openAddComponentsModal() {
      this.addComponentDialog = true;
    },
    addComponent(componentName: string) {
      this.components[componentName] = true;
      this.addComponentDialog = false;
    },
    toggleTopBar() {
      this.showTopBar = !this.showTopBar;
    },
  },
  setup() {
    const dark = ref(false);
    const store = useStore();
    const router = useRouter();
    const isLoggedIn = ref(false);
    const dialog = ref(false);

    const toggleDarkMode = () => {
      if (colors.topBar === "primary") {
        colors.topBar = "slategrey";
        colors.sideDrawer = "#28282b";
        colors.background = "#000";
      } else {
        colors.topBar = "primary";
        colors.sideDrawer = "white";
        colors.background = "white";
      }
    };

    const logout = () => {
      store.commit("removeToken");
      isLoggedIn.value = false;
    };

    const colors = reactive({
      topBar: "primary",
      sideDrawer: "white",
      background: "white",
    });

    const fullscreen: FullscreenComponents = reactive({
      chessBoard: false,
      pointCounter: false,
      noteCard: false,
      webDavViewer: false,
    });

    const toggleFullscreen = (componentName: string) => {
      fullscreen[componentName] = !fullscreen[componentName];
    };

    const getColCols = (componentName: string) => {
      return fullscreen[componentName] ? 12 : 12;
    };

    const getColMd = (componentName: string) => {
      return fullscreen[componentName] ? 12 : 6;
    };

    const getColStyles = (componentName: string) => {
      return {
        height: fullscreen[componentName] ? "100vh" : "auto",
      };
    };

    onMounted(() => {
      if (store.getters.getToken) {
        isLoggedIn.value = true;
      } else {
        dialog.value = true;
      }
    });

    return {
      dark,
      toggleDarkMode,
      fullscreen,
      toggleFullscreen,
      colors,
      getColCols,
      getColMd,
      getColStyles,
      logout,
      isLoggedIn,
      dialog,
    };
  },
});
</script>

<style scoped>
.component-border {
  border: 1px solid #ccc;
  padding: 16px;
}

.fullscreen {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 9999;
}
</style>
