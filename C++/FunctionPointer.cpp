/**
 * This file gives an example of using function pointer
 * **/

#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

class Tick {
public:
    Tick(string line); // constructor
    
    // various loaders
    void load_stock_symbol(string input);
    void load_trade_price(string input);
    void load_trade_volume(string input);
    void load_time_in_sec(string input);

private:
    const uint8_t NUM_FIELDS = 4;
    string symbol;
    double price;
    int volume;
    long double time;

    // function pointer
    void (Tick::*loaders[NUM_FIELDS])(string) = {
        [0] = &Tick::load_stock_symbol,
        [1] = &Tick::load_trade_price,
        [2] = &Tick::load_trade_volume,
        [3] = &Tick::load_time_in_sec
    };
};

Tick::Tick(string line) {
    istringstream iss(line);
    string input;
    for (size_t i = 1; i < NUM_FIELDS; ++i) {
        getline(iss, input, ',');
        (this->*loaders[i])(input);
    }
}

void Tick::load_stock_symbol(string input) {
    symbol = input;
}

void Tick::load_trade_price(string input) {
    try {
        price = stod(input);
    }
    catch (exception &e) {
        price = 0.0;
    }
}

void Tick::load_trade_volume(string input) {
    try {
        volume = stoi(input);
    }
    catch (exception &e) {
        volume = 0;
    }
}

void Tick::load_time_in_sec(string input) {
    try {
        time = stold(input);
    }
    catch (exception &e) {
        time = 0;
    }
}
