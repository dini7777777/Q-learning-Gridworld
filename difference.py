import ast
import numpy as np


def load_q_values(neg_enviorment, tasks):
    '''returns a list of for q values of different tasks.
    list_task_q[task_id] = q values for different coordinates.'''
    saved_q = []
    for t in tasks:
        saved_q.append("Q value " + str([neg_enviorment, t]) + ".txt")

    # Q = []
    # for q in saved_q:
    #     with open(q, "r") as saved_file:
    #         Q.append(ast.literal_eval(saved_file.read()))

    #
    list_task_q = [ast.literal_eval(open(qq, "r").read()) for qq in saved_q]
    assert len(tasks) == len(list_task_q)

    # coordinates = np.asarray(list(list_task_q[0].keys()))
    coordinates = list(list_task_q[0].keys())
    return coordinates, list_task_q


# def cross_entropy():
def norm_of_q(q_1, q_2):
    '''return distance of different actions for one state'''
    assert len(q_1) == len(q_2), "different number of actions in one state!"
    from numpy import linalg as la
    return la.norm(q_1-q_2)


def task_difference_in_q(Q_1, Q_2):
    Q_1 = list(Q_1.values())
    Q_2 = list(Q_2.values())
    norm = []

    for q1, q2 in zip(Q_1, Q_2):
        norm.append(norm_of_q(np.asarray(list(q1.values()), dtype=np.float32),
                              np.asarray(list(q2.values()), dtype=np.float32)))
        # print(q1, "\n", q2, "\n")
        # print(list(q1.values()), "\n", list(q2.values()), "\n")

    assert len(norm) == len(Q_1), "Missed some q values!"
    return np.asarray(norm)


def save_csv(filename, data_array):
    '''save np.array to csv'''
    np.savetxt(filename, data_array, delimiter=", ")


def save_difference_to_csv(filename, difference, coordinates):
    max_index = coordinates[-1]
    # Assume in a 2D grid world, check the environment space dims matches
    assert len(difference) == (max_index[0]+1) * (max_index[1]+1), "dimentions of difference doesn't match coordinates!"

    differ = difference.reshape([max_index[0]+1, -1])
    save_csv(filename, differ)


def main():
    env = (6, 4, "red3", -1)
    task = [(2, 0, "SkyBlue2", 1),
            (6, 7, "goldenrod", 1),
            (3, 11, "OliveDrab1", 1)]

    cor, Q = load_q_values(env, task)

    diff = []
    diff.append(task_difference_in_q(Q[0], Q[1]))
    diff.append(task_difference_in_q(Q[0], Q[2]))
    diff.append(task_difference_in_q(Q[1], Q[2]))

    save_difference_to_csv("0_1.csv", diff[0], cor)
    save_difference_to_csv("0_2.csv", diff[1], cor)
    save_difference_to_csv("1_2.csv", diff[2], cor)


if __name__ == '__main__':
    main()