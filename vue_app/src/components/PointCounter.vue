<template>
  <v-container>
    <v-row>
      <v-col>
        <v-text-field
          v-model="name"
          label="Name"
          @keydown.enter="addName"
        ></v-text-field>
      </v-col>
      <v-col>
        <v-btn color="primary" @click="addName">Add Name</v-btn>
      </v-col>
    </v-row>
    <v-list>
      <v-list-item v-for="(item, index) in names" :key="index">
        <v-list-item-content>
          {{ item.name }}: {{ item.points }} (${{
            (item.points * 0.25).toFixed(2)
          }})
        </v-list-item-content>
        <v-list-item-action>
          <v-btn text @click="incrementPoints(index)">Add point</v-btn>
        </v-list-item-action>
      </v-list-item>
      <v-list-item>
        <v-list-item-content>
          Total: ${{ totalAmount.toFixed(2) }}
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-container>
</template>

<script lang="ts">
import { computed, defineComponent, ref } from "vue";

export default defineComponent({
  setup() {
    const name = ref("");
    const names = ref<Array<{ name: string; points: number }>>([]);

    const addName = () => {
      if (name.value.trim()) {
        names.value.push({ name: name.value, points: 0 });
        name.value = "";
      }
    };

    const incrementPoints = (index: number) => {
      names.value[index].points++;
    };

    const totalAmount = computed(() => {
      let sum = 0;
      for (const item of names.value) {
        sum += item.points * 0.25;
      }
      return sum;
    });

    return {
      name,
      names,
      addName,
      incrementPoints,
      totalAmount,
    };
  },
});
</script>
