<template>
  <v-container class="chess-board">
    <v-row v-for="row in 8" :key="row">
      <v-col
        v-for="col in 8"
        :key="col"
        :class="[getSquareColor(row, col), 'square']"
      >
        <draggable
          :value="{ row, col }"
          @end="onDrag"
          draggable="true"
          :transfer-data="JSON.stringify({ row, col })"
        >
          <v-img
            :src="getPiece(row, col)"
            :alt="getPiece(row, col) ? 'Chess piece' : ''"
            class="piece"
          ></v-img>
        </draggable>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from "vue";

import whiteRook from "../assets/img/white-rook.png";
import whiteKnight from "../assets/img/white-knight.png";
import whiteBishop from "../assets/img/white-bishop.png";
import whiteQueen from "../assets/img/white-queen.png";
import whiteKing from "../assets/img/white-king.png";
import whitePawn from "../assets/img/white-pawn.png";
import blackRook from "../assets/img/black-rook.png";
import blackKnight from "../assets/img/black-knight.png";
import blackBishop from "../assets/img/black-bishop.png";
import blackQueen from "../assets/img/black-queen.png";
import blackKing from "../assets/img/black-king.png";
import blackPawn from "../assets/img/black-pawn.png";

const pieceImages: { [key: string]: any } = {
  R: whiteRook,
  N: whiteKnight,
  B: whiteBishop,
  Q: whiteQueen,
  K: whiteKing,
  P: whitePawn,
  r: blackRook,
  n: blackKnight,
  b: blackBishop,
  q: blackQueen,
  k: blackKing,
  p: blackPawn,
};

interface CustomEvent {
  detail: {
    row: number;
    col: number;
  };
}

export default defineComponent({
  methods: {
    getSquareColor(row: number, col: number) {
      return (row + col) % 2 === 0 ? "white-square" : "black-square";
    },
    getPiece(row: number, col: number) {
      const initialPosition = [
        "RNBQKBNR",
        "PPPPPPPP",
        "        ",
        "        ",
        "        ",
        "        ",
        "pppppppp",
        "rnbqkbnr",
      ];

      const piece = initialPosition[8 - row]?.[col - 1];
      return piece ? pieceImages[piece] : "";
    },
    onDrag(event: DragEvent) {
      const { row, col } = JSON.parse(
        event.dataTransfer?.getData("application/json") || "{}"
      );
      const piece = this.getPiece(row, col);
      if (!piece) return;
      console.log(`Moving piece from (${row}, ${col})`);
    },
  },
});
</script>

<style scoped>
.square {
  height: 60px;
  width: 60px;
}

.white-square {
  background-color: #f0d9b5;
}

.black-square {
  background-color: #b58863;
}

.piece {
  max-height: 100%;
  max-width: 100%;
}
</style>
