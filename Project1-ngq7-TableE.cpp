// CS 4346 - Project 1 - Table E: Should the car sound an alert?
// Student ID: ngq7
// PSR Definition: PSR(P) = #{rows where P=1 AND Y=1} / #{rows where P=1}
//
// Rules discovered using PSR:
//   Rule 1: If Driver_Drowsy=1 AND Speed_Exceeded=1 => Y=1
//   Rule 2: If Seatbelt_Off=1 AND Lane_Departure=1  => Y=1
//   Default: Otherwise => Y=0
//
// Compile: g++ -std=c++17 Project1-ngq7-TableE.cpp -o Project1-ngq7-TableE
// Run:     ./Project1-ngq7-TableE

#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;

struct Row {
    int label, dd, se, ld, sb, y;
};

int predict(const Row& r) {
    bool rule1 = (r.dd == 1 && r.se == 1);
    bool rule2 = (r.sb == 1 && r.ld == 1);
    return (rule1 || rule2) ? 1 : 0;
}

int psr_npos(const vector<Row>& data, int col) {
    int n = 0;
    for (const auto& r : data) {
        int val = (col==0)?r.dd:(col==1)?r.se:(col==2)?r.ld:r.sb;
        if (val == 1 && r.y == 1) n++;
    }
    return n;
}

int psr_n(const vector<Row>& data, int col) {
    int n = 0;
    for (const auto& r : data) {
        int val = (col==0)?r.dd:(col==1)?r.se:(col==2)?r.ld:r.sb;
        if (val == 1) n++;
    }
    return n;
}

int main() {
    vector<Row> data = {
        {1,1,1,1,1,1},{2,1,1,1,0,1},{3,0,1,0,1,0},{4,0,1,1,1,1},{5,1,0,1,0,0},
        {6,0,1,0,1,0},{7,0,1,0,0,0},{8,1,0,0,1,0},{9,1,1,1,0,1},{10,1,1,1,1,1},
        {11,0,0,0,1,0},{12,0,0,1,0,0},{13,0,1,0,1,0},{14,0,0,1,0,0},{15,1,1,1,1,1},
        {16,0,0,1,0,0},{17,0,0,0,1,0},{18,0,1,0,0,0},{19,1,1,1,1,1},{20,0,1,1,0,0},
        {21,0,1,1,1,1},{22,1,1,1,1,1},{23,0,1,1,0,0},{24,0,1,1,1,1},{25,1,0,1,1,1},
        {26,0,0,1,1,1},{27,0,1,0,0,0},{28,1,0,0,0,0},{29,1,1,0,1,1},{30,0,0,1,1,1},
        {31,1,0,0,0,0},{32,1,1,0,1,1},{33,1,1,1,0,1},{34,1,0,0,0,0},{35,1,1,0,1,1},
        {36,0,1,0,1,0},{37,1,1,1,1,1},{38,0,0,1,0,0},{39,1,0,0,1,0},{40,1,1,0,0,1},
        {41,0,0,1,1,1},{42,0,0,0,0,0},{43,1,1,1,1,1},{44,0,1,0,1,0},{45,1,1,0,1,1},
        {46,0,1,1,0,0},{47,1,0,1,1,1},{48,0,1,1,0,0},{49,0,1,0,0,0},{50,0,0,1,0,0},
        {51,0,0,0,0,0},{52,0,0,1,0,0},{53,0,1,0,0,0},{54,1,0,0,0,0},{55,0,0,1,0,0},
        {56,1,0,0,1,0},{57,0,0,1,0,0},{58,0,1,1,1,1},{59,0,1,0,0,0},{60,1,1,0,0,1},
        {61,1,1,1,0,1},{62,1,1,0,0,1},{63,1,0,0,0,0},{64,1,1,1,1,1},{65,1,1,0,0,1},
        {66,0,1,1,0,0},{67,1,1,1,1,1},{68,1,0,1,1,1},{69,1,1,1,0,1},{70,1,0,0,0,0},
        {71,0,1,0,1,0},{72,0,0,1,0,0},{73,1,1,1,0,1},{74,1,1,1,0,1},{75,0,0,1,0,0},
        {76,0,1,1,0,0},{77,1,0,1,0,0},{78,1,0,0,1,0},{79,1,1,1,0,1},{80,0,0,1,0,0},
        {81,0,0,0,0,0},{82,1,1,1,1,1},{83,0,1,1,1,1},{84,0,0,0,0,0},{85,0,0,1,1,1},
        {86,1,1,1,1,1},{87,1,0,0,1,0},{88,1,0,1,1,1},{89,1,0,0,1,0},{90,0,0,0,1,0},
        {91,0,0,1,1,1},{92,1,0,0,1,0},{93,1,0,0,1,0},{94,0,1,0,1,0},{95,0,1,0,1,0},
        {96,0,1,1,1,1},{97,1,1,0,1,1},{98,0,1,0,1,0},{99,1,0,1,0,0},{100,0,1,1,0,0}
    };

    string names[] = {"Driver_Drowsy","Speed_Exceeded","Lane_Departure","Seatbelt_Off"};

    cout << "============================================================" << endl;
    cout << "CS 4346 Project 1 - Table E: Should the car sound an alert?" << endl;
    cout << "============================================================" << endl;

    int pos = 0, neg = 0;
    for (auto& r : data) (r.y==1 ? pos : neg)++;
    cout << "\nTotal rows : " << data.size() << endl;
    cout << "Positives  : " << pos << "  (Y=1, sound alert)" << endl;
    cout << "Negatives  : " << neg << "  (Y=0, no alert)" << endl;

    cout << "\n--- PSR Values ---" << endl;
    for (int c = 0; c < 4; c++) {
        int np = psr_npos(data, c), n = psr_n(data, c);
        cout << fixed << setprecision(4);
        cout << "  PSR(" << names[c] << ") = " << np << "/" << n
             << " = " << (n > 0 ? (double)np/n : 0.0) << endl;
    }

    cout << "\n--- Generated Rules ---" << endl;
    cout << "  Rule 1: Driver_Drowsy=1 AND Speed_Exceeded=1  =>  Y=1" << endl;
    cout << "  Rule 2: Seatbelt_Off=1  AND Lane_Departure=1  =>  Y=1" << endl;
    cout << "  Default: Otherwise  =>  Y=0" << endl;

    cout << "\n--- Predictions vs Actual ---" << endl;
    cout << setw(6) << "Label" << setw(4) << "DD" << setw(4) << "SE"
         << setw(4) << "LD" << setw(4) << "SB" << setw(10) << "Actual Y"
         << setw(8) << "Pred Y" << setw(7) << "Match" << endl;
    cout << string(50, '-') << endl;

    int errors = 0;
    for (auto& r : data) {
        int pred = predict(r);
        string match = (pred == r.y) ? "OK" : "FAIL";
        if (pred != r.y) errors++;
        cout << setw(6) << r.label << setw(4) << r.dd << setw(4) << r.se
             << setw(4) << r.ld << setw(4) << r.sb << setw(10) << r.y
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
