#include <iostream>
using namespace std;

int main() {
    int n = 5;
    move(n, 'A', 'C', 'B');
    return 0;
}

void move(int disk, char source, char destination, char auxiliary) {
    if (disk == 1) {
        cout << "Move disk 1 from " << source << " to " << destination << endl;
        return;
    }

    move(disk - 1, source, auxiliary, destination);
    cout << "Move disk " << disk << " from " << source << " to " << destination << endl;
    move(disk - 1, auxiliary, destination, source);
}
