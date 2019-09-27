# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 08:36:32 2019
@author: rubay
"""

import sys
import re
import ast
from decimal import Decimal

class_list = dict()


def check_validity(street):
    if street in class_list:
        return True
    else:
        return False


def duplicate_street_check(street):
    if street in class_list:
        return False
    else:
        return True


def street_validity_check(street):
    if all(x.isalpha() or x.isspace() for x in street):
        return True
    else:
        return False


def balanced_paranthesis_check(coordinate):
    a = []
    balanced = True
    index = 0
    while index < len(coordinate) and balanced:
        check = coordinate[index]
        if check == "(":
            a.append(check)
        elif check == ")":
            if len(a) == 0:
                balanced = False
            else:
                a.pop()

        index += 1
    return balanced and len(a) == 0


def location_validity(coordinate):
    r_exp = r'\(-?\d+,-?\d+\)'
    compiled_regex = re.compile(r_exp)
    if (compiled_regex.match(coordinate)):
        return True
    else:
        return False


def generate_graph():
    Var_1 = 1
    Var_2 = 1
    vertices_each_street = list()
    list_vertices_intersecting_lines = list()
    graph_edges = list()
    edge_set = set()
    graph_set = set()
    edge_duplicate = list()
    edge_duplicate_1 = list()
    vertices_final = dict()
    intersection_list = list()
    vertices_intersection = list()
    temp_list = list()
    list_vertices_of_intersecting_lines = list()
    big_line = 0
    list_values = list(class_list.values())
    total_streets = len(list_values)
    vertices_each_street = [None] * total_streets

    for a in range(0, total_streets):
        temp_list = [i.split(', ', 1)[0] for i in list_values[a]]

        vertices_each_street[a] = temp_list

    for i in range(0, total_streets):
        S1_length = len(vertices_each_street[i])

        for j in range(i + 1, total_streets):
            S2_length = len(vertices_each_street[j])
            while Var_1 < S1_length:
                while Var_2 < S2_length:
                    pair1 = vertices_each_street[i][Var_1 - 1]
                    pair2 = vertices_each_street[i][Var_1]
                    pair3 = vertices_each_street[j][Var_2 - 1]
                    pair4 = vertices_each_street[j][Var_2]
                    x1, y1 = ast.literal_eval(pair1)
                    x2, y2 = ast.literal_eval(pair2)
                    x3, y3 = ast.literal_eval(pair3)
                    x4, y4 = ast.literal_eval(pair4)
                    x1 = float(x1)
                    x1 = round(x1, 2)
                    x2 = float(x2)
                    x2 = round(x2, 2)
                    x3 = float(x3)
                    x3 = round(x3, 2)
                    x4 = float(x4)
                    x4 = round(x4, 2)
                    y1 = float(y1)
                    y1 = round(y1, 2)
                    y2 = float(y2)
                    y2 = round(y2, 2)
                    y3 = float(y3)
                    y3 = round(y3, 2)
                    y4 = float(y4)
                    y4 = round(y4, 2)
                    A1 = y2 - y1
                    B1 = x1 - x2
                    C1 = A1 * (x1) + B1 * (y1)

                    A2 = y4 - y3
                    B2 = x3 - x4
                    C2 = A2 * (x3) + B2 * (y3)
                    determinant = A1 * B2 - A2 * B1
                    min_x1 = min(x1, x2);
                    min_x2 = min(x3, x4);
                    max_x1 = max(x1, x2);
                    max_x2 = max(x3, x4);
                    min_y1 = min(y1, y2);
                    min_y2 = min(y3, y4);
                    max_y1 = max(y1, y2);
                    max_y2 = max(y3, y4);
                    flag1 = False
                    flag2 = False

                    pair1 = "(" + str(x1) + "," + str(y1) + ")"
                    pair2 = "(" + str(x2) + "," + str(y2) + ")"
                    pair3 = "(" + str(x3) + "," + str(y3) + ")"
                    pair4 = "(" + str(x4) + "," + str(y4) + ")"
                    list_pairs = list((pair1, pair2, pair3, pair4))

                    if (determinant != 0):
                        X = Decimal((B2 * C1 - B1 * C2) / determinant)
                        X = round(X, 2)
                        Y = Decimal((A1 * C2 - A2 * C1) / determinant)
                        Y = round(Y, 2)

                        if (bool(X <= max_x1) & bool(X >= min_x1)):

                            if (bool(Y <= max_y1) & bool(Y >= min_y1)):
                                flag1 = True
                            if (bool(X <= max_x2) & bool(X >= min_x2)):

                                if (bool(Y <= max_y2) & bool(Y >= min_y2)):
                                    flag2 = True
                        if (flag1 == True & flag2 == True):

                            new_vertex = "(" + str(X) + "," + str(Y) + ")"
                            list_vertices_intersecting_lines.extend(list_pairs)
                            intersection_list.append(new_vertex)
                            vertices_intersection.append(list_pairs)
                            list_vertices_intersecting_lines.append(new_vertex)
                            graph_set = set(list_vertices_intersecting_lines)
                            list_vertices_intersecting_lines = list(graph_set)
                            for z in range(0, len(list_vertices_intersecting_lines)):
                                vertices_final[z + 1] = list_vertices_intersecting_lines[z]
                        else:
                            pass
                    elif (pair1 == pair4):

                        new_vertex = "(" + str(x4) + "," + str(y4) + ")"
                        list_vertices_intersecting_lines.extend(list_pairs)
                        intersection_list.append(new_vertex)
                        vertices_intersection.append(list_pairs)
                        list_vertices_intersecting_lines.append(new_vertex)
                        graph_set = set(list_vertices_intersecting_lines)
                        list_vertices_intersecting_lines = list(graph_set)
                        for z in range(0, len(list_vertices_intersecting_lines)):
                            vertices_final[z + 1] = list_vertices_intersecting_lines[z]
                    elif (pair2 == pair3):
                        new_vertex = "(" + str(x3) + "," + str(y3) + ")"
                        list_vertices_intersecting_lines.extend(list_pairs)
                        intersection_list.append(new_vertex)
                        vertices_intersection.append(list_pairs)
                        list_vertices_intersecting_lines.append(new_vertex)
                        graph_set = set(list_vertices_intersecting_lines)
                        list_vertices_intersecting_lines = list(graph_set)
                        for z in range(0, len(list_vertices_intersecting_lines)):
                            vertices_final[z + 1] = list_vertices_intersecting_lines[z]

                    elif (x1 == x2 == x3 == x4):
                        y_range1 = abs(y2 - y1)
                        y_range2 = abs(y4 - y3)
                        if (y_range1 > y_range2):
                            big_line = 1
                        elif (y_range2 > y_range1):
                            big_line = 2
                        if (big_line == 1):
                            if (y3 > min_y1 and y3 < max_y1):
                                new_vertex = "(" + str(x3) + "," + str(y3) + ")"
                                list_vertices_intersecting_lines.extend(list_pairs)
                                intersection_list.append(new_vertex)
                                vertices_intersection.append(list_pairs)
                                list_vertices_intersecting_lines.append(new_vertex)
                                graph_set = set(list_vertices_intersecting_lines)
                                list_vertices_intersecting_lines = list(graph_set)
                                for z in range(0, len(list_vertices_intersecting_lines)):
                                    vertices_final[z + 1] = list_vertices_intersecting_lines[z]
                            if (y4 > min_y1 and y4 < max_y1):
                                new_vertex = "(" + str(x4) + "," + str(y4) + ")"
                                list_vertices_intersecting_lines.extend(list_pairs)
                                intersection_list.append(new_vertex)
                                vertices_intersection.append(list_pairs)
                                list_vertices_intersecting_lines.append(new_vertex)
                                graph_set = set(list_vertices_intersecting_lines)
                                list_vertices_intersecting_lines = list(graph_set)
                                for z in range(0, len(list_vertices_intersecting_lines)):
                                    vertices_final[z + 1] = list_vertices_intersecting_lines[z]

                        if (big_line == 2):
                            if (y1 > min_y2 and y1 < max_y2):
                                new_vertex = "(" + str(x1) + "," + str(y1) + ")"
                                list_vertices_intersecting_lines.extend(list_pairs)
                                intersection_list.append(new_vertex)
                                vertices_intersection.append(list_pairs)
                                list_vertices_intersecting_lines.append(new_vertex)
                                graph_set = set(list_vertices_intersecting_lines)
                                list_vertices_intersecting_lines = list(graph_set)
                                for z in range(0, len(list_vertices_intersecting_lines)):
                                    vertices_final[z + 1] = list_vertices_intersecting_lines[z]
                            if (y2 > min_y2 and y2 < max_y2):
                                new_vertex = "(" + str(x2) + "," + str(y2) + ")"
                                list_vertices_intersecting_lines.extend(list_pairs)
                                intersection_list.append(new_vertex)
                                vertices_intersection.append(list_pairs)
                                list_vertices_intersecting_lines.append(new_vertex)
                                graph_set = set(list_vertices_intersecting_lines)
                                list_vertices_intersecting_lines = list(graph_set)
                                for z in range(0, len(list_vertices_intersecting_lines)):
                                    vertices_final[z + 1] = list_vertices_intersecting_lines[z]

                    elif (y1 == y2 == y3 == y4):
                        x_range1 = abs(x2 - x1)
                        x_range2 = abs(x4 - x3)
                        if (x_range1 > x_range2):
                            big_line = 1
                        elif (x_range2 > x_range1):
                            big_line = 2
                        if (big_line == 1):
                            if (x3 > min_x1 and x3 < max_x1):
                                new_vertex = "(" + str(x3) + "," + str(y3) + ")"
                                list_vertices_intersecting_lines.extend(list_pairs)
                                intersection_list.append(new_vertex)
                                vertices_intersection.append(list_pairs)
                                list_vertices_intersecting_lines.append(new_vertex)
                                graph_set = set(list_vertices_intersecting_lines)
                                list_vertices_intersecting_lines = list(graph_set)
                                for z in range(0, len(list_vertices_intersecting_lines)):
                                    vertices_final[z + 1] = list_vertices_intersecting_lines[z]
                            if (x4 > min_x1 and x4 < max_x1):
                                new_vertex = "(" + str(x4) + "," + str(y4) + ")"
                                list_vertices_intersecting_lines.extend(list_pairs)
                                intersection_list.append(new_vertex)
                                vertices_intersection.append(list_pairs)
                                list_vertices_intersecting_lines.append(new_vertex)
                                graph_set = set(list_vertices_intersecting_lines)
                                list_vertices_intersecting_lines = list(graph_set)
                                for z in range(0, len(list_vertices_intersecting_lines)):
                                    vertices_final[z + 1] = list_vertices_intersecting_lines[z]

                        if (big_line == 2):
                            if (x1 > min_x2 and x1 < max_x2):
                                new_vertex = "(" + str(x1) + "," + str(y1) + ")"
                                list_vertices_intersecting_lines.extend(list_pairs)
                                intersection_list.append(new_vertex)
                                vertices_intersection.append(list_pairs)
                                list_vertices_intersecting_lines.append(new_vertex)
                                graph_set = set(list_vertices_intersecting_lines)
                                list_vertices_intersecting_lines = list(graph_set)
                                for z in range(0, len(list_vertices_intersecting_lines)):
                                    vertices_final[z + 1] = list_vertices_intersecting_lines[z]
                            if (x2 > min_x2 and x2 < max_x2):
                                new_vertex = "(" + str(x2) + "," + str(y2) + ")"
                                list_vertices_intersecting_lines.extend(list_pairs)
                                intersection_list.append(new_vertex)
                                vertices_intersection.append(list_pairs)
                                list_vertices_intersecting_lines.append(new_vertex)
                                graph_set = set(list_vertices_intersecting_lines)
                                list_vertices_intersecting_lines = list(graph_set)
                                for z in range(0, len(list_vertices_intersecting_lines)):
                                    vertices_final[z + 1] = list_vertices_intersecting_lines[z]

                    Var_2 = Var_2 + 1
                Var_1 = Var_1 + 1
                Var_2 = 1
            Var_1 = 1

    sys.stdout.write("V = {" + '\n')
    for x, y in vertices_final.items():
        sys.stdout.write(str(x) + ": " + str(y) + '\n')
    sys.stdout.write("}" + '\n')

    for b in range(0, len(intersection_list)):
        intersection_pt = intersection_list[b]
        vertexlist = vertices_intersection[b]
        [pair1, pair2, pair3, pair4] = vertexlist
        for c in vertices_final:

            if intersection_pt == vertices_final[c]:
                edge_intersection = c
        for st, gps in vertices_final.items():
            if gps == pair1:
                participating_vertex1 = st

        for st, gps in vertices_final.items():
            if gps == pair2:
                participating_vertex2 = st

        for st, gps in vertices_final.items():
            if gps == pair3:
                participating_vertex3 = st

        for st, gps in vertices_final.items():
            if gps == pair4:
                participating_vertex4 = st

        edge1 = "<" + str(edge_intersection) + "," + str(participating_vertex1) + ">"
        edge2 = "<" + str(edge_intersection) + "," + str(participating_vertex2) + ">"
        edge3 = "<" + str(edge_intersection) + "," + str(participating_vertex3) + ">"
        edge4 = "<" + str(edge_intersection) + "," + str(participating_vertex4) + ">"

        edgelist = list((edge1, edge2, edge3, edge4))
        graph_edges.extend(edgelist)
        edge_set = set(graph_edges)
        graph_edges = list(edge_set)
        distinct_new_vertices = list()
        for d in range(0, len(graph_edges)):
            pair = graph_edges[d]
            pair = re.sub('<', '(', pair)
            pair = re.sub('>', ')', pair)
            x_coord, y_coord = ast.literal_eval(pair)
            distinct_new_vertices.append(x_coord)
            distinct_set = set(distinct_new_vertices)
            distinct_new_vertices = list(distinct_set)
            for e in range(0, len(distinct_new_vertices)):
                for f in range(e + 1, len(distinct_new_vertices)):
                    edge_between = "<" + str(distinct_new_vertices[e]) + "," + str(distinct_new_vertices[f]) + ">"
                    graph_edges.append(edge_between)
                    graph_set = set(graph_edges)
                    graph_edges = list(graph_set)

    for g in range(0, len(graph_edges)):
        edge_1 = graph_edges[g]
        edge_1 = re.sub('<', '(', edge_1)
        edge_1 = re.sub('>', ')', edge_1)
        pair1, pair2 = ast.literal_eval(edge_1)
        if (pair1 == pair2):
            delete = "<" + str(pair1) + "," + str(pair2) + ">"
            edge_duplicate.append(delete)

        for h in vertices_final:
            v1 = vertices_final[pair1]
            v2 = vertices_final[pair2]

            v_x1, v_y1 = ast.literal_eval(v1)
            v_x2, v_y2 = ast.literal_eval(v2)
            min_x1 = min(v_x1, v_x2)
            max_x1 = max(v_x1, v_x2)
            min_y1 = min(v_y1, v_y2)
            max_y1 = max(v_y1, v_y2)
            check_v1_v2 = vertices_final[h]

            c_x, c_y = ast.literal_eval(check_v1_v2)
            if ((bool(c_x != min_x1) & bool(c_x != max_x1)) | ((bool(c_y != min_y1) & bool(c_y != max_y1)))):
                if (bool(c_x <= max_x1) & bool(c_x >= min_x1)):
                    if (bool(c_y <= max_y1) & bool(c_y >= min_y1)):
                        del_duplicate = "<" + str(pair1) + "," + str(pair2) + ">"
                        edge_duplicate.append(del_duplicate)
                        edge_duplicate_set = set(edge_duplicate)
                        edge_duplicate = list(edge_duplicate_set)

    for k in range(0, len(edge_duplicate)):
        graph_edges.remove(edge_duplicate[k])

    for l in range(0, len(graph_edges)):
        for l1 in range(l + 1, len(graph_edges)):
            edge_1 = graph_edges[l]
            edge_1 = re.sub('<', '(', edge_1)
            edge_1 = re.sub('>', ')', edge_1)
            pair1, pair2 = ast.literal_eval(edge_1)
            edge_2 = graph_edges[l1]
            edge_2 = re.sub('<', '(', edge_2)
            edge_2 = re.sub('>', ')', edge_2)
            pair3, pair4 = ast.literal_eval(edge_2)
            if (pair1 == pair4 and pair2 == pair3):
                delete = "<" + str(pair1) + "," + str(pair2) + ">"
                edge_duplicate_1.append(delete)
                edge_duplicate_set_1 = set(edge_duplicate_1)
                edge_duplicate_1 = list(edge_duplicate_set_1)

    for m in range(0, len(edge_duplicate_1)):
        graph_edges.remove(edge_duplicate_1[m])

    sys.stdout.write("E = {" + '\n')
    for u in graph_edges:
        sys.stdout.write("%s" % u + '\n')
    sys.stdout.write("}" + '\n')

def user_input():
    line = sys.stdin.readline()
    return line.replace('\n', '')

def main():
    while True:
        line = user_input()
        line=line.strip()
        if (line == ''):
            break
        elif (line[0] == 'r'):
            y = re.split(' +"|"|', line)
        else:
            y = re.split('" +| +"', line)

        if (len(y) == 1):
            selection = y[0]
        elif (len(y) == 2):
            selection = y[0]
            street = y[1]
            street = street.lower()
        elif (len(y) == 3):
            selection = y[0]
            street = y[1]
            street = street.lower()
            coordinate = y[2]
        else:
            sys.stderr.write(
                "Error: " + "Incorrect Command Format. Please enter command in format: " + " a \"street_name\" (coordinates) (coordinates)" + '\n')
            continue

        if selection == 'a':
            try:
                if street_validity_check(street):
                    if balanced_paranthesis_check(coordinate):
                        if duplicate_street_check(street):
                            coordinate = re.sub(' +', '', coordinate)
                            coordinate = re.sub('\)\(', ') ( ', coordinate)
                            coordinate = re.sub('\( ', '(', coordinate)
                            coordinate = coordinate.split(' ')
                            if all(location_validity(i) for i in coordinate):
                                if len(coordinate) > 1:
                                    class_list[street] = coordinate
                                else:
                                    sys.stderr.write("Error: At least 2 coordinate required for a street" + '\n')
                            else:
                                sys.stderr.write("Error: " + "Invalid Format." + '\n')
                        else:
                            sys.stderr.write("Error: " + "Street already exists " + '\n')
                    else:
                        sys.stderr.write("Error: " + "Invalid Format. Paranthesis does not match!!" + '\n')
                else:
                    sys.stderr.write(
                        "Error: " + "Invalid Format. No special charecter or number is acceptable as street name or keep atleast one whitespace between street name and coordinates!!" + '\n')
            except UnboundLocalError:
                sys.stderr.write(
                    "Error: " + "Invalid Format. Please Enter the command as: " + "a 'street name' (coordinates)" + '\n')

        elif selection == 'c':
            try:
                if (check_validity(street)):
                    if (street_validity_check(street)):
                        if (balanced_paranthesis_check(coordinate)):
                            coordinate = re.sub(' +', '', coordinate)
                            coordinate = re.sub('\)\(', ') ( ', coordinate)
                            coordinate = re.sub('\( ', '(', coordinate)
                            coordinate = coordinate.split(' ')
                            if all(location_validity(i) for i in coordinate):
                                if len(coordinate) > 1:
                                    class_list[street] = coordinate
                                else:
                                    sys.stderr.write("Error: At least 2 coordinate required for a street" + '\n')
                            else:
                                sys.stderr.write("Error: " + "Invalid Format. Integer input only!!" + '\n')
                        else:
                            sys.stderr.write("Error: " + "Invalid Format. Paranthesis does not match!!" + '\n')
                    else:
                        sys.stderr.write(
                            "Error: " + "Invalid Format. No special charecter or number is acceptable as street name or keep atleast one whitespace between street name and coordinates!!" + '\n')
                else:
                    sys.stderr.write(
                        "Error: " + "Street not found or has been removed already or enter coordinates to change!! " + '\n')
            except UnboundLocalError:
                sys.stderr.write(
                    "Error: " + "Invalid Format. Please Enter the command as: " + "c 'street name' (coordinates)" + '\n')

        elif selection == 'r':
            try:
                try:
                    if y[2] != "":
                        sys.stderr.write("Error: " + "Incorrect input format" + '\n')
                    else:
                        del class_list[street]
                except KeyError:
                    sys.stderr.write("Error: " + street + " Street not added or has been removed already!!" + '\n')
            except UnboundLocalError:
                sys.stderr.write("Error: " + "Invalid Format. Please Enter the command as: " + "r 'street name'" + '\n')

        elif selection == 'g':
            generate_graph()
        else:
            sys.stderr.write("Error: " + "Input format is invalid!!" + '\n')

if __name__ == '__main__':
    main()