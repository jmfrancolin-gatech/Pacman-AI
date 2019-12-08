/*
Author: Joao Matheus Francolin
Class: ECE 4122
Last date modified: September 25, 2019
Description: Implements ECE_Matrix class
*/

// Implemantation only works in C++ 11
// In order to compile in a Mac, run the following:
// clang++ -std=c++11 Hmk2_Test1.cpp ECE_Matrix.cpp -o Hmk2_Test1

#include "ECE_Matrix.h"

#include <iostream>
#include <vector>
#include <fstream>
#include <iomanip>
#include <limits>

// Constructor chaining
ECE_Matrix::ECE_Matrix() : ECE_Matrix(0) {}
ECE_Matrix::ECE_Matrix(int num_rows) : ECE_Matrix(num_rows, 0.0) {}
ECE_Matrix::ECE_Matrix(int num_rows, double init_value) : ECE_Matrix(num_rows, num_rows, init_value) {}
// Main constructor
ECE_Matrix::ECE_Matrix(int num_rows, int num_columns, double init_value)
{
    this->num_rows = num_rows;
    this->num_columns = num_columns;
    this->vector = std::vector< std::vector<double> > (num_rows, \
        std::vector<double>(num_columns, init_value));
}
// Constructor for txt files
ECE_Matrix::ECE_Matrix(char const *file_name) : ECE_Matrix(0)
{
    // Open file
    std::ifstream my_file (file_name);
    if (!my_file.is_open())
    {
        return;
    }

    // Initialyze fields
    my_file >> this->num_rows;
    my_file >> this->num_columns;
    this->vector = std::vector< std::vector<double> > (num_rows, \
        std::vector<double>(num_columns, 0));

    // Populate matrix
    for (int ii = 0; ii < this->num_rows; ii++)
    {
        for (int jj = 0; jj < this->num_columns; jj++)
        {
            my_file >> this->vector[ii][jj];
        }
    }
    my_file.close();
}



    "*** YOUR CODE HERE ***"
    stack = util.Stack()
    visited_set = set()

    state = (problem.getStartState(), [])
    stack.push(state)

    while not stack.isEmpty():
        curr_node, path = stack.pop()

        if problem.isGoalState(curr_node):
            return path

        if curr_node not in visited_set:
            visited_set.add(curr_node)

            successors = problem.getSuccessors(curr_node)
            for candidate in successors:
                next_node = candidate[0]
                next_action = candidate[1]

                if next_node not in visited_set:
                    state = (next_node, path + [next_action])
                    stack.push(state)
                    # print stack
    return []
