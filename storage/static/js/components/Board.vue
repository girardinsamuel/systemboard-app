<template>
  <div
    id="container"
    class="flex-grow w-full h-full m-auto overflow-auto text-center bg-black"
  >
    <!-- :style="
        `padding-top: ${paddingY}px; padding-bottom: ${paddingY}px; margin: auto;`
      " -->
    <!-- :style="`padding: ${paddingY}px ${paddingX}px;`" -->
    <canvas
      ref="canvas"
      id="board"
      :width="width"
      :height="height"
      class="bg-black"
      @mousedown="startPainting"
      @mouseup="finishedPainting"
    >
    </canvas>
    <BoardTooltip
      ref="tooltip"
      :role="tooltip.role"
      :width="tooltip.width"
      :pos="tooltip.position"
      v-if="tooltip.visible"
    />
    <!-- <button @click="toggleSym">Sym (reversed ? {{ inverted }})</button> -->
    <!-- create -->
    <!-- <button @click="validateProblem">Next</button> -->
  </div>
</template>

<script>
// import { nextTick } from "vue";
// import { extend } from "vue";
import { getColor, roles } from "../data/holds";

const drawRotImage = (ctx, image, x, y, w, h, angle) => {
  ctx.save();
  ctx.translate(x + w / 2, y + h / 2);
  ctx.rotate((angle * Math.PI) / 180.0);
  ctx.translate(-x - w / 2, -y - h / 2);
  ctx.drawImage(image, x, y, w, h);
  ctx.restore();
};

