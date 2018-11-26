import { ThreeSumMulti } from "./Collection/3SumWithMulti";
import { KnightDialer } from "./Collection/KnightDialer";
import { Knapsack } from "./Collection/Knapsack";
import { ShortestBridges } from "./Collection/ShortestBridges";
import { ShortestSuperstring } from "./Collection/ShortestSuperstring";

export const Problems: object = {
  "3SumWithMulti": new ThreeSumMulti(),
  KnightDialer: new KnightDialer(),
  Knapsack: new Knapsack(),
  ShortestBridges: new ShortestBridges(),
  ShortestSuperstring: new ShortestSuperstring()
};
