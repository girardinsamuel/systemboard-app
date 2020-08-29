<template>
  <div
    class="fixed w-10 px-2 text-sm font-medium text-center text-white capitalize rounded-md pointer-events-none text"
    :style="
      `background-color: ${color}; left: ${pos.x}px; top: ${pos.y}px; width: ${width}px;`
    "
  >
    <span>{{ role }}</span>
  </div>
</template>

<script>
import { getColor } from "../data/holds";

export default {
  name: "BoardTooltip",
  props: {
    role: {
      type: String,
      default: "start",
    },
    width: {
      type: String,
      default: 20,
    },
    pos: {
      type: Object,
      default: () => ({ x: 0, y: 0 }),
    },
  },
  computed: {
    color() {
      return getColor(this.role);
    },
  },
};
</script>

<style></style>