import BoardTooltip from "./BoardTooltip.vue";
export default {
  name: "Board",
  components: {
    BoardTooltip, //: () => import("./BoardTooltip.vue"),
  },
  props: {
    placements: {
      type: Array,
      default: () => [
        {
          role: "start",
          x: 1,
          y: 1,
          x_inverted: 11,
        },
        {
          role: "end",
          x: 11,
          y: 18,
          x_inverted: 1,
        },
        {
          role: "middle",
          x: 6,
          y: 7,
          x_inverted: 6,
        },
        {
          role: "middle",
          x: 4,
          y: 15,
          x_inverted: 7,
        },
      ],
    },
    holdsTypes: {
      type: Object,
      default: () => ({
        start: "green",
        middle: "blue",
        end: "red",
        foot: "pink",
      }),
    },
    boardSize: {
      type: Object,
      default: () => ({
        nbRows: 18,
        nbCols: 11,
      }),
    },
    boardLayout: {
      type: Array,
      default: () => [
        {
          id: 8, // the one we get the image from
          rotation: 10,
          x: 1,
          y: 1,
        },
        {
          id: 2, // the one we get the image from
          rotation: 0,
          x: 1,
          y: 2,
        },
      ],
    },
    backgroundColor: {
      type: String,
      default: "black",
    },
  },
  data() {
    return {
      canvas: null,
      width: null,
      height: null,
      paddingX: 12,
      paddingY: 2,
      holdRadius: 15,
      holdStroke: 3,
      holdPadding: 3,
      dx: 0,
      dy: 0,
      inverted: false,
      canvasEl: null,
      // create problem
      newProblemHolds: [],
      tooltipTimeout: 2000,
      painting: false,
      tooltip: {
        role: null,
        position: { x: 0, y: 0 },
        visible: false,
        timeout: null,
      },
    };
  },
  created() {},
  destroyed() {
    // destroy listeners
  },
  mounted() {
    document.addEventListener("swiped-right", (e) => {
      this.$emit("swipe-right");
    });
    document.addEventListener("swiped-left", (e) => {
      this.$emit("swipe-left");
    });

    let containerEl = document.getElementById("container");
    this.height = containerEl.clientHeight - this.paddingY * 2;
    this.dy = this.height / (this.boardSize.nbRows + 1);
    this.holdRadius = this.dy / 2;
    this.dx = this.dy;
    this.paddingX = (containerEl.width - this.dx * this.boardSize.nbCols) / 2;
    // this.width = containerEl.clientWidth - 40; //- this.paddingX * 2;
    this.width = this.dx * (this.boardSize.nbCols + 1); //- this.paddingX * 2;

    this.canvasEl = document.getElementById("board");
    // canvasEl.width = canvasEl.getBoundingClientRect().width;
    // canvasEl.height = canvasEl.getBoundingClientRect().height;
    this.canvas = this.canvasEl.getContext("2d");
    // prepare coordinates system
    // this.dx = this.width / (this.boardSize.nbCols + 1);

    this.drawBoard();

    // draw problem
    this.$nextTick(() => {
      // test
      // const allHolds = this.getAllHolds();
      // for (const hold of allHolds) {
      //   this.drawHold(hold);
      // }
      this.drawProblem();
    });

    // add event handling for problem creation
  },
  computed: {
    // problem creation computed methods
    hasTwoStarts() {
      return this.newProblemHolds.filter((p) => p.role == "start").length == 2;
    },
    hasTwoEnds() {
      return this.newProblemHolds.filter((p) => p.role == "end").length == 2;
    },
  },
  methods: {
    // TEST
    getAllHolds() {
      const holds = [];
      for (let i = 1; i < this.boardSize.nbCols + 1; i++) {
        for (let j = 1; j < this.boardSize.nbRows + 1; j++) {
          holds.push({
            x: i,
            y: j,
            role: "start",
          });
        }
      }
      return holds;
    },
    // END TEST
    _normalizeCoords(x, y) {
      // origin on board is left-bottom corner as origin of canvas is top left corne
      return { x, y: this.boardSize.nbRows - y + 1 };
    },
    drawBoard() {
      // inner circle
      const maxHoldSize =
        (this.holdRadius - this.holdStroke - this.holdPadding) * 2;

      // for (const hold of this.boardLayout) {
      // all for test
      const allHolds = this.getAllHolds();
      const allIds = [2, 8, 15, 16, 30, 31];
      for (const hold of allHolds) {
        let holdId = allIds[Math.floor(Math.random() * allIds.length)];
        // get hold image
        let imageObj = new Image();
        imageObj.src = `/static/img/holds/${holdId}.png`;
        // imageObj.src = `holds/${hold.id}.png`;
        // get hold coords
        let coords = this._normalizeCoords(hold.x, hold.y);
        imageObj.onload = () => {
          // compute width and height of image to be contained inside circle
          const ratio =
            maxHoldSize /
            Math.max(imageObj.naturalWidth, imageObj.naturalHeight);
          const width = imageObj.naturalWidth * ratio;
          const height = imageObj.naturalHeight * ratio;
          drawRotImage(
            this.canvas,
            imageObj,
            coords.x * this.dx - width / 2,
            coords.y * this.dy - height / 2,
            width,
            height,
            hold.rotation
          );
        };
      }
    },
    clear() {
      this.canvas.clearRect(0, 0, this.width, this.height);
      // TODO: issue, clear also clears the holds images, for now board is drawn again too
      this.drawBoard();
    },
    drawCircle(x = 20, y = 20, color = "red") {
      this.canvas.beginPath();
      this.canvas.arc(x, y, this.holdRadius, 0, 2 * Math.PI, false);
      this.canvas.lineWidth = this.holdStroke;
      this.canvas.strokeStyle = color;
      this.canvas.stroke();
    },
    drawHold(hold, inverted = false) {
      const color = getColor(hold.role_id);
      // convert coordinate to x,y coordinate on canvas
      const coords = this._normalizeCoords(
        inverted ? hold.x_inverted : hold.coords.x,
        hold.coords.y
      );
      this.drawCircle(coords.x * this.dx, coords.y * this.dy, color);
    },
    drawProblem(inverted = false) {
      for (const placement of this.placements) {
        this.drawHold(placement, inverted);
      }
    },
    drawCreatedProblem(inverted = false) {
      for (const hold of this.newProblemHolds) {
        this.drawHold(hold, inverted);
      }
    },
    toggleSym() {
      this.inverted = !this.inverted;
    },
    // creating problem method
    finishedPainting() {
      this.painting = false;
      this.canvas.beginPath();
    },
    startPainting(e) {
      this.painting = true;
      // TODO: find closed hold to add circle to
      // TODO: handle color, if hold already in array then loop through color
      // and if end of color array is reached then delete holds
      // mouse
      let mouseX, mouseY;
      if (e.offsetX) {
        mouseX = e.offsetX;
        mouseY = e.offsetY;
      } else if (e.layerX) {
        mouseX = e.layerX;
        mouseY = e.layerY;
      }
      const indexX = Math.round(mouseX / this.dx);
      const indexY = Math.round(mouseY / this.dy);
      let coordsRequested = this._normalizeCoords(indexX, indexY);

      // if not X,Y in array create new with default role
      let holdIndex = this.newProblemHolds.findIndex(
        (p) => p.x == coordsRequested.x && p.y == coordsRequested.y
      );
      let hold = {};
      if (holdIndex !== -1) {
        hold = this.newProblemHolds[holdIndex];
        // TODO: maybe use a computed for checking two holds for start
        // TODO idem for end !!
        let idx = roles.findIndex((r) => r == hold.role);
        if (idx + 1 == roles.length) {
          this.newProblemHolds.splice(holdIndex, 1);
          this.clear();
          this.drawCreatedProblem();
          // hold.role = this.hasTwoStarts ? roles[1] : roles[0];
        } else if (this.hasTwoEnds) {
          console.log("?");
        } else {
          hold.role = roles[idx + 1];
        }
      } else {
        const startRole =
          this.newProblemHolds.filter((p) => p.role == "start").length == 2
            ? "middle"
            : "start";
        hold = {
          x: coordsRequested.x,
          y: coordsRequested.y,
          role: startRole,
        };
        this.newProblemHolds.push(hold);
      }
      this.drawHold(hold);

      const tooltipWidth = 60;
      this.tooltip.role = hold.role;
      this.tooltip.width = tooltipWidth;
      this.tooltip.position = {
        x: indexX * this.dx + 16 - tooltipWidth / 2,
        y: indexY * this.dy + 48 - this.holdRadius * 3,
      };
      if (this.tooltip.timeout) {
        clearTimeout(this.tooltip.timeout);
      }
      this.tooltip.visible = true;
      this.tooltip.timeout = setTimeout(() => {
        this.tooltip.visible = false;
      }, this.tooltipTimeout);
      // this.$nextTick(() => {
      //   this.$refs.tooltip.parentNode = this.canvasEl;
      // });

      // var BoardTooltipClass = this.$vue.extend(BoardTooltip);
      // var instance = new BoardTooltipClass({
      //   propsData: { role: hold.role, position: { x: mouseX, y: mouseY } },
      // });
      // instance.$mount(); // pass nothing
      // this.$refs.canvas.appendChild(instance.$el);

      // var t1 = new ToolTip(this.canvasEl, hold.role, color, 40, 2000);
    },
    validateProblem() {
      if (
        this.newProblemHolds.filter((hold) => hold.role == "start").length == 0
      ) {
        alert("Ajoutez au moins 1 prise de départ");
        return false;
      } else if (
        this.newProblemHolds.filter((hold) => hold.role == "end").length == 0
      ) {
        alert("Ajoutez au moins 1 prise de fin");
        return false;
      } else {
        return true;
      }
    },
  },
  watch: {
    inverted(isInverted, oldVal) {
      if (isInverted) {
        this.clear();
        this.drawProblem(true);
      } else {
        this.clear();
        this.drawProblem();
      }
    },
  },
};
</script>

<style>
#container canvas {
  display: block;
  overflow: auto;
  padding-left: 0;
  padding-right: 0;
  margin-left: auto;
  margin-right: auto;
}
#board {
  z-index: 50;
  border: 1px solid black;
}
</style>
