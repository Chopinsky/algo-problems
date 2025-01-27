'''
3435_frequencies-of-shortest-supersequences
'''

class Solution {
public:
    vector<vector<int>> supersequences(vector<string>& words) {
        // 1) Gather distinct letters
        unordered_set<char> lettersSet;
        for (auto &w : words) {
            lettersSet.insert(w[0]);
            lettersSet.insert(w[1]);
        }

        vector<char> letters(lettersSet.begin(), lettersSet.end());
        sort(letters.begin(), letters.end());  // not mandatory
        int k = (int)letters.size();

        // Map char -> index
        unordered_map<char,int> indexOf;
        for (int i = 0; i < k; i++) {
            indexOf[letters[i]] = i;
        }

        // 2) Build adjacency (hasEdge[x][y] = true if x->y)
        vector<vector<bool>> hasEdge(k, vector<bool>(k,false));
        vector<bool> selfLoop(k,false);
        for (auto &w : words) {
            int x = indexOf[w[0]];
            int y = indexOf[w[1]];
            if (x == y) {
                // word "xx" => freq[x] >= 2
                selfLoop[x] = true;
            } else {
                hasEdge[x][y] = true;
            }
        }

        // 3) Identify all 2-cycles x <-> y
        vector<pair<int,int>> twoCycles;
        for (int x = 0; x < k; x++) {
            for (int y = x+1; y < k; y++) {
                if (hasEdge[x][y] && hasEdge[y][x]) {
                    twoCycles.push_back({x,y});
                }
            }
        }

        // 4) Base frequency: if selfLoop[x], freq[x] >= 2, so effectively baseFreq[x] = 2, else 1.
        //    Then if "x is chosen to be repeated," freq[x] = baseFreq[x] + 1.
        vector<int> baseFreq(k);
        for (int x = 0; x < k; x++) {
            baseFreq[x] = (selfLoop[x] ? 2 : 1);
        }

        // Helper function: check if subgraph among "letters that appear exactly once" has a cycle.
        // We'll do a quick DFS cycle check on that induced subgraph.
        auto hasCycleInSubgraph = [&](int mask) {
            // "Exactly once" means: baseFreq[x]=1 and x not in mask (not repeated).
            // Construct adjacency among those vertices.
            vector<bool> inSub(k, false);
            for (int x = 0; x < k; x++) {
                bool repeated = (mask & (1<<x)) != 0;
                if (baseFreq[x] == 2) {
                    // forced freq=2, so not in subgraph
                    inSub[x] = false;
                } else {
                    // baseFreq[x] == 1 => inSub[x] if it is NOT repeated
                    inSub[x] = (!repeated);
                }
            }

            // DFS cycle detection on the subgraph
            vector<int> visited(k, 0); // 0=unvisited,1=visiting,2=done
            function<bool(int)> dfs = [&](int u) -> bool {
                visited[u] = 1; // visiting
                for (int v = 0; v < k; v++) {
                    if (hasEdge[u][v] && inSub[v]) {
                        // edge in subgraph
                        if (visited[v] == 0 && dfs(v)) {
                          return true;
                        } 
                        
                        if (visited[v] == 1) {
                            // found a cycle
                            return true;
                        }
                    }
                }

                visited[u] = 2;
                return false;
            };

            for (int x = 0; x < k; x++) {
                if (inSub[x] && visited[x] == 0) {
                    if (dfs(x)) {
                        return true; // cycle found
                    }
                }
            }
            
            return false; // no cycle
        };

        // We will try all subsets (bitmasks) of letters that might be "repeated" beyond their baseFreq.
        // For letters with baseFreq[x] == 2, we do NOT treat them as free to add "another" repeat:
        // we only do that if we wish, but there's usually no reason to set freq[x]=3 in minimal solutions.
        // So let's keep the code simpler: we allow it but that rarely helps unless needed to break a cycle
        // that doesn't contain that letter. We'll still include them in the bitmask choices, although
        // typically that won't minimize length. We'll filter them out anyway in the final step if they
        // aren't minimal.

        int limit = (1 << k);
        int minLen = INT_MAX;
        vector<int> validMasks;  // store bitmasks that yield minimal length

        for (int mask = 0; mask < limit; mask++) {
            // (A) Check 2-cycle constraints: for each x<->y, freq[x]>=2 or freq[y]>=2
            // freq[x]>=2 means baseFreq[x]==2 or x repeated in mask
            bool ok = true;
            for (auto &p : twoCycles) {
                int x = p.first, y = p.second;
                bool xHas2 = (baseFreq[x] >= 2) || ((mask & (1<<x)) != 0);
                bool yHas2 = (baseFreq[y] >= 2) || ((mask & (1<<y)) != 0);
                if (!(xHas2 || yHas2)) {
                    ok = false;
                    break;
                }
            }

            if (!ok) {
              continue;
            }

            // (B) Check "subgraph of letters used exactly once is acyclic"
            if (hasCycleInSubgraph(mask)) {
                continue;
            }

            // (C) Compute total length
            int total = 0;
            for (int x = 0; x < k; x++) {
                int f = baseFreq[x];
                if (mask & (1<<x)) {
                    f += 1; // one extra occurrence
                }
                total += f;
            }

            if (total < minLen) {
                minLen = total;
                validMasks.clear();
                validMasks.push_back(mask);
            } else if (total == minLen) {
                validMasks.push_back(mask);
            }
        }

        // Build final frequency arrays
        vector<vector<int>> ans;
        for (int mask: validMasks) {
            vector<int> freq(k);
            for (int x = 0; x < k; x++) {
                freq[x] = baseFreq[x];
                if (mask & (1<<x)) {
                    freq[x] += 1;
                }
            }

            // convert to 26-wide
            vector<int> freq26(26, 0);
            for (int x = 0; x < k; x++) {
                freq26[letters[x] - 'a'] = freq[x];
            }

            ans.push_back(freq26);
        }

        return ans;
    }
};