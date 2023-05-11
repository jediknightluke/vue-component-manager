/* eslint-disable */
declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  const component: DefineComponent<{}, {}, any>
  export default component
}

declare module "vue-chessboard" {
  import { DefineComponent } from "vue";
  const ChessBoard: DefineComponent<{}, {}, any>;
  export default ChessBoard;
}

declare module '*.png';