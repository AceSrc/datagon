#include <iostream>
using namespace std;

const int maxn = 100 + 10;
const int INF = 2147483647;

int mp[maxn][maxn];
bool visited[maxn];
int dist[maxn];

int main() {
    int n, m, a, b;
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++) mp[i][j] = INF;
    for (int i = 1; i <= m; i++) {
        cin >> a >> b;
        cin >> mp[a][b];
    }
    for (int i = 1; i <= n; i++) visited[i] = false;
    for (int i = 1; i <= n; i++) dist[i] = INF;
    dist[1] = 0;
    for (int i = 1; i <= n; i++) {
        int cur = -1;
        for (int j = 1; j <= n; j++) 
            if (!visited[j] && (cur == -1 || dist[cur] > dist[j])) cur = j;
        if (cur == -1 || dist[cur] == INF || visited[cur]) break;
        visited[cur] = true;
        for (int j = 1; j <= n; j++)
            if (!visited[j] && mp[cur][j] != INF && dist[j] > dist[cur] + mp[cur][j]) {
                dist[j] = dist[cur] + mp[cur][j];
            }       
    }
    for (int i = 1; i <= n; i++) cout << dist[i] << ' ';
    cout << endl;
    return 0;
}
