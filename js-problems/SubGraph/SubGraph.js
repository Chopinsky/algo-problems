let graph = [];
let visited = [];

const init = function(edges, steps, nodes, debug) {
  initGraph(edges, nodes);
  if (debug) console.log(graph);
  return walk(0, steps + 1, debug);
};

const initGraph = function(edges, nodes) {
  if (!edges || edges.length < 1) {
    console.error(
      `Illegal edges input: expecting an non-null array, receiving ${edges}`
    );

    return;
  }

  let first, second, dist;

  edges.forEach(edge => {
    if (edge && edge.length === 3) {
      first = edge[0];
      second = edge[1];
      dist = edge[2];

      if (first === second || dist.length === 0) {
        return;
      }

      if (!graph[first]) {
        graph[first] = {};
      }

      if (!graph[second]) {
        graph[second] = {};
      }

      graph[first][second] = dist;
      graph[second][first] = dist;
    }
  });

  count = 0;
  visited = Array(nodes);
};

const walk = function(source, steps, debug) {
  let count = 0;

  if (
    typeof steps !== "number" ||
    !steps ||
    source < 0 ||
    source >= visited.length
  ) {
    return count;
  }

  steps--;
  count++;
  visited[source] = true;

  if (steps === 0) {
    return count;
  }

  let next = [];
  for (const neighbor in graph[source]) {
    let dist = graph[source][neighbor];
    if (dist === 0) {
      continue; // already visited this neighbor and exhuasted all interval nodes
    }

    if (debug) {
      console.log(`${source} -> ${neighbor}: `, dist, steps);
    }

    if (!visited[neighbor] && dist < steps) {
      next.push({
        node: neighbor,
        remainder: steps - dist
      });
    }

    if (dist <= steps) {
      graph[source][neighbor] = 0;
      graph[neighbor][source] = 0;
      count += dist;
    } else {
      graph[source][neighbor] -= steps;
      graph[neighbor][source] -= steps;
      count += steps;
    }
  }

  if (debug) {
    console.log(`visited: ${visited}`);
  }

  for (const n of next) {
    count += walk(n.node, n.remainder);
  }

  return count;
};

module.exports = {
  init
};
