<!-- DraggableWrapper.vue -->

<template>
  <div v-bind="$attrs" v-on="{ ...$attrs }">
    <slot />
  </div>
</template>

<script>
export default {
  name: "DraggableWrapper",
};
</script>
