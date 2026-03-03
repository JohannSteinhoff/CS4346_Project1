// CS 4346 - Project 1 - Table A: Should the car brake?
// Student ID: ngq7
// PSR Definition: PSR(P) = #{rows where P=1 AND Y=1} / #{rows where P=1}
//
// Rules discovered using PSR:
//   Rule 1: If Obstacle_Detected=1 AND Short_Distance=1 => Y=1
//   Rule 2: If Speed_High=1 AND Wet_Road=1 AND Short_Distance=1 => Y=1
//   Default: Otherwise => Y=0
//
// Compile: g++ -std=c++17 Project1-ngq7-TableA.cpp -o Project1-ngq7-TableA
// Run:     ./Project1-ngq7-TableA

#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;

struct Row {
    int label, obstacle, speed, wet, shortdist, y;
};

int predict(const Row& r) {
    bool rule1 = (r.obstacle == 1 && r.shortdist == 1);
    bool rule2 = (r.speed == 1 && r.wet == 1 && r.shortdist == 1);
    return (rule1 || rule2) ? 1 : 0;
}

double psr(const vector<Row>& data, int col) {
    int n = 0, n_pos = 0;
    for (const auto& r : data) {
        int val = (col==0)?r.obstacle:(col==1)?r.speed:(col==2)?r.wet:r.shortdist;
        if (val == 1) { n++; if (r.y == 1) n_pos++; }
    }
    return n > 0 ? (double)n_pos / n : 0.0;
}

int psr_n(const vector<Row>& data, int col) {
    int n = 0;
    for (const auto& r : data) {
        int val = (col==0)?r.obstacle:(col==1)?r.speed:(col==2)?r.wet:r.shortdist;
        if (val == 1) n++;
    }
    return n;
}

int psr_npos(const vector<Row>& data, int col) {
    int n = 0;
    for (const auto& r : data) {
        int val = (col==0)?r.obstacle:(col==1)?r.speed:(col==2)?r.wet:r.shortdist;
        if (val == 1 && r.y == 1) n++;
    }
    return n;
}

