#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <algorithm>
#include <ctime>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <iomanip>

using namespace std;
typedef long long ll;

int SCOUT_BEES = 50000;
int ELITE = 20;
int NON_ELITE = 50;
int RECRUITED_ELITE = 500;
int RECRUITED_NON_ELITE = 300;
int MAX_DELTA = 5;

inline int getrandomvalue(int mod) {
	return ((rand() * rand() * rand()) % mod + mod) % mod;
	//random_shuffle(kokoko.begin(), kokoko.end(), myrandom);
}
double d(pair<int, int> f, pair<int, int> s) {
	int result = (f.first - s.first) * (f.first - s.first) + (f.second - s.second) * (f.second - s.second);
	return sqrt((double)result);
}
double fitness(vector<pair<int, int>> &route) {
	double result = 0;
	for (int i = 1; i < route.size(); i++) {
		result += d(route[i], route[i - 1]);
	}
	result += d(route[0], route[route.size() - 1]);
	return result;
}
double find_best_neighbour(vector<pair<int, int>> route, int it) {
	double result = fitness(route);
	for (int t = 0; t < it; t++) {
		vector<pair<int, int>> current = route;
		int swapnum = getrandomvalue(MAX_DELTA + 1);
		for (int u = 0; u < swapnum; u++) {
			int i = getrandomvalue(current.size());
			int j = getrandomvalue(current.size());
			swap(current[i], current[j]);
		}
		result = min(result, fitness(current));
	}
	return result;
}
double iteration(vector<pair<int, int>> cities) {
	double answer = 1e30;
	vector<pair<double, vector<pair<int, int>>>> situation;
	for (int i = 0; i < SCOUT_BEES; i++) {
		vector<pair<int, int>> current = cities;
		random_shuffle(current.begin(), current.end(), getrandomvalue);
		situation.push_back(make_pair(fitness(current), current));
	}
	sort(situation.begin(), situation.end());
	for (int i = 0; i < ELITE && i < situation.size(); i++) {
		answer = min(answer, find_best_neighbour(situation[i].second, RECRUITED_ELITE));
	}
	for (int t = 0, i = ELITE; t < NON_ELITE && i < situation.size(); i++, t++) {
		answer = min(answer, find_best_neighbour(situation[i].second, RECRUITED_NON_ELITE));
	}
	return answer;
}
double find(vector<pair<int, int>> cities) {
	double answer = 1e30;
	int counter = 0;
	while (SCOUT_BEES > 0) {
		counter++;
		double itanswer = iteration(cities);
		answer = min(answer, itanswer);
		system("CLS");
		cout << "Iteration " << counter << endl;
		cout << "Current iteration result " << itanswer << endl;
		cout << "Global minimum " << answer << endl;
		SCOUT_BEES -= (ELITE + NON_ELITE);
	}
	return answer;
}

vector<pair<int, int>> ddata;

int main() {
	freopen("data.in", "r", stdin);
	srand(unsigned(time(0)));
	int n, benchmark;
	scanf("%d %d", &n, &benchmark);
	for (int i = 0; i < n; i++) {
		int c1, c2; scanf("%d %d", &c1, &c2);
		ddata.push_back(make_pair(c1, c2));
	}
	find(ddata);
	return 0;
}