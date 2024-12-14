#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <queue>
#include <vector>

using std::endl;
using std::fixed;
using std::greater;
using std::ifstream;
using std::numeric_limits;
using std::ofstream;
using std::pair;
using std::priority_queue;
using std::round;
using std::setprecision;
using std::vector;

double dijkstra(vector<vector<pair<int, double>>> &graph, int start,
                int finish) {
  vector<double> distances(graph.size(), numeric_limits<double>::max());
  distances[start] = 0;
  priority_queue<pair<double, int>, vector<pair<double, int>>, greater<>> pq;
  pq.push({distances[start], start});

  while (!pq.empty()) {
    pair<double, int> node = pq.top();
    pq.pop();

    if (node.first > distances[node.second])
      continue;

    for (auto pair : graph[node.second]) {
      double new_distance = node.first + pair.second;
      if (new_distance >= distances[pair.first])
        continue;
      distances[pair.first] = new_distance;
      pq.push({distances[pair.first], pair.first});
    }
  }

  return distances[finish];
}

int main() {
  ifstream infile("in.txt");
  ofstream outfile("out.txt");

  int S;
  infile >> S;

  double cost;
  int capacity, consumption, N;
  infile >> capacity >> consumption >> cost >> N;
  cost = round(cost * 10) / 10;

  vector<vector<pair<int, double>>> highway(N + 2, vector<pair<int, double>>());
  vector<pair<int, double>> gas_station(N + 2);

  gas_station[0] = {0, 0};
  for (auto i = 1; i < N + 1; i++) {
    infile >> gas_station[i].first >> gas_station[i].second;
  }
  gas_station[N + 1] = {S, 0};

  infile.close();

  int l = 0, r = 1;
  while (l < r) {
    while (r < N + 2 && gas_station[r].first - gas_station[l].first <=
                            capacity * consumption)
      r++;

    bool flag = true;
    for (auto i = r - 1; i > l; i--) {
      if (i == N + 1) {
        highway[l].push_back({i, 0.0});
        flag = false;
        continue;
      }

      double distance = gas_station[i].first - gas_station[l].first;
      double fuelNeeded = distance / consumption;

      if (fuelNeeded - static_cast<double>(capacity) / 2 >= 0 || flag) {
        double cost_i = round(fuelNeeded * gas_station[i].second * 10) / 10;

        highway[l].push_back({i, cost_i + 20});
        flag = false;
      }
    }

    l++;
  }

  cost += dijkstra(highway, 0, N + 1);

  outfile << fixed << setprecision(2);
  outfile << cost << endl;
  outfile.close();
}