int main() {
    vector<Row> data = {
        {1,0,0,1,0,0},{2,0,0,0,0,0},{3,1,0,0,0,0},{4,0,0,0,0,0},{5,1,0,1,1,1},
        {6,0,0,1,1,0},{7,1,0,0,1,1},{8,0,0,1,0,0},{9,1,1,1,0,0},{10,1,0,1,0,0},
        {11,1,1,0,0,0},{12,0,0,1,0,0},{13,0,0,1,1,0},{14,1,1,0,1,1},{15,1,0,1,0,0},
        {16,0,0,0,1,0},{17,1,1,0,1,1},{18,0,0,0,1,0},{19,1,1,0,0,0},{20,1,0,1,1,1},
        {21,1,0,1,0,0},{22,0,1,1,1,1},{23,1,0,0,1,1},{24,0,0,0,0,0},{25,0,1,0,1,0},
        {26,1,1,1,0,0},{27,0,1,1,0,0},{28,1,1,0,1,1},{29,0,1,0,0,0},{30,1,0,0,1,1},
        {31,0,0,1,1,0},{32,0,0,1,1,0},{33,0,0,0,0,0},{34,0,1,0,0,0},{35,0,1,0,1,0},
        {36,1,0,0,1,1},{37,1,1,1,1,1},{38,0,0,0,0,0},{39,1,0,0,0,0},{40,0,0,0,0,0},
        {41,0,0,1,0,0},{42,0,1,1,0,0},{43,0,1,0,1,0},{44,1,0,0,0,0},{45,1,1,1,1,1},
        {46,1,0,0,0,0},{47,1,1,0,0,0},{48,0,0,1,0,0},{49,1,0,1,1,1},{50,0,0,1,0,0},
        {51,0,0,0,0,0},{52,0,1,1,1,1},{53,0,1,0,0,0},{54,1,0,1,1,1},{55,1,1,1,1,1},
        {56,0,0,1,0,0},{57,0,0,1,0,0},{58,0,1,0,0,0},{59,0,0,0,0,0},{60,0,1,0,0,0},
        {61,0,0,1,1,0},{62,1,0,1,0,0},{63,1,1,0,1,1},{64,1,1,0,0,0},{65,1,0,0,0,0},
        {66,1,0,1,0,0},{67,0,1,1,0,0},{68,1,1,0,1,1},{69,0,0,1,0,0},{70,0,0,1,1,0},
        {71,0,1,0,1,0},{72,1,1,0,0,0},{73,1,1,0,0,0},{74,1,0,1,0,0},{75,1,1,0,0,0},
        {76,0,0,0,1,0},{77,0,1,0,0,0},{78,1,1,0,1,1},{79,0,0,0,1,0},{80,1,0,0,0,0},
        {81,0,1,0,0,0},{82,1,1,0,1,1},{83,0,0,1,0,0},{84,1,0,0,1,1},{85,1,1,0,0,0},
        {86,0,0,1,1,0},{87,1,0,1,1,1},{88,1,1,0,0,0},{89,1,0,1,0,0},{90,0,1,1,1,1},
        {91,1,0,1,0,0},{92,1,0,1,0,0},{93,0,1,1,0,0},{94,1,1,0,1,1},{95,1,1,1,1,1},
        {96,1,0,0,1,1},{97,1,0,1,1,1},{98,0,1,1,0,0},{99,1,1,1,1,1},{100,1,0,1,0,0}
    };

    string names[] = {"Obstacle_Detected","Speed_High","Wet_Road","Short_Distance"};

    cout << "=======================================================" << endl;
    cout << "CS 4346 Project 1 - Table A: Should the car brake?" << endl;
    cout << "=======================================================" << endl;

    int pos = 0, neg = 0;
    for (auto& r : data) (r.y==1 ? pos : neg)++;
    cout << "\nTotal rows : " << data.size() << endl;
    cout << "Positives  : " << pos << "  (Y=1, car should brake)" << endl;
    cout << "Negatives  : " << neg << "  (Y=0, no braking needed)" << endl;

    cout << "\n--- PSR Values ---" << endl;
    for (int c = 0; c < 4; c++) {
        int np = psr_npos(data, c), n = psr_n(data, c);
        cout << fixed << setprecision(3);
        cout << "  PSR(" << names[c] << ") = " << np << "/" << n << " = " << psr(data, c) << endl;
    }

    cout << "\n--- Generated Rules ---" << endl;
    cout << "  Rule 1: Obstacle_Detected=1 AND Short_Distance=1  =>  Y=1" << endl;
    cout << "  Rule 2: Speed_High=1 AND Wet_Road=1 AND Short_Distance=1  =>  Y=1" << endl;
    cout << "  Default: Otherwise  =>  Y=0" << endl;

    cout << "\n--- Predictions vs Actual ---" << endl;
    cout << setw(6) << "Label" << setw(10) << "Obstacle" << setw(7) << "Speed"
         << setw(5) << "Wet" << setw(7) << "Short" << setw(10) << "Actual Y"
         << setw(8) << "Pred Y" << setw(7) << "Match" << endl;
    cout << string(60, '-') << endl;

    int errors = 0;
    for (auto& r : data) {
        int pred = predict(r);
        string match = (pred == r.y) ? "OK" : "FAIL";
        if (pred != r.y) errors++;
        cout << setw(6) << r.label << setw(10) << r.obstacle << setw(7) << r.speed
             << setw(5) << r.wet << setw(7) << r.shortdist << setw(10) << r.y
             << setw(8) << pred << setw(7) << match << endl;
    }

    cout << "\n--- Verification Summary ---" << endl;
    cout << "  Total rows : " << data.size() << endl;
    cout << "  Correct    : " << (data.size() - errors) << endl;
    cout << "  Errors     : " << errors << endl;
    cout << fixed << setprecision(1);
    cout << "  Accuracy   : " << (100.0*(data.size()-errors)/data.size()) << "%" << endl;
    if (errors == 0)
        cout << "\n  RESULT: Rules satisfy ALL 100 rows. Verification PASSED." << endl;
    else
        cout << "\n  RESULT: " << errors << " row(s) failed. Verification FAILED." << endl;

    return 0;
}
